#!/usr/bin/env python3
"""Publish readable v0-v5 ChangeLog narratives with backups and state checks."""

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
DEFAULT_INPUT = REMEDIATION / "version-changelogs.json"
DEFAULT_REPO = "thsno02/jugo_jugo"
MARKER_RE = re.compile(r"<!--\s*version-narrative:\s*([^>]+?)\s*-->")


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
        raise RuntimeError("A version comment contains multiple narrative markers")
    return matches[0].strip()


def rendered_comment(comment: dict) -> str:
    title = comment["title"]
    body = comment["body"].rstrip()
    if body.startswith("### "):
        if not body.startswith(f"### {title}\n"):
            raise RuntimeError(f"Comment title/body mismatch: {title}")
        return body
    return f"### {title}\n\n{body}"


def fetch_comments(repo: str, issue_number: int) -> list[dict]:
    comments = gh(
        "GET",
        f"repos/{repo}/issues/{issue_number}/comments?per_page=100",
    )
    if not isinstance(comments, list):
        raise RuntimeError(f"Unexpected comments response for #{issue_number}")
    return sorted(comments, key=lambda item: (item["created_at"], item["id"]))


def validate(payload: dict, publication_map: dict) -> list[dict]:
    if payload.get("schema_version") != "1.0.0":
        raise RuntimeError("Unsupported version narrative schema")
    versions = payload.get("versions", [])
    expected = {f"v{index}-changelog" for index in range(6)}
    slugs = [version.get("slug") for version in versions]
    if set(slugs) != expected or len(slugs) != len(expected):
        raise RuntimeError("Version narratives must contain v0-v5 exactly once")

    seen_markers: set[str] = set()
    for version in versions:
        slug = version["slug"]
        mapped = publication_map["version_issues"][slug]["number"]
        if version.get("issue_number") != mapped:
            raise RuntimeError(f"Issue number mismatch for {slug}")
        if version.get("desired_state") not in {"open", "closed"}:
            raise RuntimeError(f"Invalid desired_state for {slug}")
        if not version.get("state_rationale", "").strip():
            raise RuntimeError(f"Missing state_rationale for {slug}")
        if not version.get("body", "").strip():
            raise RuntimeError(f"Missing issue body for {slug}")
        comments = version.get("comments", [])
        if len(comments) != 2:
            raise RuntimeError(f"Expected two narrative comments for {slug}")
        keys = [comment.get("comment_key") for comment in comments]
        if len(keys) != len(set(keys)):
            raise RuntimeError(f"Duplicate comment keys for {slug}")
        for comment in comments:
            title = comment["title"]
            body = rendered_comment(comment)
            expected_marker = f"{slug.removesuffix('-changelog')}:{comment['comment_key']}"
            if marker(body) != expected_marker:
                raise RuntimeError(f"Version marker mismatch for {slug}/{title}")
            if expected_marker in seen_markers:
                raise RuntimeError(f"Duplicate version marker: {expected_marker}")
            seen_markers.add(expected_marker)
    return sorted(versions, key=lambda item: item["issue_number"])


