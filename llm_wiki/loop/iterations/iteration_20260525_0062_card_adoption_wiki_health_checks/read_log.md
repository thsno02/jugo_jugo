| path | reason | usage |
| --- | --- | --- |
| /Users/lw/.codex/skills/agent-loop-runner/SKILL.md | 环境要求循环类任务使用该技能 | 仅用于确认循环执行流程约束，不作为知识卡事实来源 |
| llm_wiki/loop/iterations/iteration_20260525_0062_card_adoption_wiki_health_checks/task.md | 当前任务包 | 确认允许输入、允许写入、采纳规则和成功门禁 |
| llm_wiki/loop/iterations/iteration_20260525_0060_card_drafting_wiki_health_checks/artifacts/draft_card.md | 任务允许输入 | 采纳知识卡正文，并将 `status` 从 `draft` 改为 `accepted` |
| llm_wiki/loop/iterations/iteration_20260525_0060_card_drafting_wiki_health_checks/artifacts/provenance.md | 任务允许输入 | 采纳出处论证，并轻量调整采纳后证据边界说明 |
| llm_wiki/loop/iterations/iteration_20260525_0061_card_audit_wiki_health_checks/artifacts/audit_report.md | 任务允许输入 | 确认 `audit_result: pass` |
| llm_wiki/kb/cards/llm-wiki-health-checks.md | 任务允许输入 | 仅用于目标卡片存在性和覆盖冲突检查 |
| llm_wiki/kb/provenance/llm-wiki-health-checks.md | 任务允许输入 | 仅用于目标出处文件存在性和覆盖冲突检查 |
| llm_wiki/kb/indexes/cards.md | 任务允许输入 | 保留既有最小索引内容并增量追加本卡 |
| llm_wiki/loop/iterations/iteration_20260525_0062_card_adoption_wiki_health_checks/loop_status.md | 本轮允许写入 | 自检 `LOOP_DONE` 状态是否落盘 |
| llm_wiki/loop/iterations/iteration_20260525_0062_card_adoption_wiki_health_checks/loop_delivery.md | 本轮允许写入 | 自检交付文件是否包含 `LOOP_DONE` 与门禁结果 |
| llm_wiki/loop/iterations/iteration_20260525_0062_card_adoption_wiki_health_checks/read_log.md | 本轮允许写入 | 自检读日志文件存在 |
