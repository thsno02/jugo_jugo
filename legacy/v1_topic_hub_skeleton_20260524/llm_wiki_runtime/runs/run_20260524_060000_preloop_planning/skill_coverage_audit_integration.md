# Skill Coverage Audit Integration

run_id:: run_20260524_060000_preloop_planning
status:: fixed_highest_priority_gap

## Audit finding

Newton audit verdict was `needs_work`: specialist skills covered most protocol roles, but there was no hard orchestration/planner gate preventing a planner or generator from bypassing source mining and `knowledge_frontier.yaml`.

## Fix applied

Added:

- `.llmwiki/skills/llmwiki-loop-orchestration/SKILL.md`
- `.llmwiki/control/orchestration_gates.yaml`

Patched:

- `.llmwiki/control/planner_protocol.md`
- `.llmwiki/control/autonomous_loop_plan.md`
- `.llmwiki/control/skill_registry.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/action_queue.yaml`

## New hard rule

`next_task_packet.md` may only be emitted for a candidate already present in `.llmwiki/control/knowledge_frontier.yaml` with `status: ready_to_build`, source lineage, evidence state, and no unresolved retrieval blocker.

## Current consequence

Turing planner output remains useful as evidence handoff, but it cannot authorize card generation yet. The next autonomous run must be source mining for the origin/canon source batch.

