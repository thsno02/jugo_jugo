---
id: retriever-quality-consistent-impact
title: 检索器质量对 RAG 性能的一致性影响
status: draft
card_type: experimental-finding
tags: [retriever, bm25, e5-mistral, dense-retrieval, sparse-retrieval, rag-performance]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
evidence_basis: experimental_paper
justification: ../justification/retriever-quality-consistent-impact.md
canonical_concept: retriever-quality-consistent-impact
aliases: [Retriever Matters Consistently, 检索器质量一致性影响]
summary: >-
  RAGChecker 实验表明检索器质量对 RAG 系统性能的提升是一致的（与 generator 选择无关）。在固定 generator 条件下，从 BM25 切换到 E5-Mistral 使 claim recall 从 74.0 提升至 83.5，context precision 从 52.3 提升至 61.8，整体 F1 从约 45 提升至约 48。该改善对四种 generator（GPT-4/Llama3-8B/Llama3-70B/Mixtral-8x7B）均一致成立。
related: [ragchecker-retriever-metrics, ragchecker-overall-metrics, context-utilization-key-factor]
---

RAGChecker 在 8 个 RAG 系统（2 retriever x 4 generator）跨 10 域的实验中发现：检索器质量的提升对 overall performance 的正向影响是一致且与 generator 无关的。[^src-1]

**定量证据**（10 域平均）：[^src-2]
- BM25 → E5-Mistral: Claim Recall 74.0 → 83.5, Context Precision 52.3 → 61.8
- 固定 GPT-4: F1 50.3 → 52.7
- 固定 Llama3-70B: F1 46.3 → 50.2
- 固定 Llama3-8B: F1 42.1 → 45.0
- 固定 Mixtral-8x7B: F1 42.9 → 45.7

该改善在 Precision 和 Recall 维度均有体现，且不依赖于具体 generator 的选择。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex Main Results" -- "Retriever Matters Consistently. The quality of retrieval is crucial...This improvement is agnostic to the specific choice of generator, suggesting a consistent benefit from employing a better retriever"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "tables/ragchecker_results_avg.tex" -- BM25_GPT-4 F1 50.3 vs E5-Mistral_GPT-4 F1 52.7, etc.

[^card-6]: 参见 [ragchecker-retriever-metrics] 了解 claim recall 和 context precision 的定义
