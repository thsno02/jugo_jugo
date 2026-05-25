# Task

run_id:: run_20260524_063500_worker_node_planning_repair_origin_canon
executor_role:: worker_executor
phase:: node_planning_repair
task_packet:: controller request in current worker turn
repair_target_run:: .llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon
candidate_id:: cand_001_origin_and_canon

## Objective

Repair the node planning handoff contract for `cand_001_origin_and_canon` so the generator writes a first-version bundle under `nodes/<node_id>/versions/1.0/` and does not write or adopt root metadata before audit.

## Required Inputs Read

- `KB_INIT_KNOWLEDGE_MINING_PROTOCOL.md` sections 2, 7, 8, 9, 10, and 11
- `.llmwiki/skills/llmwiki-node-planning/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/next_task_packet.md`
- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/generation_entry_gate.md`

## Allowed Outputs

- `.llmwiki/runs/run_20260524_063500_worker_node_planning_repair_origin_canon/task.md`
- `.llmwiki/runs/run_20260524_063500_worker_node_planning_repair_origin_canon/next_task_packet.md`
- `.llmwiki/runs/run_20260524_063500_worker_node_planning_repair_origin_canon/generation_entry_gate.md`
- `.llmwiki/runs/run_20260524_063500_worker_node_planning_repair_origin_canon/planning_repair_report.md`
- `.llmwiki/runs/run_20260524_063500_worker_node_planning_repair_origin_canon/loop_status.md`
- `.llmwiki/runs/run_20260524_063500_worker_node_planning_repair_origin_canon/loop_delivery.md`
- `.llmwiki/skills/llmwiki-node-planning/SKILL.md`
- `.llmwiki/control/orchestration_gates.yaml`

## Execution Constraints

- Preserve the selected candidate, node id, source mining authority, allowed inputs, and evidence boundaries from the original planning handoff.
- Repair only the output-path and adoption contract.
- Do not generate `node.yaml`, `card.md`, `provenance.md`, or `change.md`.
- Do not modify `nodes/`, `kb/`, or `generated/`.
- Do not retrieve network sources.

## Completion Marker

LOOP_DONE
