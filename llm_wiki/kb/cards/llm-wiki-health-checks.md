# LLM health checks 清理 wiki

statement: 被引用推文描述，LLM 可以对 wiki 运行 `health checks`，用于发现不一致数据、补全缺失数据、寻找新文章候选的有趣连接，并以此逐步清理 wiki、提升整体数据完整性。

fact_type: known_fact

support: 该 quote text 的 `Linting` 段落直接说到运行 LLM `health checks`，并列出 `find inconsistent data`、`impute missing data`、`find interesting connections for new article candidates` 等例子；同一段还说明这些检查用于逐步清理 wiki 并增强整体数据完整性。

scope: 仅限该 quote text 对 wiki 检查和清理方式的描述；不外推为通用最佳实践、产品功能承诺或已验证的长期效果。

status: accepted

## Notes

这张卡只保留一个事实：被引用推文如何描述 LLM 对 wiki 的检查与清理用途。`health checks` 保留原文术语，因为它是该段事实边界的核心表述。

## References

- `data/raw/webpage/karpathy-x-launch-post/raw.json`，JSON pointer `$.tweet.quote.text`，相关段落为 `Linting`。
- 出处论证：`llm_wiki/kb/provenance/llm-wiki-health-checks.md`

## Footnotes

- 本卡不使用该 JSON pointer 之外的作者身份、发布时间或外部背景。
