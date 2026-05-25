| 路径 | 原因 | 用途 |
| --- | --- | --- |
| `llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague/artifacts/draft_card.md` | 任务允许输入 | 获取待采纳知识卡正文，并将 `status` 从 `draft` 改为 `accepted` |
| `llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague/artifacts/provenance.md` | 任务允许输入 | 获取出处论证正文，并轻量加入对应知识卡链接和采纳状态 |
| `llm_wiki/loop/iterations/iteration_20260525_0058_card_audit_idea_file_abstract_vague/artifacts/audit_report.md` | 任务允许输入 | 确认 `audit_result: pass` |
| `llm_wiki/kb/cards/idea-file-abstract-vague.md` | 任务允许输入 | 用于目标卡片存在性、覆盖冲突检查，以及写入后的门禁验证 |
| `llm_wiki/kb/provenance/idea-file-abstract-vague.md` | 任务允许输入 | 用于目标出处文件存在性、覆盖冲突检查，以及写入后的门禁验证 |
| `llm_wiki/kb/indexes/cards.md` | 任务允许输入 | 保留既有最小索引内容、追加本卡索引行，并做写入后的门禁验证 |
| `llm_wiki/loop/iterations/iteration_20260525_0059_card_adoption_idea_file_abstract_vague/loop_status.md` | 本轮允许写入产物 | 写入后验证状态文件存在且结果为 `LOOP_DONE` |
| `llm_wiki/loop/iterations/iteration_20260525_0059_card_adoption_idea_file_abstract_vague/loop_delivery.md` | 本轮允许写入产物 | 写入后验证交付文件存在且包含 `LOOP_DONE` |
| `llm_wiki/loop/iterations/iteration_20260525_0059_card_adoption_idea_file_abstract_vague/read_log.md` | 本轮允许写入产物 | 写入后验证读取记录已落盘 |
