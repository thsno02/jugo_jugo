# Task

run_id:: run_20260524_085000_worker_node_planning_workflow
executor_role:: worker_executor
worker_kind:: node-planning worker
task:: frontier-gated generator handoff for `cand_004_workflow` / `llm_wiki_ingest_compile_query_lint_workflow`
status:: LOOP_DONE

## Allowed Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-node-planning/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/runs/run_20260524_084000_worker_source_mining_workflow/loop_delivery.md`
- `.llmwiki/runs/run_20260524_084000_worker_source_mining_workflow/source_mining.md`
- `.llmwiki/runs/run_20260524_084000_worker_source_mining_workflow/candidate_frontier_delta.yaml`
- `kb/_index.yaml`
- Local file-state checks for paths named in the selected candidate's evidence scope.

## Allowed Outputs

- `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/task.md`
- `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/planner_report.md`
- `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/evidence_scope.yaml`
- `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/next_task_packet.md`
- `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/generation_entry_gate.md`
- `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/loop_status.md`
- `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/loop_delivery.md`

## Hard Boundaries

- Select only `cand_004_workflow` if it is `ready_to_build`.
- Do not generate a node bundle, card, provenance, change log, KB view, root node metadata, or adoption artifact.
- Do not modify `nodes/`, `kb/`, `generated/`, or any source/control files.
- Do not perform network retrieval.
- Use only version-bundle generator output paths under `nodes/<node_id>/versions/1.0/`.
