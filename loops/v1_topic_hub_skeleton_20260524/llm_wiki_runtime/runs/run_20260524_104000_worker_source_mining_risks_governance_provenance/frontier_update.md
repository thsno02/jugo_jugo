# Frontier Update

run_id:: run_20260524_104000_worker_source_mining_risks_governance_provenance
executor_role:: worker_executor
target_candidate:: cand_008_risks_governance_provenance
decision:: ready_to_plan

## Candidate Decision

candidate_id:: cand_008_risks_governance_provenance
frontier_status:: ready_to_build
evidence_state:: enough_for_first_version
retrieval_required_before_build:: false
recommended_next_action:: node_planning_for_cand_008_risks_governance_provenance

## Rationale

Local evidence is sufficient for a bounded first-version node because:

- direct LLM Wiki implementations provide concrete provenance, review, lint, confidence, contradiction, source-hash, and stale-check mechanisms;
- WiCER provides LLM Wiki-specific evidence that compilation can lose critical facts and that evaluate/refine loops are a plausible mitigation;
- Memory as Metabolism provides governance/drift vocabulary for source preservation, audit, retention, and user-coupled drift;
- ALCE provides adjacent evidence that citation quality is nontrivial and requires explicit evaluation;
- eTAMP, PoisonedRAG, and GraphRAG poisoning provide adjacent threat models for persistent memory, external knowledge databases, and compiled structures;
- HN provides early discourse for staleness, correctness, drift, scaling, second-order information, and human review concerns.

The candidate is ready only for a carefully scoped node. It is not ready for enterprise compliance, incident-rate, legal, or risk-reduction claims.

## cand_011 Merge

`cand_011_initial_risk_discourse` should not become a standalone first-version node now. Its HN evidence is useful but narrow, so it is merged into `cand_008_risks_governance_provenance` as early discourse and marked `deferred` in the frontier.

## Retrieval State

No retrieval attempted. No retrieval required before bounded build. Deferred retrieval requests are documented for OWASP detailed pages, enterprise governance primary sources, and blocked Reddit/community discourse.

