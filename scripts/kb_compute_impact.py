#!/usr/bin/env python3
"""Compute impact queue entries from major changes and citation graph edges."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from kb_common import GENERATED_DIR, NODES_DIR, load_yaml, now_local, root_relative, write_yaml


def parse_change_file(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)::\s*(.*)$", line.strip())
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return fields


def discover_major_changes() -> list[dict[str, str]]:
    changes: list[dict[str, str]] = []
    if not NODES_DIR.exists():
        return changes
    for change_path in sorted(NODES_DIR.glob("*/versions/*/change.md")):
        fields = parse_change_file(change_path)
        if fields.get("change_scale") == "major" and fields.get("propagation_required") == "true":
            fields["change_path"] = root_relative(change_path)
            fields.setdefault("node_id", change_path.parents[2].name)
            changes.append(fields)
    return changes


def impact_level(strength: str) -> str:
    if strength == "strong":
        return "high"
    if strength == "medium":
        return "medium"
    return "low"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed-node")
    parser.add_argument("--from-version")
    parser.add_argument("--to-version")
    args = parser.parse_args()

    graph_path = GENERATED_DIR / "citation_graph.yaml"
    graph = load_yaml(graph_path) if graph_path.exists() else {"edges": []}
    changes = discover_major_changes()

    if args.changed_node:
        changes.append(
            {
                "node_id": args.changed_node,
                "from_version": args.from_version or "unknown",
                "to_version": args.to_version or "unknown",
                "change_path": "manual_cli",
            }
        )

    impacts = []
    for change in changes:
        changed_node = change.get("node_id")
        for edge in graph.get("edges", []):
            if edge.get("cited_node") != changed_node:
                continue
            impacts.append(
                {
                    "impact_id": f"imp_{len(impacts) + 1:04d}",
                    "changed_node": changed_node,
                    "changed_from_version": change.get("from_version"),
                    "changed_to_version": change.get("to_version"),
                    "change_path": change.get("change_path"),
                    "impacted_node": edge.get("citing_node"),
                    "impacted_version": edge.get("citing_version"),
                    "citation_kind": edge.get("citation_kind"),
                    "citation_id": edge.get("citation_id"),
                    "impact_level": impact_level(edge.get("propagation_strength", "weak")),
                    "status": "open",
                    "suggested_action": "review_and_revise",
                    "suggested_action_zh": "审查并按需修订",
                    "reason": "受影响 node 通过已解析的 KB citation edge 引用了发生 major change 的 node。",
                }
            )

    queue = {
        "schema": "kb.impact_queue.v1",
        "generated_at": now_local(),
        "change_count": len(changes),
        "impact_count": len(impacts),
        "impacts": impacts,
    }
    out_path = GENERATED_DIR / "impact_queue.yaml"
    write_yaml(out_path, queue)
    print(f"wrote {root_relative(out_path)} with {len(impacts)} impacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
