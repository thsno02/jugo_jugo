# read_log

| path | reason | use |
| --- | --- | --- |
| `/Users/lw/.codex/skills/agent-loop-runner/SKILL.md` | 系统技能规则要求读取循环执行说明 | 仅用于对齐循环交付格式，不作为知识卡事实来源 |
| `llm_wiki/loop/iterations/iteration_20260525_0056_card_adoption_idea_file_agent_builds/task.md` | 当前任务包 | 确认允许输入、允许写入、采纳规则和成功门禁 |
| `llm_wiki/loop/iterations/iteration_20260525_0054_card_drafting_idea_file_agent_builds_r1/artifacts/draft_card.md` | 允许输入：草稿知识卡 | 采纳为目标知识卡，并将 `status` 从 `draft` 改为 `accepted` |
| `llm_wiki/loop/iterations/iteration_20260525_0054_card_drafting_idea_file_agent_builds_r1/artifacts/provenance.md` | 允许输入：出处论证 | 采纳为目标出处论证，并做互链与状态语句轻量整理 |
| `llm_wiki/loop/iterations/iteration_20260525_0055_card_audit_idea_file_agent_builds_r1/artifacts/audit_report.md` | 允许输入：审计报告 | 确认 `audit_result: pass` 和无 required changes |
| `llm_wiki/kb/cards/idea-file-share-the-idea.md` | 允许输入：目标卡片路径 | 采纳前仅检查存在性与覆盖冲突，结果为不存在；采纳后验证 `accepted`、互链和 `Footnotes` 位置 |
| `llm_wiki/kb/provenance/idea-file-share-the-idea.md` | 允许输入：目标出处路径 | 采纳前仅检查存在性与覆盖冲突，结果为不存在；采纳后验证知识卡互链 |
| `llm_wiki/kb/indexes/cards.md` | 允许输入：最小索引 | 保留既有索引内容并增量追加本卡条目，采纳后验证索引行 |
| `llm_wiki/loop/iterations/iteration_20260525_0056_card_adoption_idea_file_agent_builds/loop_status.md` | 允许写入：循环状态 | 写入与存在性检查 |
| `llm_wiki/loop/iterations/iteration_20260525_0056_card_adoption_idea_file_agent_builds/loop_delivery.md` | 允许写入：循环交付 | 写入与存在性检查 |
| `llm_wiki/loop/iterations/iteration_20260525_0056_card_adoption_idea_file_agent_builds/read_log.md` | 允许写入：读取记录 | 写入与存在性检查 |
