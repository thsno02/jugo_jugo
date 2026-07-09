---
id: langgraph-store-data-model
title: LangGraph Store 数据模型
status: accepted
card_type: data-model
tags:
- langgraph
- store
- namespace
- key
- json
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- langchain-long-term-memory-docs
evidence_basis: documentation
justification: ../justification/langgraph-store-data-model.md
canonical_concept: langgraph-store-namespace-key-model
aliases:
- LangGraph store
- namespace
- key
- store data model
- 命名空间-键模型
summary: LangGraph store 以 JSON document 为存储单元，按 namespace（类似 folder， 含 user_id/org_id 等标识）+ key（类似 filename）层级组织， 支持跨 namespace 的 content filter 搜索。namespace 为 tuple 结构如 (user_id, application_context)。
related:
- langgraph-long-term-memory-concept
- langgraph-store-search-capabilities
- langgraph-store-backend-comparison
- langgraph-tool-runtime-store-access
---
LangGraph store 将每条记忆存储为 JSON document，按 namespace 和 key 两级层级组织。[^src-1]

Namespace 类似 folder，key 类似 filename。Namespace 通常包含 user_id 或 org_id 等标签以便组织信息。[^src-1] 实际代码中 namespace 为 tuple 结构，例如 `(user_id, application_context)`。[^src-2]

这种层级结构使记忆可以按层级组织，并支持通过 content filter 进行跨 namespace 搜索。[^src-1]

[^src-1]: `data/raw/webpage/langchain-long-term-memory-docs/markdown.md` -- "Store Organization" P1 -- "Each memory is organized under a custom namespace (similar to a folder) and a distinct key (like a file name). Namespaces often include user or org IDs or other labels that makes it easier to organize information."
[^src-2]: `data/raw/webpage/langchain-long-term-memory-docs/markdown.md` -- "Code Example" P1 -- "namespace = (user_id, application_context)"

[^card-1]: 本卡为 [langgraph-long-term-memory-concept] 的数据模型细化。
