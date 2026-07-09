---
id: llm-wiki-pattern-overview
title: LLM Wiki 模式概述
status: accepted
card_type: architecture-pattern
tags:
- llm-wiki
- persistent-knowledge
- karpathy
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- marvin-hn-persistent-knowledge
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-pattern-overview.md
canonical_concept: llm-wiki-pattern
aliases:
- LLM Wiki
- llm wiki pattern
- persistent knowledge base
- 持久知识库模式
summary: LLM Wiki pattern (llm-wiki-pattern) 由 Karpathy 于 2026-04-04 提出，主张 LLM 应增量构建和维护持久 wiki 而非每次从原始文档检索重建答案。wiki 作为 compiled artifact 持续改进，区别于 RAG 的 transient answer on demand 模式。Hacker News 274 points
  / 89 comments 讨论将其视为 agent workflow 的架构模式。
related:
- llm-wiki-three-layer-architecture
- llm-wiki-vs-rag
- karpathy-llm-wiki-concept
- karpathy-llm-wiki-pattern
- karpathy-llm-wiki-pattern-automation
- karpathy-llm-wiki-three-layer-architecture
- llm-compilation-paradigm
- llm-knowledge-base-pattern
- llm-wiki-definition-and-core-value
- llm-wiki-knowledge-system
- llm-wiki-pattern
- llm-wiki-pattern-definition
- llm-wiki-three-folder-architecture
- llmwiki-compile-first-architecture
- obsidian-wiki-compile-not-retrieve-pattern
- olw-llm-as-compiler
- llm-wiki-ingest-query-lint
- llm-wiki-intentional-abstraction
- llm-wiki-maintenance-engine-analogy
---
LLM Wiki 是 Andrej Karpathy 于 2026 年 4 月发布的一种架构模式。其核心主张：LLM 不应仅在查询时从原始文档检索 chunk 再拼装答案（即传统 RAG 模式），而应增量地构建和维护一组互相链接的 markdown 页面，形成一个持久的、不断改进的知识层。[^src-1]

在此模式下，wiki 是一个 "compiled artifact"——每次有新源进入时，agent 不仅索引它，还要更新主题摘要、修订实体页面、标记矛盾、添加交叉链接并强化运行中的综合。[^src-2]

Hacker News 社区（274 points / 89 comments）将其视为 agent workflow 的架构模式而非单纯的笔记技巧。[^src-3]

[^src-1]: data/raw/webpage/marvin-hn-persistent-knowledge/markdown.md -- "From query-time retrieval to a maintained knowledge layer" P1 -- "most document workflows still look like RAG. You upload files, the model retrieves relevant chunks at query time, and then rebuilds the answer from scratch every time"
[^src-2]: data/raw/webpage/marvin-hn-persistent-knowledge/markdown.md -- "From query-time retrieval to a maintained knowledge layer" P2 -- "the wiki becomes a compiled artifact that keeps getting better over time rather than a transient answer assembled on demand"
[^src-3]: data/raw/webpage/marvin-hn-persistent-knowledge/markdown.md -- "From query-time retrieval to a maintained knowledge layer" P1 -- "the Hacker News thread around the gist had 274 points and 89 comments, with readers treating it less as a note-taking trick and more as an architectural pattern for agent workflows"
