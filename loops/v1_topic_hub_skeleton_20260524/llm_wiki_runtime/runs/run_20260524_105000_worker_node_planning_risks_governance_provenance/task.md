# Task

run_id:: run_20260524_105000_worker_node_planning_risks_governance_provenance
executor_role:: worker_executor
worker_role:: node-planning worker
target_candidate:: cand_008_risks_governance_provenance
target_node_id:: 20260524_104000_llm_wiki_risks_governance_and_provenance
task_packet:: .llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/next_task_packet.md
status:: LOOP_DONE

## Objective

Convert the source-mining evidence scope for `cand_008_risks_governance_provenance` into an executable first-version node plan and run the generation-entry gate.

## Allowed Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-node-planning/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/loop_delivery.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/next_task_packet.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/source_inventory.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/source_notes.md`
- Adopted prior KB nodes/cards as boundary continuity anchors only.

## Allowed Writes

- `.llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- Candidate planning status fields for `cand_008_risks_governance_provenance` in `.llmwiki/control/knowledge_frontier.yaml`.

## Constraints

- Do not generate node bundle content.
- Do not audit or adopt.
- Do not write `nodes/`, `kb/`, or `generated/`.
- Do not perform new source mining or retrieval.
- Keep the node focused on LLM Wiki risks, governance boundaries, provenance, traceability, and citation audit.
- Treat OWASP detail pages, enterprise governance primary sources, and Reddit/community discourse as deferred retrieval unless locally preserved evidence directly supports a bounded claim.
