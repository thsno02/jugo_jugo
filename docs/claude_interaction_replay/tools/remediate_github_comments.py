#!/usr/bin/env python3
"""Replace event-shaped GitHub comments with readable episode comments."""

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
PACKET_PATHS = sorted(PUBLISH.glob("packets-*.json"))
EVENT_PATHS = sorted((BASE / "events").glob("*.jsonl"))
DEFAULT_REPO = "thsno02/jugo_jugo"
DEFAULT_PILOTS = [
    REMEDIATION / "pilot-v0-v1.json",
    REMEDIATION / "pilot-v2-v3.json",
    REMEDIATION / "pilot-v4-v5.json",
]
FORBIDDEN_LABELS = (
    "事件性质",
    "当时状态",
    "关键判断 1",
    "推理日志",
    "core insight / action / effect",
    "用户输入（user.verbatim）",
)
MARKER_RE = re.compile(r"<!--\s*archive-events:\s*(.*?)\s*-->", re.DOTALL)


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


def marker_ids(body: str) -> list[str]:
    matches = MARKER_RE.findall(body or "")
    if not matches:
        return []
    if len(matches) > 1:
        raise RuntimeError("A comment contains more than one archive-events marker")
    return [item for item in re.split(r"[\s,]+", matches[0].strip()) if item]


def dequote_markdown(text: str) -> str:
    lines = []
    for line in text.replace("\r\n", "\n").split("\n"):
        ordered_quote = re.match(r"^\s*\d+\.\s+>\s?(.*)$", line)
        indented_quote = re.match(r"^\s+>\s?(.*)$", line)
        if ordered_quote:
            lines.append(ordered_quote.group(1))
        elif indented_quote:
            lines.append(indented_quote.group(1))
        elif line == ">":
            lines.append("")
        elif line.startswith("> "):
            lines.append(line[2:])
        else:
            lines.append(line)
    return "\n".join(lines)


def load_expected_events() -> dict[str, list[str]]:
    expected: dict[str, list[str]] = {}
    for path in PACKET_PATHS:
        packet = load_json(path)
        for issue in packet["issues"]:
            event_ids = [
                event_id
                for comment in issue.get("comments", [])
                for event_id in comment.get("event_ids", [])
            ]
            if event_ids:
                expected[issue["slug"]] = event_ids
    return expected


def load_event_inputs() -> dict[str, str]:
    events: dict[str, str] = {}
    for path in EVENT_PATHS:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            event = json.loads(line)
            events[event["event_id"]] = event["user"]["verbatim"]
    return events


def load_pilots(paths: list[Path]) -> list[dict]:
    issues = []
    for path in paths:
        payload = load_json(path)
        if payload.get("schema_version") != "1.0.0":
            raise RuntimeError(f"Unsupported pilot schema: {path}")
        for issue in payload["issues"]:
            issue = dict(issue)
            issue["pilot_path"] = str(path.relative_to(BASE))
            issues.append(issue)
    slugs = [issue["slug"] for issue in issues]
    if len(slugs) != len(set(slugs)):
        raise RuntimeError("Duplicate issue slugs across pilot files")
    return issues


def mapped_issue_number(publication_map: dict, slug: str) -> int:
    if slug == publication_map["root_issue"]["slug"]:
        return publication_map["root_issue"]["number"]
    if slug in publication_map["version_issues"]:
        return publication_map["version_issues"][slug]["number"]
    return publication_map["issue_map"][slug]["number"]


def mapped_issue_entry(publication_map: dict, slug: str) -> dict:
    if slug == publication_map["root_issue"]["slug"]:
        return publication_map["root_issue"]
    if slug in publication_map["version_issues"]:
        return publication_map["version_issues"][slug]
    return publication_map["issue_map"][slug]


