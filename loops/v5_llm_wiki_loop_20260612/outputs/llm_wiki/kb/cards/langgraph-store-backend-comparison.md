---
id: langgraph-store-backend-comparison
title: LangGraph Store 后端对比
status: accepted
card_type: comparison
tags:
- langgraph
- store
- inmemorystore
- postgresstore
- backend
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- langchain-long-term-memory-docs
evidence_basis: documentation
justification: ../justification/langgraph-store-backend-comparison.md
canonical_concept: langgraph-store-backend-types
aliases:
- InMemoryStore
- PostgresStore
- store backend
- 存储后端
summary: LangGraph 提供两种 store 后端：InMemoryStore（内存字典，用于开发测试）和 PostgresStore（PostgreSQL 数据库，用于生产）。PostgresStore 需 from_conn_string + setup() 初始化， 使用 context manager 管理连接。两者共享相同 put/get/search API。
related:
- langgraph-store-data-model
- langgraph-long-term-memory-concept
- langgraph-store-index-config
---
LangGraph 提供两种 store 后端实现：[^src-1][^src-2]

| 后端 | 存储位置 | 适用场景 | 初始化方式 |
|------|----------|----------|-----------|
| InMemoryStore | 内存字典 | 开发/测试 | `InMemoryStore()` |
| PostgresStore | PostgreSQL | 生产环境 | `PostgresStore.from_conn_string(DB_URI)` + `store.setup()` |

PostgresStore 需要使用 context manager（`with` 语句）管理数据库连接生命周期。[^src-2]

两种后端共享完全相同的 API 接口（put/get/search），代码可在开发与生产间无缝切换。[^src-1][^src-2]

[^src-1]: `data/raw/webpage/langchain-long-term-memory-docs/markdown.md` -- "InMemoryStore" P1 -- "InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use."
[^src-2]: `data/raw/webpage/langchain-long-term-memory-docs/markdown.md` -- "PostgreSQL" P1 -- "with PostgresStore.from_conn_string(DB_URI, index=IndexConfig(embed=embed, dims=2)) as store: store.setup()"

[^card-1]: 后端选择影响 [langgraph-long-term-memory-concept] 的持久化保证。
