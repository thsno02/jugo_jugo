# Task

run_id:: run_20260524_114000_worker_adoption_view_risks_governance_provenance_after_footnote_repair
executor_role:: worker_executor
worker_role:: cand_008_risks_governance_provenance adoption/view builder after footnote repair
task_packet:: user_dispatch_2026-05-24_cand_008_adoption_view_after_footnote_repair
target_candidate:: cand_008_risks_governance_provenance
target_node_id:: 20260524_104000_llm_wiki_risks_governance_and_provenance
target_version:: 1.0

## Inputs Read

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-view-building/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/skills/llmwiki-adoption-audit/SKILL.md`
- prior generation, audit, blocked adoption, and footnote repair deliveries
- target version `node.yaml`, `card.md`, `provenance.md`, and `change.md`

## Allowed Outputs

- target root node metadata
- selected version adoption/status/selected/adopted-at/audit metadata only
- target KB view
- KB index and generated view artifacts
- control state/status/queue files
- this run directory

## Forbidden Outputs Observed

No rewrite was made to target `card.md`, `provenance.md`, `change.md`, evidence files, skills, protocol, archive, or other node/kb body content.
