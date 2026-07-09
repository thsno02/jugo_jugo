---
id: llm-wiki-vs-rag
title: LLM Wiki 与 RAG 的核心差异
status: accepted
card_type: comparison
tags:
- llm-wiki
- rag
- retrieval
- compiled-artifact
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- marvin-hn-persistent-knowledge
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-vs-rag.md
canonical_concept: llm-wiki-vs-rag
aliases:
- LLM Wiki vs RAG
- wiki vs retrieval
- compiled artifact vs transient answer
summary: 'LLM Wiki 与 RAG 的核心差异 (llm-wiki-vs-rag): RAG 模式在查询时检索 chunk 并每次从头重建答案（transient answer assembled on demand）；LLM Wiki 模式在摄入时增量编译知识为持久 wiki（compiled artifact that keeps getting better）。本质区别是从 query-time
  retrieval 转向 crawl-time maintenance，wiki 随时间累积改进而非每次临时组装。'
related:
- llm-wiki-pattern-overview
- llm-wiki-maintenance-engine-analogy
- llm-wiki-vs-rag-boundary
- llm-wiki-vs-rag-ingest-time-synthesis
- llm-wiki-vs-rag-reasoning-depth
- llm-wiki-vs-rag-tradeoff
- compiled-knowledge-in-context
- karpathy-llm-wiki-skill
- llm-wiki-knowledge-system
- llm-wiki-pattern-definition
- llm-wiki-plain-file-storage
---
LLM Wiki 模式的提出直接针对传统 RAG 的局限性：[^src-1]

**RAG 模式**：上传文件 → 查询时检索相关 chunk → 每次从头重建答案。答案是 "transient answer assembled on demand"，不保留、不累积。

**LLM Wiki 模式**：新源到达 → 增量更新持久 wiki → 查询基于已合成知识回答。Wiki 是 "compiled artifact that keeps getting better over time"。

本质差异在于计算发生的时机和知识的持久性：RAG 将智力投入推迟到查询时（query-time retrieval），LLM Wiki 将智力投入前移到维护时（crawl-time maintenance）。后者的知识随时间累积改进，前者每次都是独立的临时组装。[^src-2] [^card-1]

[^src-1]: data/raw/webpage/marvin-hn-persistent-knowledge/markdown.md -- "From query-time retrieval to a maintained knowledge layer" P1 -- "most document workflows still look like RAG. You upload files, the model retrieves relevant chunks at query time, and then rebuilds the answer from scratch every time"
[^src-2]: data/raw/webpage/marvin-hn-persistent-knowledge/markdown.md -- "From query-time retrieval to a maintained knowledge layer" P2 -- "the wiki becomes a compiled artifact that keeps getting better over time rather than a transient answer assembled on demand"
[^card-1]: llm-wiki-pattern-overview
