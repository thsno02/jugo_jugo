# v3 LLM Wiki Loop

状态：`active`

这是当前 loop capsule。它只负责 v3 实验和候选产物，不代表 promoted stable `llm_wiki`。

主要入口：

- `README.md`
- `LOOP_START_PROMPT.md`
- `RUNBOOK.md`
- `CLAUDE_CODE_HANDOFF.md`
- `CONTEXT_BOUNDARY.md`
- `SKILLS_AND_DEPENDENCIES.md`
- `SUBAGENT_RUNTIME_CONSTRAINTS.md`
- `loop_manifest.json`
- `loop_state.json`
- `CARD_CONTRACT_V3.md`
- `DRAFT_FIRST_PIPELINE_V3.md`
- `SIMILARITY_MECHANISM_V3.md`
- `PROVENANCE_CONTRACT_V3.md`
- `BRAIN_MAILBOX_PROTOCOL.md`
- `brains/`
- `queues/`
- `iterations/`
- `reports/`
- `outputs/llm_wiki/`

v3 当前不复制或修改 v2 capsule。v2 的候选 KB 可以作为 read-only comparison base，是否正式导入 v3 候选产物需要独立 decision。
