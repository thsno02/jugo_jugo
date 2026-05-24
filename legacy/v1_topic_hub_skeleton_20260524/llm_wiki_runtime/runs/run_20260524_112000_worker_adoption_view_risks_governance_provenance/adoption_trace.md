# Adoption Trace

run_id:: run_20260524_112000_worker_adoption_view_risks_governance_provenance
executor_role:: worker_executor
target_node_id:: 20260524_104000_llm_wiki_risks_governance_and_provenance
target_version:: 1.0
audit_decision_input:: adopt_recommended
decision:: adoption_blocked

## Pre-Adoption Gate Results

| Gate | Result | Notes |
| --- | --- | --- |
| Audit decision | pass | Audit run `run_20260524_111000_worker_audit_risks_governance_provenance` reports `decision:: adopt_recommended`. |
| Card validator input | pass | Official card validator passes the target candidate card. |
| Root metadata gate before adoption | pass | Root `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/node.yaml` remains absent before adoption. |
| Footnote layout gate | fail | `## Footnotes` appears before `## References`, so Footnotes is not the final top-level section. |

## Section Order Finding

Observed top-level section order in `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`:

- line 1: `# LLM Wiki 的风险、治理与 provenance 边界`
- line 25: `## Footnotes`
- line 155: `## References`

Expected order:

- `## References`
- final top-level section: `## Footnotes`

## Adoption Writes

No adoption metadata writes were performed.

Exact selected-version metadata fields changed: none.

Root `node.yaml` written: no.

KB view rendered: no.

Generated view artifacts refreshed: no.

## Minimal Repair Task

Dispatch a repair worker to adjust only the card section order so that `References` appears before final `Footnotes`, then rerun citation/card validation and this adoption gate. The repair worker should also synchronize the footnote layout contract into card-generation, citation-formatting, and view-building skills so future cards and rendered KB views keep Footnotes as the final top-level section.
