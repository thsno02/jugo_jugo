allowed_reads:
- path: llm_wiki/loop/iterations/iteration_20260525_0050_card_adoption_llm_wiki_use_cases/task.md
  purpose: 确认任务、允许输入、允许写入和采纳规则。
- path: llm_wiki/loop/iterations/iteration_20260525_0044_card_drafting_llm_wiki_use_cases/artifacts/draft_card.md
  purpose: 读取待采纳草稿卡内容。
- path: llm_wiki/loop/iterations/iteration_20260525_0044_card_drafting_llm_wiki_use_cases/artifacts/provenance.md
  purpose: 读取待采纳出处论证内容。
- path: llm_wiki/loop/iterations/iteration_20260525_0049_card_audit_llm_wiki_use_cases/artifacts/audit_report.md
  purpose: 确认审计结论为 audit_result: pass。
- path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
  purpose: 目标卡片存在性检查；结果为不存在；采纳后校验 status、provenance 链接和 Footnotes 位置。
- path: llm_wiki/kb/provenance/llm-wiki-listed-use-cases.md
  purpose: 目标出处论证存在性检查；结果为不存在；采纳后校验 card 回链。
- path: llm_wiki/kb/indexes/cards.md
  purpose: 保留既有最小索引内容并做增量更新；采纳后校验新增索引行。
outside_allowed_reads:
- path: llm_wiki/loop/iterations/iteration_20260525_0050_card_adoption_llm_wiki_use_cases/loop_status.md
  reason: 采纳后确认必需状态文件已写入完成态。
  use: 校验本轮状态记录。
- path: llm_wiki/loop/iterations/iteration_20260525_0050_card_adoption_llm_wiki_use_cases/loop_delivery.md
  reason: 采纳后确认必需交付文件包含 LOOP_DONE。
  use: 校验本轮交付记录。
- path: llm_wiki/loop/iterations/iteration_20260525_0050_card_adoption_llm_wiki_use_cases/read_log.md
  reason: 采纳后确认必需读日志已写入。
  use: 校验本轮读日志记录。
