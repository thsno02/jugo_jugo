# Loop Status

run_id:: run_20260524_112000_worker_adoption_view_risks_governance_provenance
executor_role:: worker_executor
worker_role:: cand_008_risks_governance_provenance adoption/view builder
status:: LOOP_BLOCKED
decision:: adoption_blocked
blocker:: footnote_layout_gate_failed
target_candidate:: cand_008_risks_governance_provenance
target_node_id:: 20260524_104000_llm_wiki_risks_governance_and_provenance
target_version:: 1.0

## Current State

Audit decision is adopt-recommended, but adoption is blocked by the newly required Markdown layout gate: `Footnotes` must be the final top-level section and `References` must appear before it.

## Required Next Action

dispatch_repair_worker_for_cand_008_footnote_layout_contract

Repair scope:

- Move `References` before final `Footnotes` in the target card without changing claims, citations, provenance, change history, or evidence content.
- Update card-generation, citation-formatting, and view-building skill contracts so future KB/card Markdown keeps `Footnotes` as the final top-level section.
- Rerun card validator target and `--all`, then rerun adoption/view worker.
