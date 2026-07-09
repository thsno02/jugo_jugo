---
id: conversational-wiki-query
title: 对话式 Wiki 查询
status: draft
card_type: feature
tags: [llm-wiki, query, chat, streaming, wiki-links]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
evidence_basis: documentation
justification: ../justification/conversational-wiki-query.md
canonical_concept: conversational-wiki-query
aliases: [Query wiki, 对话查询, wiki query, conversational Q&A]
summary: >-
  ChatGPT 风格对话界面，流式 Markdown 渲染内嵌 [[wiki-links]]。多轮对话历史。
  回答基于用户笔记而非互联网。Query-to-Wiki Feedback 将对话保存回 Wiki 并执行
  实体/概念提取和语义去重。Hash 跟踪防止重复评估。
related: [karpathy-llm-wiki-concept, full-context-vs-rag]
---

对话式 Wiki 查询提供 ChatGPT 风格的问答界面：[^src-1]

- 流式 Markdown 渲染，回答中内嵌 [[wiki-links]] 作为面包屑导航
- 多轮对话历史保持
- 回答基于用户自己的笔记知识图谱，而非互联网知识
- 每个回答是"深入路径的起点"（trailhead），而非死胡同

**Query-to-Wiki Feedback**：可将有价值的对话保存回 Wiki，保存时执行实体/概念提取和语义去重。Hash 跟踪防止未变更对话被重复评估。[^src-2] [^card-1]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Features" P1 -- "Conversational Query — ChatGPT-style dialog with streaming Markdown and [[wiki-links]], multi-turn history"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Features" P1 -- "Query-to-Wiki Feedback — Save valuable conversations to Wiki with entity/concept extraction, semantic dedup before save"
[^card-1]: 参见 [[full-context-vs-rag]] 了解为何不用 RAG 而用全量上下文
