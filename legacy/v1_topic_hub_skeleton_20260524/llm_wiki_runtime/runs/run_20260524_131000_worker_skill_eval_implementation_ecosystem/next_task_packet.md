# Next Worker Task Packet

task_name:: cand_007_evaluation_evidence_source_mining_frontier
target_candidate:: cand_007_evaluation_evidence
worker_role:: source-mining/frontier worker
recommended_run_dir:: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/
decision_schema_version:: kb.worker_task_packet.v1

## Mission

Mine evidence for a bounded first-version LLM Wiki evaluation-evidence node. Determine whether local and limited-retrieval evidence can support a v1 node about how LLM Wiki should be evaluated, without claiming measured superiority, production effectiveness, or comprehensive benchmark validation.

## Topic Boundary

In scope:

- Citation faithfulness and citation/claim support evaluation.
- RAG/GraphRAG answer-grounding and retrieval-augmented evaluation as adjacent evidence.
- Knowledge compounding, knowledge maintenance, stale knowledge, provenance, and source-preservation evaluation signals.
- Evaluation criteria suitable for LLM Wiki: source traceability, claim-level support, update/writeback correctness, contradiction/staleness handling, lint/audit outcomes, and human review gates.
- Local evidence that is already preserved under `data/`, reports, manifests, and adopted KB anchors.

Out of scope:

- Claims that LLM Wiki is empirically better than RAG, GraphRAG, PKM, agent memory, or documentation systems.
- Enterprise readiness, production ROI, market adoption, user growth, downloads, or benchmark leadership.
- Building a final evaluation benchmark suite unless direct sources support it.
- Generating a node bundle, audit, adoption, or view build in this worker.

## Required Inputs To Read First

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-source-mining/SKILL.md`
- `.llmwiki/skills/llmwiki-frontier-management/SKILL.md`
- `.llmwiki/skills/llmwiki-dynamic-retrieval/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/summary_state.md`
- `reports/coverage_framework.md`
- `reports/source_gap_review.md`
- relevant local `data/raw/` and `data/manifests/` entries for evaluation, RAG evaluation, citation faithfulness, ALCE, WiCER, memory/knowledge-compounding, GraphRAG, and provenance/security-adjacent papers
- adopted KB anchors only for continuity and boundaries:
  - `kb/20260524_062000_llm_wiki_origin_and_canon.md`
  - `kb/20260524_072000_llm_wiki_working_definition.md`
  - `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
  - `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
  - `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`
  - `kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md`
  - `kb/20260524_122000_llm_wiki_implementation_ecosystem.md`

## Allowed Writes

- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- dynamic retrieval outputs under `data/raw/` and manifest entries only if retrieval is actually needed and allowed by the limits below

## Forbidden Writes

- `nodes/`
- `kb/`
- `generated/`
- any version bundle, audit, adoption, or view artifact
- archive/protocol originals
- unrelated skill files

## Retrieval Limits

Start with local corpus mining. Use dynamic retrieval only if local preserved sources cannot support a bounded v1 evaluation-evidence candidate.

If retrieval is needed:

- maximum 3 external retrieval attempts
- prefer primary papers, official project docs, or preserved open-access pages
- preserve each successful source under `data/raw/` and update manifests before citing it
- write failures and deferred requests to `retrieval_requests.md`
- do not block v1 for broad benchmark, enterprise, adoption, or market-evidence gaps if a bounded evaluation-criteria node is otherwise supportable

## Required Artifacts

Write these in the run directory:

- `task.md`
- `source_scope.md`
- `source_inventory.md`
- `source_notes.md`
- `source_mining.md`
- `evidence_matrix.yaml`
- `candidate_frontier_delta.yaml`
- `evidence_gaps.md`
- `retrieval_requests.md`
- `mining_trace.md`
- `frontier_update.md`
- `frontier_trace.md`
- `next_task_packet.md`
- `loop_status.md`
- `loop_delivery.md`

## Decision Schema

End with exactly one decision:

- `ready_to_plan`: local plus any limited retrieved evidence supports a bounded v1 evaluation-evidence node; frontier status should become `ready_to_build`.
- `needs_more_mining`: evidence is promising but still too indirect or scattered; list exact missing source classes.
- `needs_retrieval`: a specific retrieval blocker prevents bounded v1; write concrete retrieval requests.
- `defer`: candidate should not be built now because evidence is too weak or better merged into another candidate.
- `blocked`: worker cannot proceed within allowed inputs/writes; write `LOOP_BLOCKED`, blocker, and minimal unblock condition.

For `ready_to_plan`, the next packet must be a node-planning packet and must name the source-mining run that made `cand_007_evaluation_evidence` ready.

## Footnote Layout Contract For Future Generation Packet

If this worker emits a future generation packet, include the hard contract:

- `## References` must appear before the final `## Footnotes`.
- `## Footnotes` must be the last top-level section in `card.md`.
- No section may appear after `## Footnotes`.
- Audit and adoption/view workers must rerun this gate before adoption.

## Output Delivery Requirements

`loop_delivery.md` must include:

- `executor_role`
- `task_packet`
- `allowed_inputs`
- `outputs_written`
- `status:: LOOP_DONE` or `status:: LOOP_BLOCKED`
- decision
- evidence_state
- retrieval attempts and deferred retrieval
- frontier changes made
- next_action

