# Task

run_id:: run_20260524_093000_worker_adoption_metadata_repair_workflow
executor_role:: worker_executor
task_packet:: cand_004_workflow adoption metadata repair + revalidation
status:: LOOP_DONE
decision:: repair_validated

## Objective

Repair only the selected version metadata for `20260524_084000_llm_wiki_ingest_compile_query_lint_workflow@1.0` so the adopted root metadata and version metadata agree, then rerun node/card/status related validation.

## Required Inputs Read

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-view-building/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/runs/run_20260524_092000_worker_skill_eval_workflow/loop_delivery.md`
- `.llmwiki/runs/run_20260524_092000_worker_skill_eval_workflow/skill_eval_report.md`
- `.llmwiki/runs/run_20260524_091000_worker_adoption_view_workflow/loop_delivery.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/node.yaml`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/node.yaml`

## Write Boundary

Allowed writes were limited to the selected version metadata adoption fields, mechanical generated/status refreshes, control status files, and this run directory. No card, provenance, change, evidence, source, skill, protocol, archive, or KB text content was modified by this worker.
