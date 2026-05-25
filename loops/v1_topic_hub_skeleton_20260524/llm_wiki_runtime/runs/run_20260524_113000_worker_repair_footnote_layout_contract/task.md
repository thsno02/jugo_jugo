# Task

run_id:: run_20260524_113000_worker_repair_footnote_layout_contract
executor_role:: worker_executor
worker_role:: cand_008_risks_governance_provenance footnote layout repair + skill contract update worker
task_packet:: user_dispatch_2026-05-24_cand_008_footnote_layout_contract_repair
status:: completed

## Objective

Repair the candidate card Markdown section order so `## References` appears before `## Footnotes`, with `## Footnotes` as the final top-level section.

## Allowed Writes Used

- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`
- `.llmwiki/skills/llmwiki-card-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-citation-formatting/SKILL.md`
- `.llmwiki/skills/llmwiki-view-building/SKILL.md`
- `.llmwiki/skills/llmwiki-adoption-audit/SKILL.md`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/runs/run_20260524_113000_worker_repair_footnote_layout_contract/`

## Forbidden Writes Avoided

No root `node.yaml`, selected-version `node.yaml` metadata, `kb/`, `generated/`, `provenance.md`, `change.md`, source data, archive/protocol originals, or other card bodies were modified.

