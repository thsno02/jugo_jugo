# Iteration 20260525 0001 First Production Pass

## Focus

Run the first formal v3 production pass through the draft-first pipeline.

## Frozen Variables

- Use v3 context boundaries.
- Use `claude --permission-mode auto -p` for top-level and process-level nested Claude execution.
- Produce draft artifacts and similarity results only.
- Do not adopt public KB cards in this iteration.
- Do not run fusion or provenance-delta adoption in this iteration.

## Expected Artifacts

- updated `queues/material_queue.md`;
- draft cards under `outputs/llm_wiki/drafts/cards/`;
- draft provenance under `outputs/llm_wiki/drafts/provenance/`;
- similarity JSON under `outputs/llm_wiki/drafts/similarity/`;
- updated `queues/draft_backlog.md`;
- updated `loop_state.json`, `status.json`, and `reports/loop_report.md`.
