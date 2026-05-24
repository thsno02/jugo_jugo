# Repair Trace

run_id:: run_20260524_093000_worker_adoption_metadata_repair_workflow
executor_role:: worker_executor
decision:: repair_validated

## Initial Finding

The adopted root metadata at `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/node.yaml` points to version `1.0` with:

- `version_status: adopted`
- `status: active`
- `version_adopted_at: "2026-05-24T17:04:30+08:00"`
- `audit.state: passed`
- `audit.decision: adopt_recommended`
- `audit.adoption_run: .llmwiki/runs/run_20260524_091000_worker_adoption_view_workflow`

The selected version metadata still recorded candidate state, causing `kb_validate_node.py` to fail with `adopted root points to non-adopted version`.

## Metadata Fields Changed

File: `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/node.yaml`

- `status`: `candidate` -> `active`
- `version_status`: `candidate_pending_audit` -> `adopted`
- `adoption_status`: `pending_audit` -> `adopted`
- `adopted`: `false` -> `true`
- `adoption_gate`: `citation_and_adoption_audit_required` -> `citation_and_adoption_audit_passed`
- `version_adopted_at`: added `"2026-05-24T17:04:30+08:00"`
- `audit.state`: `pending` -> `passed`
- `audit.run`: `null` -> `.llmwiki/runs/run_20260524_090000_worker_audit_workflow/audit_report.md`
- `audit.decision`: `pending` -> `adopt_recommended`
- `audit.adoption_run`: added `.llmwiki/runs/run_20260524_091000_worker_adoption_view_workflow`

## Non-Changes

Did not modify:

- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/provenance.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/change.md`
- evidence files under `data/`
- KB text content
- skills or protocol files
