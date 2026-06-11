# read_log

## 启动记录

- 路径: `.`
  - 原因: 确认当前工作目录与任务包路径一致。
  - 用途: 启动前定位允许写入目录。
- 路径: `llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague/loop_status.md`
  - 原因: 确认启动状态文件是否已存在。
  - 用途: 决定创建最小状态文件。
- 路径: `llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague/read_log.md`
  - 原因: 确认读日志是否已存在。
  - 用途: 决定创建空读日志。
- 路径: `llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague/artifacts`
  - 原因: 确认允许写入的 artifacts 目录是否存在。
  - 用途: 后续写入草稿卡和出处论证。

## 额外流程说明读取

- 路径: `~/.codex/skills/agent-loop-runner/SKILL.md`
  - 原因: 当前任务明确属于 loop 执行任务，运行环境要求使用匹配技能。
  - 用途: 仅用于流程约束，不作为事实来源或候选证据。

## 任务与证据读取

- 路径: `llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague/task.md`
  - 原因: 当前任务包是唯一任务来源。
  - 用途: 确认候选、允许输入、允许写入、知识卡要求和完成门禁。
- 路径: `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md`
  - 范围: 仅 `## 候选 6` 块。
  - 原因: 任务允许用指定候选块核对候选字段。
  - 用途: 核对 `statement`、`fact_type`、`support`、`scope` 和来源字段。
  - 边界说明: 精确块读取未暴露相邻候选；候选块中的作者归属语未作为事实证据使用。
- 路径: `data/raw/webpage/karpathy-x-launch-post/raw.json`
  - 范围: 仅 JSON pointer `$.tweet.text`。
  - 原因: 任务指定的唯一来源证据。
  - 用途: 支撑知识卡和出处论证中的事实表述。

## 边界检查

- 未读取 `legacy/`。
- 未读取旧审计报告。
- 未读取其它主题页、枢纽页、已采纳 KB 卡片或 provenance。
- 未使用 `data/raw/webpage/karpathy-x-launch-post/raw.json` 中 `$.tweet.text` 之外的字段。

## 交付校验读取

- 路径: `llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague/loop_status.md`
  - 原因: 校验必需状态文件存在。
  - 用途: 完成门禁检查。
- 路径: `llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague/loop_delivery.md`
  - 原因: 校验交付文件存在并包含 `LOOP_DONE`。
  - 用途: 完成门禁检查。
- 路径: `llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague/read_log.md`
  - 原因: 校验读日志存在。
  - 用途: 完成门禁检查。
- 路径: `llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague/artifacts/draft_card.md`
  - 原因: 校验知识卡必需字段和 section 顺序。
  - 用途: 确认包含 `statement`、`fact_type`、`support`、`scope`、`status: draft`，且 `References` 位于 `Footnotes` 前。
- 路径: `llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague/artifacts/provenance.md`
  - 原因: 校验出处论证文件存在。
  - 用途: 完成门禁检查。
