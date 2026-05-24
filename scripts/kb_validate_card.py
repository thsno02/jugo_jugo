#!/usr/bin/env python3
"""Validate KB card markdown sections and citation field contracts."""

from __future__ import annotations

import argparse
from pathlib import Path

from kb_common import (
    KB_DIR,
    NODES_DIR,
    REQUIRED_CITATION_FIELDS,
    ROOT,
    parse_card_citations,
    resolve_declared_path,
    root_relative,
)


def card_paths_from_args(paths: list[str], all_cards: bool) -> list[Path]:
    if paths:
        return [Path(path) if Path(path).is_absolute() else ROOT / path for path in paths]
    if all_cards:
        version_cards = sorted(NODES_DIR.glob("*/versions/*/card.md")) if NODES_DIR.exists() else []
        kb_cards = sorted(KB_DIR.glob("*.md")) if KB_DIR.exists() else []
        return version_cards + kb_cards
    raise SystemExit("pass card paths or --all")


def validate_card(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"{path}: missing card"]
    text = path.read_text(encoding="utf-8")
    if not text.startswith("# "):
        errors.append(f"{root_relative(path)}: first line must be a level-1 title")
    for section in ["## Footnotes", "## References"]:
        if section not in text:
            errors.append(f"{root_relative(path)}: missing {section}")

    citations = parse_card_citations(path)
    if not citations:
        errors.append(f"{root_relative(path)}: no parseable citations")
    for citation in citations:
        fields = citation["fields"]
        prefix = f"{root_relative(path)}:{citation['citation_kind']}:{citation['citation_id']}"
        for field in REQUIRED_CITATION_FIELDS:
            if not fields.get(field):
                errors.append(f"{prefix}: missing {field}")
        for field in ["target", "pinned_version"]:
            if fields.get(field) and not resolve_declared_path(fields[field], path).exists():
                errors.append(f"{prefix}: {field} does not exist: {fields[field]}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    all_errors: list[str] = []
    checked = 0
    for path in card_paths_from_args(args.paths, args.all):
        checked += 1
        all_errors.extend(validate_card(path))

    if all_errors:
        for error in all_errors:
            print(error)
        print(f"card validation failed: {len(all_errors)} errors across {checked} cards")
        return 1
    print(f"card validation passed: {checked} cards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
