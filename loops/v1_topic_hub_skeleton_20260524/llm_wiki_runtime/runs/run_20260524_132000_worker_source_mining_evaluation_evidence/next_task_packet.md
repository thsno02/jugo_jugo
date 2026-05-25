# Next Worker Task Packet

task_name:: cand_007_evaluation_evidence_node_planning
target_candidate:: cand_007_evaluation_evidence
worker_role:: node-planning worker
recommended_run_dir:: .llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/
decision_schema_version:: kb.worker_task_packet.v1

## Mission

Plan a first-version node bundle for `cand_007_evaluation_evidence`, using the source-mining run that made it ready:

`.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/`

Target node id suggestion:

`20260524_132000_llm_wiki_evaluation_evidence`

## Required Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-loop-orchestration/SKILL.md`
- `.llmwiki/skills/llmwiki-frontier-management/SKILL.md`
- `.llmwiki/skills/llmwiki-node-planning/SKILL.md` if present
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/source_scope.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/source_inventory.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/source_notes.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/source_mining.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_gaps.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/retrieval_requests.md`
- Direct source paths named in `evidence_matrix.yaml`
- Adopted KB anchors only for continuity and boundaries

## Required Outputs

Write under the planning run directory:

- `task.md`
- initial `loop_status.md` before long source reads or validation
- `planner_report.md`
- `evidence_scope.yaml`
- `generation_entry_gate.md`
- `next_task_packet.md` for a generation worker if the gate passes
- `loop_delivery.md`

## Evidence Scope

Use:

- `arxiv-wicer` as strongest direct LLM Wiki evaluation evidence.
- `arxiv-knowledge-compounding` only for cautious economic/evaluation framing because local full method/log extraction is limited.
- `repo-atomicstrata-llm-wiki-compiler` and `repo-kytmanov-obsidian-local` only for implementation-described auditability/evaluation-adjacent controls.
- `arxiv-alce`, `arxiv-ragas`, `arxiv-ares`, `arxiv-ragchecker` as adjacent evaluation frameworks.
- `reports/coverage_framework.md` and `reports/source_gap_review.md` as process/gap context.

## Non-Goals

- Do not generate a node bundle in the planning worker.
- Do not write `nodes/`, `kb/`, or `generated/`.
- Do not claim empirical superiority over RAG, GraphRAG, PKM, agent memory, or documentation systems.
- Do not make enterprise readiness, production ROI, market/adoption, user-growth, model-quality, or benchmark-leadership claims.
- Do not treat prior KB anchors as new primary evidence.
- Do not treat adjacent RAG/citation metrics as direct proof of LLM Wiki reliability.

## Citation Constraints

- Every empirical claim must name the source, method/baseline scope, and limitation.
- Every adjacent framework citation must be labeled adjacent, not direct LLM Wiki proof.
- Every implementation README citation must be framed as project self-description unless independently validated.
- Distinguish source-backed observations, worker synthesis, process notes, and prior KB continuity anchors.
- Use direct paths from `evidence_matrix.yaml` for generation source scope.

## Generation Risks To Pass Forward

- Overclaiming WiCER as proof that all LLM Wikis work.
- Treating Knowledge Compounding abstract claims as fully audited economic evidence.
- Turning implementation controls into measured reliability.
- Collapsing citation presence into citation support.
- Forgetting unresolved evidence gaps and deferred retrieval.
- Expanding into generic LLM evaluation or benchmark rankings.

## Footnote Layout Contract

Future generation packet must include this hard contract:

- `## References` must appear before the final `## Footnotes`.
- `## Footnotes` must be the last top-level section in `card.md`.
- No section may appear after `## Footnotes`.
- Audit and adoption/view workers must rerun this gate before adoption.

## Decision Criteria

If candidate remains `ready_to_build` in `.llmwiki/control/knowledge_frontier.yaml`, emit a generation-entry gate. If the planner finds any unresolved retrieval blocker, write `LOOP_BLOCKED` and a concrete minimal unblock condition.
