# Task

run_id:: run_20260524_102000_worker_adoption_view_vs_rag_write_loop
executor_role:: worker_executor
worker_role:: cand_010_vs_rag_write_loop adoption/view builder
task_packet:: user_dispatch_2026-05-24
target_node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
version:: 1.0

## Objective

Adopt `20260524_094000_llm_wiki_vs_rag_write_loop` version `1.0` after audit decision `adopt_recommended`, synchronize root and selected-version adoption metadata, rebuild KB consumption views and generated graph/status artifacts, then run post-adoption validation.

## Required Inputs Read

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-view-building/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/skills/llmwiki-adoption-audit/SKILL.md`
- `.llmwiki/runs/run_20260524_100000_worker_generation_vs_rag_write_loop/loop_delivery.md`
- `.llmwiki/runs/run_20260524_101000_worker_audit_vs_rag_write_loop/loop_delivery.md`
- `.llmwiki/runs/run_20260524_101000_worker_audit_vs_rag_write_loop/audit_report.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/node.yaml`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/provenance.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/change.md`

## Constraints

- Do not rewrite `card.md`, `provenance.md`, `change.md`, or evidence contents.
- Only synchronize selected-version adoption/status/selected/adopted-at/audit metadata fields.
- Prefer existing scripts and formats for view/index/citation/backlinks/impact/status refresh.
- Do not dispatch sub-agents.

