---
id: llm-wiki-query-phase
title: LLM Wiki Query 阶段
status: accepted
card_type: process-description
tags:
- llm-wiki
- query
- reasoning
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- anthemcreation-en-guide
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-query-phase.md
canonical_concept: llm-wiki-query-phase
aliases:
- query phase
- wiki query
- querying the wiki
summary: LLM wiki query 阶段 query-phase：构建完成后直接查询 canonical wiki 而非 raw sources。模型在已积累和结构化的知识上推理，实现纯
  RAG 在大规模语料上难以达到的分析深度。
related:
- llm-wiki-ingestion-workflow
- llm-wiki-vs-rag-reasoning-depth
- conversational-wiki-query
- llm-kb-query-filing-back
- llm-wiki-multi-phase-query-pipeline
---

Query 阶段是 LLM wiki 的读取操作。一旦 wiki 构建完成，用户直接查询 canonical wiki 而非原始源文档 [^src-1]。

模型可以在已积累和结构化的知识上进行推理，这使得某些分析——如需要跨多个概念关联的复杂问题——成为可能，而纯 RAG 在大规模语料上难以实现同等深度 [^card-1]。

[^src-1]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- "Query phase" -- "Once the wiki is built, you query the canonical wiki directly instead of the raw sources. The model can reason on accumulated and structured knowledge"
[^card-1]: 参见 [[llm-wiki-vs-rag-reasoning-depth]] 关于 multi-hop reasoning 的优势展开