def validate_pilots(
    issues: list[dict],
    expected_by_slug: dict[str, list[str]],
    event_inputs: dict[str, str],
    publication_map: dict,
) -> None:
    for issue in issues:
        slug = issue["slug"]
        if slug not in expected_by_slug:
            raise RuntimeError(f"Unknown or eventless issue slug: {slug}")
        mapped_number = mapped_issue_number(publication_map, slug)
        if issue["issue_number"] != mapped_number:
            raise RuntimeError(
                f"Issue number mismatch for {slug}: "
                f"{issue['issue_number']} != {mapped_number}"
            )
        if issue.get("desired_state") not in {"open", "closed"}:
            raise RuntimeError(f"Missing or invalid desired_state for {slug}")
        if not issue.get("state_rationale", "").strip():
            raise RuntimeError(f"Missing state_rationale for {slug}")
        episodes = issue.get("episodes", [])
        if not episodes:
            raise RuntimeError(f"No episodes for {slug}")
        flattened = [
            event_id
            for episode in episodes
            for event_id in episode.get("event_ids", [])
        ]
        if flattened != expected_by_slug[slug]:
            raise RuntimeError(f"Event order or coverage mismatch for {slug}")
        if len(flattened) != len(set(flattened)):
            raise RuntimeError(f"Duplicate event IDs in pilot for {slug}")

        for episode in episodes:
            title = episode["episode_title"]
            body = episode["body"].replace("\r\n", "\n").rstrip()
            event_ids = episode["event_ids"]
            if not body.startswith(f"### {title}\n"):
                raise RuntimeError(f"Episode title/body mismatch in {slug}: {title}")
            if "<details>" not in body or "完整用户输入" not in body:
                raise RuntimeError(f"Missing raw-input details in {slug}: {title}")
            bad_labels = [label for label in FORBIDDEN_LABELS if label in body]
            if bad_labels:
                raise RuntimeError(
                    f"Template labels remain in {slug}/{title}: {bad_labels}"
                )
            if marker_ids(body) != event_ids:
                raise RuntimeError(f"Archive marker mismatch in {slug}: {title}")
            readable_body = dequote_markdown(body)
            for event_id in event_ids:
                raw_input = event_inputs[event_id].replace("\r\n", "\n").strip()
                if raw_input not in readable_body:
                    raise RuntimeError(
                        f"Raw user input missing from {slug}/{title}: {event_id}"
                    )


def fetch_issue_comments(repo: str, issue_number: int) -> list[dict]:
    comments = gh(
        "GET",
        f"repos/{repo}/issues/{issue_number}/comments?per_page=100",
    )
    if not isinstance(comments, list):
        raise RuntimeError(f"Unexpected comments response for issue #{issue_number}")
    return sorted(comments, key=lambda item: (item["created_at"], item["id"]))


def index_remote_events(
    comments: list[dict], expected_ids: list[str]
) -> tuple[dict[str, dict], dict[int, dict]]:
    expected = set(expected_ids)
    by_event: dict[str, dict] = {}
    by_comment: dict[int, dict] = {}
    for comment in comments:
        ids = marker_ids(comment.get("body") or "")
        if not ids:
            continue
        if not set(ids).issubset(expected):
            continue
        enriched = dict(comment)
        enriched["event_ids"] = ids
        by_comment[comment["id"]] = enriched
        for event_id in ids:
            if event_id in by_event:
                raise RuntimeError(f"Remote event is duplicated: {event_id}")
            by_event[event_id] = enriched
    missing = [event_id for event_id in expected_ids if event_id not in by_event]
    if missing:
        raise RuntimeError(f"Remote events are missing: {missing}")
    return by_event, by_comment


