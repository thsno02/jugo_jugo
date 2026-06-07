---
id: comparison-rag-eval-reference-dependency
title: 无参考 vs 有参考 RAG 评估：完整性度量的代价
status: accepted
card_type: distinction
tags: [rag, evaluation, reference-free, ground-truth, completeness, trade-off]
created_time: 2026-06-05T18:00:00+08:00
edited_time: 2026-06-05T18:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragas, arxiv-ragchecker, arxiv-ares]
justification: ../justification/comparison-rag-eval-reference-dependency.md
canonical_concept: comparison-rag-eval-reference-dependency
aliases: [RAG评估参考依赖取舍, reference-free vs reference-required RAG evaluation]
summary: >-
  comparison-rag-eval-reference-dependency（RAG评估参考依赖取舍）三大 RAG 评估框架在对 ground truth 的依赖程度上形成光谱：RAGAS 完全无参考、ARES 少量参考（PPI 校准）、RAGChecker 全量参考（claim recall）；无参考方法可快速迭代但无法衡量完整性（recall），有参考方法诊断更精准但需标注成本
related: [ares-rag-evaluation-framework, ragas-reference-free-rag-evaluation, ragchecker-three-tier-metrics]
---

RAG 评估框架在对 ground truth 答案的依赖程度上存在一条根本性设计光谱，三个代表性框架分别占据不同位置：

**无参考端：RAGAS**。RAGAS 明确以"无参考评估"为核心设计原则，所有指标的计算"不需要依赖 ground truth 人工标注"[^card-1][^src-1]。这使得 RAGAS 可以在无标注数据的场景下快速部署，加速 RAG 架构的评估迭代周期。但无参考设计的代价是：当不存在标准答案时，无法衡量回答的**完整性（recall/completeness）**——即回答是否覆盖了用户问题应有的全部关键信息。

**少参考中间态：ARES**。ARES 通过合成数据微调 LM 评审模型，再用少量人工标注（数百条）进行 PPI 校准[^card-2][^src-2]。这一设计在标注成本与评估可靠性之间取得了折中：PPI 校准提供了统计意义上的置信区间，且评审模型在领域迁移场景下仍保持有效性。但 ARES 的"少参考"本质上仍是用于校准评审模型，而非直接衡量回答完整性。

**全参考端：RAGChecker**。RAGChecker 的核心指标（如 claim recall：标准答案声明中被检索块覆盖的比例；overall recall：标准答案声明中被回答覆盖的比例）本质上依赖 ground truth 答案[^card-3][^src-3]。正是因为拥有标准答案作为参照，RAGChecker 才能将评估深入到声明级别的完整性度量。元评估结果佐证了这一选择：RAGChecker 在 completeness 维度的 Pearson 相关性（60.67）显著优于 RAGAS Answer Similarity（53.16）。

这一光谱揭示了 RAG 评估中一个不可调和的张力：**completeness 度量本质上需要参照物**。衡量"回答遗漏了什么"逻辑上预设了"应该包含什么"的知识——即 ground truth。无参考方法可以衡量 faithfulness（回答是否基于上下文）和 context relevance（检索是否相关），但无法回答"回答够不够完整"这一问题。三个框架的设计取舍因此映射到不同的使用场景：RAGAS 适用于快速原型迭代；ARES 适用于需要统计校准的生产评估；RAGChecker 适用于需要精细诊断的系统优化。

## Footnotes

[^card-1]: [RAGAS 无参考评估框架](ragas-reference-free-rag-evaluation.md) -- 无参考评估的代表，完全消除对 ground truth 的依赖
[^card-2]: [ARES 自动化 RAG 评估框架](ares-rag-evaluation-framework.md) -- 少参考评估的代表，通过合成数据+PPI 仅需数百条人工标注
[^card-3]: [RAGChecker 三层诊断指标体系](ragchecker-three-tier-metrics.md) -- 有参考评估的代表，claim recall 等指标依赖 ground truth 答案
[^src-1]: arxiv-ragas (Es et al. 2023) -- "a framework for reference-free evaluation of Retrieval Augmented Generation (RAG) pipelines... a suite of metrics which can be used to evaluate these different dimensions without having to rely on ground truth human annotations."
[^src-2]: arxiv-ares (Saad-Falcon et al. 2023) -- "ARES utilizes a small set of human-annotated datapoints for prediction-powered inference (PPI)... accurately evaluates RAG systems while using only a few hundred human annotations during evaluation."
[^src-3]: arxiv-ragchecker (Ru et al. 2024) -- "Meta evaluation verifies that RAGChecker has significantly better correlations with human judgments than other evaluation metrics." RAGChecker 的 Completeness Pearson 相关性 60.67 显著优于 RAGAS Answer Similarity 的 53.16。
