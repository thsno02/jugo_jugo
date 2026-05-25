# Loop Delivery

run_id:: run_20260524_112000_worker_adoption_view_risks_governance_provenance
executor_role:: worker_executor
worker_role:: cand_008_risks_governance_provenance adoption/view builder
task_packet:: user_dispatch_2026-05-24_cand_008_adoption_view
status:: LOOP_BLOCKED
decision:: adoption_blocked
next_action:: dispatch_repair_worker_for_cand_008_footnote_layout_contract

## Gate Summary

- audit decision input: `adopt_recommended`
- card validator: pass
- root metadata gate before adoption: pass
- footnote_layout_gate: fail

## Blocker

The target card does not satisfy the added Markdown section layout contract.

Observed order in `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`:

- line 25: `## Footnotes`
- line 155: `## References`

Required order:

- `## References` before `## Footnotes`
- `## Footnotes` as the final top-level section

## Touched Files

- `.llmwiki/runs/run_20260524_112000_worker_adoption_view_risks_governance_provenance/task.md`
- `.llmwiki/runs/run_20260524_112000_worker_adoption_view_risks_governance_provenance/adoption_trace.md`
- `.llmwiki/runs/run_20260524_112000_worker_adoption_view_risks_governance_provenance/view_build_trace.md`
- `.llmwiki/runs/run_20260524_112000_worker_adoption_view_risks_governance_provenance/validation_trace.md`
- `.llmwiki/runs/run_20260524_112000_worker_adoption_view_risks_governance_provenance/loop_status.md`
- `.llmwiki/runs/run_20260524_112000_worker_adoption_view_risks_governance_provenance/loop_delivery.md`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/action_queue.yaml`

## Exact Selected-Version Metadata Fields Changed

None. Adoption was blocked before selected-version metadata synchronization.

## Validation Summary

- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`: `card validation passed: 1 cards`
- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py --all`: `card validation passed: 11 cards`
- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_104000_llm_wiki_risks_governance_and_provenance`: expected pre-adoption failure, missing root `node.yaml`
- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py --all`: expected pre-adoption failure, missing target root `node.yaml`
- footnote_layout_gate: fail
- view/index/citation/backlinks/impact/status builds: not run because adoption was blocked before writes

Current retained counts from existing `generated/status.yaml`:

- adopted nodes count: 5
- citation edge count: 73
- open impact count: 0

## Minimal Repair Task

Dispatch a repair worker to adjust the target card section order so `References` appears before final `Footnotes`. The repair worker should also update card-generation, citation-formatting, and view-building skills with this footnote layout contract. After repair, rerun validators and adoption/view build.

LOOP_BLOCKED
