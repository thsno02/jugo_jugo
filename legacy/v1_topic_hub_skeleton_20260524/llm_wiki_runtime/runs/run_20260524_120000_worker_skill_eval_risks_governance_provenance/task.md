# Task

run_id:: run_20260524_120000_worker_skill_eval_risks_governance_provenance
executor_role:: skill_eval_worker
target_candidate:: cand_008_risks_governance_provenance
task_type:: skill_eval_and_next_decision

## Scope

Evaluate the completed cand_008 chain from source mining through node planning, generation, audit, blocked adoption/view, footnote layout repair, successful adoption/view, and legacy footnote layout migration.

## Required Inputs Read

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-skill-evolution/SKILL.md`
- `.llmwiki/control/skill_registry.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/summary_state.md`
- cand_008 source mining, planning, generation, audit, adoption/view, repair, repaired adoption/view, and legacy migration deliveries
- `generated/status.yaml`
- `generated/impact_queue.yaml`

## Allowed Outputs

- `.llmwiki/runs/run_20260524_120000_worker_skill_eval_risks_governance_provenance/`
- `.llmwiki/control/skill_eval_log.yaml`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`

## Explicit Non-Scope

- Do not redo source mining, generation, audit, adoption, view build, or migration.
- Do not edit `nodes/`, `kb/`, `generated/`, data source files, or archive/protocol originals.
- Do not dispatch sub-agents.

