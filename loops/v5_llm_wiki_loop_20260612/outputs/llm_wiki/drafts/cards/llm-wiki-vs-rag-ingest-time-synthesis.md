---
id: llm-wiki-vs-rag-ingest-time-synthesis
title: LLM Wiki 与 RAG 的综合时机对比
status: draft
card_type: comparison
tags: [llm-wiki, rag, knowledge-architecture, synthesis-timing, ingest-vs-query]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-astro-han-karpathy-llm-wiki]
evidence_basis: code_implementation
justification: ../justification/llm-wiki-vs-rag-ingest-time-synthesis.md
canonical_concept: llm-wiki-vs-rag-ingest-time-synthesis
aliases: [LLM Wiki vs RAG, wiki model vs retrieval augmented generation, ingest-time synthesis vs query-time retrieval]
summary: >-
  LLM wiki 与 RAG 在综合时机 (synthesis timing) 上的对比：RAG 将知识存于 raw chunks
  和 embeddings 中在 query time 查询时综合，适合 broad retrieval across large corpora
  大规模语料广泛检索；LLM wiki 将知识存于 curated markdown pages 中在
  ingest/maintenance 时综合，适合 compounding knowledge 复合知识、summaries 摘要和
  durable cross-links 持久交叉链接。karpathy-llm-wiki 明确针对 wiki model 优化：
  知识随时间改善而非每次查询重新推导关系。
related: [llm-wiki-knowledge-system, karpathy-llm-wiki-skill]
---

LLM wiki 与 RAG 代表两种不同的知识管理范式，核心区别在于知识综合发生的时机和知识的存储形式。[^src-1]

## 对比维度

| 维度 | RAG | LLM Wiki |
|------|-----|----------|
| 知识存储 | Raw chunks 和 embeddings | Curated markdown pages |
| 综合时机 | 查询时 (at query time) | 摄入和维护时 (during ingest and maintenance) |
| 适用场景 | 大规模语料的广泛检索 | 复合知识、摘要和持久交叉链接 |

[^src-1]

## 设计倾向

该项目明确针对 wiki 模型进行优化：知识随时间改善（improves over time），而非在每次查询时重新推导关系（re-deriving relationships on every query）。[^src-2] [^card-1]

---
[^src-1]: data/raw/github_repo/repo-astro-han-karpathy-llm-wiki/repo/README.md -- "LLM Wiki vs RAG" P1 -- "RAG: Raw chunks and embeddings / At query time / Broad retrieval across large corpora; LLM Wiki: Curated markdown pages / During ingest and maintenance / Compounding knowledge, summaries, and durable cross-links"
[^src-2]: data/raw/github_repo/repo-astro-han-karpathy-llm-wiki/repo/README.md -- "LLM Wiki vs RAG" P2 -- "This skill is optimized for the wiki model: knowledge that improves over time instead of re-deriving relationships on every query."
[^card-1]: llm-wiki-knowledge-system -- LLM wiki 核心定义中的复合增长机制