def build_plan(repo: str, versions: list[dict]) -> list[dict]:
    plans = []
    for version in versions:
        issue = gh("GET", f"repos/{repo}/issues/{version['issue_number']}")
        if not isinstance(issue, dict):
            raise RuntimeError(f"Unexpected issue response for #{version['issue_number']}")
        comments = fetch_comments(repo, version["issue_number"])
        existing_by_marker = {
            item_marker: comment
            for comment in comments
            if (item_marker := marker(comment.get("body") or "")) is not None
        }
        comment_plans = []
        for comment in version["comments"]:
            body = rendered_comment(comment)
            item_marker = marker(body)
            existing = existing_by_marker.get(item_marker)
            comment_plans.append(
                {
                    "comment_key": comment["comment_key"],
                    "title": comment["title"],
                    "body": body,
                    "marker": item_marker,
                    "comment_id": existing["id"] if existing else None,
                    "url": existing["html_url"] if existing else None,
                    "needs_update": existing is None
                    or (existing.get("body") or "").rstrip() != body,
                }
            )
        desired_state = version["desired_state"]
        needs_state_change = issue["state"] != desired_state
        if needs_state_change and desired_state == "open" and not version.get(
            "state_transition_comment", ""
        ).strip():
            raise RuntimeError(
                f"Reopening {version['slug']} requires state_transition_comment"
            )
        plans.append(
            {
                "slug": version["slug"],
                "issue_number": version["issue_number"],
                "body": version["body"].rstrip(),
                "body_needs_update": (issue.get("body") or "").rstrip()
                != version["body"].rstrip(),
                "current_state": issue["state"],
                "desired_state": desired_state,
                "state_rationale": version["state_rationale"],
                "state_transition_comment": version.get(
                    "state_transition_comment", ""
                ).strip(),
                "needs_state_change": needs_state_change,
                "comments": comment_plans,
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
        "versions": [
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
        "versions": [],
    }
    for plan in plans:
        if plan["body_needs_update"]:
            gh(
                "PATCH",
                f"repos/{repo}/issues/{plan['issue_number']}",
                {"body": plan["body"]},
            )
            time.sleep(delay)

        published_comments = []
        for comment in plan["comments"]:
            if comment["comment_id"] is None:
                remote = gh(
                    "POST",
                    f"repos/{repo}/issues/{plan['issue_number']}/comments",
                    {"body": comment["body"]},
                )
                if not isinstance(remote, dict):
                    raise RuntimeError(f"Unexpected comment response for {plan['slug']}")
                comment_id = remote["id"]
                url = remote["html_url"]
            else:
                comment_id = comment["comment_id"]
                url = comment["url"]
                if comment["needs_update"]:
                    gh(
                        "PATCH",
                        f"repos/{repo}/issues/comments/{comment_id}",
                        {"body": comment["body"]},
                    )
            if comment["needs_update"]:
                time.sleep(delay)
            published_comments.append(
                {
                    "comment_key": comment["comment_key"],
                    "comment_id": comment_id,
                    "url": url,
                }
            )

        transition_comment_id = None
        if plan["needs_state_change"] and plan["desired_state"] == "open":
            transition = gh(
                "POST",
                f"repos/{repo}/issues/{plan['issue_number']}/comments",
                {"body": plan["state_transition_comment"]},
            )
            if not isinstance(transition, dict):
                raise RuntimeError(f"Unexpected state comment for {plan['slug']}")
            transition_comment_id = transition["id"]
            time.sleep(delay)
        if plan["needs_state_change"]:
            gh(
                "PATCH",
                f"repos/{repo}/issues/{plan['issue_number']}",
                {
                    "state": plan["desired_state"],
                    "state_reason": (
                        "completed" if plan["desired_state"] == "closed" else "reopened"
                    ),
                },
            )
            time.sleep(delay)

        remote_issue = gh("GET", f"repos/{repo}/issues/{plan['issue_number']}")
        remote_comments = fetch_comments(repo, plan["issue_number"])
        if not isinstance(remote_issue, dict) or remote_issue["state"] != plan["desired_state"]:
            raise RuntimeError(f"Remote state mismatch for {plan['slug']}")
        if (remote_issue.get("body") or "").rstrip() != plan["body"]:
            raise RuntimeError(f"Remote body mismatch for {plan['slug']}")
        remote_by_marker = {
            item_marker: comment
            for comment in remote_comments
            if (item_marker := marker(comment.get("body") or "")) is not None
        }
        for comment in plan["comments"]:
            if remote_by_marker[comment["marker"]]["body"].rstrip() != comment["body"]:
                raise RuntimeError(
                    f"Remote version comment mismatch for {plan['slug']}/{comment['title']}"
                )

        entry = publication_map["version_issues"][plan["slug"]]
        entry["closed"] = plan["desired_state"] == "closed"
        entry["state_rationale"] = plan["state_rationale"]
        entry["narrative_comments"] = published_comments
        if transition_comment_id is not None:
            entry["state_transition_comment_id"] = transition_comment_id
        save_json(MAP_PATH, publication_map)

        result["versions"].append(
            {
                "slug": plan["slug"],
                "issue_number": plan["issue_number"],
                "desired_state": plan["desired_state"],
                "state_rationale": plan["state_rationale"],
                "comments": published_comments,
                "state_transition_comment_id": transition_comment_id,
            }
        )
        print(f"published {plan['slug']} on #{plan['issue_number']}", flush=True)
    result["status"] = "complete"
    result["completed_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--backup", type=Path)
    parser.add_argument("--result", type=Path)
    parser.add_argument("--delay", type=float, default=0.6)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    input_path = args.input if args.input.is_absolute() else BASE / args.input
    publication_map = load_json(MAP_PATH)
    versions = validate(load_json(input_path), publication_map)
    plans = build_plan(args.repo, versions)
    summary = {
        "versions": len(plans),
        "body_updates": sum(plan["body_needs_update"] for plan in plans),
        "comment_creates": sum(
            comment["comment_id"] is None
            for plan in plans
            for comment in plan["comments"]
        ),
        "comment_updates": sum(
            comment["comment_id"] is not None and comment["needs_update"]
            for plan in plans
            for comment in plan["comments"]
        ),
        "state_changes": sum(plan["needs_state_change"] for plan in plans),
    }
    print(json.dumps(summary, ensure_ascii=False), flush=True)
    if not args.apply:
        return 0

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = args.backup or REMEDIATION / "backups" / f"versions-before-{stamp}.json"
    result_path = args.result or REMEDIATION / "version-publication-map.json"
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
