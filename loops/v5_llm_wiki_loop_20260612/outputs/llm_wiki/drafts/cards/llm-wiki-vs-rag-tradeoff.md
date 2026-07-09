---
id: llm-wiki-vs-rag-tradeoff
title: LLM Wiki 与 RAG 的权衡
status: draft
card_type: comparison
tags: [llm-wiki, rag, retrieval, pre-compilation, knowledge-management]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-vs-rag-tradeoff.md
canonical_concept: llm-wiki-vs-rag-tradeoff
aliases: [LLM wiki vs RAG, wiki vs RAG, pre-compilation vs retrieval, RAG repeats work wiki accumulates]
summary: >-
  LLM wiki 与 RAG 权衡 llm-wiki-vs-rag-tradeoff：RAG 在查询时从文档检索 chunks 并每次重新综合答案（repeats work）；LLM wiki 将综合预编译为稳定 markdown 页面带显式交叉引用（accumulates work）。<500 页时 wiki 更快更便宜且答案更连贯；>10K 文档时 RAG 胜出因为预编译不切实际。核心区别是 repeated synthesis vs accumulated synthesis。
related: []
---

RAG 与 LLM wiki 的核心区别 [^src-1]：

| 维度 | RAG | LLM Wiki |
|------|-----|----------|
| 综合时机 | 查询时（每次重做） | 预编译（累积） |
| 输出形式 | 临时生成答案 | 稳定 markdown 页面 + 显式交叉引用 |
| 工作模式 | Repeats work | Accumulates work |

**适用边界**：
- <500 页：wiki 更快、更便宜、答案更连贯
- >10K 文档：RAG 胜出（预编译不切实际）

[^card-1]: 与 [llm-wiki-scale-thresholds] 相关——规模阈值决定 wiki vs RAG 选择
[^card-2]: 与 [ripple-effect-ingest] 相关——涟漪效应是预编译累积的具体机制

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "FAQ" P84 -- "RAG retrieves chunks...synthesizes a fresh answer each time. The Karpathy LLM wiki pre-compiles the synthesis into stable markdown pages...RAG repeats work; the wiki accumulates it."
