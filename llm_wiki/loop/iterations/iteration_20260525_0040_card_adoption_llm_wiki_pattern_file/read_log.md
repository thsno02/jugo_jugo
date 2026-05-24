# read_log

## 已读取的允许输入

- `llm_wiki/loop/iterations/iteration_20260525_0040_card_adoption_llm_wiki_pattern_file/task.md`：确认任务、允许输入、允许写入、采纳规则和阻塞条件。
- `llm_wiki/loop/iterations/iteration_20260525_0036_card_drafting_llm_wiki_pattern_file/artifacts/draft_card.md`：读取待采纳草稿知识卡。
- `llm_wiki/loop/iterations/iteration_20260525_0036_card_drafting_llm_wiki_pattern_file/artifacts/provenance.md`：读取待采纳出处论证。
- `llm_wiki/loop/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file/artifacts/audit_report.md`：确认 `audit_result: pass`。
- `llm_wiki/kb/cards/llm-wiki-pattern-file.md`：目标卡片路径存在性检查，结果为不存在。
- `llm_wiki/kb/provenance/llm-wiki-pattern-file.md`：目标出处路径存在性检查，结果为不存在。
- `llm_wiki/kb/indexes/cards.md`：读取既有最小索引内容，用于增量追加。

## 未读取

- 未读取 `legacy/`。
- 未读取其它 KB 卡片或 provenance。
- 未读取未列出的事实来源。
