## 读取记录

- `llm_wiki/loop/iterations/iteration_20260525_0003_card_drafting_raw_sources_truth/task.md`
  - 原因：当前任务包，是本轮唯一任务来源。
  - 用途：确认候选、允许输入、允许写入和成功门禁。
- `~/.codex/skills/agent-loop-runner/SKILL.md`
  - 原因：系统可用技能要求在循环执行任务中使用该技能。
  - 用途：仅用于确认循环产物写回工作流，不作为知识卡事实来源。
- `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
  - 原因：任务允许作为候选核对输入。
  - 用途：仅核对 `候选 8` 的字段。
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
  - 原因：任务指定的来源证据文件。
  - 用途：仅读取并使用第 27-30 行支撑草稿卡。
