---
id: ragchecker-retriever-metrics
title: RAGChecker 检索器指标 Claim Recall 与 Context Precision
status: draft
card_type: metric-definition
tags: [rag-evaluation, retriever, claim-recall, context-precision, chunk-level]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
evidence_basis: experimental_paper
justification: ../justification/ragchecker-retriever-metrics.md
canonical_concept: ragchecker-retriever-metrics
aliases: [claim recall, context precision, retriever metrics, 检索器指标]
summary: >-
  RAGChecker retriever metrics 包含两个指标：Claim Recall = |{c^(gt)_i | c^(gt)_i ∈ {chunk_j}}| / |{c^(gt)_i}|，衡量 ground truth claims 被 retrieved chunks 覆盖的比例；Context Precision = |{r-chunk_j}| / k，其中 relevant chunk 定义为包含至少一个 ground truth claim 的 chunk，衡量检索结果中有用 chunk 的占比。Context precision 采用 chunk-level 而非 claim-level，因为固定大小分块策略下 chunk 可能同时包含相关和无关信息。
related: [ragchecker-framework-overview, claim-level-entailment-checking, ragchecker-overall-metrics]
---

RAGChecker 的 retriever metrics 面向 RAG 开发者诊断检索模块性能。[^src-1]

**Claim Recall** = |{c^(gt)_i | c^(gt)_i ∈ {chunk_j}}| / |{c^(gt)_i}|

衡量 ground truth answer 中有多少 claims 被 retrieved chunks 覆盖（完备性）。[^src-1]

**Context Precision** = |{r-chunk_j}| / k

其中 relevant chunk (r-chunk) 定义为：chunk_j 中至少存在一个 ground truth claim c^(gt)_i 使得 c^(gt)_i ∈ chunk_j。其余 chunk 称为 irrelevant chunk (irr-chunk)。k 为 retrieved chunks 总数。[^src-2]

Context precision 选择 chunk-level 而非 claim-level 的设计理由：由于固定大小分块策略，一个 chunk 可能同时包含相关 claims 和无关/误导信息。因此理想检索器的 claim-level precision 上界低于 100%，且其具体值取决于文本分布和分块策略。Chunk-level precision 提供了更好的可解释性。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex Retriever Metrics" -- "we compute claim recall as the proportion of {c^(gt)_i | c^(gt)_i ∈ {chunk_j}}"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex Retriever Metrics" -- "A retrieved chunk is called relevant chunk (r-chunk), if any ground-truth claim is entailed in it...The retriever's context precision is defined as |{r-chunk_j}|/k"
[^src-3]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex Retriever Metrics" -- "a chunk-level precision provides better interpretability than a claim-level one, because in practice RAG systems usually work with documents processed to be text chunks in a fixed size"

[^card-3]: 参见 [ragchecker-overall-metrics] 了解 overall 层面指标
