---
id: generator-model-size-improvement
title: 生成器模型规模带来全方位指标改善
status: accepted
card_type: experimental-finding
tags:
- model-size
- llama3-8b
- llama3-70b
- generator-capability
- scaling
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ragchecker
evidence_basis: experimental_paper
justification: ../justification/generator-model-size-improvement.md
canonical_concept: generator-model-size-improvement
aliases:
- Generator Model Size Brings All-Round Improvement
- 模型规模全面改善
summary: RAGChecker 实验表明 generator 模型规模的增大带来所有 generator metrics 的全面改善。在相同 retriever（E5-Mistral）下，Llama3-70B 相比 Llama3-8B：context utilization 57.6 vs 55.0，noise sensitivity(I) 31.7 vs 33.5，hallucination
  3.3 vs 6.6，faithfulness 95.9 vs 92.7，overall F1 50.2 vs 45.0。这一改善覆盖了上下文利用、噪声抗性和幻觉抑制所有方面。
related:
- ragchecker-generator-metrics
- context-utilization-key-factor
- open-source-blind-trust-context
---

RAGChecker 通过对比同族模型的不同规模（Llama3-8B vs Llama3-70B），在固定 retriever 条件下验证了模型规模对 generator 性能的影响。[^src-1]

**定量对比**（E5-Mistral retriever，10 域平均）：[^src-2]

| 指标 | Llama3-8B | Llama3-70B | 方向 |
|------|-----------|-----------|------|
| Context Utilization | 55.0 | 57.6 | 提升 |
| NS (Relevant) | 33.5 | 31.7 | 降低 |
| NS (Irrelevant) | 5.5 | 4.3 | 降低 |
| Hallucination | 6.6 | 3.3 | 降低 |
| Self-knowledge | 0.8 | 0.8 | 相当 |
| Faithfulness | 92.7 | 95.9 | 提升 |
| Overall F1 | 45.0 | 50.2 | 提升 |

模型规模的增大带来了上下文利用率提升、噪声敏感度降低和幻觉减少的全方位改善，而非仅在单一维度上的提升。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex Main Results" -- "Generator Model Size Brings All-Round Improvement. Paired to the same retriever, Llama3-70B consistently achieves better overall performance than Llama3-8B...improved context utilization, reduced noise sensitivity, and less hallucination"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "tables/ragchecker_results_avg.tex" -- E5-Mistral_Llama3-8b vs E5-Mistral_Llama3-70b rows

[^card-14]: 参见 [context-utilization-key-factor] 了解为何 CU 的提升对 F1 尤为重要
