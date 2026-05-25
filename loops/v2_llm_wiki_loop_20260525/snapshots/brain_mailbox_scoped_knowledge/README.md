# Legacy snapshot: v2 brain-mailbox scoped-knowledge loop

- `archived_at`: `2026-05-25T16:10:00+08:00`
- `snapshot_source_commit`: `9c10bfa`
- `snapshot_source`: active V2 loop control plane after `Adopt loop design v2`
- `status`: historical reference only

This directory freezes the V2 loop design before the next control-plane change.
It is a snapshot of the active design surface, not a live recovery entry.

## What V2 Assumed

- The primary object is `scoped_knowledge_card`.
- A card must contain knowledge, not only a title restatement.
- Cards use fixed metadata from `CARD_CONTRACT_V2.md`.
- The body remains free-form, with separate `References` and `Footnotes`.
- Similarity is a lightweight title-index mechanism: Jieba tokens, Jaccard set
  similarity, top 3 accepted cards, then comparison provenance.
- Brain lanes communicate through filesystem mailbox files:
  `production`, `similarity`, `audit`, and `ops`.
- Fusion and provenance-delta actions require audit before accepted A card
  provenance can be linked or changed.

## Snapshot Contents

- `root/`: active root docs, `loop_manifest.json`, and `loop_state.json`.
- `system_prompts/`: V2 stable role prompts.
- `task_templates/`: V2 task packet templates.
- `queues/`: active queue snapshots.
- `plans/`: long-horizon and next-session recovery prompts.
- `reports/`: active loop report snapshot.
- `decisions/`: the V2 adoption decision.
- `brains/`: mailbox state, protocol README, and smoke test evidence.
- `hooks/`, `tools/`, `logs/`: brain mailbox hook, control tool, and log snapshots.

Do not default to this directory for current work. Active agents should recover
from the live `llm_wiki/loop/README.md`, `LOOP_DESIGN_V2.md`,
`CARD_CONTRACT_V2.md`, `brains/README.md`, `loop_manifest.json`, and
`loop_state.json`.
