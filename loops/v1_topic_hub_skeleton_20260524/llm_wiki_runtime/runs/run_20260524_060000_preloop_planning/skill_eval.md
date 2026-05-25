# Skill Eval: Pre-Loop Planning

run_id:: run_20260524_060000_preloop_planning
status:: planning_eval

## What improved

The loop is now explicitly mining-first. Static topic backlog and Turing planner handoff no longer authorize card generation by themselves.

## Failure mode prevented

failure_mode:: direct_card_generation_from_guideline

The previous deviation came from treating a plan/protocol as executable topic content. The new plan inserts source mining and frontier management before node planning.

## Skills initialized

- `llmwiki-source-mining`
- `llmwiki-frontier-management`
- `llmwiki-node-planning`
- `llmwiki-card-generation`
- `llmwiki-citation-formatting`
- `llmwiki-provenance-generation`
- `llmwiki-change-generation`
- `llmwiki-node-metadata`
- `llmwiki-citation-audit`
- `llmwiki-adoption-audit`
- `llmwiki-dynamic-retrieval`
- `llmwiki-view-building`
- `llmwiki-impact-analysis`
- `llmwiki-skill-evolution`

## Patch decision

patch_required:: false

These are first drafts. Future patching should happen after concrete run failures, high-risk gaps, or hard contract breaks.

## Independent audit patch

patch_required:: true

Newton audit found one high-risk contract gap: no hard orchestration/planner gate. Added `llmwiki-loop-orchestration` and `.llmwiki/control/orchestration_gates.yaml`, and patched planner protocol so generator task packets require a frontier-backed `ready_to_build` candidate.
