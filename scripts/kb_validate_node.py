#!/usr/bin/env python3
"""Validate node metadata and version bundle completeness."""

from __future__ import annotations

import argparse
from pathlib import Path

from kb_common import NODES_DIR, ROOT, load_yaml, node_dirs, resolve_declared_path, root_relative
from kb_validate_card import validate_card


REQUIRED_NODE_FIELDS = [
    "schema",
    "id",
    "title",
    "version",
    "version_status",
    "node_created_at",
    "version_created_at",
    "version_adopted_at",
    "status",
    "stability",
    "usable_as_support",
    "paths",
    "tags",
    "audit",
]

REQUIRED_BUNDLE_FILES = ["node.yaml", "card.md", "provenance.md", "change.md"]


def validate_node_dir(node_dir: Path) -> list[str]:
    errors: list[str] = []
    root_yaml = node_dir / "node.yaml"
    if not root_yaml.exists():
        return [f"{root_relative(node_dir)}: missing root node.yaml"]
    try:
        metadata = load_yaml(root_yaml)
    except Exception as exc:
        return [f"{root_relative(root_yaml)}: invalid yaml: {exc}"]

    node_id = metadata.get("id")
    if node_id != node_dir.name:
        errors.append(f"{root_relative(root_yaml)}: id does not match folder name")
    for field in REQUIRED_NODE_FIELDS:
        if field not in metadata:
            errors.append(f"{root_relative(root_yaml)}: missing {field}")
    if metadata.get("schema") != "kb.node_metadata.v1":
        errors.append(f"{root_relative(root_yaml)}: schema must be kb.node_metadata.v1")

    version = str(metadata.get("version", ""))
    version_dir = node_dir / "versions" / version
    if not version_dir.exists():
        errors.append(f"{root_relative(root_yaml)}: version dir missing: versions/{version}")
        return errors

    for name in REQUIRED_BUNDLE_FILES:
        if not (version_dir / name).exists():
            errors.append(f"{root_relative(version_dir / name)}: missing bundle file")

    version_yaml = version_dir / "node.yaml"
    if version_yaml.exists():
        version_metadata = load_yaml(version_yaml)
        if version_metadata.get("id") != node_id:
            errors.append(f"{root_relative(version_yaml)}: id differs from root")
        if str(version_metadata.get("version")) != version:
            errors.append(f"{root_relative(version_yaml)}: version differs from root")
        if metadata.get("version_status") == "adopted" and version_metadata.get("version_status") != "adopted":
            errors.append(f"{root_relative(version_yaml)}: adopted root points to non-adopted version")

    paths = metadata.get("paths", {})
    for key in ["version_dir", "card", "provenance", "change", "kb_view"]:
        value = paths.get(key)
        if not value:
            errors.append(f"{root_relative(root_yaml)}: paths.{key} missing")
            continue
        if key != "version_dir" and not resolve_declared_path(value, root_yaml).exists():
            errors.append(f"{root_relative(root_yaml)}: paths.{key} does not exist: {value}")

    card_path = version_dir / "card.md"
    if card_path.exists():
        errors.extend(validate_card(card_path))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    if args.paths:
        dirs = [Path(path) if Path(path).is_absolute() else ROOT / path for path in args.paths]
    elif args.all:
        dirs = node_dirs()
    else:
        raise SystemExit("pass node dirs or --all")

    all_errors: list[str] = []
    for node_dir in dirs:
        all_errors.extend(validate_node_dir(node_dir))

    if all_errors:
        for error in all_errors:
            print(error)
        print(f"node validation failed: {len(all_errors)} errors across {len(dirs)} nodes")
        return 1
    print(f"node validation passed: {len(dirs)} nodes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
