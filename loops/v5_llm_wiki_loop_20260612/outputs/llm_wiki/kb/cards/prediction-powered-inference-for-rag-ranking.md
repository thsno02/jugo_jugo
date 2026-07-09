---
id: prediction-powered-inference-for-rag-ranking
title: 预测驱动推断用于 RAG 排名
status: accepted
card_type: mechanism
tags:
- ppi
- prediction-powered-inference
- confidence-interval
- rag-evaluation
- statistical-method
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ares
evidence_basis: experimental_paper
justification: ../justification/prediction-powered-inference-for-rag-ranking.md
canonical_concept: prediction-powered-inference-for-rag-ranking
aliases:
- PPI
- prediction-powered inference
- 预测驱动推断
summary: ARES 使用 Prediction-Powered Inference (PPI) 结合少量人工标注（约 150-300 个 human preference
  validation set）和大量 LLM judge 预测，学习 rectifier function 校正模型偏差，构建比纯标注或纯模型预测更紧的 95%
  置信区间。PPI 在 judge 精度下降时（如跨域场景）仍能缓解排序退化，是 ARES 提供统计保证的关键。
related:
- ares-automated-rag-evaluation-system
- ares-human-preference-validation-set
- ares-ranking-accuracy-vs-baselines
- gpt4-labels-replacing-human-annotations
---

PPI (Prediction-Powered Inference) 是 ARES 第三阶段的核心统计方法，用于产出置信区间和可靠排名。[^src-1]

机制：PPI 用 LLM judge 在 human preference validation set 上学习 rectifier function，将 judge 在大量无标注数据上的预测校正为更准确的置信区间估计。结合少量人工标注（~150+）和大量模型预测，产出比纯标注方法更紧的区间。[^src-2]

实验使用 95% 置信水平。PPI 在所有测试数据集上均提升了 LLM judge 的排名准确度。[^src-3]

在跨域应用中，即使 LLM judge 精度下降，PPI 也能缓解排序退化，维持 ARES 的有效性。[^src-4]

最低人工标注需求约 150 个；低于 100 时 ARES 无法有效区分系统。400 个标注时效果进一步提升。[^src-5]

[^card-1]: [^ref→ares-automated-rag-evaluation-system] 三阶段流程之阶段 3
[^card-2]: [^ref→ares-llm-judge-finetuning] PPI 校正 judge 预测

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "methods.tex" P742-744 -- "ARES uses prediction-powered inference (PPI) to predict the system scores"
[^src-2]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "methods.tex" P756-758 -- "PPI uses the LLM judges on the human preference validation set to learn a rectifier function"
[^src-3]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P819 -- "for all datasets tested, PPI improved the ranking prediction accuracy"
[^src-4]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P895-896 -- "even when the LLM judge's accuracy suffered in cross-domain applications, PPI helped mitigate the loss"
[^src-5]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "Tables/ppi_comparison_table.tex" P197 -- "below about 100-150 datapoints...ARES cannot meaningfully distinguish"
