path: ~/.codex/skills/agent-loop-runner/SKILL.md
reason: 环境要求循环类任务使用该技能；仅读取流程约束，不作为事实证据。
use: 确认循环产物写入与结束纪律。

path: llm_wiki/loop/iterations/iteration_20260525_0058_card_audit_idea_file_abstract_vague/task.md
reason: 当前任务包。
use: 确认审计目标、允许输入、允许写入、门禁和结论格式。

path: llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague/artifacts/draft_card.md
reason: 任务指定草稿知识卡。
use: 审计卡片正文、字段、引用顺序和结构。

path: llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague/artifacts/provenance.md
reason: 任务指定出处论证。
use: 检查草稿卡是否由出处论证暂时 justify。

path: data/raw/webpage/karpathy-x-launch-post/raw.json $.tweet.text
reason: 任务指定来源证据字段。
use: 只用 tweet.text 字段核对 statement 与 support。

path: llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md candidate 6
reason: 任务指定候选事实。
use: 只用 candidate 6 核对草稿事实来源链。
