# Context Boundary V3

This file is the access-control contract for agents running v3 without chat context.

## Principle

Use the smallest useful context. V3 should not inherit v2's process drift by reading v2 execution history. V2 candidate cards may be used only as accepted-card comparison material.

## Write Allowlist

Default write allowlist:

- `loops/v3_llm_wiki_loop_20260525/**`

Default write denylist:

- `README.md`
- `loops/README.md`
- `loops/registry.json`
- `loops/current_loop.json`
- `loops/v0_meta_kb_initialization_demo_20260524/**`
- `loops/v1_topic_hub_skeleton_20260524/**`
- `loops/v2_llm_wiki_loop_20260525/**`
- `data/**`
- `docs/**`
- `scripts/**`
- `user-insights/**`

Registry exception:

- `loops/registry.json` and `loops/current_loop.json` may be edited only when the human explicitly asks for repository-level loop state changes.

## Orientation Read Allowlist

Read only:

- `loops/v3_llm_wiki_loop_20260525/CLAUDE_CODE_HANDOFF.md`
- `loops/v3_llm_wiki_loop_20260525/README.md`
- `loops/v3_llm_wiki_loop_20260525/RUNBOOK.md`
- `loops/v3_llm_wiki_loop_20260525/loop_manifest.json`
- `loops/v3_llm_wiki_loop_20260525/loop_state.json`
- `loops/v3_llm_wiki_loop_20260525/CARD_CONTRACT_V3.md`
- `loops/v3_llm_wiki_loop_20260525/DRAFT_FIRST_PIPELINE_V3.md`
- `loops/v3_llm_wiki_loop_20260525/SIMILARITY_MECHANISM_V3.md`
- `loops/v3_llm_wiki_loop_20260525/PROVENANCE_CONTRACT_V3.md`
- `loops/v3_llm_wiki_loop_20260525/BRAIN_MAILBOX_PROTOCOL.md`
- `loops/v3_llm_wiki_loop_20260525/SKILLS_AND_DEPENDENCIES.md`
- `loops/v3_llm_wiki_loop_20260525/SUBAGENT_RUNTIME_CONSTRAINTS.md`
- `loops/v3_llm_wiki_loop_20260525/queues/**`
- `loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`

## material_to_draft Read Allowlist

Allowed:

- v3 loop files;
- the current material queue entry;
- `data/manifests/sources.jsonl`;
- `data/manifests/seed_sources.json`;
- `data/manifests/source_digests.jsonl`;
- `data/manifests/source_digests_index.md`;
- only `data/raw/...` paths named by the current material task;
- `data/logs/source_access_log.jsonl` when needed to verify source access status.

Forbidden in this phase:

- v2 card bodies;
- v2 provenance;
- v2 iterations, audits, reports, reflections, brain state, logs, and snapshots;
- all unrelated raw materials.

## similarity_top3 Read Allowlist

Allowed:

- v3 draft cards that need similarity;
- `outputs/llm_wiki/kb/indexes/cards.md`;
- `loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/indexes/cards.md`.

Forbidden in this phase:

- accepted card bodies;
- accepted provenance files;
- v2 process/history files.

## comparison_provenance Read Allowlist

Allowed:

- the draft card under comparison;
- its draft provenance;
- its similarity result;
- only the top 3 existing card bodies named by the similarity result;
- only the provenance files for those top 3 cards when needed.

Forbidden:

- browsing the whole KB;
- reading v2 process/history files to infer intent.

## audit Read Allowlist

Allowed:

- the audit queue item;
- the draft, comparison provenance, and proposed adoption delta;
- only the accepted card/provenance files targeted by the audit;
- relevant v3 contracts.

Forbidden:

- expanding audit into broad historical review unless the audit task explicitly asks for process audit.

## Required Access Log

If an agent reads outside the current phase allowlist, append one JSONL row to `source_access_log.jsonl`:

```json
{"time":"2026-05-25T21:03:26+08:00","event":"out_of_scope_read","path":"path/read","reason":"why this was necessary","use":"how it affected the task"}
```

Repeated unlogged out-of-scope reads should be treated as context contamination.
