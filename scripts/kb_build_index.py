#!/usr/bin/env python3
"""Build kb/_index.yaml from adopted node metadata."""

from __future__ import annotations

from kb_common import KB_DIR, adopted_nodes, now_local, root_relative, write_yaml


def build_index() -> dict:
    nodes = []
    for node in adopted_nodes():
        item = {
            "id": node["id"],
            "title": node.get("title"),
            "version": str(node.get("version")),
            "version_status": node.get("version_status"),
            "status": node.get("status"),
            "stability": node.get("stability"),
            "usable_as_support": node.get("usable_as_support"),
            "node_created_at": node.get("node_created_at"),
            "version_adopted_at": node.get("version_adopted_at"),
            "tags": node.get("tags", []),
            "paths": node.get("paths", {}),
            "audit": node.get("audit", {}),
        }
        nodes.append(item)

    return {
        "schema": "kb.index.v1",
        "generated_at": now_local(),
        "node_count": len(nodes),
        "nodes": nodes,
    }


def main() -> int:
    KB_DIR.mkdir(parents=True, exist_ok=True)
    index = build_index()
    out_path = KB_DIR / "_index.yaml"
    write_yaml(out_path, index)
    print(f"wrote {root_relative(out_path)} with {index['node_count']} adopted nodes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
