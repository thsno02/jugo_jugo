#!/usr/bin/env python3
"""Publish audited interaction packets to GitHub Issues with resumable mapping."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
PUBLISH = BASE / "publish"
MAP_PATH = PUBLISH / "github-publication-map.json"
REPO = "thsno02/jugo_jugo"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save(data: dict) -> None:
    temporary = MAP_PATH.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(MAP_PATH)


def gh(method: str, endpoint: str, payload: dict | None = None) -> dict:
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


def issue_number(mapping: dict, slug: str) -> int:
    if slug == mapping["root_issue"]["slug"]:
        return mapping["root_issue"]["number"]
    if slug in mapping["version_issues"]:
        return mapping["version_issues"][slug]["number"]
    return mapping["issue_map"][slug]["number"]


def all_existing_titles() -> dict[str, dict]:
    issues = gh("GET", f"repos/{REPO}/issues?state=all&per_page=100")
    return {item["title"]: item for item in issues if "pull_request" not in item}


def create_issues(packets: list[dict], mapping: dict, delay: float) -> None:
    existing = all_existing_titles()
    reserved = set(mapping["version_issues"]) | {mapping["root_issue"]["slug"]}
    for packet in packets:
        for issue in packet["issues"]:
            slug = issue["slug"]
            if slug in reserved or slug in mapping["issue_map"]:
                continue
            found = existing.get(issue["title"])
            if found is None:
                found = gh(
                    "POST",
                    f"repos/{REPO}/issues",
                    {"title": issue["title"], "body": issue["body"]},
                )
                time.sleep(delay)
            mapping["issue_map"][slug] = {
                "number": found["number"],
                "url": found["html_url"],
                "title": found["title"],
                "author": found["user"]["login"],
                "parent_slug": issue.get("parent_slug"),
                "related_slugs": issue.get("related_slugs", []),
                "parent_linked": False,
            }
            save(mapping)
            print(f"issue #{found['number']}: {slug}", flush=True)


def link_parents(packets: list[dict], mapping: dict, delay: float) -> None:
    by_slug = {issue["slug"]: issue for packet in packets for issue in packet["issues"]}
    for slug, entry in mapping["issue_map"].items():
        if entry.get("parent_linked"):
            continue
        parent_slug = by_slug.get(slug, {}).get("parent_slug") or entry.get("parent_slug")
        if not parent_slug:
            entry["parent_linked"] = True
            save(mapping)
            continue
        parent_number = issue_number(mapping, parent_slug)
        child = gh("GET", f"repos/{REPO}/issues/{entry['number']}")
        try:
            gh(
                "POST",
                f"repos/{REPO}/issues/{parent_number}/sub_issues",
                {"sub_issue_id": child["id"]},
            )
        except RuntimeError as error:
            message = str(error).lower()
            if "already" in message:
                pass
            elif "layers of sub-issues" in message:
                version_ids = by_slug.get(slug, {}).get("version_ids", [])
                if not version_ids:
                    raise
                requested_parent = parent_slug
                parent_slug = f"{version_ids[0]}-changelog"
                parent_number = issue_number(mapping, parent_slug)
                gh(
                    "POST",
                    f"repos/{REPO}/issues/{parent_number}/sub_issues",
                    {"sub_issue_id": child["id"]},
                )
                current = gh("GET", f"repos/{REPO}/issues/{entry['number']}")
                requested_number = issue_number(mapping, requested_parent)
                note = f"\n\nDerived from: #{requested_number}"
                if note.strip() not in (current.get("body") or ""):
                    gh(
                        "PATCH",
                        f"repos/{REPO}/issues/{entry['number']}",
                        {"body": (current.get("body") or "") + note},
                    )
                entry["requested_parent_slug"] = requested_parent
                entry["parent_slug"] = parent_slug
                entry["depth_fallback"] = True
            else:
                raise
        entry["parent_linked"] = True
        save(mapping)
        time.sleep(delay)
        print(f"parent #{parent_number} <- #{entry['number']}", flush=True)


def publish_comments(packets: list[dict], mapping: dict, delay: float) -> None:
    for packet in packets:
        for issue in packet["issues"]:
            number = issue_number(mapping, issue["slug"])
            for comment in issue.get("comments", []):
                event_ids = comment["event_ids"]
                mapped = [event_id in mapping["event_map"] for event_id in event_ids]
                if all(mapped):
                    continue
                if any(mapped):
                    raise RuntimeError(f"Partially mapped comment: {event_ids}")
                footer = "\n\n<!-- archive-events: " + ", ".join(event_ids) + " -->"
                result = gh(
                    "POST",
                    f"repos/{REPO}/issues/{number}/comments",
                    {"body": comment["body"] + footer},
                )
                for event_id in event_ids:
                    mapping["event_map"][event_id] = {
                        "issue_number": number,
                        "comment_id": result["id"],
                        "url": result["html_url"],
                    }
                mapping["coverage"]["published_events"] = len(mapping["event_map"])
                save(mapping)
                time.sleep(delay)
                print(f"comment {result['id']} on #{number}: {event_ids[0]}", flush=True)


def update_related_links(packets: list[dict], mapping: dict, delay: float) -> None:
    by_slug = {issue["slug"]: issue for packet in packets for issue in packet["issues"]}
    for slug, entry in mapping["issue_map"].items():
        if entry.get("relations_written"):
            continue
        related = by_slug.get(slug, {}).get("related_slugs", [])
        if related:
            numbers = [issue_number(mapping, item) for item in related]
            current = gh("GET", f"repos/{REPO}/issues/{entry['number']}")
            suffix = "\n\nRelated: " + ", ".join(f"#{number}" for number in numbers)
            if suffix.strip() not in (current.get("body") or ""):
                gh(
                    "PATCH",
                    f"repos/{REPO}/issues/{entry['number']}",
                    {"body": (current.get("body") or "") + suffix},
                )
                time.sleep(delay)
        entry["relations_written"] = True
        save(mapping)


def close_completed_issues(packets: list[dict], mapping: dict, delay: float) -> None:
    for packet in packets:
        for issue in packet["issues"]:
            if not any(comment.get("close_after") for comment in issue.get("comments", [])):
                continue
            slug = issue["slug"]
            number = issue_number(mapping, slug)
            if slug in mapping["issue_map"]:
                entry = mapping["issue_map"][slug]
            else:
                entry = mapping["version_issues"].setdefault(slug, {"number": number})
            if entry.get("closed"):
                continue
            gh(
                "PATCH",
                f"repos/{REPO}/issues/{number}",
                {"state": "closed", "state_reason": "completed"},
            )
            entry["closed"] = True
            save(mapping)
            time.sleep(delay)
            print(f"closed #{number}: {slug}", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--delay", type=float, default=0.85)
    parser.add_argument("--issues-only", action="store_true")
    args = parser.parse_args()

    packet_paths = sorted(PUBLISH.glob("packets-*.json"))
    packets = [load(path) for path in packet_paths]
    mapping = load(MAP_PATH)
    mapped_ids = [
        event_id
        for packet in packets
        for issue in packet["issues"]
        for comment in issue.get("comments", [])
        for event_id in comment["event_ids"]
    ]
    if len(mapped_ids) != len(set(mapped_ids)):
        raise RuntimeError("Duplicate event IDs across publication packets")
    mapping["coverage"]["mapped_events"] = len(mapped_ids)
    save(mapping)

    create_issues(packets, mapping, args.delay)
    link_parents(packets, mapping, args.delay)
    update_related_links(packets, mapping, args.delay)
    if not args.issues_only:
        publish_comments(packets, mapping, args.delay)
        close_completed_issues(packets, mapping, args.delay)
    mapping["status"] = (
        "complete"
        if mapping["coverage"]["published_events"] == mapping["coverage"]["expected_events"]
        else "in_progress"
    )
    save(mapping)
    print(json.dumps(mapping["coverage"], ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
