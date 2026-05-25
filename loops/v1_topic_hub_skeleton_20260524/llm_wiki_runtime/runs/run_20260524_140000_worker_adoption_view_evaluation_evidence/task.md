# Task

run_id:: run_20260524_140000_worker_adoption_view_evaluation_evidence
executor_role:: worker_executor
worker_role:: cand_007_evaluation_evidence adoption/view builder
task_packet:: user_dispatch_for_cand_007_evaluation_evidence_adoption_view
candidate:: cand_007_evaluation_evidence
node_id:: 20260524_132000_llm_wiki_evaluation_evidence
version:: 1.0

## Objective

Adopt `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0`, synchronize root and selected-version adoption metadata, render the adopted KB view, refresh generated view/index/citation/backlink/impact/status artifacts, and run post-adoption validation.

## Gate Inputs

- Audit decision: `adopt_recommended`.
- Card validator: pass in prior generation/audit runs.
- Footnote layout gate: pass in prior generation/audit runs.
- Root metadata gate before adoption: closed and expected.

## Allowed Writes

- `nodes/20260524_132000_llm_wiki_evaluation_evidence/node.yaml`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/node.yaml` adoption/status/selected/adopted-at/audit metadata only
- `kb/20260524_132000_llm_wiki_evaluation_evidence.md`
- `kb/_index.yaml`
- relevant `generated/` outputs
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/action_queue.yaml`
- this run directory

## Forbidden Writes

- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/card.md`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/provenance.md`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/change.md`
- other node or KB bodies except mechanical adopted KB view refreshes by existing scripts
- skills, protocol, archive, or data source files

## Required Outputs

- `adoption_trace.md`
- `view_build_trace.md`
- `validation_trace.md`
- `loop_status.md`
- `loop_delivery.md`

