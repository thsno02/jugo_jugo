#!/usr/bin/env python3
"""Validate that a task packet contains the minimum isolation contract."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]

REQUIRED_PHRASES = [
    "## 允许输入",
    "## 禁止输入",
    "## 允许写入",
    "## 成功门禁",
    "## 阻塞条件",
    "父聊天上下文",
]

INPUT_PATH_SKIP_KEYS = {
    # Adoption tasks intentionally read these target paths for existence and
    # conflict checks; the paths often do not exist before adoption.
    "target_card_path",
    "target_provenance_path",
}


def section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    end = text.find("\n## ", start + len(heading))
    if end < 0:
        end = len(text)
    return text[start:end]


def code_spans(text: str) -> list[str]:
    return re.findall(r"`([^`]+)`", text)


def strip_line_suffix(value: str) -> str:
    return re.sub(r":\d+(?:-\d+)?$", "", value)


def looks_like_local_path(value: str) -> bool:
    if not value or value.startswith(("http://", "https://")):
        return False
    if "<" in value or ">" in value or value.startswith("..."):
        return False
    return "/" in value or value.startswith((".", "~", "/"))


def missing_allowed_input_paths(text: str) -> list[tuple[str | None, str, Path]]:
    missing: list[tuple[str | None, str, Path]] = []
    for line in section(text, "## 允许输入").splitlines():
        spans = code_spans(line)
        if not spans:
            continue

        key: str | None = None
        value: str | None = None
        if len(spans) >= 2 and line.lstrip().startswith("- `"):
            key = spans[0].rstrip(":")
            value = spans[1].strip()
        else:
            value = spans[-1].strip()

        if key in INPUT_PATH_SKIP_KEYS:
            continue
        if not looks_like_local_path(value):
            continue

        raw_path = strip_line_suffix(value)
        path = Path(raw_path).expanduser()
        if not path.is_absolute():
            path = ROOT / path
        if not path.exists():
            missing.append((key, raw_path, path))
    return missing


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
    missing_paths = missing_allowed_input_paths(text)
    if missing_paths:
        print("scope_validation: fail")
        for key, raw_path, resolved in missing_paths:
            label = f"{key}: " if key else ""
            print(f"missing_input_path: {label}{raw_path} -> {resolved}")
        return 1
    print("scope_validation: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
