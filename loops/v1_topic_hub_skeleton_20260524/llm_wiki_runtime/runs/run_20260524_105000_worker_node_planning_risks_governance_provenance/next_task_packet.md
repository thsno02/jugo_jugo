# Next Worker Task Packet

task_name:: cand_008_risks_governance_provenance_generation
target_candidate:: cand_008_risks_governance_provenance
target_node_id:: 20260524_104000_llm_wiki_risks_governance_and_provenance
target_version:: 1.0
recommended_run_dir:: .llmwiki/runs/run_20260524_110000_worker_generation_risks_governance_provenance/
worker_role:: generation worker
generation_entry_decision:: pass

## Allowed Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/skills/llmwiki-card-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/source_scope.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/source_mining.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/source_inventory.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/source_notes.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/evidence_gaps.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/retrieval_requests.md`
- `.llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/planner_report.md`
- `.llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/node_plan.yaml`
- `.llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/evidence_scope.md`
- `.llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/evidence_scope.yaml`
- Prior KB nodes only as boundary continuity anchors:
  - `kb/20260524_062000_llm_wiki_origin_and_canon.md`
  - `kb/20260524_072000_llm_wiki_working_definition.md`
  - `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
  - `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
  - `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`

## Forbidden Inputs

- No new web retrieval.
- No blocked Reddit/community pages.
- No controller drift sample as authority.
- No prior KB as primary evidence for risk, governance, incident, or effectiveness facts.
- No unmined OWASP detailed category claims.
- No enterprise governance primary-source assumptions beyond preserved local evidence.

## Allowed Writes

- `.llmwiki/runs/run_20260524_110000_worker_generation_risks_governance_provenance/`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/node.yaml`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/provenance.md`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/change.md`
- Control status files only if generation completes and the task packet permits it.

## Forbidden Writes

- Do not write or adopt `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/node.yaml`.
- Do not write `kb/` or `generated/` views.
- Do not audit or adopt the node.
- Do not alter source evidence, skills, protocols, or archive files.

## Required Artifacts

- `task.md`
- `node.yaml`
- `card.md`
- `provenance.md`
- `change.md`
- `loop_status.md`
- `loop_delivery.md`

## Citation And Provenance Constraints

- Every substantive risk/control claim must identify source type and cite allowed source ids.
- Implementation READMEs and WiCER are the strongest LLM Wiki-specific evidence.
- ALCE, eTAMP, PoisonedRAG, GraphRAG poisoning, and Memory as Metabolism must be marked as adjacent or framing sources where applicable.
- OWASP/NIST/Microsoft are vocabulary/framework sources only unless exact preserved local text supports a narrow claim.
- HN is early discourse only.
- Prior KB links are continuity anchors, not primary evidence.
- Provenance must explicitly list deferred retrieval gaps for detailed OWASP pages, enterprise governance primary sources, and blocked Reddit/community discourse.

## Change Constraints

- Version target is `1.0`.
- Use node id `20260524_104000_llm_wiki_risks_governance_and_provenance`.
- Keep the card focused on LLM Wiki source/compile/wiki/writeback risks and controls.
- Include limitations for no incident evidence, no measured mitigation effectiveness, no enterprise compliance sufficiency, and no direct attack-rate transfer.

## Audit Concerns

- Watch for generic AI governance filler.
- Watch for source preservation being framed as security/privacy safety.
- Watch for citation presence being framed as citation faithfulness.
- Watch for adjacent threat models becoming direct LLM Wiki incidents.
- Watch for prior KB anchors being used as new evidence.
- Watch for root adoption metadata written before audit.

## Completion Marker

The generation worker must finish with `LOOP_DONE` or `LOOP_BLOCKED`.
