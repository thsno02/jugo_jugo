# read_log

## 允许输入读取

- `llm_wiki/loop/iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1/artifacts/draft_card.md`
  - 用途：读取待采纳草稿知识卡。
- `llm_wiki/loop/iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1/artifacts/provenance.md`
  - 用途：读取待采纳出处论证。
- `llm_wiki/loop/iterations/iteration_20260525_0007_card_audit_raw_sources_truth_r1/artifacts/audit_report.md`
  - 用途：确认审计结论是否为 `pass`。

## 额外读取

- `llm_wiki/kb/cards/raw-sources-readonly-source-of-truth.md`
  - 原因：目标知识卡路径未列入允许输入，但阻塞条件要求检查是否会覆盖已有不同内容。
  - 用途：若文件存在，则比对采纳内容；若不存在，仅确认可写入。
- `llm_wiki/kb/provenance/raw-sources-readonly-source-of-truth.md`
  - 原因：目标出处路径未列入允许输入，但阻塞条件要求检查是否会覆盖已有不同内容。
  - 用途：若文件存在，则比对采纳内容；若不存在，仅确认可写入。
- `llm_wiki/kb/indexes/cards.md`
  - 原因：任务要求更新最小索引，但该路径未列入允许输入。
  - 用途：保留现有索引内容并追加或确认本卡条目。
