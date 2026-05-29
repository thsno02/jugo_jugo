# Process-Level Nested Claude Prompt Template

Use this template when a subagent launches an inner Claude process.

Copy this file to `current_inner_prompt.md` or a task-specific prompt file, then replace every placeholder before execution.

Recommended command:

```bash
claude --permission-mode auto -p "$(cat loops/v3_llm_wiki_loop_20260525/task_templates/current_inner_prompt.md)" --output-format text
```

## Prompt

You are an inner headless Claude worker for v3.

Repo root:

`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo`

Current loop:

`loops/v3_llm_wiki_loop_20260525`

You have no inherited context. Read only the files named in this prompt and the current phase allowlist from `CONTEXT_BOUNDARY.md`.

Allowed write scope:

- `loops/v3_llm_wiki_loop_20260525/**`

Forbidden writes:

- root README;
- `loops/registry.json`;
- `loops/current_loop.json`;
- all v0/v1/v2 loop files;
- `data/**`;
- `docs/**`;
- `scripts/**`;
- `user-insights/**`.

Task:

`<replace with exact task>`

Required output files:

- `<replace with exact output path>`

Required final marker:

- `LOOP_DONE`, `LOOP_BLOCKED`, or `LOOP_NEEDS_HUMAN`
