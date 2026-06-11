---
id: thread-scoped-memory-boundary
title: 线程作用域作为记忆持久化边界
status: accepted
card_type: mechanism
tags: [long-term-memory, short-term-memory, thread, scope, langchain, langgraph, memory-taxonomy]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [langchain-long-term-memory-docs]
justification: ../justification/thread-scoped-memory-boundary.md
canonical_concept: thread-scoped-memory-boundary
aliases: [线程作用域记忆边界, thread-scoped memory, 短期记忆线程作用域]
summary: >-
  thread-scoped-memory-boundary（线程作用域记忆边界 / thread-scoped memory / 短期记忆线程作用域）是 LangChain/LangGraph 对 agent 记忆持久性的分类标准：以"线程（thread）"为边界，短期记忆局限于单个线程内，长期记忆跨线程持久化且可随时召回
related: [namespace-key-memory-model, cross-session-continuity]
---

LangChain/LangGraph 将 agent 记忆的持久性按**线程（thread）**划分为两个层次[^src-1]：

1. **短期记忆（short-term memory）**——作用域限定于单个线程（single thread），线程结束即不可访问
2. **长期记忆（long-term memory）**——跨线程持久化（persists across threads），可在任何时刻被召回

这一分类的关键设计决策在于选择"线程"作为边界单位。在 LangGraph 中，一个线程（thread）对应一次连续对话交互，类似于一个 conversation session。长期记忆通过 LangGraph store 实现跨线程持久化，并按命名空间-键值结构组织[^src-2]。

该文档未讨论"线程"的精确生命周期定义（何时创建、何时结束），也未讨论短期记忆的具体实现机制（是否为纯上下文窗口内容，还是有额外的线程内持久化层），更未讨论介于短期与长期之间的中间层（如 MemGPT 的 recall storage 提供了线程内但超出上下文窗口的中间层记忆）。

## Footnotes

[^src-1]: `data/raw/webpage/langchain-long-term-memory-docs/markdown.md` -- 开篇段落 -- "Unlike short-term memory, which is scoped to a single thread, long-term memory persists across threads and can be recalled at any time."
[^src-2]: `data/raw/webpage/langchain-long-term-memory-docs/markdown.md` -- 开篇段落 -- "Long-term memory is built on LangGraph stores, which save data as JSON documents organized by namespace and key."
