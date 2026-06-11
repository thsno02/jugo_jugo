| path | reason | usage |
|---|---|---|
| ~/.codex/skills/agent-loop-runner/SKILL.md | 开发者技能规则要求在循环任务中使用该技能 | 仅用于确认循环执行产物写回和状态交付流程，不作为知识卡事实来源 |
| llm_wiki/loop/iterations/iteration_20260525_0026_card_adoption_rag_no_accumulation/task.md | 当前任务包 | 确认采纳对象、允许输入、允许写入、门禁和阻塞条件 |
| llm_wiki/loop/iterations/iteration_20260525_0024_card_drafting_rag_no_accumulation/artifacts/draft_card.md | 任务允许输入 | 作为被采纳知识卡正文来源，并将状态从 draft 改为 accepted |
| llm_wiki/loop/iterations/iteration_20260525_0024_card_drafting_rag_no_accumulation/artifacts/provenance.md | 任务允许输入 | 作为出处论证正文来源，并做轻量状态与链接整理 |
| llm_wiki/loop/iterations/iteration_20260525_0025_card_audit_rag_no_accumulation/artifacts/audit_report.md | 任务允许输入 | 确认审计结论为 audit_result: pass |
| llm_wiki/kb/cards/rag-document-qa-does-not-accumulate-synthesized-knowledge.md | 任务允许输入 | 用于存在性检查和采纳后成功门禁核对；目标原先不存在，未用于补充事实 |
| llm_wiki/kb/provenance/rag-document-qa-does-not-accumulate-synthesized-knowledge.md | 任务允许输入 | 用于存在性检查和采纳后成功门禁核对；目标原先不存在，未用于补充事实 |
| llm_wiki/kb/indexes/cards.md | 任务允许输入 | 保留既有最小索引内容、追加本卡条目，并核对索引包含标题、路径、状态和来源 |
