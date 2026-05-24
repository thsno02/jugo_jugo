# Task

run_id:: run_20260524_132000_worker_source_mining_evaluation_evidence
executor_role:: worker_executor
worker_role:: source-mining/frontier worker
target_candidate:: cand_007_evaluation_evidence
task_packet:: .llmwiki/runs/run_20260524_131000_worker_skill_eval_implementation_ecosystem/next_task_packet.md
started_at:: 2026-05-24T22:15:00+08:00
status:: initialized

## Mission

Mine local, traceable evidence for a bounded first-version LLM Wiki evaluation/evidence node and update the candidate frontier. The worker must decide whether `cand_007_evaluation_evidence` is ready for node planning, needs more mining, needs retrieval, or should be deferred.

## Allowed Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-loop-orchestration/SKILL.md`
- `.llmwiki/skills/llmwiki-source-mining/SKILL.md`
- `.llmwiki/skills/llmwiki-frontier-management/SKILL.md`
- `.llmwiki/skills/llmwiki-dynamic-retrieval/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- `generated/status.yaml`
- `reports/coverage_framework.md`
- `reports/source_gap_review.md`
- relevant preserved local `data/` sources and manifests
- adopted `kb/` anchors only for continuity and boundaries

## Allowed Writes

- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- `data/logs/source_access_log.jsonl` only for actual source access attempts if needed

## Forbidden Writes

- `nodes/`
- `kb/`
- `generated/`
- `.llmwiki/skills/`
- archive/protocol originals
- raw data source content unless a protocol-authorized retrieval succeeds

## Scope Boundary

Focus on LLM Wiki evaluation/evidence: evidence quality, citation auditability, evaluation boundaries, verifiable and unverifiable claims, source gaps/deferred retrieval, and KB-node confidence/trust expression. Do not expand into general LLM benchmark ranking, model quality, product evaluation, adoption/scale claims, or superiority over adjacent systems.

## Startup Gate

This `task.md` and the initial `loop_status.md` are written before source reads, per the revised orchestration skill.
