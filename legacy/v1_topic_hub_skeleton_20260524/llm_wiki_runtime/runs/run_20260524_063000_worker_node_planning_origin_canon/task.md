# Task

run_id:: run_20260524_063000_worker_node_planning_origin_canon
executor_role:: worker_executor
phase:: node_planning
task_packet:: controller request in current worker turn
candidate_id:: cand_001_origin_and_canon

## Objective

Generate a frontier-gated generator handoff for `cand_001_origin_and_canon` without generating the KB bundle.

## Required Inputs Read

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-node-planning/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/runs/run_20260524_062500_worker_frontier_update_origin_canon/loop_delivery.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/loop_delivery.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/candidate_frontier_delta.yaml`

## Allowed Outputs

- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/task.md`
- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/planner_report.md`
- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/evidence_scope.yaml`
- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/next_task_packet.md`
- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/generation_entry_gate.md`
- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/loop_status.md`
- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/loop_delivery.md`

## Execution Constraints

- Select only from `ready_to_build` candidates in `.llmwiki/control/knowledge_frontier.yaml`.
- Do not select from topic plans, static backlog, or controller-authored drift artifacts.
- Preserve worker-mined evidence boundaries: gist primary; HN text only for early discourse; empty X raw files cannot support exact X wording, timestamps, quoted-post text, or metrics.
- Do not generate `node.yaml`, `card.md`, `provenance.md`, or `change.md`.
- Do not modify `nodes/`, `kb/`, or `generated/`.
- Do not retrieve network sources.

## Completion Marker

LOOP_DONE
