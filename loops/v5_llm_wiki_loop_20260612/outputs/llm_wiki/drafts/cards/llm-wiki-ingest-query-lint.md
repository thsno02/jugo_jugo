---
id: llm-wiki-ingest-query-lint
title: LLM Wiki 三种核心操作
status: draft
card_type: operation-pattern
tags: [llm-wiki, ingest, query, lint, operating-loop]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [marvin-hn-persistent-knowledge]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-ingest-query-lint.md
canonical_concept: llm-wiki-ingest-query-lint
aliases: [ingest/query/lint, 三种核心操作, operating loop, 操作循环]
summary: >-
  LLM Wiki 三种核心操作 (llm-wiki-ingest-query-lint): Ingest 读取新源→讨论→写摘要→更新索引→触碰相关页→追加日志；Query 针对 wiki 回答问题并可选归档分析为新页面；Lint 定期检查矛盾/过时声明/孤立页面/弱交叉引用/缺失概念。配合 index.md（内容地图）和 log.md（时间线记录）两个特殊文件。
related: [llm-wiki-three-layer-architecture, llm-wiki-pattern-overview]
---

LLM Wiki 模式定义三种核心操作构成其运行循环：[^src-1]

**Ingest（摄入）**：读取新源 → 讨论 → 写摘要 → 更新索引 → 触碰相关页面 → 追加日志。这不是简单的索引操作，而是一次完整的知识编译过程。

**Query（查询）**：针对 wiki 本身回答问题，然后可选地将产出的分析作为新页面归档回知识库。查询不仅消费知识，也可生产知识。

**Lint（审查）**：定期检查矛盾、过时声明、孤立页面、弱交叉引用或缺失概念。这是维护知识一致性的关键操作。

两个特殊文件辅助导航：index.md 提供内容导向的 wiki 地图，log.md 记录 wiki 演化的时间线。两者分离了"结构"与"历史"两个关注点。[^src-2] [^card-1]

[^src-1]: data/raw/webpage/marvin-hn-persistent-knowledge/markdown.md -- "The three layers and the operating loop" P2 -- "Ingest means reading a new source, discussing it, writing a summary, updating the index, touching related pages, and appending to the log. Query means answering questions against the wiki itself, then optionally filing the resulting analysis back into the knowledge base as a new page. Lint means periodically checking for contradictions, stale claims, orphan pages, weak cross-references, or missing concepts."
[^src-2]: data/raw/webpage/marvin-hn-persistent-knowledge/markdown.md -- "The three layers and the operating loop" P2 -- "Two special files, index.md and log.md, help navigation by separating the content-oriented map of the wiki from the chronological record of how it evolved."
[^card-1]: llm-wiki-three-layer-architecture
