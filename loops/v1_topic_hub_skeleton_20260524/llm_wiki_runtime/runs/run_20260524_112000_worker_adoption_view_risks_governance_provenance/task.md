# Task

run_id:: run_20260524_112000_worker_adoption_view_risks_governance_provenance
executor_role:: worker_executor
worker_role:: cand_008_risks_governance_provenance adoption/view builder
task_packet:: user_dispatch_2026-05-24_cand_008_adoption_view
target_candidate:: cand_008_risks_governance_provenance
target_node_id:: 20260524_104000_llm_wiki_risks_governance_and_provenance
target_version:: 1.0

## Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-view-building/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/skills/llmwiki-adoption-audit/SKILL.md`
- `.llmwiki/runs/run_20260524_110000_worker_generation_risks_governance_provenance/loop_delivery.md`
- `.llmwiki/runs/run_20260524_111000_worker_audit_risks_governance_provenance/loop_delivery.md`
- `.llmwiki/runs/run_20260524_111000_worker_audit_risks_governance_provenance/audit_report.md`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/node.yaml`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/provenance.md`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/change.md`

## Added Gate

footnote_layout_gate:: required

All KB/card Markdown must have `Footnotes` as the final top-level section. `References` must appear before `Footnotes`.

## Required Action

Adopt only if the audit decision is adopt-recommended and the footnote layout gate passes. If the footnote layout gate fails, do not adopt and do not modify forbidden bundle files.
