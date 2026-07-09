---
id: llm-kb-vs-rag-comparison
title: LLM KB 与 RAG 的对比
status: accepted
card_type: comparative-analysis
tags:
- knowledge-management
- rag
- llm-kb
- retrieval
- wiki
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- developersio-jp-pattern
evidence_basis: practitioner_report
justification: ../justification/llm-kb-vs-rag-comparison.md
canonical_concept: llm-kb-vs-rag-comparison
aliases:
- RAG vs wiki
- RAG とどう違うのか
- LLM KB と RAG
summary: 'LLM Knowledge Base 与 RAG 的核心差异: RAG 逐 query 检索碎片无持久结构; LLM KB 事前整理为持久 wiki
  并通过 filing back 成长。Karpathy 表示 ~100 articles / ~400K words 规模下不必 fancy RAG。作者认为两者非二择一:
  ad-hoc 查询用 RAG, 全局理解用 wiki。llm-kb-vs-rag-comparison RAG wiki 比較'
related:
- llm-kb-scale-threshold
- full-context-vs-rag
- compile-time-vs-query-time-knowledge-assembly
---

LLM Knowledge Base 与 RAG(Retrieval-Augmented Generation)的对比 [^src-1]:

| 维度 | RAG | LLM Knowledge Base |
|------|-----|-------------------|
| 信息生命周期 | 逐 query 检索, 用后即弃 | 事前整理, 永续保持 |
| 结构 | 无持久结构 | 结构化 wiki (index + entity + backlink) |
| 成长机制 | 无 | filing back 使 wiki 因使用成长 |
| 适用规模 | 大规模文档 | ~small scale (~100 articles, ~400K words) 已验证 |

Karpathy 原话: "I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries" [^src-2]。

但作者指出两者非互斥: "アドホックな質問には RAG 的な検索が便利で、全体像の把握やプロジェクト横断の理解には wiki が便利" [^src-3]。规模增大后(数千件/数百万語)纯 wiki 可能不足, RAG 式检索成为必要补充 [^card-1]。

[^src-1]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "RAG とどう違うのか" P27 -- "RAG は、質問されるたびにドキュメントの断片を検索して LLM に渡すアプローチです...一方、LLM Knowledge Base は、LLM が事前に情報を読み込んで構造化し、永続的な wiki として保持します。"
[^src-2]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "RAG とどう違うのか" P29 -- "I thought I had to reach for fancy RAG..."
[^src-3]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "RAG とどう違うのか" P32 -- "アドホックな質問には RAG 的な検索が便利で、全体像の把握やプロジェクト横断の理解には wiki が便利という使い分けに落ち着いてきました。"
[^card-1]: 参见 [llm-kb-scale-threshold] — 规模阈值讨论
