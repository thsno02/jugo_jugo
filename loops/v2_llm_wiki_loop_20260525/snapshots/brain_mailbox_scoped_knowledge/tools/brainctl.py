#!/usr/bin/env python3
"""Minimal brain mailbox controller for loop brain-agent experiments."""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
LOOP_ROOT = ROOT / "llm_wiki" / "loop"
BRAINS_ROOT = LOOP_ROOT / "brains"
LOG_ROOT = LOOP_ROOT / "logs"
MESSAGE_BUS = LOG_ROOT / "brain_message_bus.jsonl"
LIFECYCLE_LOG = LOG_ROOT / "subagent_lifecycle.jsonl"

DEFAULT_BRAINS = ("production", "similarity", "audit", "ops")


def now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def ensure_dirs() -> None:
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    BRAINS_ROOT.mkdir(parents=True, exist_ok=True)


def brain_dir(brain: str) -> Path:
    return BRAINS_ROOT / brain


def jsonl_path(brain: str, name: str) -> Path:
    return brain_dir(brain) / name


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows)
    path.write_text(text, encoding="utf-8")


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def read_json(path: Path, default: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def list_brains() -> list[str]:
    if not BRAINS_ROOT.exists():
        return list(DEFAULT_BRAINS)
    names = [
        p.name
        for p in BRAINS_ROOT.iterdir()
        if p.is_dir()
        and (p / "brain_state.json").exists()
        and (p / "inbox.jsonl").exists()
        and (p / "outbox.jsonl").exists()
    ]
    return sorted(set(names) | set(DEFAULT_BRAINS))


def message_id() -> str:
    return f"msg_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"


def bus(event: str, **fields: Any) -> None:
    append_jsonl(MESSAGE_BUS, {"event": event, "time": now(), **fields})


def lifecycle(event: str, **fields: Any) -> None:
    append_jsonl(LIFECYCLE_LOG, {"event": event, "time": now(), **fields})


def init_brains(args: argparse.Namespace) -> int:
    ensure_dirs()
    brains = args.brain or list(DEFAULT_BRAINS)
    for brain in brains:
        d = brain_dir(brain)
        d.mkdir(parents=True, exist_ok=True)
        for name in ("inbox.jsonl", "outbox.jsonl", "queue.jsonl"):
            path = d / name
            if not path.exists():
                path.write_text("", encoding="utf-8")
        state_path = d / "brain_state.json"
        if not state_path.exists():
            write_json(
                state_path,
                {
                    "brain": brain,
                    "status": "idle",
                    "updated_time": now(),
                    "last_message_id": None,
                    "notes": "Initialized by brainctl.",
                },
            )
        wake_path = d / "wake_required.json"
        if not wake_path.exists():
            write_wake(brain, False, "initialized")
    bus("brainctl_init", brains=brains)
    print("brainctl_init: ok")
    return 0


def write_wake(brain: str, wake_required: bool, reason: str, message_ids: list[str] | None = None) -> None:
    write_json(
        brain_dir(brain) / "wake_required.json",
        {
            "brain": brain,
            "wake_required": wake_required,
            "updated_time": now(),
            "reason": reason,
            "message_ids": message_ids or [],
        },
    )


def set_state(brain: str, status: str, message: dict[str, Any] | None = None) -> None:
    state_path = brain_dir(brain) / "brain_state.json"
    state = read_json(state_path, {"brain": brain})
    state.update(
        {
            "brain": brain,
            "status": status,
            "updated_time": now(),
            "last_message_id": message.get("message_id") if message else state.get("last_message_id"),
        }
    )
    write_json(state_path, state)


def find_message(rows: list[dict[str, Any]], mid: str) -> dict[str, Any] | None:
    for row in rows:
        if row.get("message_id") == mid:
            return row
    return None


def update_outbox_message(brain: str, mid: str, **updates: Any) -> bool:
    path = jsonl_path(brain, "outbox.jsonl")
    rows = read_jsonl(path)
    msg = find_message(rows, mid)
    if not msg:
        return False
    msg.update(updates)
    write_jsonl(path, rows)
    return True


def message_exists(brain: str, mailbox: str, mid: str) -> bool:
    return find_message(read_jsonl(jsonl_path(brain, mailbox)), mid) is not None


def send(args: argparse.Namespace) -> int:
    ensure_dirs()
    mid = args.message_id or message_id()
    msg = {
        "message_id": mid,
        "from": args.from_brain,
        "to": args.to_brain,
        "type": args.type,
        "status": "open",
        "subject": args.subject,
        "request": args.request,
        "required_response": args.required_response,
        "artifact_refs": args.artifact_ref or [],
        "created_time": now(),
        "routed_time": None,
        "claimed_by": None,
        "claimed_time": None,
        "completed_time": None,
        "response": None,
    }
    append_jsonl(jsonl_path(args.from_brain, "outbox.jsonl"), msg)
    bus("message_created", message_id=mid, from_brain=args.from_brain, to_brain=args.to_brain, type=args.type)
    print(mid)
    return 0


def route(args: argparse.Namespace) -> int:
    ensure_dirs()
    routed: list[str] = []
    for source in list_brains():
        outbox_path = jsonl_path(source, "outbox.jsonl")
        rows = read_jsonl(outbox_path)
        changed = False
        for msg in rows:
            mid = msg.get("message_id")
            target = msg.get("to")
            if not mid or not target:
                continue
            if msg.get("status") not in {"open", "routed"}:
                continue
            if message_exists(target, "inbox.jsonl", mid):
                if msg.get("status") == "open":
                    msg["status"] = "routed"
                    msg["routed_time"] = msg.get("routed_time") or now()
                    changed = True
                continue
            delivered = dict(msg)
            delivered["status"] = "routed"
            delivered["routed_time"] = now()
            append_jsonl(jsonl_path(target, "inbox.jsonl"), delivered)
            msg["status"] = "routed"
            msg["routed_time"] = delivered["routed_time"]
            changed = True
            routed.append(mid)
            bus("message_routed", message_id=mid, from_brain=source, to_brain=target, type=msg.get("type"))
        if changed:
            write_jsonl(outbox_path, rows)
    if not args.no_wake:
        mark_wake("route")
    print(json.dumps({"routed": routed}, ensure_ascii=False, sort_keys=True))
    return 0


def open_messages(brain: str) -> list[dict[str, Any]]:
    return [
        msg
        for msg in read_jsonl(jsonl_path(brain, "inbox.jsonl"))
        if msg.get("status") in {"open", "routed"}
    ]


def mark_wake(reason: str) -> dict[str, list[str]]:
    wake_map: dict[str, list[str]] = {}
    for brain in list_brains():
        mids = [msg["message_id"] for msg in open_messages(brain) if msg.get("message_id")]
        if mids:
            write_wake(brain, True, reason, mids)
            wake_map[brain] = mids
        else:
            write_wake(brain, False, "no_open_messages")
    bus("wake_marked", wake_map=wake_map, reason=reason)
    return wake_map


def hook(args: argparse.Namespace) -> int:
    route(argparse.Namespace(no_wake=True))
    wake_map = mark_wake(f"hook:{args.event}")
    print(json.dumps({"wake_required": wake_map}, ensure_ascii=False, sort_keys=True))
    return 0


def next_message(args: argparse.Namespace) -> int:
    messages = open_messages(args.brain)
    if not messages:
        print("{}")
        return 0
    print(json.dumps(messages[0], ensure_ascii=False, indent=2, sort_keys=True))
    return 0


def claim(args: argparse.Namespace) -> int:
    path = jsonl_path(args.brain, "inbox.jsonl")
    rows = read_jsonl(path)
    msg = find_message(rows, args.message_id)
    if not msg:
        print(f"missing_message: {args.message_id}", file=sys.stderr)
        return 1
    if msg.get("status") not in {"open", "routed"}:
        print(f"message_not_claimable: {args.message_id} status={msg.get('status')}", file=sys.stderr)
        return 1
    msg["status"] = "claimed"
    msg["claimed_by"] = args.agent_id
    msg["claimed_time"] = now()
    write_jsonl(path, rows)
    set_state(args.brain, "working", msg)
    bus("message_claimed", message_id=args.message_id, brain=args.brain, agent_id=args.agent_id)
    lifecycle("brain_message_claimed", brain=args.brain, agent_id=args.agent_id, message_id=args.message_id)
    mark_wake("claim")
    print("claim: ok")
    return 0


def complete(args: argparse.Namespace) -> int:
    path = jsonl_path(args.brain, "inbox.jsonl")
    rows = read_jsonl(path)
    msg = find_message(rows, args.message_id)
    if not msg:
        print(f"missing_message: {args.message_id}", file=sys.stderr)
        return 1
    if msg.get("status") not in {"claimed", "open", "routed"}:
        print(f"message_not_completable: {args.message_id} status={msg.get('status')}", file=sys.stderr)
        return 1
    msg["status"] = "resolved"
    msg["completed_time"] = now()
    msg["response"] = args.response
    msg["response_artifact_refs"] = args.artifact_ref or []
    write_jsonl(path, rows)
    set_state(args.brain, "idle", msg)
    bus("message_completed", message_id=args.message_id, brain=args.brain, response=args.response)
    lifecycle("brain_message_completed", brain=args.brain, message_id=args.message_id)
    source_brain = msg.get("from")
    if source_brain:
        update_outbox_message(
            source_brain,
            args.message_id,
            status="resolved",
            completed_time=msg["completed_time"],
            response=args.response,
            response_artifact_refs=args.artifact_ref or [],
        )

    if args.response_type:
        response_msg = {
            "message_id": args.response_message_id or message_id(),
            "from": args.brain,
            "to": args.to_brain or msg.get("from"),
            "type": args.response_type,
            "status": "open",
            "subject": f"Response to {args.message_id}: {msg.get('subject')}",
            "request": args.response,
            "required_response": args.required_response,
            "artifact_refs": args.artifact_ref or [],
            "responds_to": args.message_id,
            "created_time": now(),
            "routed_time": None,
            "claimed_by": None,
            "claimed_time": None,
            "completed_time": None,
            "response": None,
        }
        append_jsonl(jsonl_path(args.brain, "outbox.jsonl"), response_msg)
        bus(
            "response_created",
            message_id=response_msg["message_id"],
            responds_to=args.message_id,
            from_brain=args.brain,
            to_brain=response_msg["to"],
            type=args.response_type,
        )
    mark_wake("complete")
    print("complete: ok")
    return 0


def reconcile(args: argparse.Namespace) -> int:
    ensure_dirs()
    reconciled: list[str] = []
    for target in list_brains():
        for msg in read_jsonl(jsonl_path(target, "inbox.jsonl")):
            mid = msg.get("message_id")
            source = msg.get("from")
            if not mid or not source:
                continue
            if msg.get("status") not in {"resolved", "blocked"}:
                continue
            if update_outbox_message(
                source,
                mid,
                status=msg.get("status"),
                completed_time=msg.get("completed_time"),
                blocked_time=msg.get("blocked_time"),
                response=msg.get("response"),
                response_artifact_refs=msg.get("response_artifact_refs", []),
                blocked_reason=msg.get("blocked_reason"),
            ):
                reconciled.append(mid)
                bus("message_reconciled", message_id=mid, from_brain=source, to_brain=target, status=msg.get("status"))
    mark_wake("reconcile")
    print(json.dumps({"reconciled": sorted(set(reconciled))}, ensure_ascii=False, sort_keys=True))
    return 0


def block(args: argparse.Namespace) -> int:
    path = jsonl_path(args.brain, "inbox.jsonl")
    rows = read_jsonl(path)
    msg = find_message(rows, args.message_id)
    if not msg:
        print(f"missing_message: {args.message_id}", file=sys.stderr)
        return 1
    msg["status"] = "blocked"
    msg["blocked_time"] = now()
    msg["blocked_reason"] = args.reason
    write_jsonl(path, rows)
    set_state(args.brain, "blocked", msg)
    bus("message_blocked", message_id=args.message_id, brain=args.brain, reason=args.reason)
    lifecycle("brain_message_blocked", brain=args.brain, message_id=args.message_id)
    mark_wake("block")
    print("block: ok")
    return 0


def status(args: argparse.Namespace) -> int:
    data: dict[str, Any] = {}
    for brain in list_brains():
        data[brain] = {
            "inbox_open": len(open_messages(brain)),
            "inbox_claimed": sum(1 for msg in read_jsonl(jsonl_path(brain, "inbox.jsonl")) if msg.get("status") == "claimed"),
            "outbox_open": sum(1 for msg in read_jsonl(jsonl_path(brain, "outbox.jsonl")) if msg.get("status") == "open"),
            "outbox_routed": sum(1 for msg in read_jsonl(jsonl_path(brain, "outbox.jsonl")) if msg.get("status") == "routed"),
            "wake_required": read_json(brain_dir(brain) / "wake_required.json", {}).get("wake_required"),
            "state": read_json(brain_dir(brain) / "brain_state.json", {}).get("status"),
        }
    print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="Create brain mailbox files.")
    p.add_argument("--brain", action="append")
    p.set_defaults(func=init_brains)

    p = sub.add_parser("send", help="Append a message to a brain outbox.")
    p.add_argument("--from", dest="from_brain", required=True)
    p.add_argument("--to", dest="to_brain", required=True)
    p.add_argument("--type", required=True)
    p.add_argument("--subject", required=True)
    p.add_argument("--request", required=True)
    p.add_argument("--required-response", default="")
    p.add_argument("--artifact-ref", action="append")
    p.add_argument("--message-id")
    p.set_defaults(func=send)

    p = sub.add_parser("route", help="Route open outbox messages to target inboxes.")
    p.add_argument("--no-wake", action="store_true")
    p.set_defaults(func=route)

    p = sub.add_parser("hook", help="Hook-friendly route + wake marker command.")
    p.add_argument("--event", default="manual")
    p.set_defaults(func=hook)

    p = sub.add_parser("next", help="Print next open/routed message for a brain.")
    p.add_argument("--brain", required=True)
    p.set_defaults(func=next_message)

    p = sub.add_parser("claim", help="Claim a routed/open message.")
    p.add_argument("--brain", required=True)
    p.add_argument("--message-id", required=True)
    p.add_argument("--agent-id", required=True)
    p.set_defaults(func=claim)

    p = sub.add_parser("complete", help="Complete a claimed message and optionally create a response.")
    p.add_argument("--brain", required=True)
    p.add_argument("--message-id", required=True)
    p.add_argument("--response", required=True)
    p.add_argument("--artifact-ref", action="append")
    p.add_argument("--response-type")
    p.add_argument("--to-brain")
    p.add_argument("--required-response", default="")
    p.add_argument("--response-message-id")
    p.set_defaults(func=complete)

    p = sub.add_parser("reconcile", help="Reconcile source outbox statuses from target inbox completions.")
    p.set_defaults(func=reconcile)

    p = sub.add_parser("block", help="Mark a message blocked.")
    p.add_argument("--brain", required=True)
    p.add_argument("--message-id", required=True)
    p.add_argument("--reason", required=True)
    p.set_defaults(func=block)

    p = sub.add_parser("status", help="Print brain mailbox status.")
    p.set_defaults(func=status)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
