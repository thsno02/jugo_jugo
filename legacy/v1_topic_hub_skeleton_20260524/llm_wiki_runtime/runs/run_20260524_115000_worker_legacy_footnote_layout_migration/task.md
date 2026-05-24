# Task

run_id:: run_20260524_115000_worker_legacy_footnote_layout_migration
executor_role:: worker_executor
worker_role:: legacy adopted-card footnote layout migration worker
task_packet:: user_dispatch_2026-05-24_legacy_adopted_card_footnote_layout_migration
status:: completed

## Scope

Migrate already adopted legacy card/view Markdown files to the current footnote layout contract:

- `## References` must appear before `## Footnotes`.
- `## Footnotes` must be the final top-level section.

## Allowed Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-citation-formatting/SKILL.md`
- `.llmwiki/skills/llmwiki-view-building/SKILL.md`
- `.llmwiki/skills/llmwiki-adoption-audit/SKILL.md`
- `.llmwiki/runs/run_20260524_113000_worker_repair_footnote_layout_contract/legacy_layout_audit.md`
- `.llmwiki/runs/run_20260524_114000_worker_adoption_view_risks_governance_provenance_after_footnote_repair/loop_delivery.md`
- Adopted selected-version `card.md` files.
- Adopted `kb/*.md` view cards.

## Allowed Outputs

- Adopted selected-version `card.md` files, section order only.
- Adopted `kb/*.md` view cards, section order only.
- Mechanical view/index/citation/backlink/impact/status refresh outputs.
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/action_queue.yaml`
- This run directory.

## Forbidden Changes

- No provenance, change, node metadata, source evidence, skill, protocol, archive, or data source content changes.
- No claim, citation text, footnote id, reference entry, evidence summary, or node metadata changes.
