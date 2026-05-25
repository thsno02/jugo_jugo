## 任务外读取

- `/Users/lw/.codex/skills/agent-loop-runner/SKILL.md`
  - 原因：本会话技能规则要求循环类任务使用 `agent-loop-runner` 技能。
  - 用途：仅确认执行流程约束；不作为知识卡审计事实证据。

## 任务允许读取

- `llm_wiki/loop/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/task.md`
  - 原因：当前任务包。
  - 用途：确认审计边界、允许输入、允许写入和交付格式。
- `llm_wiki/loop/iterations/iteration_20260525_0052_card_drafting_idea_file_agent_builds/artifacts/draft_card.md`
  - 原因：任务指定草稿知识卡。
  - 用途：审计 statement、fact_type、scope、support、正文结构、References 和 Footnotes。
- `llm_wiki/loop/iterations/iteration_20260525_0052_card_drafting_idea_file_agent_builds/artifacts/provenance.md`
  - 原因：任务指定出处论证。
  - 用途：检查论证是否能支撑草稿卡暂时成立。
- `data/raw/webpage/karpathy-x-launch-post/raw.json` 的 `$.tweet.text`
  - 原因：任务指定来源证据字段。
  - 用途：核对草稿卡核心事实是否由原始来源文字支撑。
- `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md` 中 candidate 3
  - 原因：任务指定允许候选。
  - 用途：核对草稿卡是否对应允许候选事实。
