# V3 Loop Start Prompt

You are the top-level runner for the v3 LLM Wiki loop.

Repo root:

`.`

Current loop path:

`loops/v3_llm_wiki_loop_20260525`

You are starting without prior chat context. Do not rely on memory, hidden skills, or previous conversation. The v3 files are the source of truth.

## Goal

Run the first formal v3 production pass through the draft-first pipeline:

```text
material
-> knowledge-dense draft cards
-> draft provenance
-> title similarity top 3
-> draft backlog update
-> loop report/state update
```

Do not adopt cards into `outputs/llm_wiki/kb/cards/` in this pass unless a separate publication gate task explicitly authorizes adoption. Do not perform fusion or provenance-delta adoption in this pass. This first production pass should produce recoverable draft artifacts and similarity results, then leave adoption decisions queued for the proper gate.

## Required Startup

1. `cd .`
2. Read, in this order:
   - `loops/v3_llm_wiki_loop_20260525/CLAUDE_CODE_HANDOFF.md`
   - `loops/v3_llm_wiki_loop_20260525/CONTEXT_BOUNDARY.md`
   - `loops/v3_llm_wiki_loop_20260525/SKILLS_AND_DEPENDENCIES.md`
   - `loops/v3_llm_wiki_loop_20260525/SUBAGENT_RUNTIME_CONSTRAINTS.md`
   - `loops/v3_llm_wiki_loop_20260525/RUNBOOK.md`
   - `loops/v3_llm_wiki_loop_20260525/CARD_CONTRACT_V3.md`
   - `loops/v3_llm_wiki_loop_20260525/DRAFT_FIRST_PIPELINE_V3.md`
   - `loops/v3_llm_wiki_loop_20260525/SIMILARITY_MECHANISM_V3.md`
   - `loops/v3_llm_wiki_loop_20260525/PROVENANCE_CONTRACT_V3.md`
   - `loops/v3_llm_wiki_loop_20260525/BRAIN_MAILBOX_PROTOCOL.md`
3. Run dependency preflight from `SKILLS_AND_DEPENDENCIES.md`.
4. If `jieba` is missing, run:

```bash
bash loops/v3_llm_wiki_loop_20260525/tools/bootstrap_dependencies.sh
```

If dependency installation fails, update status/report with the blocker and finish with `LOOP_BLOCKED`.

## Access Rules

Default write allowlist:

- `loops/v3_llm_wiki_loop_20260525/**`

Forbidden writes:

- root `README.md`
- `loops/README.md`
- `loops/registry.json`
- `loops/current_loop.json`
- all v0/v1/v2 loop files
- `data/**`
- `docs/**`
- `scripts/**`
- `user-insights/**`

Read access must follow `CONTEXT_BOUNDARY.md`.

For this first production pass, you may read:

- v3 loop files;
- `data/manifests/source_digests_index.md`;
- `data/manifests/source_digests.jsonl`;
- `data/manifests/sources.jsonl`;
- `data/manifests/seed_sources.json`;
- exactly one raw source path after you queue it in `queues/material_queue.md`;
- v2 accepted-card title index only for similarity:
  `loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/indexes/cards.md`.

Do not read v2 card bodies or v2 provenance in this production pass. Do not read v2 iterations, audits, reports, reflections, brain state, logs, or snapshots.

If you must read outside these rules, append an `out_of_scope_read` JSONL row to `loops/v3_llm_wiki_loop_20260525/source_access_log.jsonl` before using that information.

## First Material

Use this material unless it is missing or unreadable:

- `material_id`: `karpathy-x-launch-post`
- `digest_id`: `digest_karpathy-x-launch-post`
- `source_path`: `data/raw/webpage/karpathy-x-launch-post/text.txt`

If it is missing or unreadable, choose one complete source from `data/manifests/source_digests_index.md` that has a readable text path and covers `origin_and_canon`, `problem_and_motivation`, or `workflow_and_operations`. Record the chosen source in `queues/material_queue.md`.

## Required Work

1. Update `queues/material_queue.md` with the chosen material and set it to `drafting`.
2. Read only the chosen source text.
3. Produce 2-5 knowledge-dense draft cards under:
   - `loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/cards/`
4. Produce matching draft provenance under:
   - `loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/provenance/`
5. Each draft card must follow `CARD_CONTRACT_V3.md`.
6. Draft card bodies must contain actual knowledge, not title restatements.
7. Run title similarity top 3 for each draft against:
   - `loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/indexes/cards.md`
8. Write similarity JSON artifacts under:
   - `loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/similarity/`
9. Update:
   - `loops/v3_llm_wiki_loop_20260525/queues/draft_backlog.md`
   - `loops/v3_llm_wiki_loop_20260525/loop_state.json`
   - `loops/v3_llm_wiki_loop_20260525/status.json`
   - `loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`
   - relevant `brains/*` queue/state files if you use mailbox roles
10. Set the material queue item to `drafted` or `blocked`.

## Subagent Policy

You may run this first formal production pass in one top-level Claude session.

If you delegate to a process-level nested Claude worker, use only this command shape:

```bash
claude --permission-mode auto -p "$(cat loops/v3_llm_wiki_loop_20260525/task_templates/current_inner_prompt.md)" --output-format text
```

Before doing that, copy `task_templates/process_level_nested_prompt_template.md` to `task_templates/current_inner_prompt.md` and replace every placeholder. The inner prompt must include repo root, current loop path, allowed read paths, allowed write paths, exact task, required output files, and final marker.

Do not assume the inner Claude process inherits context.

## Quality Gate For This Production Pass

The run is successful if:

- at least one draft card exists;
- every draft card has matching draft provenance;
- every draft card has one similarity result artifact;
- `queues/draft_backlog.md` lists the draft cards and similarity artifacts;
- `loop_state.json`, `status.json`, and `reports/loop_report.md` reflect the run;
- no public KB adoption happened.

If no source can be read or dependencies cannot be initialized, preserve the blocker in status/report and finish with `LOOP_BLOCKED`.

## Final Response

Summarize:

- chosen material;
- draft cards created;
- similarity artifacts created;
- files updated;
- blockers or risks;
- next action.

End with exactly one marker:

- `LOOP_DONE`
- `LOOP_BLOCKED`
- `LOOP_NEEDS_HUMAN`
