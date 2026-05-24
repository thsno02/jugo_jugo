# Adoption Trace

decision:: adopted
audit_input_decision:: adopt_recommended
repair_input_decision:: repair_validated
adopted_at:: 2026-05-24T18:54:17+08:00

## Gate Inputs

- Audit delivery: `.llmwiki/runs/run_20260524_111000_worker_audit_risks_governance_provenance/loop_delivery.md`
- Audit report: `.llmwiki/runs/run_20260524_111000_worker_audit_risks_governance_provenance/audit_report.md`
- Footnote repair delivery: `.llmwiki/runs/run_20260524_113000_worker_repair_footnote_layout_contract/loop_delivery.md`
- Target card validator before adoption: pass
- Target footnote layout gate before adoption: pass

## Root Metadata Written

Wrote `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/node.yaml` with adopted root metadata pointing to version `1.0`.

## Exact Selected-Version Metadata Fields Changed

- `status`: `candidate` -> `active`
- `version_status`: `pending_audit` -> `adopted`
- `adoption_status`: `pending_audit` -> `adopted`
- `adopted`: `false` -> `true`
- `selected`: `false` -> `true`
- `adoption_gate`: `citation_and_adoption_audit_required` -> `citation_and_adoption_audit_passed`
- `version_adopted_at`: added `2026-05-24T18:54:17+08:00`
- `audit.state`: `pending` -> `passed`
- `audit.run`: `null` -> `.llmwiki/runs/run_20260524_111000_worker_audit_risks_governance_provenance/audit_report.md`
- `audit.decision`: `pending` -> `adopt_recommended`
- `audit.adoption_run`: `null` -> `.llmwiki/runs/run_20260524_114000_worker_adoption_view_risks_governance_provenance_after_footnote_repair`

## Non-Writes

- Did not rewrite `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`.
- Did not rewrite `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/provenance.md`.
- Did not rewrite `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/change.md`.
- Did not alter evidence content.
