# First Production Pass Task

Run from repository root:

```bash
claude --permission-mode auto -p "$(cat loops/v3_llm_wiki_loop_20260525/LOOP_START_PROMPT.md)" --output-format text
```

This is a formal v3 production pass, not a demo or smoke test.

The runner must follow `LOOP_START_PROMPT.md`, respect `CONTEXT_BOUNDARY.md`, and keep all new artifacts under `loops/v3_llm_wiki_loop_20260525/`.

Do not write root-level files. Do not write `data/`, `docs/`, `scripts/`, `user-insights/`, or v0/v1/v2 loop files.
