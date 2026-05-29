# Subagent Runtime Constraints V3

This file records the runtime check for Claude Code orchestration.

## Current Finding

Local Claude Code version checked:

```text
2.1.128 (Claude Code)
```

Official Claude Code documentation says:

- standard subagents can be configured with tool access;
- an agent running as the main thread with `claude --agent` can spawn subagents through the Agent tool;
- subagents cannot spawn other subagents;
- if nested delegation is needed, use skills or chain subagents from the main conversation;
- agent teams are experimental, disabled by default, require `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, and require Claude Code v2.1.32 or later.

Sources:

- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/agent-teams

## Verified Process-Level Nesting

Local feasibility result reported on 2026-05-25:

- Claude CLI path: `/opt/homebrew/bin/claude`
- Pattern: top-level Claude -> Agent tool subagent -> Bash command invoking `claude --permission-mode auto -p "..." --output-format text`
- Result marker: `NESTED_CLAUDE_OK_9X2Y4Z`
- Working directory inherited as `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo`
- Exit code: 0

This means v3 can use two runtime layers if the second layer is treated as an independent headless Claude process launched by Bash, not as a standard nested Claude Code subagent spawned by the Agent tool.

Viable shape:

```text
top-level Claude
-> Agent tool subagent
   -> Bash: claude --permission-mode auto -p "<self-contained prompt>" --output-format text
```

Important constraints:

- the inner `claude -p` session does not inherit current conversation context, memory, or already-read files;
- the inner prompt must include all necessary instructions, file paths, boundaries, and output schema;
- headless mode is best for one-shot tasks;
- use `--resume <session-id>` or `-c` only when an explicit continued inner session is needed;
- start the inner process with an initial prompt via `-p`; do not start an empty inner session;
- use `--permission-mode auto` for v3 process-level nested tasks; it avoids permission prompts while preserving automatic action-level safety classification;
- `--permission-mode auto` requires Claude Code v2.1.83 or later; local version 2.1.128 satisfies this requirement;
- do not use `bypassPermissions` / `--dangerously-skip-permissions` as the v3 default because it skips permission prompts without safety checks;
- the prompt must restate v3 read/write boundaries because the worker is headless and non-interactive;
- token cost is additive: outer subagent tokens plus inner Claude process tokens.

## Implication For V3

Do not implement v3 as native nested Agent spawning:

```text
main agent
-> brain subagent
   -> worker subagent
```

That native nested Agent shape is not supported by standard Claude Code subagents.

V3 may be implemented as either:

```text
Claude Code lead/main session
-> one-layer runtime subagents or teammates
-> filesystem brain mailboxes and queues
```

or, for tasks that genuinely need a second runtime layer:

```text
Claude Code lead/main session
-> brain subagent
   -> independent headless Claude process launched through Bash
```

The two layers in v3 are conceptual:

1. `brains/*` store role-local state, mailbox messages, and queues.
2. Concrete tasks produce draft cards, similarity results, comparison provenance, audits, and adoption artifacts.

The lead/main session is the only default runtime entity that spawns actual subagents.

## Default Mode

Use this unless the human explicitly enables agent teams:

- one Claude Code lead/main session;
- optional one-layer named subagents invoked by the lead;
- production, similarity, audit, and ops are role contracts backed by files;
- a brain that needs help writes a queue/mailbox request;
- the lead reads the request and spawns the appropriate one-layer worker if needed.

## Process-Level Nested Mode

Use this only when the outer subagent has a bounded task that can be delegated to a fully self-contained inner prompt:

```bash
claude --permission-mode auto -p "<self-contained task prompt>" --output-format text
```

The inner prompt must include:

- repo root;
- current loop path;
- allowed read paths;
- allowed write paths;
- exact task;
- required output files;
- final marker such as `LOOP_DONE`, `LOOP_BLOCKED`, or `LOOP_NEEDS_HUMAN`;
- instruction to update files, not just return chat text, when artifacts are required.

For reproducibility, copy `task_templates/process_level_nested_prompt_template.md` to a task-specific prompt file, fill every placeholder, then invoke it as command substitution:

```bash
claude --permission-mode auto -p "$(cat loops/v3_llm_wiki_loop_20260525/task_templates/current_inner_prompt.md)" --output-format text
```

Because this mode is non-interactive, never use a vague prompt. The prompt must name exact allowed write paths and must forbid edits outside `loops/v3_llm_wiki_loop_20260525/**` unless the human explicitly requests registry-level changes.

`bypassPermissions` / `--dangerously-skip-permissions` is reserved for explicitly approved throwaway sandboxes. It is not the v3 default.

## Agent Teams Mode

Agent teams may be used if all are true:

- `claude --version` is at least 2.1.32;
- `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is enabled;
- the user intentionally wants teammate communication and accepts higher token cost.

Recommended team shape:

- lead: loop controller;
- teammate `production`: material_to_draft;
- teammate `similarity`: title_similarity_top3;
- teammate `audit`: fusion/provenance audit;
- teammate `ops`: queues, reports, and consistency.

Even in agent teams mode:

- teammates must follow `CONTEXT_BOUNDARY.md`;
- teammates should use v3 mailbox files for durable state;
- teammates must not assume they can spawn nested subagents;
- task ownership should avoid editing the same file concurrently.

## Unsupported Mode

Do not ask a brain subagent to spawn sub-subagents.

Do not make v3 correctness depend on `Agent` being available inside a subagent definition.

Do not rely on agent teams unless the environment variable is enabled and the session actually starts a team.

Do not treat process-level nesting as context inheritance. It is a fresh session and must be prompted like a new worker.
