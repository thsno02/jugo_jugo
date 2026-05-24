#!/usr/bin/env python3
"""Render a sub-agent dispatch payload from prompts and task packet."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
LOOP_ROOT = ROOT / "llm_wiki" / "loop"


AGENT_TYPE_BY_ROLE = {
    "monitor": "explorer",
}


def load_manifest() -> dict:
    return json.loads((LOOP_ROOT / "loop_manifest.json").read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--role", required=True)
    parser.add_argument("--iteration-id", required=True)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    manifest = load_manifest()
    role_spec = manifest.get("roles", {}).get(args.role)
    if not role_spec:
        raise SystemExit(f"Unknown role: {args.role}")

    task_path = LOOP_ROOT / "iterations" / args.iteration_id / "task.md"
    if not task_path.exists():
        raise SystemExit(f"Missing task: {task_path}")

    base_prompt = (LOOP_ROOT / "system_prompts" / "base_worker.md").read_text(encoding="utf-8")
    role_prompt_path = ROOT / role_spec.get("system_prompt", "")
    if not role_prompt_path.exists():
        raise SystemExit(f"Missing role prompt: {role_prompt_path}")
    role_prompt = role_prompt_path.read_text(encoding="utf-8")
    task_text = task_path.read_text(encoding="utf-8")

    message = "\n\n".join(
        [
            "请严格按照下面的 system prompt 和 task packet 执行。不要使用父聊天上下文。",
            "## base_worker.md",
            base_prompt,
            f"## {args.role}.md",
            role_prompt,
            f"## task.md ({task_path})",
            task_text,
            "最终回复必须以 LOOP_DONE 或 LOOP_BLOCKED 开头。",
        ]
    )

    payload = {
        "agent_type": AGENT_TYPE_BY_ROLE.get(args.role, "worker"),
        "fork_context": False,
        "role": args.role,
        "iteration_id": args.iteration_id,
        "task_path": str(task_path),
        "message": message,
    }

    out_path = Path(args.output) if args.output else task_path.parent / "dispatch_request.json"
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
