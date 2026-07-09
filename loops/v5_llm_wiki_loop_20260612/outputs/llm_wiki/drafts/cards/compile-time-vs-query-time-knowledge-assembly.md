---
id: compile-time-vs-query-time-knowledge-assembly
title: 编译时与查询时知识组装
status: draft
card_type: conceptual_distinction
tags: [knowledge-assembly, llm-wiki, rag, architecture-comparison]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [atlan-llm-wiki-vs-rag-dynamic-20260524]
evidence_basis: practitioner_report
justification: ../justification/compile-time-vs-query-time-knowledge-assembly.md
canonical_concept: compile-time-vs-query-time-knowledge-assembly
aliases: [compile-time knowledge assembly, query-time knowledge assembly, 编译时知识组装, 查询时知识组装]
summary: >-
  compile-time vs query-time knowledge assembly 是 LLM wiki 与 RAG 的核心架构区分。LLM wiki 在查询前将知识预编译为结构化索引整体加载进 context（compile-time）；RAG 在收到查询后从向量库动态检索相关片段注入 context（query-time）。该区分关乎知识组装时机，非智能水平差异。
related: [llm-wiki-three-folder-architecture]
---

LLM wiki 与 RAG 知识库的架构区分比争论所暗示的更简单：它是编译时(compile-time)与查询时(query-time)知识组装的差异，而非智能水平的差异。[^src-1]

**编译时知识组装（LLM wiki）**：LLM wiki 将结构化索引直接加载进 context——LLM 预先读取所有相关内容。知识在查询发生前已完成组装。[^src-2]

**查询时知识组装（RAG）**：RAG 知识库在查询时从向量存储中动态检索语义相关片段。LLM 从不加载完整语料——仅基于检索到的 context 生成回答。[^src-3]

这一区分意味着两者回答的是同一表层问题（"如何让 LLM 访问知识？"）的不同版本，基于对规模的不同底层假设。[^src-4] [^card-1]

[^src-1]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "LLM wiki vs RAG knowledge base: what's the difference?" P17 -- "The distinction is compile-time versus query-time knowledge assembly, not intelligence."
[^src-2]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "LLM wiki vs RAG knowledge base: what's the difference?" P17 -- "An LLM wiki loads a structured index directly into context - the LLM reads everything relevant upfront."
[^src-3]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is a RAG knowledge base?" P33 -- "A RAG knowledge base combines a vector-indexed document store with a retrieval layer that surfaces semantically relevant chunks at query time."
[^src-4]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "LLM wiki vs RAG knowledge base: what's the difference?" P19 -- "both approaches answer the same surface-level question with different underlying assumptions about scale."
[^card-1]: 参见 [[llm-wiki-three-folder-architecture]] — LLM wiki 编译时组装的具体实现架构
