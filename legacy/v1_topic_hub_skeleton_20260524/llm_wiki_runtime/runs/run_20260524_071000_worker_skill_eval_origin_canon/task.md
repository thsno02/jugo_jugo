# Task Packet

run_id:: run_20260524_071000_worker_skill_eval_origin_canon
executor_role:: skill_eval_worker
phase:: skill_eval_and_next_decision
status:: LOOP_DONE

## Objective

Evaluate the completed origin/canon 0-1 node run, close frontier/status, and choose exactly one next controller action. Do not generate a new node and do not modify `nodes/`, `kb/`, or `generated/`.

## Allowed Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-skill-evolution/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/skill_eval_log.yaml`
- Origin/canon worker deliveries from source mining through adoption/view.
- `generated/status.yaml`
- `kb/_index.yaml`

## Allowed Outputs

- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/skill_eval_log.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/action_queue.yaml`
- This run directory's `task.md`, `skill_eval.md`, `next_decision.md`, `loop_status.md`, and `loop_delivery.md`.

## Guardrails

- Do not write `nodes/`, `kb/`, or `generated/`.
- Do not run network retrieval.
- Do not generate a second node.
- Keep main agent as controller; the next action must be a worker task packet dispatch.
