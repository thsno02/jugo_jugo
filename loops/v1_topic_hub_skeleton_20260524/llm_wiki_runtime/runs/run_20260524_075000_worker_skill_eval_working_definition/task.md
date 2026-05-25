# Task

run_id:: run_20260524_075000_worker_skill_eval_working_definition
executor_role:: skill_eval_worker
task_packet:: working-definition 0-1 node run skill evaluation, frontier/status closure, and next-decision recommendation
status:: in_progress

## Objective

Evaluate the completed `cand_002_working_definition` 0-1 node chain, record adoption status and skill/process observations, close the frontier/status controls, and choose exactly one next controller action.

## Allowed Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-skill-evolution/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/skill_eval_log.yaml`
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/loop_delivery.md`
- `.llmwiki/runs/run_20260524_073000_worker_node_planning_working_definition/loop_delivery.md`
- `.llmwiki/runs/run_20260524_073500_worker_generation_working_definition/loop_delivery.md`
- `.llmwiki/runs/run_20260524_074000_worker_audit_working_definition/loop_delivery.md`
- `.llmwiki/runs/run_20260524_074500_worker_adoption_view_working_definition/loop_delivery.md`
- `generated/status.yaml`
- `kb/_index.yaml`

## Allowed Outputs

- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/skill_eval_log.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/runs/run_20260524_075000_worker_skill_eval_working_definition/task.md`
- `.llmwiki/runs/run_20260524_075000_worker_skill_eval_working_definition/skill_eval.md`
- `.llmwiki/runs/run_20260524_075000_worker_skill_eval_working_definition/next_decision.md`
- `.llmwiki/runs/run_20260524_075000_worker_skill_eval_working_definition/loop_status.md`
- `.llmwiki/runs/run_20260524_075000_worker_skill_eval_working_definition/loop_delivery.md`

## Forbidden Actions

- Do not write `nodes/`, `kb/`, or `generated/`.
- Do not run network retrieval.
- Do not generate a third node.
- Do not let the main agent directly execute the next concrete source-mining/node-building phase.

