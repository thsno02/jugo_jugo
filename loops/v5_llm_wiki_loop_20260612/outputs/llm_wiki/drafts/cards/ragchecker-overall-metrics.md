---
id: ragchecker-overall-metrics
title: RAGChecker 总体指标 Precision/Recall/F1
status: draft
card_type: metric-definition
tags: [rag-evaluation, precision, recall, f1, claim-level]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
evidence_basis: experimental_paper
justification: ../justification/ragchecker-overall-metrics.md
canonical_concept: ragchecker-overall-metrics
aliases: [RAGChecker overall metrics, claim-level precision, claim-level recall, RAG F1]
summary: >-
  RAGChecker overall metrics 在 claim 级别计算 precision 和 recall。Precision = |{c^(m)_i | c^(m)_i ∈ gt}| / |{c^(m)_i}|，即 response claims 中被 ground truth 蕴含的比例。Recall = |{c^(gt)_i | c^(gt)_i ∈ m}| / |{c^(gt)_i}|，即 ground truth claims 中被 response 蕴含的比例。F1 为二者调和平均。这组指标面向 RAG 用户提供单一数值排名能力。
related: [ragchecker-framework-overview, claim-level-entailment-checking]
---

RAGChecker 的 overall metrics 面向 RAG 用户设计，提供可直接用于系统排名的单一数值指标。[^src-1]

**Precision** = |{c^(m)_i | c^(m)_i ∈ gt}| / |{c^(m)_i}|

即 model response 的所有 claims 中，被 ground truth answer 蕴含（正确）的 claims 占比。[^src-2]

**Recall** = |{c^(gt)_i | c^(gt)_i ∈ m}| / |{c^(gt)_i}|

即 ground truth answer 的所有 claims 中，被 model response 蕴含（已覆盖）的 claims 占比。[^src-2]

**F1** 为 precision 和 recall 的调和平均值，作为系统综合性能的 overall performance metric。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex RAGChecker Metrics" -- "For a RAG user, we design metrics to compare the performance among RAG systems, including a single-value F1 score as an overall metric"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex Overall Metrics" -- "precision is the proportion of correct claims in all response claims, and recall is the proportion of correct claims in all ground-truth answer claims. Further, the harmonic average of precision and recall gives the F1 score"

[^card-2]: 参见 [claim-level-entailment-checking] 了解 claim extraction 和 entailment 判定的具体操作
