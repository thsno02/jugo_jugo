#!/usr/bin/env python3
"""Publish direct answer/status comments for all problem Issues."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import time
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
PUBLISH = BASE / "publish"
REMEDIATION = BASE / "remediation"
MAP_PATH = PUBLISH / "github-publication-map.json"
DEFAULT_REPO = "thsno02/jugo_jugo"
DEFAULT_INPUTS = sorted(REMEDIATION.glob("resolutions-*.json"))
MARKER_RE = re.compile(r"<!--\s*issue-resolution:\s*([^>]+?)\s*-->")
LINK_RE = re.compile(
    r"\n*<!-- issue-resolution-link:start -->.*?"
    r"<!-- issue-resolution-link:end -->\s*",
    re.DOTALL,
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def gh(method: str, endpoint: str, payload: dict | None = None) -> dict | list:
    command = ["gh", "api", "--method", method, endpoint]
    if payload is not None:
        command.extend(["--input", "-"])
    result = subprocess.run(
        command,
        input=json.dumps(payload, ensure_ascii=False) if payload is not None else None,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(f"gh api failed: {endpoint}: {result.stderr.strip()}")
    return json.loads(result.stdout) if result.stdout.strip() else {}


def marker(body: str) -> str | None:
    matches = MARKER_RE.findall(body or "")
    if not matches:
        return None
    if len(matches) != 1:
        raise RuntimeError("A resolution comment contains multiple markers")
    return matches[0].strip()


def fetch_comments(repo: str, issue_number: int) -> list[dict]:
    comments = gh(
        "GET",
        f"repos/{repo}/issues/{issue_number}/comments?per_page=100",
    )
    if not isinstance(comments, list):
        raise RuntimeError(f"Unexpected comments response for #{issue_number}")
    return sorted(comments, key=lambda item: (item["created_at"], item["id"]))


def load_inputs(paths: list[Path]) -> list[dict]:
    issues = []
    for path in paths:
        payload = load_json(path)
        if payload.get("schema_version") != "1.0.0":
            raise RuntimeError(f"Unsupported resolution schema: {path}")
        for issue in payload.get("issues", []):
            issue = dict(issue)
            issue["source_path"] = str(path.relative_to(BASE))
            issues.append(issue)
    return issues


def validate(issues: list[dict], publication_map: dict) -> list[dict]:
    expected = publication_map["issue_map"]
    slugs = [issue.get("slug") for issue in issues]
    if set(slugs) != set(expected) or len(slugs) != len(expected):
        missing = sorted(set(expected) - set(slugs))
        extra = sorted(set(slugs) - set(expected))
        raise RuntimeError(f"Resolution coverage mismatch: missing={missing}, extra={extra}")

    for issue in issues:
        slug = issue["slug"]
        mapped = expected[slug]
        if issue.get("issue_number") != mapped["number"]:
            raise RuntimeError(f"Issue number mismatch for {slug}")
        mapped_state = "closed" if mapped.get("closed", False) else "open"
        if issue.get("state") != mapped_state:
            raise RuntimeError(
                f"State mismatch for {slug}: {issue.get('state')} != {mapped_state}"
            )
        expected_kind = "answer" if mapped_state == "closed" else "current_status"
        if issue.get("kind") != expected_kind:
            raise RuntimeError(f"Resolution kind mismatch for {slug}")
        title = issue.get("title", "").strip()
        body = issue.get("body", "").replace("\r\n", "\n").rstrip()
        if not title or not body.startswith(f"### {title}\n"):
            raise RuntimeError(f"Resolution title/body mismatch for {slug}")
        if marker(body) != slug:
            raise RuntimeError(f"Resolution marker mismatch for {slug}")
        visible = body.split("<!-- issue-resolution:", 1)[0]
        if len(visible) < 180:
            raise RuntimeError(f"Resolution is too short for {slug}")
    return sorted(issues, key=lambda item: item["issue_number"])


def body_with_resolution_link(body: str, url: str, state: str) -> str:
    clean = LINK_RE.sub("", body or "").rstrip()
    label = "当前答案" if state == "closed" else "当前状态"
    link_text = "查看收口评论" if state == "closed" else "查看已知结论与关闭条件"
    block = (
        "<!-- issue-resolution-link:start -->\n"
        f"{label}：[{link_text}]({url})\n"
        "<!-- issue-resolution-link:end -->"
    )
    return clean + "\n\n" + block


def build_plan(repo: str, issues: list[dict]) -> list[dict]:
    plans = []
    for item in issues:
        issue = gh("GET", f"repos/{repo}/issues/{item['issue_number']}")
        if not isinstance(issue, dict):
            raise RuntimeError(f"Unexpected issue response for #{item['issue_number']}")
        if issue["state"] != item["state"]:
            raise RuntimeError(f"Remote state changed for {item['slug']}")
        comments = fetch_comments(repo, item["issue_number"])
        matches = [comment for comment in comments if marker(comment.get("body") or "") == item["slug"]]
        if len(matches) > 1:
            raise RuntimeError(f"Duplicate remote resolution comments for {item['slug']}")
        existing = matches[0] if matches else None
        plans.append(
            {
                "slug": item["slug"],
                "issue_number": item["issue_number"],
                "state": item["state"],
                "kind": item["kind"],
                "title": item["title"],
                "body": item["body"].rstrip(),
                "source_path": item["source_path"],
                "comment_id": existing["id"] if existing else None,
                "url": existing["html_url"] if existing else None,
                "comment_needs_update": existing is None
                or (existing.get("body") or "").rstrip() != item["body"].rstrip(),
                "remote_issue": issue,
                "remote_comments": comments,
            }
        )
    return plans


def backup_payload(repo: str, plans: list[dict]) -> dict:
    return {
        "schema_version": "1.0.0",
        "repository": repo,
        "captured_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "issues": [
            {
                "slug": plan["slug"],
                "issue": plan["remote_issue"],
                "comments": plan["remote_comments"],
            }
            for plan in plans
        ],
    }


def apply_plan(
    repo: str,
    plans: list[dict],
    publication_map: dict,
    delay: float,
) -> dict:
    result = {
        "schema_version": "1.0.0",
        "repository": repo,
        "status": "in_progress",
        "started_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "issues": [],
    }
    for plan in plans:
        if plan["comment_id"] is None:
            remote = gh(
                "POST",
                f"repos/{repo}/issues/{plan['issue_number']}/comments",
                {"body": plan["body"]},
            )
            if not isinstance(remote, dict):
                raise RuntimeError(f"Unexpected comment response for {plan['slug']}")
            comment_id = remote["id"]
            url = remote["html_url"]
        else:
            comment_id = plan["comment_id"]
            url = plan["url"]
            if plan["comment_needs_update"]:
                gh(
                    "PATCH",
                    f"repos/{repo}/issues/comments/{comment_id}",
                    {"body": plan["body"]},
                )
        if plan["comment_needs_update"]:
            time.sleep(delay)

        linked_body = body_with_resolution_link(
            plan["remote_issue"].get("body") or "",
            url,
            plan["state"],
        )
        if (plan["remote_issue"].get("body") or "").rstrip() != linked_body.rstrip():
            gh(
                "PATCH",
                f"repos/{repo}/issues/{plan['issue_number']}",
                {"body": linked_body},
            )
            time.sleep(delay)

        remote_issue = gh("GET", f"repos/{repo}/issues/{plan['issue_number']}")
        remote_comments = fetch_comments(repo, plan["issue_number"])
        if not isinstance(remote_issue, dict) or remote_issue["state"] != plan["state"]:
            raise RuntimeError(f"Remote state mismatch for {plan['slug']}")
        remote_resolution = next(
            comment
            for comment in remote_comments
            if marker(comment.get("body") or "") == plan["slug"]
        )
        if remote_resolution["body"].rstrip() != plan["body"]:
            raise RuntimeError(f"Remote resolution mismatch for {plan['slug']}")
        if url not in (remote_issue.get("body") or ""):
            raise RuntimeError(f"Resolution link missing from body for {plan['slug']}")

        entry = publication_map["issue_map"][plan["slug"]]
        entry["resolution"] = {
            "kind": plan["kind"],
            "title": plan["title"],
            "comment_id": comment_id,
            "url": url,
        }
        save_json(MAP_PATH, publication_map)
        result["issues"].append(
            {
                "slug": plan["slug"],
                "issue_number": plan["issue_number"],
                "state": plan["state"],
                "kind": plan["kind"],
                "title": plan["title"],
                "comment_id": comment_id,
                "url": url,
            }
        )
        print(f"published resolution for #{plan['issue_number']} {plan['slug']}", flush=True)
    result["status"] = "complete"
    result["completed_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--input", action="append", type=Path)
    parser.add_argument("--backup", type=Path)
    parser.add_argument("--result", type=Path)
    parser.add_argument("--delay", type=float, default=0.6)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    input_paths = args.input or DEFAULT_INPUTS
    input_paths = [path if path.is_absolute() else BASE / path for path in input_paths]
    publication_map = load_json(MAP_PATH)
    issues = validate(load_inputs(input_paths), publication_map)
    plans = build_plan(args.repo, issues)
    summary = {
        "issues": len(plans),
        "closed_answers": sum(plan["kind"] == "answer" for plan in plans),
        "open_statuses": sum(plan["kind"] == "current_status" for plan in plans),
        "comment_creates": sum(plan["comment_id"] is None for plan in plans),
        "comment_updates": sum(
            plan["comment_id"] is not None and plan["comment_needs_update"]
            for plan in plans
        ),
    }
    print(json.dumps(summary, ensure_ascii=False), flush=True)
    if not args.apply:
        return 0

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = args.backup or REMEDIATION / "backups" / f"resolutions-before-{stamp}.json"
    result_path = args.result or REMEDIATION / "resolution-publication-map.json"
    if backup_path.exists():
        raise RuntimeError(f"Refusing to overwrite backup: {backup_path}")
    save_json(backup_path, backup_payload(args.repo, plans))
    result = apply_plan(args.repo, plans, publication_map, args.delay)
    result["backup_path"] = str(backup_path.relative_to(BASE))
    save_json(result_path, result)
    print(f"backup: {backup_path}", flush=True)
    print(f"result: {result_path}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
