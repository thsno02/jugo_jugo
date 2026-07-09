---
id: graphrag-claim-based-validation
title: GraphRAG 基于 Claim 的定量验证
status: accepted
card_type: empirical-finding
tags:
- graphrag
- evaluation
- claims
- claimify
- clustering
- rouge-l
- validation
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-graphrag
evidence_basis: experimental_paper
justification: ../justification/graphrag-claim-based-validation.md
canonical_concept: graphrag-claim-based-validation
aliases:
- claim-based validation
- Claimify evaluation
- GraphRAG Experiment 2
- claim diversity metric
summary: GraphRAG graphrag-claim-based-validation Experiment 2 使用 Claimify 从各条件回答中抽取 factual claims（47075 条，均值 31/answer）进行定量验证。Comprehensiveness 用 claim 数量衡量，diversity 用 agglomerative clustering（complete
  linkage, 距离 1-ROUGE-L）在多阈值下的 cluster 数衡量。结果：所有全局条件 claim 数显著高于 SS (p<.05)；LLM judge 与 claim-based 标签在非平局情况对齐 78% comprehensiveness 69-70% diversity。
related:
- graphrag-adaptive-benchmarking
- graphrag-community-hierarchy-cost-performance
---

Experiment 2 独立于 LLM-as-judge 评估，使用 claim-based 定量指标验证 Experiment 1 的结论。

**Claim 抽取**: 使用 Claimify (Metropolitansky & Larson, 2025) 从各条件的回答中抽取 factual claims——"a statement that explicitly presents some verifiable facts"。去重后获得 47,075 条 claim，均值 31 claims/answer。

**指标定义**:
- **Comprehensiveness**: 直接用抽取的 claim 数量
- **Diversity**: 对各答案的 claims 进行 agglomerative clustering（complete linkage, 距离 = 1 - ROUGE-L），报告不同 distance threshold (0.5-0.8) 下的 cluster 数

**关键结果**:
- Comprehensiveness: 所有全局条件 (C0-C3, TS) 的 claim 数显著高于 SS (p<.05)
- Diversity: Podcast 数据集所有全局条件在所有阈值显著高于 SS；News 数据集 C0 在所有阈值显著，C1-C3 仅在部分阈值显著
- 全局条件之间及与 TS 之间无显著差异

**与 LLM Judge 的对齐**:
- 聚焦非平局情况（comprehensiveness 33%, diversity 39% 的对比）
- Claim-based 标签与 LLM judge 标签对齐 78%（comprehensiveness）和 69-70%（diversity），表明中等偏强的一致性

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Experiment 2" (Section 3.2) -- "we use the definition of a factual claim from Ni et al....a statement that explicitly presents some verifiable facts"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Results Experiment 2" (Section 4.2) -- "the aggregated LLM label matched the claim-based label in 78% of pairwise comparisons for comprehensiveness and 69-70% for diversity"
[^card-1]: [graphrag-adaptive-benchmarking] 此方法验证 Experiment 1 中 LLM-as-judge 结果
