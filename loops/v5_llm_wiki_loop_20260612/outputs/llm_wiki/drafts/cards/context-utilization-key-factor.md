---
id: context-utilization-key-factor
title: Context Utilization 是 RAG F1 的关键因子
status: draft
card_type: experimental-finding
tags: [context-utilization, f1-correlation, generator-capability, rag-performance]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
evidence_basis: experimental_paper
justification: ../justification/context-utilization-key-factor.md
canonical_concept: context-utilization-key-factor
aliases: [Context Utilization is Key, context utilization 关键性]
summary: >-
  RAGChecker 实验发现 context utilization 在所有 generator metrics 中与 overall F1 的相关性最强。同时 context utilization 在不同 retriever 之间相对稳定（如 GPT-4 的 CU: BM25 61.4 vs E5-Mistral 60.4），这意味着通过提升 retriever 可直接改善 overall recall。该发现表明生成器充分利用检索上下文的能力是 RAG 系统性能的关键因素。
related: [ragchecker-generator-metrics, retriever-quality-consistent-impact]
---

RAGChecker 在 10 域平均实验中观察到：在所有 generator metrics 中，context utilization 与 overall F1 score 的相关性最强，而其他 generator metrics（faithfulness、noise sensitivity 等）与 F1 的相关性相对较弱。[^src-1]

此外，各 generator 的 context utilization 在两种 retriever 之间保持相对稳定。例如 GPT-4 的 context utilization 在 BM25 下为 61.4，在 E5-Mistral 下为 60.4；Llama3-70B 为 56.2 vs 57.6。[^src-2]

这一稳定性意味着：当 retriever 改善（claim recall 提升）时，generator 能以相对固定的利用率将新增信息转化为正确回答，从而直接改善 overall recall。[^src-1]

该发现表明，提升 generator 充分利用检索上下文的能力是改善 RAG 系统性能的关键方向——因为 RAG 系统的价值正在于利用外部知识超越 generator 自身的 self-knowledge。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex Main Results" -- "Stable and Performant Context Utilization is Key. Among all generator metrics, we observe that context utilization strongly correlates to the overall F1 score...generators' context utilization are relatively stable between the two retrievers, meaning their overall recall can be improved with a better retriever"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "tables/ragchecker_results_avg.tex" -- BM25_GPT-4 CU 61.4, E5-Mistral_GPT-4 CU 60.4

[^card-7]: 参见 [ragchecker-generator-metrics] 了解 context utilization 的公式定义
