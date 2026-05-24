# Task

run_id:: run_20260524_085500_worker_generation_workflow
executor_role:: worker_executor
worker_kind:: generator
task_packet:: .llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/next_task_packet.md
candidate_id:: cand_004_workflow
target_node_id:: 20260524_084000_llm_wiki_ingest_compile_query_lint_workflow
version_target:: 1.0

## Objective

Generate the first candidate version bundle for the bounded LLM Wiki workflow node covering ingest/source intake, compile/wiki update, query/synthesis, lint/health-check, update/file-back, and index/log maintenance.

## Allowed Inputs

The run used only the inputs listed in `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/next_task_packet.md` and `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/evidence_scope.yaml`.

## Forbidden Inputs

- Network retrieval.
- Unscoped implementation/ecosystem sources.
- Enterprise, benchmark, adoption, social metric, governance, or broad comparison sources outside the scoped boundary.
- Controller drift sample artifacts.

## Required Outputs

- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/node.yaml`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/provenance.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/change.md`

Root `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/node.yaml`, `kb/`, and `generated/` were not written.
