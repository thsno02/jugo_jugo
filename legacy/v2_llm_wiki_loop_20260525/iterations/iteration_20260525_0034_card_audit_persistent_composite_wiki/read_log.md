- `llm_wiki/loop/iterations/iteration_20260525_0034_card_audit_persistent_composite_wiki/task.md`：读取当前任务包，确认审计对象、允许输入、允许写入和结论格式。
- `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/artifacts/draft_card.md`：读取指定草稿知识卡，检查 statement、fact_type、support、scope、status、References 和 Footnotes。
- `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/artifacts/provenance.md`：读取指定出处论证，检查来源明说部分、整理表述部分和成立范围。
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:13`：只读取任务指定来源证据行，用于核对草稿卡事实支撑。

未读取允许输入之外的文件。
