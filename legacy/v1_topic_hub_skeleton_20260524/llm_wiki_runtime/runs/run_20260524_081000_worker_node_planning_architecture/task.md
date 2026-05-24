# Node Planning Task

run_id:: run_20260524_081000_worker_node_planning_architecture
executor_role:: worker_executor
task_packet:: cand_003_architecture_frontier_gated_generator_handoff
status:: LOOP_DONE

## Objective

Generate a frontier-gated generator handoff for `cand_003_architecture` / `llm_wiki_three_layer_architecture`.

This run must not generate a node/card and must not adopt any node. It may only write the node-planning and generation-entry handoff artifacts listed below.

## Required Reads Completed

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-node-planning/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/runs/run_20260524_080000_worker_source_mining_architecture/loop_delivery.md`
- `.llmwiki/runs/run_20260524_080000_worker_source_mining_architecture/source_mining.md`
- `.llmwiki/runs/run_20260524_080000_worker_source_mining_architecture/candidate_frontier_delta.yaml`
- `kb/_index.yaml`

## Allowed Outputs

- `.llmwiki/runs/run_20260524_081000_worker_node_planning_architecture/task.md`
- `.llmwiki/runs/run_20260524_081000_worker_node_planning_architecture/planner_report.md`
- `.llmwiki/runs/run_20260524_081000_worker_node_planning_architecture/evidence_scope.yaml`
- `.llmwiki/runs/run_20260524_081000_worker_node_planning_architecture/next_task_packet.md`
- `.llmwiki/runs/run_20260524_081000_worker_node_planning_architecture/generation_entry_gate.md`
- `.llmwiki/runs/run_20260524_081000_worker_node_planning_architecture/loop_status.md`
- `.llmwiki/runs/run_20260524_081000_worker_node_planning_architecture/loop_delivery.md`

## Non-Goals

- Do not write `nodes/`, `kb/`, or `generated/`.
- Do not generate `card.md`, `node.yaml`, `provenance.md`, or `change.md`.
- Do not adopt root node metadata.
- Do not use network retrieval.
