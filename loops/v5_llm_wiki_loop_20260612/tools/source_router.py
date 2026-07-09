#!/usr/bin/env python3
"""
source_router.py — 逐类型 boundary-read dispatch + 质量门控。

用法:
    python source_router.py <source_type> <slug>
    python source_router.py --scan-all

返回仓库根相对路径（如 data/raw/webpage/llm-wiki-net/markdown.md）。
质量门控: < 500 字节或含 blocked/captcha/403 -> scrape_status: failed。
"""

import sys
import os
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
RAW_DIR = REPO_ROOT / "data" / "raw"

BLOCKED_KEYWORDS = ["blocked", "captcha", "403 forbidden", "access denied",
                    "you have been blocked", "network security"]
MIN_BYTES = 500


def quality_gate(filepath: Path) -> tuple[bool, str]:
    """检查文件是否通过质量门控。返回 (passed, reason)。"""
    if not filepath.exists():
        return False, "file_not_found"
    size = filepath.stat().st_size
    if size < MIN_BYTES:
        content = filepath.read_text(errors="replace").lower()
        for kw in BLOCKED_KEYWORDS:
            if kw in content:
                return False, f"blocked_content ({kw})"
        return False, f"too_small ({size}B)"
    content_head = filepath.read_bytes()[:2048].decode(errors="replace").lower()
    for kw in BLOCKED_KEYWORDS:
        if kw in content_head:
            return False, f"blocked_content ({kw})"
    return True, "ok"


def route_arxiv(slug_dir: Path) -> list[str] | None:
    """arxiv: agent_source_bundle.txt (primary)"""
    bundle = slug_dir / "agent_source_bundle.txt"
    if bundle.exists():
        passed, reason = quality_gate(bundle)
        if passed:
            return [str(bundle.relative_to(REPO_ROOT))]
    return None


def route_webpage(slug_dir: Path) -> list[str] | None:
    """webpage: markdown.md > text.txt"""
    for fname in ["markdown.md", "text.txt"]:
        f = slug_dir / fname
        if f.exists():
            passed, reason = quality_gate(f)
            if passed:
                return [str(f.relative_to(REPO_ROOT))]
    return None


def route_github_repo(slug_dir: Path) -> list[str] | None:
    """github_repo: material_bundle*.txt (可能多个 sub-bundle) > repo/README.md"""
    bundles = sorted(slug_dir.glob("material_bundle*.txt"))
    valid_bundles = []
    for b in bundles:
        passed, reason = quality_gate(b)
        if passed:
            valid_bundles.append(str(b.relative_to(REPO_ROOT)))
    if valid_bundles:
        return valid_bundles

    readme = slug_dir / "repo" / "README.md"
    if readme.exists():
        passed, reason = quality_gate(readme)
        if passed:
            return [str(readme.relative_to(REPO_ROOT))]
    return None


def route_text_only(slug_dir: Path) -> list[str] | None:
    """reddit/hacker_news/pypi/gist_raw: text.txt"""
    f = slug_dir / "text.txt"
    if f.exists():
        passed, reason = quality_gate(f)
        if passed:
            return [str(f.relative_to(REPO_ROOT))]
    return None


ROUTERS = {
    "arxiv": route_arxiv,
    "webpage": route_webpage,
    "github_repo": route_github_repo,
    "reddit": route_text_only,
    "hacker_news": route_text_only,
    "pypi": route_text_only,
    "gist_raw": route_text_only,
}


def route_source(source_type: str, slug: str) -> dict:
    """路由单个源，返回结果字典。"""
    slug_dir = RAW_DIR / source_type / slug
    if not slug_dir.exists():
        return {
            "source_type": source_type,
            "slug": slug,
            "status": "failed",
            "reason": "directory_not_found",
            "paths": [],
        }

    router = ROUTERS.get(source_type)
    if not router:
        return {
            "source_type": source_type,
            "slug": slug,
            "status": "failed",
            "reason": f"unknown_source_type: {source_type}",
            "paths": [],
        }

    paths = router(slug_dir)
    if paths:
        return {
            "source_type": source_type,
            "slug": slug,
            "status": "ok",
            "reason": "ok",
            "paths": paths,
        }
    else:
        return {
            "source_type": source_type,
            "slug": slug,
            "status": "failed",
            "reason": "no_valid_reading_surface",
            "paths": [],
        }


def scan_all() -> list[dict]:
    """扫描全部 data/raw/ 源，返回路由结果列表。"""
    results = []
    for source_type in sorted(RAW_DIR.iterdir()):
        if not source_type.is_dir():
            continue
        st_name = source_type.name
        for slug_dir in sorted(source_type.iterdir()):
            if not slug_dir.is_dir():
                continue
            results.append(route_source(st_name, slug_dir.name))
    return results


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--scan-all":
        results = scan_all()
        ok = [r for r in results if r["status"] == "ok"]
        failed = [r for r in results if r["status"] == "failed"]
        print(f"=== Source Router Scan ===")
        print(f"Total: {len(results)} | OK: {len(ok)} | Failed: {len(failed)}")
        print()
        if failed:
            print("--- FAILED ---")
            for r in failed:
                print(f"  [{r['source_type']}] {r['slug']}: {r['reason']}")
            print()
        print("--- OK ---")
        for r in ok:
            for p in r["paths"]:
                print(f"  [{r['source_type']}] {r['slug']}: {p}")
    elif len(sys.argv) == 3:
        source_type, slug = sys.argv[1], sys.argv[2]
        result = route_source(source_type, slug)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Usage: {sys.argv[0]} <source_type> <slug>")
        print(f"       {sys.argv[0]} --scan-all")
        sys.exit(1)


if __name__ == "__main__":
    main()
