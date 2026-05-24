#!/usr/bin/env python3
"""Shared helpers for the filesystem-backed KB initialization demo."""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
NODES_DIR = ROOT / "nodes"
KB_DIR = ROOT / "kb"
GENERATED_DIR = ROOT / "generated"

REQUIRED_CITATION_FIELDS = [
    "target",
    "target_version",
    "pinned_version",
    "citation_role",
    "why_cited",
    "evidence_summary",
]


def now_local() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no}: invalid JSONL: {exc}") from exc
    return rows


def write_yaml(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not contain a YAML mapping")
    return data


def root_relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def resolve_declared_path(value: str, base_file: Path | None = None) -> Path:
    raw = Path(value)
    if raw.is_absolute():
        return raw
    root_candidate = ROOT / raw
    if root_candidate.exists() or value.split("/", 1)[0] in {
        ".llmwiki",
        "data",
        "docs",
        "generated",
        "kb",
        "nodes",
        "reports",
        "scripts",
    }:
        return root_candidate
    if base_file is not None:
        return base_file.parent / raw
    return root_candidate


def node_dirs() -> list[Path]:
    if not NODES_DIR.exists():
        return []
    return sorted(path for path in NODES_DIR.iterdir() if path.is_dir())


def load_root_node(node_dir: Path) -> dict[str, Any]:
    return load_yaml(node_dir / "node.yaml")


def adopted_nodes() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for node_dir in node_dirs():
        root_yaml = node_dir / "node.yaml"
        if not root_yaml.exists():
            continue
        data = load_yaml(root_yaml)
        if data.get("version_status") != "adopted" or data.get("status") == "archived":
            continue
        data["_node_dir"] = node_dir
        rows.append(data)
    return sorted(rows, key=lambda row: (row.get("node_created_at", ""), row.get("id", "")))


def parse_citation_block(lines: list[str]) -> dict[str, str]:
    fields: dict[str, str] = {}
    current_key: str | None = None
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if match:
            current_key = match.group(1)
            fields[current_key] = match.group(2).strip()
        elif current_key:
            fields[current_key] = (fields[current_key] + " " + line).strip()
    return fields


def parse_card_citations(card_path: Path) -> list[dict[str, Any]]:
    text = card_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    citations: list[dict[str, Any]] = []

    i = 0
    while i < len(lines):
        match = re.match(r"^\[\^([^\]]+)\]:\s*$", lines[i])
        if not match:
            i += 1
            continue
        citation_id = match.group(1)
        block: list[str] = []
        i += 1
        while i < len(lines) and not re.match(r"^\[\^[^\]]+\]:\s*$", lines[i]) and not re.match(
            r"^##\s+", lines[i]
        ):
            block.append(lines[i])
            i += 1
        fields = parse_citation_block(block)
        citations.append(
            {
                "citation_kind": "footnote",
                "citation_id": citation_id,
                "fields": fields,
            }
        )

    ref_start = None
    for idx, line in enumerate(lines):
        if line.strip() == "## References":
            ref_start = idx + 1
            break
    if ref_start is not None:
        i = ref_start
        while i < len(lines):
            header = re.match(r"^###\s+\[([^\]]+)\]\s*(.*)$", lines[i])
            if not header:
                i += 1
                continue
            ref_id = header.group(1)
            title = header.group(2).strip()
            block = []
            i += 1
            while i < len(lines) and not re.match(r"^###\s+\[[^\]]+\]", lines[i]):
                if re.match(r"^##\s+", lines[i]):
                    break
                block.append(lines[i])
                i += 1
            fields = parse_citation_block(block)
            citations.append(
                {
                    "citation_kind": "reference",
                    "citation_id": ref_id,
                    "title": title,
                    "fields": fields,
                }
            )
    return citations


def infer_target_identity(fields: dict[str, str]) -> dict[str, str | None]:
    target = fields.get("target", "")
    pinned = fields.get("pinned_version", "")
    combined = f"{target} {pinned}"

    node_match = re.search(r"(?:^|/)nodes/([^/\s]+)/versions/([^/\s]+)/card\.md", combined)
    if node_match:
        return {
            "target_kind": "node",
            "cited_node": node_match.group(1),
            "cited_version": node_match.group(2),
            "cited_source": None,
        }

    kb_match = re.search(r"(?:^|/)kb/([^/\s]+)\.md", combined)
    if kb_match:
        return {
            "target_kind": "node",
            "cited_node": kb_match.group(1),
            "cited_version": fields.get("target_version"),
            "cited_source": None,
        }

    source_match = re.search(r"(?:^|/)data/raw/([^/\s]+/[^/\s]+)", combined)
    if source_match:
        return {
            "target_kind": "source",
            "cited_node": None,
            "cited_version": fields.get("target_version"),
            "cited_source": source_match.group(1),
        }

    return {
        "target_kind": "artifact",
        "cited_node": None,
        "cited_version": fields.get("target_version"),
        "cited_source": None,
    }


def propagation_strength(citation_kind: str) -> str:
    if citation_kind == "footnote":
        return "strong"
    if citation_kind == "reference":
        return "medium"
    return "weak"
