# Adoption Trace

run_id:: run_20260524_102000_worker_adoption_view_vs_rag_write_loop
executor_role:: worker_executor
decision:: adopted
audit_decision_input:: adopt_recommended
target_node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
version:: 1.0
adopted_at:: 2026-05-24T17:54:00+08:00

## Actions

- Created root metadata: `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/node.yaml`.
- Synchronized selected-version metadata in `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/node.yaml`.
- Did not modify `card.md`, `provenance.md`, `change.md`, or evidence contents.

## Exact Selected-Version Metadata Fields Changed

- `status`: `candidate` -> `active`
- `version_status`: `pending_audit` -> `adopted`
- `adoption_status`: `pending_audit` -> `adopted`
- `adopted`: `false` -> `true`
- `selected`: absent -> `true`
- `adoption_gate`: `citation_and_adoption_audit_required` -> `citation_and_adoption_audit_passed`
- `version_adopted_at`: `null` -> `2026-05-24T17:54:00+08:00`
- `audit.state`: `pending` -> `passed`
- `audit.run`: `null` -> `.llmwiki/runs/run_20260524_101000_worker_audit_vs_rag_write_loop/audit_report.md`
- `audit.decision`: `pending` -> `adopt_recommended`
- `audit.adoption_run`: `null` -> `.llmwiki/runs/run_20260524_102000_worker_adoption_view_vs_rag_write_loop`

## Root Metadata Created

Root `node.yaml` now points to version `1.0`, marks `version_status: adopted`, `status: active`, `usable_as_support: true`, and records audit state `passed` with adoption run `.llmwiki/runs/run_20260524_102000_worker_adoption_view_vs_rag_write_loop`.

