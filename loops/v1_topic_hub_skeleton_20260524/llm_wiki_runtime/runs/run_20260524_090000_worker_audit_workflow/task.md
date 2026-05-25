# Task

run_id:: run_20260524_090000_worker_audit_workflow
executor_role:: worker_executor
task_packet:: user_request_2026-05-24_workflow_candidate_citation_adoption_audit
status:: LOOP_DONE
decision:: adopt_recommended

## Scope

Audit the workflow candidate version bundle:

- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/node.yaml`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/provenance.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/change.md`

## Required Reads

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-citation-audit/SKILL.md`
- `.llmwiki/skills/llmwiki-adoption-audit/SKILL.md`
- `.llmwiki/runs/run_20260524_085500_worker_generation_workflow/loop_delivery.md`
- Candidate version bundle files listed above.

## Allowed Inputs

Only local repository artifacts needed to validate the candidate, citation targets, pinned paths, provenance, change note, and official card validator result were used. No network retrieval was performed.

## Forbidden Outputs

The audit did not modify generation bundle files, root node metadata, `kb/`, `generated/`, frontier, or skill files.

## Outputs Written

- `.llmwiki/runs/run_20260524_090000_worker_audit_workflow/task.md`
- `.llmwiki/runs/run_20260524_090000_worker_audit_workflow/citation_audit.md`
- `.llmwiki/runs/run_20260524_090000_worker_audit_workflow/audit_report.md`
- `.llmwiki/runs/run_20260524_090000_worker_audit_workflow/validation_trace.md`
- `.llmwiki/runs/run_20260524_090000_worker_audit_workflow/loop_status.md`
- `.llmwiki/runs/run_20260524_090000_worker_audit_workflow/loop_delivery.md`