def build_plan(repo: str, issues: list[dict], expected_by_slug: dict[str, list[str]]) -> list[dict]:
    plans = []
    for issue in issues:
        remote_issue = gh("GET", f"repos/{repo}/issues/{issue['issue_number']}")
        if not isinstance(remote_issue, dict):
            raise RuntimeError(f"Unexpected issue response for #{issue['issue_number']}")
        comments = fetch_issue_comments(repo, issue["issue_number"])
        desired_state = issue["desired_state"]
        needs_state_change = remote_issue["state"] != desired_state
        transition_comment = issue.get("state_transition_comment", "").strip()
        if needs_state_change and desired_state == "open" and not transition_comment:
            raise RuntimeError(f"Reopening {issue['slug']} requires state_transition_comment")
        by_event, by_comment = index_remote_events(
            comments, expected_by_slug[issue["slug"]]
        )
        episode_plans = []
        retained_ids: set[int] = set()
        for episode in issue["episodes"]:
            first = episode["event_ids"][0]
            anchor = by_event[first]
            involved = {
                by_event[event_id]["id"] for event_id in episode["event_ids"]
            }
            retained_ids.add(anchor["id"])
            episode_plans.append(
                {
                    "episode_title": episode["episode_title"],
                    "event_ids": episode["event_ids"],
                    "body": episode["body"].rstrip(),
                    "anchor_comment_id": anchor["id"],
                    "anchor_url": anchor["html_url"],
                    "delete_comment_ids": sorted(involved - {anchor["id"]}),
                    "needs_update": (anchor.get("body") or "").rstrip()
                    != episode["body"].rstrip(),
                }
            )
        event_comment_ids = set(by_comment)
        planned_deletes = {
            comment_id
            for episode in episode_plans
            for comment_id in episode["delete_comment_ids"]
        }
        if retained_ids | planned_deletes != event_comment_ids:
            raise RuntimeError(f"Remote comment plan is incomplete for {issue['slug']}")
        plans.append(
            {
                "slug": issue["slug"],
                "issue_number": issue["issue_number"],
                "pilot_path": issue["pilot_path"],
                "current_state": remote_issue["state"],
                "desired_state": desired_state,
                "state_rationale": issue["state_rationale"],
                "state_transition_comment": transition_comment,
                "needs_state_change": needs_state_change,
                "old_event_comment_count": len(event_comment_ids),
                "new_episode_comment_count": len(episode_plans),
                "episodes": episode_plans,
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
                "issue_number": plan["issue_number"],
                "comments": plan["remote_comments"],
            }
            for plan in plans
        ],
    }


def verify_remote_issue(
    repo: str, plan: dict, expected_ids: list[str]
) -> dict[str, dict]:
    comments = fetch_issue_comments(repo, plan["issue_number"])
    by_event, by_comment = index_remote_events(comments, expected_ids)
    event_comments = [
        item
        for item in by_comment.values()
        if set(item["event_ids"]).issubset(set(expected_ids))
    ]
    if len(event_comments) != plan["new_episode_comment_count"]:
        raise RuntimeError(f"Remote episode count mismatch for {plan['slug']}")
    for episode in plan["episodes"]:
        anchor = next(
            item
            for item in event_comments
            if item["id"] == episode["anchor_comment_id"]
        )
        if marker_ids(anchor["body"]) != episode["event_ids"]:
            raise RuntimeError(
                f"Remote archive marker mismatch for {plan['slug']}/"
                f"{episode['episode_title']}"
            )
        if anchor["body"].rstrip() != episode["body"].rstrip():
            raise RuntimeError(
                f"Remote body mismatch for {plan['slug']}/{episode['episode_title']}"
            )
    return by_event


