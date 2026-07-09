---
id: llm-wiki-persistent-knowledge-compilation
title: LLM Wiki 持久知识编译范式
status: accepted
card_type: design-philosophy
tags:
- llm-wiki
- knowledge-compilation
- persistent-wiki
- anti-rag
- incremental-build
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-nashsu-llm-wiki
evidence_basis: code_implementation
justification: ../justification/llm-wiki-persistent-knowledge-compilation.md
canonical_concept: llm-wiki-persistent-knowledge-compilation
aliases:
- persistent knowledge compilation
- 持久知识编译
- incremental wiki building
- 增量构建持久 wiki
- Karpathy LLM Wiki pattern
summary: LLM Wiki 持久知识编译范式（persistent knowledge compilation）：区别于传统 RAG（每次查询从头检索和推导）， LLM 增量构建并维护一个持久 wiki——知识编译一次并保持更新，而非每次查询时重新推导。基于 Karpathy 的 llm-wiki.md pattern，实现为跨平台桌面应用（Tauri v2）并附加大量扩展。
related:
- karpathy-llm-wiki-pattern-automation
---

LLM Wiki 的核心设计理念是"持久知识编译"——与传统 RAG（Retrieval-Augmented Generation，每次查询时从头检索并重新推导答案）形成对比。在 LLM Wiki 中，知识被**编译一次并保持更新**：LLM 从用户文档中增量提取结构化知识，写入持久的 wiki 页面，后续查询直接检索已编译的知识而非重新推导。[^src-1]

该范式源自 Andrej Karpathy 的 llm-wiki.md 设计模式——一份描述使用 LLM 增量构建和维护个人 wiki 的方法论文档。LLM Wiki 项目是这一抽象设计模式的具体实现，构建为跨平台桌面应用（Tauri v2, React 19），并在原始设计基础上做了大量扩展（两步摄入、知识图谱、多阶段检索等）。[^src-2]

[^src-1]: `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md` -- "What is this?" P49 -- "Instead of traditional RAG (retrieve-and-answer from scratch every time), the LLM incrementally builds and maintains a persistent wiki from your sources. Knowledge is compiled once and kept current, not re-derived on every query."
[^src-2]: `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md` -- "Credits" P58-59 -- "The foundational methodology comes from Andrej Karpathy's llm-wiki.md... The original document is an abstract design pattern; this project is a concrete implementation with substantial extensions."
