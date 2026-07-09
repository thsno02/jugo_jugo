---
id: llm-wiki-agent-vs-rag
title: Wiki Agent 与 RAG 的结构性差异
status: accepted
card_type: comparison
tags:
- rag
- knowledge-management
- wiki
- retrieval
- contradiction-detection
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-samuraigpt-llm-wiki-agent
evidence_basis: author_claim
justification: ../justification/llm-wiki-agent-vs-rag.md
canonical_concept: wiki-agent-vs-rag
aliases:
- LLM Wiki Agent vs RAG
- wiki vs rag
- compile vs retrieve
summary: LLM Wiki Agent 作者主张 wiki-agent-vs-rag 存在 5 维结构性差异： (1) 编译一次保持更新 vs 每次查询重新推导；(2) 结构化 wiki 页面 vs 原始 chunk 检索； (3) 预建交叉引用 vs 无交叉引用；(4) ingest 时标记矛盾 vs 查询时才可能浮现； (5) 源积累使 wiki 更丰富 vs 无积累效应。本质差异在于 RAG
  是 query-time retrieval， Wiki Agent 是 ingest-time compilation。
related:
- llm-wiki-vs-rag-tradeoff
---

LLM Wiki Agent 的 README 明确给出了与 RAG 的 5 维对比表：[^src-1]

1. **知识推导时机**：RAG 每次查询重新推导（re-derives knowledge every query），Wiki Agent 编译一次并保持更新（compiles once, keeps current）。[^card-1]
2. **检索单元粒度**：RAG 使用原始 chunk 作为检索单元，Wiki Agent 使用结构化 wiki 页面。
3. **交叉引用**：RAG 无交叉引用，Wiki Agent 的交叉引用在 ingest 时预建。
4. **矛盾检测时机**：RAG 的矛盾在查询时才可能浮现（maybe），Wiki Agent 在 ingest 时即标记。
5. **积累效应**：RAG 无积累，Wiki Agent 中每个新源使 wiki 整体更丰富。

本质差异据材料可概括为：RAG 是 query-time retrieval 范式，Wiki Agent 是 ingest-time compilation 范式。两者的 trade-off 在于前者灵活但重复计算，后者预付计算成本但查询轻量。[^src-1]

需注意这是项目作者的定位性主张，对 RAG 的描述有所简化——实际 RAG 系统可能已包含某些交叉引用或矛盾检测能力。

[^src-1]: `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md` -- "What Makes This Different from RAG" -- "Re-derives knowledge every query | Compiles once, keeps current..."
[^card-1]: llm-wiki-agent-compile-once-architecture — 编译式架构是该对比的基础
