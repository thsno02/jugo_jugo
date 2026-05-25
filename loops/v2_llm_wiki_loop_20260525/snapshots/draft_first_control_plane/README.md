# Legacy snapshot: v1 draft-first control plane

- `archived_at`: `2026-05-25T15:51:23+08:00`
- `snapshot_source`: committed `HEAD` before the V2 loop redesign in this session.
- `status`: historical reference only.

This directory freezes the V1 loop design so the active loop can move to a new
brain-mailbox and scoped-knowledge-card design without losing the old control
plane.

## What V1 Assumed

- Main-agent owned state transitions and delegated narrow workers.
- The primary object was an `atomic_fact_card`.
- Production moved from source mining to batch atomic drafts, then a coarse
  similarity gate, then audit and public adoption.
- Card metadata was deliberately minimal.
- Similarity was a gate concept, not yet a concrete title-token top-3 mechanism.

## Snapshot Contents

- `root/`: V1 root loop docs and state/manifest snapshot.
- `system_prompts/`: V1 prompts for drafting and similarity gate workers.
- `task_templates/`: V1 task templates for drafting and similarity gate workers.

Do not use this directory as a current recovery entry. Active agents should
start from `llm_wiki/loop/README.md`, `LOOP_DESIGN_V2.md`, and
`CARD_CONTRACT_V2.md`.
