---
id: langgraph-store-search-capabilities
title: LangGraph Store 搜索能力
status: accepted
card_type: capability
tags:
- langgraph
- store
- search
- vector-similarity
- filter
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- langchain-long-term-memory-docs
evidence_basis: documentation
justification: ../justification/langgraph-store-search-capabilities.md
canonical_concept: langgraph-store-search
aliases:
- store search
- store.search
- content filter
- vector similarity search
- 向量相似度搜索
summary: LangGraph store.search 支持两种搜索方式的组合：content filter（filter 参数， 精确键值匹配）和 vector similarity（query 参数，需 IndexConfig 配置 embed 函数和 dims）。 两者可在同一 search 调用中组合使用。
related:
- langgraph-store-data-model
- langgraph-store-index-config
---

LangGraph store 的 search 方法支持两种搜索机制的组合：[^src-1]

1. **Content filter**: 通过 `filter={"my-key": "my-value"}` 参数进行精确键值匹配过滤。
2. **Vector similarity**: 通过 `query="language preferences"` 参数进行向量相似度排序。

两者可在同一次 `store.search(namespace, filter=..., query=...)` 调用中组合使用，先过滤再按相似度排序。[^src-1]

向量搜索需要预先配置 IndexConfig（提供 embed 函数和向量维度）。[^src-2]

[^src-1]: `data/raw/webpage/langchain-long-term-memory-docs/markdown.md` -- "Code Example" P1 -- "items = store.search(namespace, filter={\"my-key\": \"my-value\"}, query=\"language preferences\")"
[^src-2]: `data/raw/webpage/langchain-long-term-memory-docs/markdown.md` -- "Store Setup" P1 -- "store = InMemoryStore(index=IndexConfig(embed=embed, dims=2))"

[^card-1]: 搜索是 [langgraph-store-data-model] 数据模型上的查询操作。
