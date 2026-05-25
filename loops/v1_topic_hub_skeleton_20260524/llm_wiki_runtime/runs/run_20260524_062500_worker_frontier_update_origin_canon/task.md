# Frontier Update Task

run_id:: run_20260524_062500_worker_frontier_update_origin_canon
executor_role:: worker_executor
phase:: frontier_update
status:: LOOP_DONE

## Task Packet

Merge the worker-attributed source mining output from `run_20260524_062000_worker_source_mining_origin_canon` into `.llmwiki/control/knowledge_frontier.yaml`.

## Required Inputs Read

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-frontier-management/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/loop_delivery.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/candidate_frontier_delta.yaml`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/evidence_gaps.md`

## Allowed Outputs

- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/runs/run_20260524_062500_worker_frontier_update_origin_canon/task.md`
- `.llmwiki/runs/run_20260524_062500_worker_frontier_update_origin_canon/frontier_trace.md`
- `.llmwiki/runs/run_20260524_062500_worker_frontier_update_origin_canon/loop_status.md`
- `.llmwiki/runs/run_20260524_062500_worker_frontier_update_origin_canon/loop_delivery.md`

## Constraints

- Use only the Noether worker source-mining run as authority.
- Do not use the main-authored drift run as source authority.
- Do not generate node/card artifacts.
- Do not modify `nodes/`, `kb/generated/`, or generated KB artifacts.
- Do not use network retrieval.

