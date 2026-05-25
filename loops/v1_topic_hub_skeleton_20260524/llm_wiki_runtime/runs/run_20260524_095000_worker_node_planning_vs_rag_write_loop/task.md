# Task

run_id:: run_20260524_095000_worker_node_planning_vs_rag_write_loop
executor_role:: cand_010_vs_rag_write_loop node-planning worker
task_packet:: current user/controller packet plus `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/next_task_packet.md`
target_candidate:: cand_010_vs_rag_write_loop
target_node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop

## Objective

Convert the source-mining scope for `cand_010_vs_rag_write_loop` into an executable first-version node plan and run the generation-entry gate.

The planned node must stay bounded to one comparison slice: LLM Wiki's durable wiki/node artifact, writeback, lint/update, index/log, citation, and provenance workflow versus RAG/GraphRAG/agent-memory retrieval, index, synthesis, and memory mechanisms.

## Authority And Boundaries

- Produce node-planning and generation-entry artifacts only.
- Do not generate `node.yaml`, `card.md`, `provenance.md`, or `change.md`.
- Do not write or adopt root `nodes/<node_id>/node.yaml`.
- Do not audit, adopt, view-build, source-mine, or retrieve new sources.
- Treat prior KB nodes as continuity and boundary anchors, not as primary evidence for new RAG or agent-memory facts.

## Required Inputs Read

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-node-planning/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/loop_delivery.md`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/next_task_packet.md`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/source_inventory.md`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/source_notes.md`
- adopted prior KB anchors for origin/canon, working definition, architecture, and workflow boundaries

## Required Outputs

- `task.md`
- `planner_report.md`
- `node_plan.yaml`
- `evidence_scope.md`
- `evidence_scope.yaml`
- `generation_entry_gate.md`
- `next_task_packet.md`
- `loop_status.md`
- `loop_delivery.md`

