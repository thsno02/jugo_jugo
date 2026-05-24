# Adoption Trace

run_id:: run_20260524_140000_worker_adoption_view_evaluation_evidence
executor_role:: worker_executor
candidate:: cand_007_evaluation_evidence
node_id:: 20260524_132000_llm_wiki_evaluation_evidence
version:: 1.0
decision:: adopted

## Preconditions

- Generation delivery: `.llmwiki/runs/run_20260524_134000_worker_generation_evaluation_evidence/loop_delivery.md`
- Audit delivery: `.llmwiki/runs/run_20260524_135000_worker_audit_evaluation_evidence/loop_delivery.md`
- Audit report: `.llmwiki/runs/run_20260524_135000_worker_audit_evaluation_evidence/audit_report.md`
- Audit decision: `adopt_recommended`
- Root metadata gate before adoption: closed; root `nodes/20260524_132000_llm_wiki_evaluation_evidence/node.yaml` did not exist before this worker.

## Root Metadata Written

Created `nodes/20260524_132000_llm_wiki_evaluation_evidence/node.yaml` with:

- `schema: kb.node_metadata.v1`
- `id: 20260524_132000_llm_wiki_evaluation_evidence`
- `version: "1.0"`
- `version_status: adopted`
- `node_created_at: "2026-05-24T13:40:00+08:00"`
- `version_created_at: "2026-05-24T13:40:00+08:00"`
- `version_adopted_at: "2026-05-24T21:29:27+08:00"`
- `status: active`
- `stability: initial`
- `usable_as_support: true`
- `paths.version_dir/card/provenance/change/kb_view`
- tags copied from selected version metadata
- `audit.state: passed`
- `audit.run: .llmwiki/runs/run_20260524_135000_worker_audit_evaluation_evidence/audit_report.md`
- `audit.decision: adopt_recommended`
- `audit.adoption_run: .llmwiki/runs/run_20260524_140000_worker_adoption_view_evaluation_evidence`

## Selected-Version Metadata Fields Changed

Only adoption/status/selected/adopted-at/audit metadata fields were changed in `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/node.yaml`:

- `status`: `candidate` -> `active`
- `version_status`: `pending_audit` -> `adopted`
- `adoption_status`: `pending_audit` -> `adopted`
- `adopted`: `false` -> `true`
- `selected`: `false` -> `true`
- `adoption_gate`: `pending_citation_and_adoption_audit` -> `citation_and_adoption_audit_passed`
- `version_adopted_at`: added `"2026-05-24T21:29:27+08:00"`
- `audit.state`: `pending` -> `passed`
- `audit.run`: `null` -> `.llmwiki/runs/run_20260524_135000_worker_audit_evaluation_evidence/audit_report.md`
- `audit.decision`: `pending_audit` -> `adopt_recommended`
- `audit.adoption_run`: added `.llmwiki/runs/run_20260524_140000_worker_adoption_view_evaluation_evidence`

## Forbidden Writes Avoided

- Did not edit `versions/1.0/card.md`.
- Did not edit `versions/1.0/provenance.md`.
- Did not edit `versions/1.0/change.md`.
- Did not edit source evidence, skills, protocols, archives, or data source files.

