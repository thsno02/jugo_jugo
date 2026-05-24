# Task

Worker role: `cand_007_evaluation_evidence` node-planning worker.

Candidate: `cand_007_evaluation_evidence`

Suggested node id: `20260524_132000_llm_wiki_evaluation_evidence`

Objective: convert the source-mining worker's evidence scope into an executable node plan and run the generation-entry gate.

Boundary:
- Focus on LLM Wiki evaluation/evidence: evidence quality, citation auditability, evaluation boundaries, verifiable and unverifiable claims, source gaps/deferred retrieval, and trustworthy KB-node expression.
- Frame as evaluation dimensions, evidence levels, and boundaries.
- Do not claim LLM Wiki has been comprehensively empirically validated or is superior to RAG, GraphRAG, PKM, or agent memory.
- Do not expand into generic LLM evaluation, benchmark rankings, model-quality evaluation, product review, effect claims, or adoption/scale claims.
- Only propose sections and claims supported by source evidence.
- Explicitly distinguish primary sources, secondary/process notes, and prior-KB anchors.
- Include a footnote layout contract in the next task packet: `## References` before final `## Footnotes`; `## Footnotes` is the last top-level section.

Allowed writes:
- `.llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- Candidate planning status in `.llmwiki/control/knowledge_frontier.yaml` if necessary.

Forbidden writes:
- `nodes/`, `kb/`, or `generated/` KB content.
- Source evidence content, skills, protocol, or archive originals.

Required run artifacts:
- `task.md`
- `planner_report.md`
- `node_plan.yaml`
- `evidence_scope.md`
- `generation_entry_gate.md`
- `next_task_packet.md`
- `loop_status.md`
- `loop_delivery.md`
