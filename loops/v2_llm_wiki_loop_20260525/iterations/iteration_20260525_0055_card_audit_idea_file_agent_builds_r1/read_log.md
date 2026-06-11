path: ~/.codex/skills/agent-loop-runner/SKILL.md
reason: 开发者指令要求在匹配循环任务时使用该技能
usage: 仅读取执行流程约束，不作为知识卡事实证据

path: llm_wiki/loop/iterations/iteration_20260525_0055_card_audit_idea_file_agent_builds_r1/task.md
reason: 当前任务包
usage: 确认允许输入、允许写入、审计问题和交付格式

path: llm_wiki/loop/iterations/iteration_20260525_0054_card_drafting_idea_file_agent_builds_r1/artifacts/draft_card.md
reason: 任务包允许输入 draft_card_path
usage: 审计指定草稿知识卡

path: llm_wiki/loop/iterations/iteration_20260525_0054_card_drafting_idea_file_agent_builds_r1/artifacts/provenance.md
reason: 任务包允许输入 provenance_path
usage: 核对出处论证是否支撑草稿卡暂时成立

path: data/raw/webpage/karpathy-x-launch-post/raw.json
reason: 任务包允许输入 source_evidence_path
usage: 仅使用 $.tweet.text 作为来源证据

path: llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md
reason: 任务包允许输入 fact_candidate_path
usage: 仅使用 candidate 3 作为候选事实证据

path: llm_wiki/loop/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/artifacts/audit_report.md
reason: 任务包允许输入 prior_audit_report_path
usage: 核对上一轮 revise 问题是否关闭

path: llm_wiki/loop/iterations/iteration_20260525_0054_card_drafting_idea_file_agent_builds_r1/task.md
reason: 任务包允许输入 revision_task_path
usage: 核对修订任务约束与上一轮问题目标
