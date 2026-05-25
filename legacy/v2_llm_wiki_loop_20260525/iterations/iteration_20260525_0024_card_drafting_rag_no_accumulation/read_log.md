# read_log

- path: `/Users/lw/.codex/skills/agent-loop-runner/SKILL.md`
  - reason: 系统技能指令要求在 loop 任务中读取对应技能说明。
  - usage: 仅用于执行流程约束，不作为知识卡事实来源。
- path: `llm_wiki/loop/iterations/iteration_20260525_0024_card_drafting_rag_no_accumulation/task.md`
  - reason: 当前任务包。
  - usage: 确认任务目标、允许输入、允许写入和成功门禁。
- path: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
  - reason: 任务允许用来核对候选 2 字段。
  - usage: 仅核对候选 2 的 statement、fact_type、scope 和证据路径。
- path: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
  - reason: 任务指定的来源证据。
  - usage: 仅读取第 7-10 行，作为知识卡事实支撑。
