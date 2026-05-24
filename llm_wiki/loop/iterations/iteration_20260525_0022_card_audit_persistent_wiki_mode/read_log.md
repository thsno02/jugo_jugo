- path: /Users/lw/.codex/skills/agent-loop-runner/SKILL.md
  reason: 环境技能触发要求；确认循环执行产物写回约束。
  use: 仅用于执行流程约束，不作为知识卡审计事实来源。
- path: llm_wiki/loop/iterations/iteration_20260525_0022_card_audit_persistent_wiki_mode/task.md
  reason: 当前任务包。
  use: 获取审计对象、允许输入、允许写入、审计问题和交付格式。
- path: llm_wiki/loop/iterations/iteration_20260525_0021_card_drafting_persistent_wiki_mode/artifacts/draft_card.md
  reason: task.md 指定的 draft_card_path。
  use: 审计候选 3 知识卡内容、字段、正文结构、References 和 Footnotes。
- path: llm_wiki/loop/iterations/iteration_20260525_0021_card_drafting_persistent_wiki_mode/artifacts/provenance.md
  reason: task.md 指定的 provenance_path。
  use: 核对出处论证是否支撑候选 3 暂时成立。
- path: data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:11-13
  reason: task.md 指定的 source_evidence。
  use: 核对 statement 与 support 是否被原始来源证据支撑。
