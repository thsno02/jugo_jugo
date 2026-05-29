# Claude Code Handoff: V3 LLM Wiki Loop

You are starting with no chat context. Do not rely on any prior conversation. The source of truth is this loop capsule.

## Start Here

If the goal is to launch the first formal production pass, use `LOOP_START_PROMPT.md` as the top-level prompt.

Read these files first, in order:

1. `README.md`
2. `loop_state.json`
3. `loop_manifest.json`
4. `CONTEXT_BOUNDARY.md`
5. `SKILLS_AND_DEPENDENCIES.md`
6. `SUBAGENT_RUNTIME_CONSTRAINTS.md`
7. `RUNBOOK.md`
8. `CARD_CONTRACT_V3.md`
9. `DRAFT_FIRST_PIPELINE_V3.md`
10. `SIMILARITY_MECHANISM_V3.md`
11. `PROVENANCE_CONTRACT_V3.md`
12. `BRAIN_MAILBOX_PROTOCOL.md`

After that, inspect only the queue needed for the current phase.

## Skill Assumption

Assume no Codex skills are installed. Do not rely on hidden skills, prior agent memory, or external prompt packs.

Use `SKILLS_AND_DEPENDENCIES.md` as the local skill initialization document. The v3 capsule itself defines the required roles, contracts, and task boundaries.

## Subagent Assumption

Do not assume native nested Agent spawning. Current Claude Code documentation says standard subagents cannot spawn other subagents through the Agent tool.

V3 can use two runtime layers only through process-level nesting:

```text
top-level Claude
-> Agent tool subagent
   -> Bash: claude --permission-mode auto -p "<self-contained prompt>" --output-format text
```

The inner `claude -p` process is an independent headless session. It does not inherit conversation context, memory, or already-read files. Its prompt must include all necessary instructions and boundaries.

Always launch the inner process with an initial prompt. For v3 process-level nested tasks, use `--permission-mode auto`; otherwise the headless inner process may block on permissions. Auto mode avoids permission prompts while retaining action-level safety classification. The prompt must explicitly restate allowed read paths, allowed write paths, exact task, required artifacts, and final marker.

V3 still treats brain roles and mailboxes under `brains/` as durable coordination state. Runtime workers must write their outputs back to files.

If `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is enabled, agent teams may be used for production/similarity/audit/ops teammates. See `SUBAGENT_RUNTIME_CONSTRAINTS.md`.

## What V3 Is Testing

V3 tests a faster, auditable production flow:

```text
material
-> knowledge-dense draft card
-> title similarity top 3
-> comparison provenance
-> decision
-> publication gate or fusion audit
-> candidate KB adoption
```

The key change is that material becomes draft cards before expensive fusion reasoning. Similarity is only a cheap candidate retrieval step.

## Non-Negotiable Rules

- A card is knowledge, not a title restatement.
- Production must create scoped, useful draft cards from material without reading the whole KB.
- Similarity uses title tokenization and Jaccard set similarity, top 3 only.
- Similarity does not decide truth, duplication, fusion, or publication.
- For any meaningful draft/A-card decision, write comparison provenance answering:
  1. Why does the draft appear to share something with A?
  2. Where is the draft different from A?
  3. What is the core basis for the next action?
- `merge_candidate` and `provenance_delta` require audit before adoption.
- If fusion or provenance delta passes audit, link the comparison provenance from the accepted card provenance.
- Do not leave decisions only in chat or terminal output.

## Access Boundary

Default write scope:

- `loops/v3_llm_wiki_loop_20260525/**`

Default deny writes:

- root README;
- `loops/registry.json`;
- `loops/current_loop.json`;
- all v0/v1/v2 loop files;
- `data/**`;
- `docs/**`;
- `scripts/**`;
- `user-insights/**`.

Exception: update registry/current only if the human explicitly requests repository-level loop state changes.

Read scope is phase-specific. See `CONTEXT_BOUNDARY.md`. If a file is not allowed for the current phase, do not read it unless the current task explicitly requires it, and log the read in `source_access_log.jsonl`.

## Next Action

Current state: bootstrap complete, no material queued.

Next action:

1. Run the dependency preflight from `SKILLS_AND_DEPENDENCIES.md`.
2. Add the first material unit to `queues/material_queue.md`.
3. Run `material_to_draft` on that material only.
4. Produce draft cards under `outputs/llm_wiki/drafts/cards/`.
5. Produce draft provenance under `outputs/llm_wiki/drafts/provenance/`.
6. Update `loop_state.json`, `queues/draft_backlog.md`, and `reports/loop_report.md`.

Do not adopt cards into `outputs/llm_wiki/kb/cards/` in the first production step unless a publication gate task explicitly asks for it.

## Completion Marker

When finishing a task, update the relevant status files and end your final message with one of:

- `LOOP_DONE`
- `LOOP_BLOCKED`
- `LOOP_NEEDS_HUMAN`
