# Task: cand_007 Evaluation Evidence Skill Eval

Run id: `run_20260524_141000_worker_skill_eval_evaluation_evidence`
Role: `cand_007_evaluation_evidence` skill-eval / v1-coverage decision evaluator
Date: 2026-05-24

## Objective

Evaluate the `cand_007_evaluation_evidence` process from source mining through adoption/view and decide whether the loop should proceed to v1 final audit/delivery, continue with another candidate, revise skills/control rules, or block.

## Required Decision

Return one of:

- `v1_final_audit_recommended`
- `continue_loop`
- `revise_skills_then_continue`
- `blocked`

## Required Reads

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-loop-orchestration/SKILL.md`
- `.llmwiki/skills/llmwiki-skill-evolution/SKILL.md`
- `.llmwiki/control/skill_registry.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/summary_state.md`
- `generated/status.yaml`
- `generated/impact_queue.yaml`
- `kb/_index.yaml`
- prior cand_007 worker `loop_delivery.md` files from source mining, node planning, generation, audit, and adoption/view.

## Allowed Writes

- `.llmwiki/runs/run_20260524_141000_worker_skill_eval_evaluation_evidence/`
- `.llmwiki/control/skill_eval_log.yaml`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- minimal `.llmwiki/skills/llmwiki-*/SKILL.md` revisions only if evidence requires them.

## Forbidden Writes

- `nodes/`, `kb/`, and `generated/` KB content
- data source files
- archived/protocol originals

## Evaluation Focus

1. Controller/main-agent boundary and drift risk.
2. Whether the cand_007 evidence chain closed without unsupported empirical verification, superiority, benchmark, adoption, or scale claims.
3. Stability of worker-startup guard, audit read-only guard, footnote layout contract, and selected-version adoption metadata.
4. Whether adopted v1 KB nodes now constitute a complete usable v1 KB.
5. Produce either a final audit/delivery task packet or a next source-mining/frontier task packet.

## Required Artifacts

- `skill_eval_report.md`
- `process_findings.md`
- `v1_coverage_assessment.md`
- `next_task_packet.md`
- final `loop_status.md`
- `loop_delivery.md`

