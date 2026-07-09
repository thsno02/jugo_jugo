---
id: informative-context-reduces-hallucination
title: 信息丰富的上下文降低幻觉并提升忠实度
status: draft
card_type: experimental-finding
tags: [hallucination, faithfulness, self-knowledge, retriever-quality, informative-context]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
evidence_basis: experimental_paper
justification: ../justification/informative-context-reduces-hallucination.md
canonical_concept: informative-context-reduces-hallucination
aliases: [Informative Context Improves Faithfulness, 信息丰富上下文降低幻觉]
summary: >-
  RAGChecker 实验表明当 retriever 提供更多信息量（E5-Mistral 的更高 claim recall）时，所有 generator 的 faithfulness 提升、hallucination 和 self-knowledge 均降低。GPT-4: faithfulness 87.9→92.9，hallucination 8.7→5.7，self-knowledge 3.4→1.4（BM25→E5-Mistral）。这表明 generator 有能力识别并利用上下文中的信息，当有更多可用信息时会减少对内部知识的依赖。
related: [ragchecker-generator-metrics, retriever-quality-consistent-impact, retrieval-noise-sensitivity-tradeoff]
---

RAGChecker 实验发现检索结果的信息丰富度（以 claim recall 衡量）直接影响 generator 的幻觉和忠实度表现。[^src-1]

**定量证据**（BM25 → E5-Mistral，10 域平均）：[^src-2]

| Generator | Faithfulness | Hallucination | Self-knowledge |
|-----------|-------------|---------------|----------------|
| GPT-4 | 87.9 → 92.9 | 8.7 → 5.7 | 3.4 → 1.4 |
| Llama3-70B | 93.2 → 95.9 | 5.1 → 3.3 | 1.7 → 0.8 |
| Llama3-8B | 88.4 → 92.7 | 9.8 → 6.6 | 1.8 → 0.8 |
| Mixtral-8x7B | 92.0 → 95.2 | 6.2 → 4.0 | 1.8 → 0.8 |

当 retriever 提供更完整的相关信息（claim recall 74.0 → 83.5）时：[^src-1]
- Generator 的 faithfulness 提升——它们能够识别并利用上下文中的信息
- Hallucination 降低——更少需要自行编造信息
- Self-knowledge 降低——更少依赖内部知识（因为相关知识已在上下文中可得）

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex Main Results" -- "Informative Context Improves Faithfulness and Reduces Hallucination. As E5-Mistral achieves better claim recall, we observe generators paired to it achieves better faithfulness...Similarly, hallucination and self-knowledge are both reduced"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "tables/ragchecker_results_avg.tex" -- comparing BM25_* vs E5-Mistral_* rows

[^card-15]: 参见 [retrieval-noise-sensitivity-tradeoff] 了解该改善的副作用（noise sensitivity 上升）
