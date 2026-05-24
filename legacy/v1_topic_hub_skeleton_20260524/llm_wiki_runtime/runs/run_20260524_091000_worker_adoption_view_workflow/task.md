# Task

run_id:: run_20260524_091000_worker_adoption_view_workflow
executor_role:: adoption_view_worker
task_packet:: user_direct_adoption_view_request_2026-05-24
candidate:: 20260524_084000_llm_wiki_ingest_compile_query_lint_workflow
version:: 1.0
gate_input_decision:: adopt_recommended
validator_input:: passed

## Objective

Adopt node `20260524_084000_llm_wiki_ingest_compile_query_lint_workflow` version `1.0`, render/refresh KB views and generated citation/index/status artifacts, and record post-adoption validation.

## Required Inputs Read

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-view-building/SKILL.md`
- `.llmwiki/skills/llmwiki-adoption-audit/SKILL.md`
- `.llmwiki/runs/run_20260524_085500_worker_generation_workflow/loop_delivery.md`
- `.llmwiki/runs/run_20260524_090000_worker_audit_workflow/loop_delivery.md`
- `.llmwiki/runs/run_20260524_090000_worker_audit_workflow/audit_report.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/node.yaml`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/provenance.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/change.md`

## Output Boundary

Writes are limited to root adoption metadata, rendered KB/generated views, permitted control status files, and this run directory. The workflow version bundle under `versions/1.0/` is read-only for this run.
