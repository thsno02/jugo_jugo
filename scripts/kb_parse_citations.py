#!/usr/bin/env python3
"""Parse kb/*.md citations into generated citation graph artifacts."""

from __future__ import annotations

from collections import defaultdict

from kb_common import (
    GENERATED_DIR,
    KB_DIR,
    ROOT,
    infer_target_identity,
    load_yaml,
    now_local,
    parse_card_citations,
    propagation_strength,
    resolve_declared_path,
    root_relative,
    write_yaml,
)


def index_by_node() -> dict:
    index_path = KB_DIR / "_index.yaml"
    if not index_path.exists():
        return {}
    index = load_yaml(index_path)
    return {row["id"]: row for row in index.get("nodes", [])}


def build_graph() -> tuple[dict, dict]:
    index = index_by_node()
    edges = []
    backlinks: dict[str, list[dict]] = defaultdict(list)

    for card_path in sorted(KB_DIR.glob("*.md")):
        citing_node = card_path.stem
        citing_version = str(index.get(citing_node, {}).get("version", "unknown"))
        for citation in parse_card_citations(card_path):
            fields = citation["fields"]
            identity = infer_target_identity(fields)
            target_path = resolve_declared_path(fields.get("target", ""), card_path)
            pinned_path = resolve_declared_path(fields.get("pinned_version", ""), card_path)
            edge = {
                "citing_node": citing_node,
                "citing_version": citing_version,
                "citation_kind": citation["citation_kind"],
                "citation_id": citation["citation_id"],
                "citation_role": fields.get("citation_role"),
                "target": fields.get("target"),
                "target_exists": target_path.exists(),
                "target_version": fields.get("target_version"),
                "pinned_version": fields.get("pinned_version"),
                "pinned_version_exists": pinned_path.exists(),
                "why_cited": fields.get("why_cited"),
                "evidence_summary": fields.get("evidence_summary"),
                "propagation_strength": propagation_strength(citation["citation_kind"]),
                **identity,
            }
            edges.append(edge)
            if edge.get("cited_node"):
                backlinks[edge["cited_node"]].append(
                    {
                        "citing_node": citing_node,
                        "citing_version": citing_version,
                        "citation_kind": edge["citation_kind"],
                        "citation_id": edge["citation_id"],
                        "propagation_strength": edge["propagation_strength"],
                    }
                )

    graph = {
        "schema": "kb.citation_graph.v1",
        "generated_at": now_local(),
        "edge_count": len(edges),
        "edges": edges,
    }
    backlink_doc = {
        "schema": "kb.backlinks.v1",
        "generated_at": now_local(),
        "backlinks": dict(sorted(backlinks.items())),
    }
    return graph, backlink_doc


def main() -> int:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    graph, backlinks = build_graph()
    graph_path = GENERATED_DIR / "citation_graph.yaml"
    backlinks_path = GENERATED_DIR / "backlinks.yaml"
    write_yaml(graph_path, graph)
    write_yaml(backlinks_path, backlinks)
    print(
        f"wrote {root_relative(graph_path)} and {root_relative(backlinks_path)} "
        f"with {graph['edge_count']} edges"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
