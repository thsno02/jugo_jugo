# Task Packet

run_id:: run_20260524_083000_worker_skill_eval_architecture
executor_role:: skill_eval_worker
task_type:: skill_evaluation_frontier_status_next_decision
status:: completed

## Objective

Complete skill evaluation, frontier/status closure, and next-decision selection for the `cand_003_architecture` 0-1 node run.

## Required Inputs Read

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-skill-evolution/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/skill_eval_log.yaml`
- `.llmwiki/runs/run_20260524_080000_worker_source_mining_architecture/loop_delivery.md`
- `.llmwiki/runs/run_20260524_081000_worker_node_planning_architecture/loop_delivery.md`
- `.llmwiki/runs/run_20260524_081500_worker_generation_architecture/loop_delivery.md`
- `.llmwiki/runs/run_20260524_082000_worker_audit_architecture/loop_delivery.md`
- `.llmwiki/runs/run_20260524_082500_worker_adoption_view_architecture/loop_delivery.md`
- `generated/status.yaml`
- `kb/_index.yaml`

## Allowed Outputs

- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/skill_eval_log.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/runs/run_20260524_083000_worker_skill_eval_architecture/task.md`
- `.llmwiki/runs/run_20260524_083000_worker_skill_eval_architecture/skill_eval.md`
- `.llmwiki/runs/run_20260524_083000_worker_skill_eval_architecture/next_decision.md`
- `.llmwiki/runs/run_20260524_083000_worker_skill_eval_architecture/loop_status.md`
- `.llmwiki/runs/run_20260524_083000_worker_skill_eval_architecture/loop_delivery.md`

## Forbidden Outputs

- Do not write `nodes/`.
- Do not write `kb/`.
- Do not write `generated/`.
- Do not generate the next node.
- Do not run network retrieval.

## Completion Criteria

- Record adopted node count/status and what passed.
- Record whether any new architecture-loop failure mode appeared.
- Mark `cand_003_architecture` built/adopted in frontier.
- Choose exactly one next action.
- Keep main agent as controller; next action must be dispatching a worker task packet.

