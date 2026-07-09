---
id: nli-based-citation-quality-metrics
title: 基于 NLI 的引用质量评测指标
status: accepted
card_type: evaluation-metric
tags:
- NLI
- citation-recall
- citation-precision
- TRUE-model
- entailment
- AIS
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-alce
evidence_basis: experimental_paper
justification: ../justification/nli-based-citation-quality-metrics.md
canonical_concept: nli-based-citation-quality
aliases:
- citation recall
- citation precision
- NLI citation evaluation
- AIS score
- attributable to identified sources
summary: ALCE 使用 NLI 模型 TRUE (T5-11B fine-tuned on NLI datasets) 自动评估引用质量 (nli-based-citation-quality)。Citation recall 定义为：语句 s_i 的 recall=1 当且仅当其引用集 C_i 非空且 phi(concat(C_i), s_i)=1（NLI 蕴含）。Citation precision
  定义为：引用 c_{i,j} 为 irrelevant 当且仅当 (a) phi(c_{i,j}, s_i)=0 且 (b) phi(concat(C_i\{c_{i,j}}), s_i)=1。该指标与人类判断高度相关：Cohen's kappa 0.698(recall)/0.525(precision)，准确率 85.1%/77.6%。局限是无法检测 partial support 导致 precision
  偏低。
related:
- alce-three-dimensional-evaluation
- alce-citation-support-gap
- claim-recall-eli5-evaluation
---
ALCE 引用质量评测使用 NLI 模型 TRUE（基于 T5-11B，在 SNLI/MNLI/Fever/Scitail/PAWS/VitaminC 上微调），自动判断引用段落是否蕴含生成语句。[^src-1]

Citation recall 的形式定义：对每个语句 s_i，recall=1 当且仅当 C_i 非空且 phi(concat(C_i), s_i)=1。该评测符合 AIS (Attributable to Identified Sources) 框架。[^src-2]

Citation precision 检测无关引用但不要求引用最小集。c_{i,j} 为 irrelevant 当且仅当 (a) phi(c_{i,j}, s_i)=0 且 (b) 移除 c_{i,j} 后剩余引用仍能蕴含 s_i。以 recall=1 为 precision=1 的前提条件。[^src-3]

人类评估验证了自动指标的有效性：citation recall 的 Cohen's kappa 为 0.698（substantial agreement），citation precision 为 0.525（moderate agreement）。自动评测准确率分别为 85.1% 和 77.6%。[^src-4]

已知局限：NLI 模型无法区分 partial support，导致精确率评估存在假阳性（将部分支持的引用误判为 irrelevant）。[^src-5]

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Implementation Details" -- "We use the version of TRUE model...which is trained on SNLI, MNLI, Fever, Scitail, PAWS, and VitaminC"
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Citation recall" -- "its citation recall is 1 if and only if there is at least one citation and phi(concat(C_i), s_i)=1...in accordance with the attributable to identified sources (AIS) framework"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Citation precision" -- "c_{i,j} is irrelevant if and only if (a) phi(c_{i,j},s_i)=0, AND (b) phi(concat(C_i\{c_{i,j}}), s_i)=1"
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Human Evaluation" -- "Cohen's kappa coefficient...suggests substantial agreement for citation recall (0.698) and moderate agreement for citation precision (0.525)...85.1% for citation recall and 77.6% for citation precision"
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Citation Recall Discussion" -- "this algorithm overlooks the scenario when one citation partially supports the statement"

[^card-1]: alce-three-dimensional-evaluation
