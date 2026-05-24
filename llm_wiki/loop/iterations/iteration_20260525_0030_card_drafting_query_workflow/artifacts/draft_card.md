# Query 操作回写好答案

statement: 该来源把 query 操作描述为：LLM 针对 wiki 搜索相关页面、阅读这些页面，并综合生成带引用的答案；来源还主张，有价值的问答结果可以作为新页面写回 wiki。

fact_type: known_fact

support: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:39-40` 的 Query 小节明说，提问发生在 wiki 之上，LLM 会搜索相关页面、阅读页面并生成带引用的综合答案；同一段还说明，好的答案可以归档回 wiki，成为新页面。

scope: 仅限该来源对 query 操作流程及答案回写主张的描述；不扩展为对任何具体实现、产品能力或通用 wiki 工作流的事实判断。

status: draft

## References

- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:39-40`

## Footnotes

- 本卡只处理 `候选 12`，候选字段用 `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md` 中对应候选块核对；事实支撑以指定来源行 `39-40` 为准。
