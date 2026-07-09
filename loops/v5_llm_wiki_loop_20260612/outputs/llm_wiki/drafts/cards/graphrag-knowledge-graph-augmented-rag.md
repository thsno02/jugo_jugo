---
id: graphrag-knowledge-graph-augmented-rag
title: GraphRAG 知识图谱增强检索生成
status: draft
card_type: system-architecture
tags: [rag, knowledge-graph, microsoft-research, information-retrieval]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
evidence_basis: code_implementation
justification: ../justification/graphrag-knowledge-graph-augmented-rag.md
canonical_concept: graphrag-knowledge-graph-augmented-rag
aliases: [GraphRAG, graph-based RAG, 图谱增强RAG, Microsoft GraphRAG]
summary: >-
  GraphRAG 是微软研究院提出的结构化层次化检索增强生成方法，通过从非结构化文本中提取知识图谱、执行层次社区检测、生成社区摘要，在查询时利用这些结构提供上下文，克服了 baseline RAG 在跨信息关联和全局语义概括两类问题上的不足。GraphRAG knowledge-graph hierarchical community structured RAG。
related: []
---

GraphRAG 是一种结构化、层次化的检索增强生成（RAG）方法，与基于朴素语义搜索的 baseline RAG 相对。其核心流程包括：从原始文本提取知识图谱，构建社区层次结构，为社区生成摘要报告，并在查询时利用这些结构辅助 LLM 推理。[^src-1]

Baseline RAG 存在两类典型失败场景：（1）需要通过共享属性跨越不同信息片段进行综合推理时表现不佳；（2）对大规模数据集或大文档的全局语义概括理解能力有限。GraphRAG 通过知识图谱的社区结构和社区摘要来系统性地解决这两类问题。[^src-2]

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index.md" P93 -- "GraphRAG is a structured, hierarchical approach to Retrieval Augmented Generation (RAG), as opposed to naive semantic-search approaches using plain text snippets."
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index.md" P105-108 -- "Baseline RAG struggles to connect the dots... Baseline RAG performs poorly when being asked to holistically understand summarized semantic concepts over large data collections"
