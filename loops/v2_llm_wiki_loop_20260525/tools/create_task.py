#!/usr/bin/env python3
"""Create a loop task packet from a role template."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
LOOP_ROOT = ROOT / "llm_wiki" / "loop"


def load_manifest() -> dict:
    return json.loads((LOOP_ROOT / "loop_manifest.json").read_text(encoding="utf-8"))


def parse_sets(values: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for item in values:
        if "=" not in item:
            raise SystemExit(f"--set expects key=value, got: {item}")
        key, value = item.split("=", 1)
        result[key.strip()] = value.strip()
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--role", required=True)
    parser.add_argument("--iteration-id", required=True)
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--set", action="append", default=[], help="Template variable as key=value")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    manifest = load_manifest()
    role_spec = manifest.get("roles", {}).get(args.role)
    if not role_spec:
        raise SystemExit(f"Unknown role: {args.role}")
    template_path = ROOT / role_spec.get("task_template", "")
    if not template_path.exists():
        raise SystemExit(f"Missing task template: {template_path}")

    iteration_dir = LOOP_ROOT / "iterations" / args.iteration_id
    artifacts_dir = iteration_dir / "artifacts"
    task_path = iteration_dir / "task.md"
    if task_path.exists() and not args.force:
        raise SystemExit(f"Task already exists: {task_path}")

    text = template_path.read_text(encoding="utf-8")
    replacements = {
        "task_id": args.task_id,
        "iteration_id": args.iteration_id,
        "role": args.role,
        **parse_sets(args.set),
    }
    for key, value in replacements.items():
        text = text.replace(f"<{key}>", value)
        text = text.replace(f"`{key}`:", f"`{key}`: `{value}`", 1)

    iteration_dir.mkdir(parents=True, exist_ok=True)
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    task_path.write_text(text, encoding="utf-8")
    print(task_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
