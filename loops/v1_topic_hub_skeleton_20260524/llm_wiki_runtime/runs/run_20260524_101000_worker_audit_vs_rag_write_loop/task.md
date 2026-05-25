# Task

run_id:: run_20260524_101000_worker_audit_vs_rag_write_loop
executor_role:: worker_executor
worker_role:: cand_010_vs_rag_write_loop citation/adoption audit worker
task_packet:: user_dispatch_2026-05-24
candidate_id:: cand_010_vs_rag_write_loop
target_node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
version:: 1.0
decision_options:: adopt_recommended | repair_before_adoption | needs_retrieval | reject_or_defer

## Scope

Audit the candidate version bundle:

- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/node.yaml`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/provenance.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/change.md`

Required checks:

- Official card validator result.
- Citation targets and pinned paths exist, citation fields are complete, and sources trace to the evidence matrix.
- No anti-RAG framing, strawman GraphRAG framing, unsupported adjacent-system claim, or agent-memory equivalence.
- Prior KB appears only as continuity anchors, not as new fact authority.
- Node maintains artifact/workflow boundary instead of product, ecosystem, benchmark, scale, adoption, or enterprise comparison.
- Provenance keeps primary/local, adjacent technical, secondary/discourse, and prior-KB categories separated.
- Change is `genesis -> 1.0` and adoption remains pending.

## Allowed Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-citation-audit/SKILL.md`
- `.llmwiki/skills/llmwiki-adoption-audit/SKILL.md`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/node_plan.yaml`
- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/evidence_scope.md`
- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/evidence_scope.yaml`
- `.llmwiki/runs/run_20260524_100000_worker_generation_vs_rag_write_loop/loop_delivery.md`
- Candidate version bundle files under `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/`
- Local source files named by the evidence matrix and card citations.

## Forbidden Actions

- Do not modify the candidate bundle.
- Do not write root node metadata.
- Do not write `kb/`, `generated/`, `frontier`, skill files, or source files.
- Do not dispatch sub-agents.

## Outputs Written

- `.llmwiki/runs/run_20260524_101000_worker_audit_vs_rag_write_loop/task.md`
- `.llmwiki/runs/run_20260524_101000_worker_audit_vs_rag_write_loop/citation_audit.md`
- `.llmwiki/runs/run_20260524_101000_worker_audit_vs_rag_write_loop/audit_report.md`
- `.llmwiki/runs/run_20260524_101000_worker_audit_vs_rag_write_loop/validation_trace.md`
- `.llmwiki/runs/run_20260524_101000_worker_audit_vs_rag_write_loop/loop_status.md`
- `.llmwiki/runs/run_20260524_101000_worker_audit_vs_rag_write_loop/loop_delivery.md`

