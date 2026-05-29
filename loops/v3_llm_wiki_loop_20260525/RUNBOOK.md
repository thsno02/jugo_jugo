# V3 Runbook

## Main-Agent Rule

The main agent owns state, task boundaries, and decisions. It should not silently become the production worker. If it creates cards directly during v3, it must record that as an explicit controlled exception.

## Claude Code Entry Rule

If Claude Code or any agent starts without chat context, first read `CLAUDE_CODE_HANDOFF.md`. Treat the files as the source of truth. Do not infer rules from prior conversation.

For starting the first formal production pass, use `LOOP_START_PROMPT.md` as the top-level prompt:

```bash
claude --permission-mode auto -p "$(cat loops/v3_llm_wiki_loop_20260525/LOOP_START_PROMPT.md)" --output-format text
```

Assume no Codex skills are installed. Run the preflight in `SKILLS_AND_DEPENDENCIES.md` before production or similarity work.

Assume no nested subagents. Read `SUBAGENT_RUNTIME_CONSTRAINTS.md` before spawning or asking Claude Code to spawn agents.

Follow the phase-specific read allowlist in `CONTEXT_BOUNDARY.md` and `loop_manifest.json`. Any read outside the current phase allowlist must be logged in `source_access_log.jsonl` with path, reason, and use.

## Operating Loop

1. Add a source or exhausted article to `queues/material_queue.md`.
2. Run `material_to_draft`: produce draft cards and draft provenance under `outputs/llm_wiki/drafts/`.
3. Run `similarity_top3`: compute title top 3 against the configured comparison base.
4. Write comparison provenance for any candidate that affects the decision.
5. Choose one action: `new_card`, `merge_candidate`, `provenance_delta`, `duplicate_skip`, or `revise_before_gate`.
6. For `new_card`, run a lightweight publication gate and adopt only if the card has enough knowledge content and source support.
7. For `merge_candidate` or `provenance_delta`, send to audit before linking anything into an accepted card provenance.
8. Update `loop_state.json`, queues, and `reports/loop_report.md`.

## Runtime Orchestration

Default mode:

- one Claude Code lead/main session;
- optional one-layer subagents spawned only by the lead/main session;
- brain mailboxes are files, not autonomous running agents.

Experimental mode:

- if `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is enabled and `claude --version` is at least 2.1.32, use an agent team with production, similarity, audit, and ops teammates;
- teammates may communicate through Claude Code team messaging and v3 mailbox files;
- teammates still must not assume they can spawn nested subagents.

## Context Hygiene

- Do not read v2 iterations, audits, reports, reflections, brains, logs, or snapshots for production context.
- Do not read v2 cards during `material_to_draft`.
- During `similarity_top3`, read only the accepted-card index, not card bodies.
- During `comparison_provenance`, read only the top 3 candidate cards and required provenance.
- Do not read `user-insights/` unless the human explicitly asks for personal-history recovery.
- Do not write outside `loops/v3_llm_wiki_loop_20260525/**` unless the human explicitly asks for registry or repository-level changes.

## Stop Conditions

Stop only when the loop has evidence for one of these conclusions:

- draft-first materially improves throughput without reducing card quality;
- title similarity top 3 catches enough likely overlaps to reduce full-KB reading;
- fusion audit remains recoverable through comparison provenance;
- the mechanism fails and should be redesigned before more production.

## Current Bootstrap Task

Before producing cards, confirm the first batch source and comparison base:

- default source queue: `queues/material_queue.md`;
- default comparison base: `loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/indexes/cards.md`;
- default candidate output: `outputs/llm_wiki/`.
- default start prompt: `LOOP_START_PROMPT.md`.
