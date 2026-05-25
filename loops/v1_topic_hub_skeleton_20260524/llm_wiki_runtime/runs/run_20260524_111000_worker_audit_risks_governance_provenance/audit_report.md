# Adoption Audit Report

run_id:: run_20260524_111000_worker_audit_risks_governance_provenance
executor_role:: worker_executor
worker_role:: cand_008_risks_governance_provenance citation/adoption audit worker
candidate_id:: cand_008_risks_governance_provenance
node_id:: 20260524_104000_llm_wiki_risks_governance_and_provenance
version:: 1.0
status:: passed
decision:: adopt_recommended

## Gate Results

| Gate | Result | Notes |
| --- | --- | --- |
| Bundle files exist | passed | `node.yaml`, `card.md`, `provenance.md`, and `change.md` exist under `versions/1.0/`. |
| Card validator | passed | Official validator returned `card validation passed: 1 cards`. |
| Citation paths and fields | passed | Citation fields and target/pinned paths pass official validation. |
| Evidence traceability | passed | Card citations trace back to source-mining matrix and planner evidence scope. |
| Citation faithfulness | passed | Main LLM Wiki claims are supported by implementation READMEs and WiCER; ALCE/security/governance sources are bounded as adjacent/framework/discourse. |
| Adjacent-source boundary | passed | eTAMP, PoisonedRAG, and GraphRAG poisoning are analogies only, with no incident-rate or exploit transfer. |
| Broad-framework boundary | passed | OWASP/NIST/Microsoft are used only as vocabulary/framework sources. |
| Discourse boundary | passed | HN is discourse seed only. |
| Prior-KB boundary | passed | Prior KB references are continuity anchors only. |
| Provenance completeness | passed | Provenance separates primary, adjacent, process/vocabulary/discourse, prior-KB, and no-dynamic-retrieval sections. |
| Change file | passed | `genesis -> 1.0`, `adoption_status:: pending_audit`, and no adopted-root write. |
| Root metadata gate | passed | `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/node.yaml` is absent, so adoption metadata remains closed. |

## Adoption Decision

decision:: adopt_recommended

The candidate bundle is suitable for controller review and adoption. No repair or additional retrieval is required before adoption.

## Minimal Repair Task

None.

## Notes For Controller

This is a first-version `genesis -> 1.0` candidate. Although `change_scale:: major` is present, there is no prior adopted version of this node to impact-analyze; `propagation_required:: false` is consistent with a genesis first version. Later major changes after adoption should use impact analysis.
