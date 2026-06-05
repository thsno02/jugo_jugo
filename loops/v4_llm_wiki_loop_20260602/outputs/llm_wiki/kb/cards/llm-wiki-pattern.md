---
id: llm-wiki-pattern
title: LLM Wiki 模式
status: accepted
card_type: concept
tags: [llm-wiki, knowledge-base, rag-alternative]
created_time: 2026-06-04T22:30:00+08:00
edited_time: 2026-06-04T22:30:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/llm-wiki-pattern.md
canonical_concept: llm-wiki-pattern
aliases: [LLM Wiki, LLM 维基模式, persistent wiki pattern]
summary: >-
  llm-wiki-pattern（LLM Wiki / LLM 维基模式 / persistent wiki pattern）是一种用 LLM
  增量构建并维护持久化 wiki 的知识库模式，区别于 RAG 每次查询重新检索，wiki 作为编译后的知识中间层持续积累
related: [three-layer-architecture, wiki-compounding-artifact]
---

LLM Wiki 是一种个人知识库构建模式：LLM 不是在查询时从原始文档中检索片段（RAG 方式），而是**增量构建并维护一个持久化的、互相链接的 markdown 文件集合**——一个位于用户和原始资料之间的结构化 wiki[^src-1]。

传统 RAG 的问题在于：每次查询都是从零开始重新发现知识，没有积累。即使是需要综合五篇文档的复杂问题，LLM 也必须每次重新找到并拼凑相关片段[^src-2]。NotebookLM、ChatGPT 文件上传等系统都是这种方式。

LLM Wiki 的关键区别在于：当添加新资料时，LLM 不只是索引它以备后用，而是阅读它、提取关键信息、并将其整合到现有 wiki 中——更新实体页面、修订主题摘要、标注新旧数据的矛盾。知识被编译一次并保持更新，而非每次查询时重新推导[^src-3]。wiki 中具体积累的结构类型见复利型制品的详细分析[^card-1]，支撑这一模式的三层架构见架构卡[^card-2]。主题隔离是该模式管理内容规模的核心架构原则[^card-3]。

然而，该模式的设计假设面向个人研究者，向企业扩展时面临结构性张力：单一策展人从特性变为瓶颈[^dist-1]，索引溢出、无 RBAC 和并发冲突三大技术失效同时浮现[^dist-2]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" 第2段 -- "the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files that sits between you and the raw sources"
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" 第1段 -- "the LLM is rediscovering knowledge from scratch on every question. There's no accumulation."
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P2 -- "The knowledge is compiled once and then kept current, not re-derived on every query."
[^card-1]: [Wiki 作为复利型知识制品](wiki-compounding-artifact.md) -- 本卡定义模式，该卡具化 wiki 中积累的五类结构
[^card-2]: [三层架构](three-layer-architecture.md) -- 支撑 LLM Wiki 模式的 raw-wiki-schema 三层结构
