#!/usr/bin/env python3
"""Record local Codex and Claude CLI capability signals without network work."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


COMMANDS = [
    ["codex", "--version"],
    ["codex", "features", "list"],
    ["claude", "--version"],
    ["claude", "--help"],
]


def run(cmd: list[str]) -> str:
    try:
        completed = subprocess.run(cmd, check=False, text=True, capture_output=True, timeout=20)
    except FileNotFoundError:
        return "COMMAND_NOT_FOUND\n"
    except subprocess.TimeoutExpired:
        return "TIMEOUT\n"
    output = (completed.stdout or "") + (completed.stderr or "")
    return f"exit_code={completed.returncode}\n{output}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    lines = ["# CLI capability probe", ""]
    for cmd in COMMANDS:
        lines.append(f"## `{' '.join(cmd)}`")
        lines.append("")
        lines.append("```text")
        lines.append(run(cmd).strip())
        lines.append("```")
        lines.append("")

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
