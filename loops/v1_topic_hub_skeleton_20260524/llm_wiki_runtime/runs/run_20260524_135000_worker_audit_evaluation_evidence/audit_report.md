# Adoption Audit Report

run_id:: run_20260524_135000_worker_audit_evaluation_evidence
executor_role:: worker_executor
candidate:: cand_007_evaluation_evidence
node_id:: 20260524_132000_llm_wiki_evaluation_evidence
version:: 1.0
decision:: adopt_recommended

## Required Bundle

- `node.yaml`: present in candidate version bundle.
- `card.md`: present and validator pass.
- `provenance.md`: present.
- `change.md`: present.

## Adoption Gates

- source_scope_gate: pass. The bundle traces to source mining and planning artifacts for `cand_007_evaluation_evidence`.
- citation_gate: pass. Citation fields and pinned paths validate; semantic citation use remains within planned source tiers.
- provenance_gate: pass. Provenance contains why this version exists, inputs used, dynamic retrieval state, prior KB treatment, process artifacts, production/citation rationale, synthesis decisions, audit trail, adoption rationale, limits, uncertainty, and revision triggers.
- direct_evidence_boundary_gate: pass. WiCER remains bounded direct evidence, not comprehensive LLM Wiki validation.
- economic_claim_boundary_gate: pass. Knowledge Compounding remains cautious economic/token-cost framing.
- implementation_self_description_boundary_gate: pass. Atomicstrata/Kytmanov are self-description only.
- adjacent_eval_transfer_gate: pass. ALCE/Ragas/ARES/RAGChecker remain adjacent vocabulary only.
- deferred_retrieval_gate: pass. Missing evidence is preserved and not written as fulfilled.
- prior_kb_anchor_gate: pass. Prior KB is continuity/boundary only.
- footnote_layout_gate: pass.
- root_metadata_gate: pass_closed. No root `nodes/20260524_132000_llm_wiki_evaluation_evidence/node.yaml` exists; adoption remains pending.

## Provenance / Change Review

- Provenance separates direct evidence, economic framing, implementation-described auditability, adjacent evaluation vocabulary, process gaps, and prior-KB continuity.
- Provenance states no dynamic retrieval was used.
- Change file is `genesis -> 1.0`.
- Change file records `adoption_status:: pending_audit`.
- Change scale is marked `major`, but this is a genesis candidate with no adopted downstream dependents and `propagation_required:: false`.

## Decision

decision:: adopt_recommended

Rationale: The candidate bundle is parseable, traceable, and scoped to the bounded evidence plan. It passes the official card validator, preserves deferred gaps, keeps source tiers separated, avoids unsupported evaluation/adoption/ROI/superiority claims, and leaves root metadata adoption closed for the controller/adoption step.

## Minimal Repair Task

None.

