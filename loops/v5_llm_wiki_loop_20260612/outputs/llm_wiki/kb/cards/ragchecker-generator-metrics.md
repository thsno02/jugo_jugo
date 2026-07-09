---
id: ragchecker-generator-metrics
title: RAGChecker 生成器诊断指标体系
status: accepted
card_type: metric-definition
tags:
- rag-evaluation
- generator
- faithfulness
- hallucination
- noise-sensitivity
- self-knowledge
- context-utilization
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ragchecker
evidence_basis: experimental_paper
justification: ../justification/ragchecker-generator-metrics.md
canonical_concept: ragchecker-generator-metrics
aliases:
- generator metrics
- 生成器指标
- generator diagnostic metrics
summary: RAGChecker generator metrics 包含六个诊断指标：Faithfulness 为 response claims 被 retrieved chunks 蕴含的比例（越高越好）；Relevant Noise Sensitivity 为不正确但被 relevant chunk 蕴含的 claims 占比；Irrelevant Noise Sensitivity 为不正确但被
  irrelevant chunk 蕴含的 claims 占比；Hallucination 为不正确且不被任何 chunk 蕴含的 claims 占比；Self-knowledge 为正确但不被 chunks 蕴含的 claims 占比；Context Utilization 为已检索到且被 response 使用的 ground truth claims 占已检索 ground truth claims
  的比例。
related:
- ragchecker-framework-overview
- ragchecker-retriever-metrics
- claim-level-entailment-checking
- context-utilization-key-factor
- generator-model-size-improvement
- informative-context-reduces-hallucination
- more-context-enhances-faithfulness
- open-source-blind-trust-context
- prompt-affects-generation-preferences
- ragchecker-limitations
- retrieval-noise-sensitivity-tradeoff
---
RAGChecker 的 generator metrics 从六个维度诊断生成器行为：[^src-1]

**Faithfulness** = |{c^(m)_i | c^(m)_i ∈ {chunk_j}}| / |{c^(m)_i}|
描述生成器对提供上下文的忠实程度，越高越好。[^src-1]

**三类不正确 claims 的分类**：[^src-2]
- **Relevant Noise Sensitivity** = |{c^(m)_i | c^(m)_i ∉ gt AND c^(m)_i ∈ {r-chunk_j}}| / |{c^(m)_i}|
  生成器对相关 chunk 中噪声的敏感度
- **Irrelevant Noise Sensitivity** = |{c^(m)_i | c^(m)_i ∉ gt AND c^(m)_i ∈ {irr-chunk_j}}| / |{c^(m)_i}|
  生成器对无关 chunk 中噪声的敏感度
- **Hallucination** = |{c^(m)_i | c^(m)_i ∉ gt AND c^(m)_i ∉ {chunk_j}}| / |{c^(m)_i}|
  生成器自行产生的不正确 claims

**信息来源诊断**：[^src-3]
- **Self-knowledge** = |{c^(m)_i | c^(m)_i ∈ gt AND c^(m)_i ∉ {chunk_j}}| / |{c^(m)_i}|
  正确但非来自上下文的 claims 占比，越低越好
- **Context Utilization** = |{c^(gt)_i | c^(gt)_i ∈ {chunk_j} AND c^(gt)_i ∈ m}| / |{c^(gt)_i | c^(gt)_i ∈ {chunk_j}}|
  生成器对已检索到的相关信息的利用率，越高越好

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex Generator Metrics" -- "we first compute the proportion of c^(m)_i that are entailed in retrieved chunks. This metric is faithfulness"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex Generator Metrics" -- "The first type includes incorrect claim that are entailed in a relevant chunk...relevant noise sensitivity...The second type...irrelevant noise sensitivity...the third type...hallucination"
[^src-3]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex Generator Metrics" -- "A correct claim not entailed by any chunk can only be based on generator's self-knowledge...context utilization is computed as the ratio"

[^card-4]: 参见 [ragchecker-retriever-metrics] 了解 relevant/irrelevant chunk 的划分定义
