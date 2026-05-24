# Generation Entry Gate

run_id:: run_20260524_085000_worker_node_planning_workflow
executor_role:: worker_executor
candidate_id:: cand_004_workflow
target_node_id:: 20260524_084000_llm_wiki_ingest_compile_query_lint_workflow
version_target:: 1.0
result:: pass

## Gate Checks

| gate | requirement | status |
|---|---|---|
| gate_000_executor_attribution | Worker delivery must state executor role, task packet, allowed inputs, outputs written, and completion marker. | pass |
| gate_002_frontier_to_node_planning | Candidate must exist in `.llmwiki/control/knowledge_frontier.yaml`, be `ready_to_build`, include required readiness fields, and have no unresolved retrieval blocker. | pass |
| gate_003_node_planning_to_generation_entry | `planner_report.md`, `evidence_scope.yaml`, and `next_task_packet.md` are present; packet names a frontier candidate, confirms `ready_to_build`, and cites the source-mining run that made the candidate ready. | pass |
| gate_004_generation_entry_to_bundle_generation | Allowed inputs, forbidden inputs, version target, and output paths are explicit; output paths are only under `nodes/<node_id>/versions/1.0/`; root node adoption is forbidden before audit. | pass |

## Allowed Inputs For Generator

Use only the inputs listed in `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/next_task_packet.md` and scoped in `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/evidence_scope.yaml`.

## Forbidden Inputs For Generator

- Network retrieval.
- Unscoped implementation/ecosystem sources.
- Enterprise, benchmark, adoption, social metric, governance, or broad comparison sources unless already scoped as boundary-only secondary context.
- Controller drift sample artifacts.

## Required Generator Output Paths

- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/node.yaml`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/provenance.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/change.md`

The generator must not write or adopt root `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/node.yaml`.

