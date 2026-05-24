# Ingest 示例流程

statement: 该来源把 ingest 描述为一个从放入新来源到更新 wiki 与日志的示例操作流程：新来源先进入 raw collection，并交给 LLM 处理；示例流中，LLM 读取来源、与用户讨论要点、写 wiki 摘要页、更新 index、更新相关实体页和概念页，并追加 log 条目。

fact_type: known_fact

support: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:35-38` 的 Operations / Ingest 小节明说，新来源会被放入 raw collection 并交给 LLM 处理；随后以 example flow 的形式列出读取来源、讨论要点、写摘要页、更新 index、更新相关实体和概念页，以及向 log 追加记录。

scope: 仅限该来源示例化的 ingest 操作流程；不推广为所有 LLM wiki 系统必须遵循的标准流程，也不包含该段落中关于监督强度或批量摄取偏好的额外判断。

status: accepted

provenance: `llm_wiki/kb/provenance/llm-wiki-ingest-example-flow.md`

## References

- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:35-38`

## Footnotes

- 本卡将来源中的 "An example flow" 整理为“示例操作流程”；卡片不把该示例扩写成通用规范。
