#!/usr/bin/env python3
"""Validate that a task packet contains the minimum isolation contract."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_PHRASES = [
    "## 允许输入",
    "## 禁止输入",
    "## 允许写入",
    "## 成功门禁",
    "## 阻塞条件",
    "父聊天上下文",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task_path")
    args = parser.parse_args()

    path = Path(args.task_path)
    text = path.read_text(encoding="utf-8")
    missing = [phrase for phrase in REQUIRED_PHRASES if phrase not in text]
    if missing:
        print("scope_validation: fail")
        for phrase in missing:
            print(f"missing: {phrase}")
        return 1
    print("scope_validation: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