def apply_plan(
    repo: str,
    plans: list[dict],
    expected_by_slug: dict[str, list[str]],
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
        deleted: list[int] = []
        transition_comment_id = None
        for episode in plan["episodes"]:
            if episode["needs_update"]:
                gh(
                    "PATCH",
                    f"repos/{repo}/issues/comments/{episode['anchor_comment_id']}",
                    {"body": episode["body"]},
                )
                time.sleep(delay)
            for comment_id in episode["delete_comment_ids"]:
                gh("DELETE", f"repos/{repo}/issues/comments/{comment_id}")
                deleted.append(comment_id)
                time.sleep(delay)

        by_event = verify_remote_issue(
            repo, plan, expected_by_slug[plan["slug"]]
        )
        if plan["needs_state_change"]:
            if plan["desired_state"] == "open":
                marker = f"<!-- state-audit: {plan['slug']} -->"
                existing = next(
                    (
                        comment
                        for comment in plan["remote_comments"]
                        if marker in (comment.get("body") or "")
                    ),
                    None,
                )
                if existing is None:
                    transition = gh(
                        "POST",
                        f"repos/{repo}/issues/{plan['issue_number']}/comments",
                        {"body": plan["state_transition_comment"].rstrip() + "\n\n" + marker},
                    )
                    if not isinstance(transition, dict):
                        raise RuntimeError(f"Unexpected state comment response for {plan['slug']}")
                    transition_comment_id = transition["id"]
                    time.sleep(delay)
                else:
                    transition_comment_id = existing["id"]
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
        if not isinstance(remote_issue, dict) or remote_issue["state"] != plan["desired_state"]:
            raise RuntimeError(f"Remote state mismatch for {plan['slug']}")
        for event_id, comment in by_event.items():
            publication_map["event_map"][event_id] = {
                "issue_number": plan["issue_number"],
                "comment_id": comment["id"],
                "url": comment["html_url"],
            }
        state_entry = mapped_issue_entry(publication_map, plan["slug"])
        state_entry["closed"] = plan["desired_state"] == "closed"
        state_entry["state_rationale"] = plan["state_rationale"]
        if transition_comment_id is not None:
            state_entry["state_transition_comment_id"] = transition_comment_id
        save_json(MAP_PATH, publication_map)
        result["issues"].append(
            {
                "slug": plan["slug"],
                "issue_number": plan["issue_number"],
                "old_event_comment_count": plan["old_event_comment_count"],
                "new_episode_comment_count": plan["new_episode_comment_count"],
                "desired_state": plan["desired_state"],
                "state_rationale": plan["state_rationale"],
                "state_transition_comment_id": transition_comment_id,
                "deleted_comment_ids": deleted,
                "episodes": [
                    {
                        "episode_title": episode["episode_title"],
                        "event_ids": episode["event_ids"],
                        "comment_id": episode["anchor_comment_id"],
                        "url": episode["anchor_url"],
                    }
                    for episode in plan["episodes"]
                ],
            }
        )
        print(
            f"migrated #{plan['issue_number']} {plan['slug']}: "
            f"{plan['old_event_comment_count']} -> "
            f"{plan['new_episode_comment_count']} comments",
            flush=True,
        )
    result["status"] = "complete"
    result["completed_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--pilot", action="append", type=Path)
    parser.add_argument("--backup", type=Path)
    parser.add_argument("--result", type=Path)
    parser.add_argument("--delay", type=float, default=0.6)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    pilot_paths = args.pilot or DEFAULT_PILOTS
    pilot_paths = [path if path.is_absolute() else BASE / path for path in pilot_paths]
    publication_map = load_json(MAP_PATH)
    expected_by_slug = load_expected_events()
    event_inputs = load_event_inputs()
    issues = load_pilots(pilot_paths)
    validate_pilots(issues, expected_by_slug, event_inputs, publication_map)
    plans = build_plan(args.repo, issues, expected_by_slug)

    summary = {
        "issues": len(plans),
        "events": sum(
            len(event_ids)
            for issue in issues
            for event_ids in [
                [
                    event_id
                    for episode in issue["episodes"]
                    for event_id in episode["event_ids"]
                ]
            ]
        ),
        "old_comments": sum(plan["old_event_comment_count"] for plan in plans),
        "new_comments": sum(plan["new_episode_comment_count"] for plan in plans),
        "delete_comments": sum(
            len(episode["delete_comment_ids"])
            for plan in plans
            for episode in plan["episodes"]
        ),
        "state_changes": sum(plan["needs_state_change"] for plan in plans),
    }
    print(json.dumps(summary, ensure_ascii=False), flush=True)
    if not args.apply:
        return 0

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = args.backup or REMEDIATION / "backups" / f"pilot-before-{stamp}.json"
    result_path = args.result or REMEDIATION / "pilot-publication-map.json"
    if backup_path.exists():
        raise RuntimeError(f"Refusing to overwrite backup: {backup_path}")
    save_json(backup_path, backup_payload(args.repo, plans))
    result = apply_plan(
        args.repo,
        plans,
        expected_by_slug,
        publication_map,
        args.delay,
    )
    result["backup_path"] = str(backup_path.relative_to(BASE))
    save_json(result_path, result)
    print(f"backup: {backup_path}", flush=True)
    print(f"result: {result_path}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
