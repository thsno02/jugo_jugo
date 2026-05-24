# Generation Entry Gate

run_id:: run_20260524_133000_worker_node_planning_evaluation_evidence
executor_role:: worker_executor
target_candidate:: cand_007_evaluation_evidence
target_node_id:: 20260524_132000_llm_wiki_evaluation_evidence

decision:: pass
normalized_decision:: generation_entry_pass

## Basis

- Candidate exists in `.llmwiki/control/knowledge_frontier.yaml`.
- Candidate status is `ready_to_build`.
- Candidate evidence state is `enough_for_first_version`.
- Source-mining run is worker-attributed: `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence`.
- Retrieval required before build is `false`.
- Scoped primary, adjacent, process, and prior-KB anchor roles are explicit.
- Generation output paths are bounded to first-version bundle files.
- Root adoption metadata, `kb/`, and `generated/` are forbidden for generation.

## Evidence Sufficiency

Sufficient for a bounded first-version node about evaluation dimensions, evidence levels, citation auditability, and unsupported-claim boundaries.

Not sufficient for broad claims of empirical superiority, production reliability, enterprise readiness, ROI, adoption/scale, benchmark leadership, or generic model-quality evaluation.

## Generation Conditions

The generation worker may proceed only if it keeps the node inside the evidence scope in `node_plan.yaml`, `evidence_scope.md`, and `evidence_scope.yaml`.

Required version target: `1.0`.

Allowed first-version outputs:

- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/node.yaml`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/card.md`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/provenance.md`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/change.md`

Forbidden generation outputs:

- `nodes/20260524_132000_llm_wiki_evaluation_evidence/node.yaml`
- `kb/20260524_132000_llm_wiki_evaluation_evidence.md`
- `generated/`

## Audit Concerns To Preserve

- Source tier labels must remain visible.
- Adjacent sources must not become direct evidence.
- Implementation self-description must not become measured reliability.
- Knowledge Compounding must remain abstract-level unless later mined.
- All unsupported or deferred evidence must be preserved in provenance/change.
- `## References` must appear before final `## Footnotes`; `## Footnotes` must be the last top-level section.

LOOP_DONE
