# Next Worker Task Packet

task_name:: cand_007_evaluation_evidence_generation
target_candidate:: cand_007_evaluation_evidence
target_node_id:: 20260524_132000_llm_wiki_evaluation_evidence
worker_role:: generation worker
recommended_run_dir:: .llmwiki/runs/run_20260524_134000_worker_generation_evaluation_evidence/
decision_schema_version:: kb.worker_task_packet.v1

## Mission

Generate the first-version node bundle for `cand_007_evaluation_evidence` as an evaluation/evidence node. The card must be framed as "evaluation dimensions, evidence levels, and boundaries", not as proof that LLM Wiki is broadly validated or superior to adjacent systems.

## Allowed Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-loop-orchestration/SKILL.md`
- `.llmwiki/skills/llmwiki-card-generation/SKILL.md` if present
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/planner_report.md`
- `.llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/node_plan.yaml`
- `.llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/evidence_scope.md`
- `.llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/evidence_scope.yaml`
- `.llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/generation_entry_gate.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/source_scope.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/source_inventory.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/source_notes.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/source_mining.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_gaps.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/retrieval_requests.md`
- Direct source paths named in `evidence_matrix.yaml`
- Prior adopted KB anchors only for continuity and boundaries

## Forbidden Inputs

- Unmined web pages or new retrieval results.
- Controller drift sample artifacts as authority.
- Prior KB anchors as primary evidence for new evaluation claims.
- Adjacent RAG/citation papers as direct LLM Wiki proof.
- Implementation README claims as measured reliability.

## Allowed Writes

Write only:

- `.llmwiki/runs/run_20260524_134000_worker_generation_evaluation_evidence/`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/node.yaml`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/card.md`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/provenance.md`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/change.md`

## Forbidden Writes

- `nodes/20260524_132000_llm_wiki_evaluation_evidence/node.yaml`
- `kb/20260524_132000_llm_wiki_evaluation_evidence.md`
- `generated/`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/state.yaml`
- source evidence, skills, protocols, or archive originals

## Required Artifacts

In the generation run directory:

- `task.md`
- initial `loop_status.md` before source reads or validation
- `generation_report.md`
- `loop_delivery.md`

In the version bundle:

- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/node.yaml`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/card.md`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/provenance.md`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/change.md`

## Citation / Provenance / Change Constraints

- Every empirical, benchmark-style, or economic claim must name source, method or baseline scope, and limitation.
- Label source tier in prose or provenance: direct LLM Wiki evaluation, primary implementation self-description, adjacent evaluation framework, secondary/process note, or prior-KB continuity.
- Use WiCER as the strongest direct evaluation source, but state its model, baseline, validation, judge, hardware, replication, and scope limits.
- Use Knowledge Compounding only for cautious abstract-level economic/token-cost framing unless later full extraction is mined.
- Use Atomicstrata/Kytmanov only for described controls, not effectiveness.
- Use ALCE/Ragas/ARES/RAGChecker only as adjacent vocabulary or method inspiration.
- Preserve source gaps and deferred retrieval in `provenance.md` and `change.md`.
- Do not add claims that require new source mining.

## Audit Concerns

- Overclaiming WiCER as proof all LLM Wikis work.
- Treating Knowledge Compounding as fully audited economic proof.
- Turning source ranges, lint, confidence labels, or review queues into measured reliability.
- Collapsing "has a citation" into "citation supports the claim".
- Hiding deferred retrieval or missing evidence.
- Expanding into generic LLM evaluation, benchmark rankings, model-quality evaluation, product review, adoption, scale, ROI, or enterprise claims.
- Misusing prior KB anchors as fresh primary evidence.

## Footnote Layout Contract

- `## References` must appear before the final `## Footnotes`.
- `## Footnotes` must be the last top-level section in `card.md`.
- No section may appear after `## Footnotes`.
- Audit and adoption/view workers must rerun this gate before adoption.

## Completion Marker

End `loop_delivery.md` and final worker response with `LOOP_DONE` if the bundle is generated within scope. Use `LOOP_BLOCKED` if source evidence, citation constraints, output path constraints, or timebox/no-progress prevents safe generation, and name the minimal unblock condition.
