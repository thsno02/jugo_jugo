path: ~/.codex/skills/agent-loop-runner/SKILL.md
reason: 开发者指令要求在循环任务中使用对应技能；用于确认循环状态和交付约束。
use: 仅读取最小必要流程约束，不作为知识卡事实证据。

path: llm_wiki/loop/iterations/iteration_20260525_0042_card_audit_human_llm_roles/task.md
reason: 当前任务包；确认允许输入、允许写入、审计问题和交付格式。
use: 作为本次执行范围和门禁依据。

path: llm_wiki/loop/iterations/iteration_20260525_0041_card_drafting_human_llm_roles/artifacts/draft_card.md
reason: 任务指定的待审计知识卡。
use: 审计 statement、fact_type、scope、support、References、Footnotes 和正文结构。

path: llm_wiki/loop/iterations/iteration_20260525_0041_card_drafting_human_llm_roles/artifacts/provenance.md
reason: 任务指定的出处论证。
use: 判断草稿卡暂时成立的论证是否充分。

path: data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt
reason: 任务指定的来源证据。
use: 只读取并使用 allowed_source_lines 15-16、68-69 作为事实证据。

path: llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md
reason: 任务指定的候选事实文件。
use: 只读取并使用 candidate 5 作为候选事实背景。
