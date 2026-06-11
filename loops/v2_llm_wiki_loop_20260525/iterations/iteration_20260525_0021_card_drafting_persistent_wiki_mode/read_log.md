# read_log

## 允许输入读取

- `llm_wiki/loop/iterations/iteration_20260525_0021_card_drafting_persistent_wiki_mode/task.md`
  - 用途：读取任务约束、允许输入、允许写入、成功门禁。
- `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
  - 用途：仅截取并核对候选 3 的字段。
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:11-13`
  - 用途：作为本卡唯一事实证据。

## 额外读取

- `~/.codex/skills/agent-loop-runner/SKILL.md`
  - 原因：当前执行环境要求在 loop/status/delivery 类任务中使用该 skill。
  - 用途：仅用于操作流程约束，不作为知识卡事实来源。
