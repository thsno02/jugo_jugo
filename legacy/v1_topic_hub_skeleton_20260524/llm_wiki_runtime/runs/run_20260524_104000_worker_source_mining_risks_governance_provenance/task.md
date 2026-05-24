# Task

run_id:: run_20260524_104000_worker_source_mining_risks_governance_provenance
executor_role:: worker_executor
worker_role:: source-mining + frontier-update worker
task_packet:: .llmwiki/runs/run_20260524_103000_worker_skill_eval_vs_rag_write_loop/next_task_packet.md
target_candidate:: cand_008_risks_governance_provenance
related_seed:: cand_011_initial_risk_discourse

## Objective

Mine local, traceable sources for a bounded first-version node on LLM Wiki risks, governance, and provenance/traceability. The candidate should distinguish direct LLM Wiki implementation evidence from adjacent LLM/RAG/agent-memory risk evidence and process/framework sources.

## Conflict Handling

The user request and task packet both require source-mining/frontier gating. `generated/status.yaml` suggests `run_dynamic_retrieval_test`, but the current controller state/action queue and task packet specifically dispatch cand_008 source mining. The stricter task-specific source-mining/frontier gate is followed here. No network retrieval is performed because local evidence is sufficient for a bounded first version.

## Allowed Inputs Used

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-source-mining/SKILL.md`
- `.llmwiki/skills/llmwiki-frontier-management/SKILL.md`
- `.llmwiki/skills/llmwiki-dynamic-retrieval/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/runs/run_20260524_103000_worker_skill_eval_vs_rag_write_loop/loop_delivery.md`
- `.llmwiki/runs/run_20260524_103000_worker_skill_eval_vs_rag_write_loop/next_task_packet.md`
- `generated/status.yaml`
- Local source files listed in `source_scope.md`

## Forbidden Inputs Honored

- No blocked Reddit pages were used as substantive evidence.
- No intercepted AICritique enterprise page was used.
- No network retrieval result was used.
- Prior KB nodes were used only as boundary continuity, not as primary evidence for risk/governance/security facts.
- No files under `nodes/`, `kb/`, `generated/`, `skills/`, `archive/`, or source-data content were written.

