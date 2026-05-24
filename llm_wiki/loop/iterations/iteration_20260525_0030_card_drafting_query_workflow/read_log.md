# read_log

- path: `/Users/lw/.codex/skills/agent-loop-runner/SKILL.md`
  reason: 循环任务触发了可用技能说明读取要求。
  use: 只用于确认循环执行需把状态、交付和产物写回磁盘；没有作为事实来源。
- path: `llm_wiki/loop/iterations/iteration_20260525_0030_card_drafting_query_workflow/task.md`
  reason: 当前任务包。
  use: 确认任务目标、允许输入、允许写入、候选范围和成功门禁。
- path: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
  reason: 任务允许用于核对 `候选 12` 字段。
  use: 只截取并核对 `候选 12` 的 statement、fact_type、support、scope 和 source_evidence。
- path: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
  reason: 任务指定的来源证据。
  use: 只读取第 `39-40` 行，用作知识卡和出处论证的事实支撑。
