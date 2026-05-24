# Task

run_id:: run_20260524_073000_worker_node_planning_working_definition
executor_role:: worker_executor
worker_type:: node-planning
candidate_id:: cand_002_working_definition
status:: LOOP_DONE

## Objective

Generate a frontier-gated generator handoff for `cand_002_working_definition`.

This run must not generate a node/card and must not adopt anything. It may only prepare planning, evidence scope, next task packet, and generation entry gate artifacts for controller review.

## Allowed Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-node-planning/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/loop_delivery.md`
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/source_mining.md`
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/candidate_frontier_delta.yaml`
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/evidence_gaps.md`
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/retrieval_requests.md`
- `kb/_index.yaml`
- Local file-state checks for candidate evidence paths, without network access.

## Required Outputs

- `.llmwiki/runs/run_20260524_073000_worker_node_planning_working_definition/task.md`
- `.llmwiki/runs/run_20260524_073000_worker_node_planning_working_definition/planner_report.md`
- `.llmwiki/runs/run_20260524_073000_worker_node_planning_working_definition/evidence_scope.yaml`
- `.llmwiki/runs/run_20260524_073000_worker_node_planning_working_definition/next_task_packet.md`
- `.llmwiki/runs/run_20260524_073000_worker_node_planning_working_definition/generation_entry_gate.md`
- `.llmwiki/runs/run_20260524_073000_worker_node_planning_working_definition/loop_status.md`
- `.llmwiki/runs/run_20260524_073000_worker_node_planning_working_definition/loop_delivery.md`

## Forbidden Actions

- Do not write `nodes/`, `kb/`, or `generated/`.
- Do not generate `node.yaml`, `card.md`, `provenance.md`, or `change.md`.
- Do not write or request root `nodes/<node_id>/node.yaml`.
- Do not adopt a node or update `kb/_index.yaml`.
- Do not use network retrieval.

