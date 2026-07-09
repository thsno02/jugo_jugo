---
id: langgraph-long-term-memory-concept
title: LangGraph 长期记忆概念
status: accepted
card_type: concept
tags:
- langgraph
- long-term-memory
- agent
- persistence
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- langchain-long-term-memory-docs
evidence_basis: documentation
justification: ../justification/langgraph-long-term-memory-concept.md
canonical_concept: langgraph-long-term-memory
aliases:
- long-term memory
- 长期记忆
- LangGraph long-term memory
summary: LangGraph long-term memory 使 agent 跨不同 conversation 和 session 存储与召回信息， 区别于 short-term memory（仅限单个 thread）。构建于 LangGraph stores 之上， 通过 create_agent 的 store 参数接入。
related:
- langgraph-store-data-model
- langgraph-store-backend-comparison
- langgraph-tool-runtime-store-access
---
Long-term memory 使 agent 能够跨不同 conversation 和 session 存储与召回信息。[^src-1]

与 short-term memory 的关键区别：short-term memory 仅限于单个 thread 范围，而 long-term memory 跨 thread 持久化，可随时召回。[^src-1]

Long-term memory 构建于 LangGraph stores 之上，将数据以 JSON documents 形式保存。接入方式为创建 store 实例并传给 `create_agent` 的 `store` 参数。[^src-1]

[^src-1]: `data/raw/webpage/langchain-long-term-memory-docs/markdown.md` -- "Introduction" P1 -- "Long-term memory lets your agent store and recall information across different conversations and sessions. Unlike short-term memory, which is scoped to a single thread, long-term memory persists across threads and can be recalled at any time."
