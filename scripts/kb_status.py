#!/usr/bin/env python3
"""Summarize KB initialization status into generated/status.yaml."""

from __future__ import annotations

from collections import Counter

from kb_common import GENERATED_DIR, KB_DIR, NODES_DIR, ROOT, adopted_nodes, load_yaml, now_local, root_relative, write_yaml


def major_candidate_count() -> int:
    if not NODES_DIR.exists():
        return 0
    count = 0
    for change_path in NODES_DIR.glob("*/versions/*/change.md"):
        text = change_path.read_text(encoding="utf-8")
        if "change_scale:: major" in text and "propagation_required:: true" in text:
            count += 1
    return count


def retrieval_counts() -> dict:
    log_path = ROOT / ".llmwiki" / "control" / "retrieval_log.yaml"
    if not log_path.exists():
        return {"requests": 0, "ok_attempts": 0, "failed_attempts": 0}
    log = load_yaml(log_path)
    requests = log.get("requests", [])
    attempts = [attempt for request in requests for attempt in request.get("attempts", [])]
    return {
        "requests": len(requests),
        "ok_attempts": len([attempt for attempt in attempts if attempt.get("status") == "ok"]),
        "failed_attempts": len([attempt for attempt in attempts if attempt.get("status") != "ok"]),
    }


def choose_next_action(nodes_count: int, retrieval: dict, major_candidates: int, open_impacts: int) -> str:
    if nodes_count < 5:
        return "continue_0_1_node_runs"
    if retrieval["ok_attempts"] < 1:
        return "run_dynamic_retrieval_test"
    if major_candidates < 1:
        return "run_major_impact_test"
    if open_impacts > 0:
        return "review_impact_queue_or_prepare_demo_report"
    return "prepare_demo_report"


def action_zh(action: str) -> str:
    return {
        "continue_0_1_node_runs": "继续生成 0-1 nodes",
        "run_dynamic_retrieval_test": "执行动态检索测试",
        "run_major_impact_test": "执行 major-impact 测试",
        "review_impact_queue_or_prepare_demo_report": "审查 impact queue，或准备 demo report",
        "prepare_demo_report": "准备 demo report",
    }.get(action, action)


def main() -> int:
    nodes = adopted_nodes()
    graph_path = GENERATED_DIR / "citation_graph.yaml"
    impact_path = GENERATED_DIR / "impact_queue.yaml"
    graph = load_yaml(graph_path) if graph_path.exists() else {"edges": []}
    impacts = load_yaml(impact_path) if impact_path.exists() else {"impacts": []}
    retrieval = retrieval_counts()
    major_candidates = major_candidate_count()
    open_impacts = len([row for row in impacts.get("impacts", []) if row.get("status") == "open"])
    stability = Counter(node.get("stability", "unknown") for node in nodes)
    tags = Counter(tag for node in nodes for tag in node.get("tags", []))

    next_action = choose_next_action(len(nodes), retrieval, major_candidates, open_impacts)
    status = {
        "schema": "kb.status.v1",
        "language": "zh-CN",
        "generated_at": now_local(),
        "nodes_total": len(list(NODES_DIR.glob("*"))) if NODES_DIR.exists() else 0,
        "adopted_nodes": len(nodes),
        "kb_view_cards": len(list(KB_DIR.glob("*.md"))) if KB_DIR.exists() else 0,
        "citation_edges": len(graph.get("edges", [])),
        "major_candidates": major_candidates,
        "dynamic_retrieval": retrieval,
        "impact_queue_open": open_impacts,
        "stability_counts": dict(stability),
        "top_tags": dict(tags.most_common(20)),
        "next_recommended_action": next_action,
        "next_recommended_action_zh": action_zh(next_action),
    }

    out_path = GENERATED_DIR / "status.yaml"
    write_yaml(out_path, status)
    print(f"wrote {root_relative(out_path)}")
    print(
        f"adopted_nodes={status['adopted_nodes']} "
        f"citation_edges={status['citation_edges']} "
        f"impact_queue_open={status['impact_queue_open']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
