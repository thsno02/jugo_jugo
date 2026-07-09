---
id: ares-ppi-statistical-calibration
title: ARES 的 PPI 统计校正机制
status: superseded
superseded_by: prediction-powered-inference-for-rag-ranking
card_type: mechanism
tags: [ppi, prediction-powered-inference, confidence-interval, statistical-calibration, gold-labels]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-stanford-ares]
evidence_basis: code_implementation
justification: ../justification/ares-ppi-statistical-calibration.md
canonical_concept: ares-ppi-statistical-calibration
aliases: [PPI, Prediction-Powered Inference, prediction-powered inference, gold_label_path]
summary: >-
  ARES 的 PPI（Prediction-Powered Inference）机制使用少量人工标注验证集（gold labels，≥50 条，理想数百条）校正微调分类器在大量未标注数据上的预测偏差，输出带统计置信区间的评估结果（如 Confidence Interval [0.547, 0.664]）。gold_label_path 参数指向人工标注集，PPI 综合考虑模型响应变异性提供统计置信度。
related: [ares-rag-evaluation-framework, ares-three-evaluation-dimensions]
---

Prediction-Powered Inference（PPI）是 ARES 框架的核心统计组件，解决的问题是：微调分类器在未标注数据上的预测存在系统性偏差，如何利用少量人工标注进行校正并量化不确定性。[^card-1]

PPI 的运作方式：(1) 用户提供一组人工标注的 query-document-answer 三元组作为 gold labels（通过 gold_label_path 参数指定），最少 50 条，数百条更佳；(2) PPI 利用这些标注数据估计分类器的预测偏差；(3) 对分类器在大量未标注数据上的分数进行校正；(4) 输出带置信区间的性能估计。[^src-1]

示例输出显示 PPI 结果包含 ARES Prediction（如 0.606）、Confidence Interval（如 [0.547, 0.664]）、Ground Truth Performance（如 0.6）以及 LLM Judge 在真实标签上的准确率（如 0.789）。使用 300 条标注样本即可完成校正。[^src-2]

[^card-1]: 参见 [ares-rag-evaluation-framework] 了解 PPI 在整体流程中的位置
[^src-1]: `data/raw/github_repo/repo-stanford-ares/repo/README.md` -- "Requirements" P1 -- "A human preference validation set of annotated query, document, and answer triples for the evaluation criteria... There should be at least 50 examples but several hundred examples is ideal."
[^src-2]: `data/raw/github_repo/repo-stanford-ares/repo/README.md` -- "Quick Start #2 Step 4" P1 -- "ARES Prediction: [0.6056978059262574] ARES Confidence Interval: [[0.547, 0.664]]... Annotated Examples used for PPI: 300"
