允许输入读取记录：

- `llm_wiki/loop/iterations/iteration_20260525_0021_card_drafting_persistent_wiki_mode/artifacts/draft_card.md`：读取草稿知识卡，用于采纳内容和状态更新。
- `llm_wiki/loop/iterations/iteration_20260525_0021_card_drafting_persistent_wiki_mode/artifacts/provenance.md`：读取出处论证，用于写入目标 provenance。
- `llm_wiki/loop/iterations/iteration_20260525_0022_card_audit_persistent_wiki_mode/artifacts/audit_report.md`：读取审计结论，确认 `audit_result: pass`。
- `llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md`：执行存在性检查；目标文件原先不存在。
- `llm_wiki/kb/provenance/llm-wiki-persistent-wiki-alternative-mode.md`：执行存在性检查；目标文件原先不存在。
- `llm_wiki/kb/indexes/cards.md`：读取既有最小索引，用于增量追加卡片索引行。
- `llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md`：写入后读取核对状态、互链和 section 顺序。
- `llm_wiki/kb/provenance/llm-wiki-persistent-wiki-alternative-mode.md`：写入后读取核对互链和采纳说明。
- `llm_wiki/kb/indexes/cards.md`：写入后读取核对新增索引行。

未读取未列出的来源；未读取 `legacy/`；未运行 git 操作。

