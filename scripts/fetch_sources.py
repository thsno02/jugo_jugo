#!/usr/bin/env python3
"""Fetch raw LLM Wiki research sources into a local knowledge database."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import html
import io
import json
import os
import re
import subprocess
import sys
import time
import tarfile
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests


ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "data" / "raw"
LOG_PATH = ROOT / "data" / "logs" / "source_access_log.jsonl"
SOURCES_PATH = ROOT / "data" / "manifests" / "sources.jsonl"
DEFAULT_TIMEOUT = 40
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36 "
    "llm-wiki-resource-acquisition/0.1"
)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip_depth += 1
        if tag in {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "tr"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self.skip_depth:
            self.skip_depth -= 1
        if tag in {"p", "div", "li", "h1", "h2", "h3", "h4", "tr"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            cleaned = " ".join(data.split())
            if cleaned:
                self.parts.append(cleaned + " ")

    def text(self) -> str:
        text = html.unescape("".join(self.parts))
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n" if text.strip() else ""


@dataclass
class FetchResult:
    source_id: str
    status: str
    local_dir: str
    files: dict[str, str]
    metadata: dict[str, Any]
    error: str | None = None


@dataclass
class ResponseLike:
    content: bytes
    status_code: int
    url: str
    headers: dict[str, str]
    ok: bool
    transport: str
    warning: str | None = None

    @property
    def text(self) -> str:
        content_type = self.headers.get("content-type", "")
        encoding = "utf-8"
        match = re.search(r"charset=([^;]+)", content_type, flags=re.I)
        if match:
            encoding = match.group(1).strip()
        try:
            return self.content.decode(encoding, errors="replace")
        except LookupError:
            return self.content.decode("utf-8", errors="replace")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"https?://", "", value)
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-._")
    return value[:120] or "source"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def save_bytes(path: Path, data: bytes) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return sha256_bytes(data)


def save_text(path: Path, data: str) -> str:
    encoded = data.encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(encoded)
    return sha256_bytes(encoded)


def safe_extract_tar(archive_path: Path, destination: Path) -> list[Path]:
    destination.mkdir(parents=True, exist_ok=True)
    extracted: list[Path] = []
    with tarfile.open(archive_path, "r:*") as archive:
        for member in archive.getmembers():
            if not member.isfile():
                continue
            target = (destination / member.name).resolve()
            if not target.is_relative_to(destination.resolve()):
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            handle = archive.extractfile(member)
            if handle is None:
                continue
            target.write_bytes(handle.read())
            extracted.append(target)
    return extracted


def agent_readable_source_files(source_root: Path) -> list[Path]:
    readable_exts = {
        ".tex",
        ".bib",
        ".bbl",
        ".sty",
        ".cls",
        ".md",
        ".txt",
        ".json",
        ".ltx",
    }
    files = [path for path in source_root.rglob("*") if path.is_file() and path.suffix.lower() in readable_exts]
    return sorted(files, key=lambda path: (path.suffix.lower() != ".tex", str(path.relative_to(source_root))))


def write_agent_source_bundle(source_root: Path, bundle_path: Path) -> tuple[str | None, int, list[str]]:
    parts: list[str] = []
    included: list[str] = []
    for path in agent_readable_source_files(source_root):
        rel = path.relative_to(source_root)
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if not text.strip():
            continue
        parts.append(f"\n\n===== {rel} =====\n\n{text}")
        included.append(str(rel))
    if not parts:
        return None, 0, []
    digest = save_text(bundle_path, "".join(parts).strip() + "\n")
    return digest, len(included), included


def curl_get(url: str) -> ResponseLike:
    with tempfile.TemporaryDirectory() as temp_dir:
        body_path = Path(temp_dir) / "body"
        write_format = "%{http_code}\t%{url_effective}\t%{content_type}"
        completed = subprocess.run(
            [
                "curl",
                "-L",
                "--max-time",
                str(DEFAULT_TIMEOUT),
                "-A",
                USER_AGENT,
                "-sS",
                "-o",
                str(body_path),
                "-w",
                write_format,
                url,
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=DEFAULT_TIMEOUT + 10,
        )
        raw = body_path.read_bytes() if body_path.exists() else b""
        parts = completed.stdout.split("\t")
        status = int(parts[0]) if parts and parts[0].isdigit() else 0
        final_url = parts[1] if len(parts) > 1 and parts[1] else url
        content_type = parts[2] if len(parts) > 2 else ""
        warning = None
        ok = completed.returncode == 0 and 200 <= status < 400
        if b"office-sec.alibaba-inc.com" in raw or "office-sec.alibaba-inc.com" in final_url:
            warning = "network_intercepted_by_office_sec"
            ok = False
        if completed.returncode != 0:
            warning = f"curl_exit_{completed.returncode}: {completed.stderr[-500:]}"
        return ResponseLike(
            content=raw,
            status_code=status,
            url=final_url,
            headers={"content-type": content_type},
            ok=ok,
            transport="curl",
            warning=warning,
        )


def request_get(url: str, accept: str | None = None) -> ResponseLike:
    headers = {"User-Agent": USER_AGENT}
    if accept:
        headers["Accept"] = accept
    try:
        response = requests.get(url, headers=headers, timeout=DEFAULT_TIMEOUT, allow_redirects=True)
    except requests.exceptions.SSLError:
        return curl_get(url)
    return ResponseLike(
        content=response.content,
        status_code=response.status_code,
        url=response.url,
        headers={key.lower(): value for key, value in response.headers.items()},
        ok=response.ok,
        transport="requests",
    )


def source_dir(source: dict[str, Any]) -> Path:
    kind = source.get("type", "webpage")
    return RAW_ROOT / kind / slugify(source["id"])


def extract_html_text(raw: bytes, content_type: str) -> str:
    encoding = "utf-8"
    match = re.search(r"charset=([^;]+)", content_type or "", flags=re.I)
    if match:
        encoding = match.group(1).strip()
    try:
        decoded = raw.decode(encoding, errors="replace")
    except LookupError:
        decoded = raw.decode("utf-8", errors="replace")
    parser = TextExtractor()
    parser.feed(decoded)
    return parser.text()


def fetch_url(source: dict[str, Any], out_dir: Path, filename: str = "raw") -> FetchResult:
    response = request_get(source["url"])
    content_type = response.headers.get("content-type", "")
    suffix = ".html" if "html" in content_type else ".txt"
    if "json" in content_type:
        suffix = ".json"
    if "pdf" in content_type:
        suffix = ".pdf"
    raw_path = out_dir / f"{filename}{suffix}"
    digest = save_bytes(raw_path, response.content)
    files = {raw_path.name: str(raw_path.relative_to(ROOT))}

    text_digest = None
    if "html" in content_type:
        text = extract_html_text(response.content, content_type)
        if text:
            text_digest = save_text(out_dir / "text.txt", text)
            files["text.txt"] = str((out_dir / "text.txt").relative_to(ROOT))
    elif "text" in content_type or suffix == ".txt":
        try:
            text = response.text
        except UnicodeDecodeError:
            text = response.content.decode("utf-8", errors="replace")
        text_digest = save_text(out_dir / "text.txt", text)
        files["text.txt"] = str((out_dir / "text.txt").relative_to(ROOT))

    metadata = {
        "source": source,
        "fetched_at": utc_now(),
        "requested_url": source["url"],
        "final_url": response.url,
        "http_status": response.status_code,
        "content_type": content_type,
        "bytes": len(response.content),
        "sha256": digest,
        "text_sha256": text_digest,
        "ok": response.ok,
        "transport": response.transport,
        "transport_warning": response.warning,
    }
    write_json(out_dir / "metadata.json", metadata)
    return FetchResult(
        source_id=source["id"],
        status="ok" if response.ok else "http_error",
        local_dir=str(out_dir.relative_to(ROOT)),
        files=files,
        metadata=metadata,
        error=None if response.ok else f"HTTP {response.status_code}",
    )


def fetch_reddit(source: dict[str, Any], out_dir: Path) -> FetchResult:
    result = fetch_url(source, out_dir, "page")
    json_url = source["url"].rstrip("/") + ".json"
    try:
        response = request_get(json_url, "application/json")
        digest = save_bytes(out_dir / "thread.json", response.content)
        result.files["thread.json"] = str((out_dir / "thread.json").relative_to(ROOT))
        result.metadata["reddit_json_url"] = json_url
        result.metadata["reddit_json_status"] = response.status_code
        result.metadata["reddit_json_sha256"] = digest
    except Exception as exc:
        result.metadata["reddit_json_error"] = repr(exc)
    write_json(out_dir / "metadata.json", result.metadata)
    return result


def fetch_hacker_news(source: dict[str, Any], out_dir: Path) -> FetchResult:
    result = fetch_url(source, out_dir, "page")
    match = re.search(r"[?&]id=(\d+)", source["url"])
    if match:
        item_id = match.group(1)
        api_url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
        try:
            response = request_get(api_url, "application/json")
            digest = save_bytes(out_dir / "item.json", response.content)
            result.files["item.json"] = str((out_dir / "item.json").relative_to(ROOT))
            result.metadata["hn_api_url"] = api_url
            result.metadata["hn_api_status"] = response.status_code
            result.metadata["hn_api_sha256"] = digest
        except Exception as exc:
            result.metadata["hn_api_error"] = repr(exc)
    write_json(out_dir / "metadata.json", result.metadata)
    return result


def fetch_arxiv(source: dict[str, Any], out_dir: Path) -> FetchResult:
    result = fetch_url(source, out_dir, "abs")
    arxiv_id = source.get("arxiv_id") or source["url"].rstrip("/").split("/")[-1]
    eprint_url = f"https://arxiv.org/e-print/{arxiv_id}"
    try:
        response = request_get(eprint_url, "application/eprint")
        content_type = response.headers.get("content-type", "")
        is_pdf = response.content.startswith(b"%PDF") or "pdf" in content_type.lower()
        is_gzip = response.content.startswith(b"\x1f\x8b")
        if is_pdf:
            source_path = out_dir / "source.pdf"
            source_kind = "pdf_only"
        elif is_gzip:
            source_path = out_dir / "source.tar.gz"
            source_kind = "tex_source_archive"
        else:
            source_path = out_dir / "source.bin"
            source_kind = "unknown_source_payload"

        digest = save_bytes(source_path, response.content)
        result.files[source_path.name] = str(source_path.relative_to(ROOT))
        result.metadata["eprint_url"] = eprint_url
        result.metadata["eprint_status"] = response.status_code
        result.metadata["eprint_content_type"] = content_type
        result.metadata["eprint_sha256"] = digest
        result.metadata["eprint_bytes"] = len(response.content)
        result.metadata["eprint_source_kind"] = source_kind

        if source_kind == "tex_source_archive" and tarfile.is_tarfile(source_path):
            extracted_root = out_dir / "source"
            extracted = safe_extract_tar(source_path, extracted_root)
            result.files["source"] = str(extracted_root.relative_to(ROOT))
            bundle_digest, bundle_count, bundle_files = write_agent_source_bundle(
                extracted_root, out_dir / "agent_source_bundle.txt"
            )
            if bundle_digest:
                result.files["agent_source_bundle.txt"] = str((out_dir / "agent_source_bundle.txt").relative_to(ROOT))
            result.metadata["source_file_count"] = len(extracted)
            result.metadata["agent_readable_file_count"] = bundle_count
            result.metadata["agent_readable_files"] = bundle_files
            result.metadata["agent_source_bundle_sha256"] = bundle_digest
        elif source_kind == "tex_source_archive":
            try:
                decompressed = gzip.decompress(response.content)
                text = decompressed.decode("utf-8", errors="replace")
                target = out_dir / "source" / "source.tex"
                digest = save_text(target, text)
                result.files["source/source.tex"] = str(target.relative_to(ROOT))
                bundle_digest = save_text(out_dir / "agent_source_bundle.txt", f"===== source.tex =====\n\n{text}")
                result.files["agent_source_bundle.txt"] = str((out_dir / "agent_source_bundle.txt").relative_to(ROOT))
                result.metadata["single_gzip_tex_sha256"] = digest
                result.metadata["agent_source_bundle_sha256"] = bundle_digest
                result.metadata["agent_readable_file_count"] = 1
                result.metadata["agent_readable_files"] = ["source.tex"]
            except Exception as exc:
                result.metadata["source_extract_error"] = repr(exc)
        elif source_kind == "pdf_only":
            result.metadata["source_note"] = "arXiv e-print returned a PDF; no TeX source was available from this endpoint."
    except Exception as exc:
        result.metadata["eprint_error"] = repr(exc)
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
        try:
            response = request_get(pdf_url, "application/pdf")
            digest = save_bytes(out_dir / "paper_fallback.pdf", response.content)
            result.files["paper_fallback.pdf"] = str((out_dir / "paper_fallback.pdf").relative_to(ROOT))
            result.metadata["pdf_fallback_url"] = pdf_url
            result.metadata["pdf_fallback_status"] = response.status_code
            result.metadata["pdf_fallback_sha256"] = digest
            result.metadata["pdf_fallback_bytes"] = len(response.content)
        except Exception as pdf_exc:
            result.metadata["pdf_fallback_error"] = repr(pdf_exc)
    write_json(out_dir / "metadata.json", result.metadata)
    return result


def fetch_pypi(source: dict[str, Any], out_dir: Path) -> FetchResult:
    result = fetch_url(source, out_dir, "page")
    package = source.get("package")
    if package:
        api_url = f"https://pypi.org/pypi/{package}/json"
        try:
            response = request_get(api_url, "application/json")
            digest = save_bytes(out_dir / "pypi.json", response.content)
            result.files["pypi.json"] = str((out_dir / "pypi.json").relative_to(ROOT))
            result.metadata["pypi_api_url"] = api_url
            result.metadata["pypi_api_status"] = response.status_code
            result.metadata["pypi_api_sha256"] = digest
        except Exception as exc:
            result.metadata["pypi_api_error"] = repr(exc)
    write_json(out_dir / "metadata.json", result.metadata)
    return result


def run(cmd: list[str], cwd: Path | None = None) -> tuple[int, str]:
    completed = subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=180,
    )
    return completed.returncode, completed.stdout


def fetch_github_repo(source: dict[str, Any], out_dir: Path, clone_repos: bool) -> FetchResult:
    repo = source.get("repo")
    if not repo:
        parsed = urlparse(source["url"])
        parts = parsed.path.strip("/").split("/")
        repo = "/".join(parts[:2])
    out_dir.mkdir(parents=True, exist_ok=True)
    files: dict[str, str] = {}
    metadata: dict[str, Any] = {"source": source, "fetched_at": utc_now(), "repo": repo}

    api_url = f"https://api.github.com/repos/{repo}"
    try:
        response = request_get(api_url, "application/vnd.github+json")
        digest = save_bytes(out_dir / "github_repo.json", response.content)
        files["github_repo.json"] = str((out_dir / "github_repo.json").relative_to(ROOT))
        metadata["github_api_url"] = api_url
        metadata["github_api_status"] = response.status_code
        metadata["github_api_sha256"] = digest
    except Exception as exc:
        metadata["github_api_error"] = repr(exc)

    readme_url = f"https://api.github.com/repos/{repo}/readme"
    try:
        response = request_get(readme_url, "application/vnd.github.raw")
        digest = save_bytes(out_dir / "README.remote", response.content)
        files["README.remote"] = str((out_dir / "README.remote").relative_to(ROOT))
        metadata["readme_api_status"] = response.status_code
        metadata["readme_sha256"] = digest
    except Exception as exc:
        metadata["readme_error"] = repr(exc)

    repo_dir = out_dir / "repo"
    if clone_repos:
        if repo_dir.exists():
            code, output = run(["git", "pull", "--ff-only"], cwd=repo_dir)
            action = "pull"
        else:
            code, output = run(["git", "clone", "--depth", "1", f"https://github.com/{repo}.git", str(repo_dir)])
            action = "clone"
        metadata["git_action"] = action
        metadata["git_exit_code"] = code
        metadata["git_output_tail"] = output[-4000:]
        if repo_dir.exists():
            files["repo"] = str(repo_dir.relative_to(ROOT))

    write_json(out_dir / "metadata.json", metadata)
    ok = metadata.get("git_exit_code", 0) == 0
    return FetchResult(
        source_id=source["id"],
        status="ok" if ok else "git_error",
        local_dir=str(out_dir.relative_to(ROOT)),
        files=files,
        metadata=metadata,
        error=None if ok else metadata.get("git_output_tail"),
    )


def fetch_source(source: dict[str, Any], clone_repos: bool) -> FetchResult:
    out_dir = source_dir(source)
    kind = source.get("type", "webpage")
    if kind == "github_repo":
        return fetch_github_repo(source, out_dir, clone_repos)
    if kind == "reddit":
        return fetch_reddit(source, out_dir)
    if kind == "hacker_news":
        return fetch_hacker_news(source, out_dir)
    if kind == "arxiv":
        return fetch_arxiv(source, out_dir)
    if kind == "pypi":
        return fetch_pypi(source, out_dir)
    return fetch_url(source, out_dir, "raw")


def load_sources(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default=str(ROOT / "data" / "manifests" / "seed_sources.json"))
    parser.add_argument("--skip-repos", action="store_true", help="Do not clone GitHub repos.")
    parser.add_argument("--only", action="append", default=[], help="Fetch only the given source id. Repeatable.")
    parser.add_argument("--limit", type=int, default=0, help="Fetch at most N selected sources.")
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    manifest_sources = load_sources(manifest_path)
    sources = list(manifest_sources)
    if args.only:
        wanted = set(args.only)
        sources = [source for source in sources if source["id"] in wanted]
    if args.limit:
        sources = sources[: args.limit]

    all_results: list[dict[str, Any]] = []
    for index, source in enumerate(sources, start=1):
        started = time.time()
        print(f"[{index}/{len(sources)}] {source['id']} ({source.get('type', 'webpage')})", flush=True)
        try:
            result = fetch_source(source, clone_repos=not args.skip_repos)
        except Exception as exc:
            out_dir = source_dir(source)
            out_dir.mkdir(parents=True, exist_ok=True)
            result = FetchResult(
                source_id=source["id"],
                status="exception",
                local_dir=str(out_dir.relative_to(ROOT)),
                files={},
                metadata={"source": source, "fetched_at": utc_now()},
                error=repr(exc),
            )
            write_json(out_dir / "metadata.json", {**result.metadata, "error": result.error})
        elapsed = round(time.time() - started, 3)
        row = {
            "source_id": result.source_id,
            "status": result.status,
            "error": result.error,
            "local_dir": result.local_dir,
            "files": result.files,
            "elapsed_seconds": elapsed,
            "fetched_at": utc_now(),
            "source_url": source.get("url"),
            "source_type": source.get("type"),
            "priority": source.get("priority"),
            "tags": source.get("tags", []),
        }
        append_jsonl(LOG_PATH, row)
        all_results.append(row)
        print(f"  -> {result.status} {result.local_dir}", flush=True)

    existing: dict[str, dict[str, Any]] = {}
    if SOURCES_PATH.exists():
        for line in SOURCES_PATH.read_text(encoding="utf-8").splitlines():
            if line.strip():
                row = json.loads(line)
                existing[row["source_id"]] = row
    for row in all_results:
        existing[row["source_id"]] = row
    ordered_ids = [source["id"] for source in manifest_sources]
    merged = [existing[source_id] for source_id in ordered_ids if source_id in existing]
    merged.extend(row for source_id, row in existing.items() if source_id not in set(ordered_ids))
    SOURCES_PATH.parent.mkdir(parents=True, exist_ok=True)
    SOURCES_PATH.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in merged),
        encoding="utf-8",
    )
    ok = sum(1 for row in all_results if row["status"] == "ok")
    print(f"Done. ok={ok} total={len(all_results)} manifest={SOURCES_PATH.relative_to(ROOT)}")
    return 0 if ok == len(all_results) else 1


if __name__ == "__main__":
    sys.exit(main())
