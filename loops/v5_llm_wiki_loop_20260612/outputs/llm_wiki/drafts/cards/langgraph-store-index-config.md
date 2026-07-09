---
id: langgraph-store-index-config
title: LangGraph Store IndexConfig 向量索引配置
status: draft
card_type: configuration
tags: [langgraph, store, indexconfig, embedding, vector]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [langchain-long-term-memory-docs]
evidence_basis: documentation
justification: ../justification/langgraph-store-index-config.md
canonical_concept: langgraph-index-config
aliases: [IndexConfig, index config, 索引配置]
summary: >-
  IndexConfig 是 LangGraph store 启用向量搜索的配置对象，需提供 embed（嵌入函数，
  接收 Sequence[str] 返回 list[list[float]]）和 dims（向量维度）两个参数。
  通过 InMemoryStore(index=IndexConfig(...)) 或 PostgresStore.from_conn_string(..., index=IndexConfig(...)) 传入。
related: [langgraph-store-search-capabilities, langgraph-store-backend-comparison]
---

IndexConfig 是启用 LangGraph store 向量搜索能力的配置对象。[^src-1]

必须参数：
- `embed`: 嵌入函数，签名为 `Sequence[str] -> list[list[float]]`，也可使用 LangChain embeddings 对象。
- `dims`: 向量维度（int）。

配置方式：在创建 store 时传入 `index=IndexConfig(embed=embed, dims=2)`。[^src-1]

[^src-1]: `data/raw/webpage/langchain-long-term-memory-docs/markdown.md` -- "Store Setup" P1 -- "from langgraph.store.base import IndexConfig ... store = InMemoryStore(index=IndexConfig(embed=embed, dims=2))"

[^card-1]: IndexConfig 是 [langgraph-store-search-capabilities] 向量搜索的前置配置。
