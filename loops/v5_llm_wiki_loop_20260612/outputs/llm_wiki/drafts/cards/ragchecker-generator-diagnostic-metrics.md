---
id: ragchecker-generator-diagnostic-metrics
title: RAGChecker 生成器诊断指标体系
status: superseded
superseded_by: ragchecker-generator-metrics
card_type: metric-set
tags: [rag-evaluation, generator-metrics, hallucination, faithfulness, noise-sensitivity]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-amazon-ragchecker]
evidence_basis: code_implementation
justification: ../justification/ragchecker-generator-diagnostic-metrics.md
canonical_concept: ragchecker-generator-diagnostic-metrics
aliases: [RAGChecker generator metrics, generator diagnostic metrics, 生成器诊断指标]
summary: >-
  RAGChecker generator diagnostic metrics 包含六个指标：context_utilization
  衡量上下文利用率，noise_sensitivity_in_relevant 和 noise_sensitivity_in_irrelevant
  分别衡量对相关/无关噪声的敏感度，hallucination 衡量凭空生成比例，
  self_knowledge 衡量模型依赖自身知识的程度，faithfulness 衡量对检索上下文的
  忠实度。这些指标共同诊断 RAG 生成组件的多维质量问题。
related: [ragchecker-claim-level-rag-evaluation-framework]
---

RAGChecker 的 Generator Diagnostic Metrics 提供六个维度的生成器质量诊断：[^src-1] [^card-1]

- **context_utilization**: 生成器对检索上下文的利用率（示例值 87.5%）
- **noise_sensitivity_in_relevant**: 对相关文档中噪声信息的敏感度（示例值 22.5%/19.1%）
- **noise_sensitivity_in_irrelevant**: 对无关文档中噪声信息的敏感度（示例值 0.0%）
- **hallucination**: 生成器凭空产生内容的比例（示例值 4.2%/4.5%）
- **self_knowledge**: 生成器依赖自身参数知识而非检索上下文的程度（示例值 25.0%/27.3%）
- **faithfulness**: 生成内容对检索上下文的忠实度（示例值 70.8%/68.2%）

noise_sensitivity 区分 relevant 和 irrelevant context 来源，这一设计暗示框架认为噪声在相关文档和无关文档中的影响机制不同，需分别诊断。hallucination 与 self_knowledge 的区分似乎表明：self_knowledge 是生成器使用自身知识的中性度量，而 hallucination 是生成与 ground truth 矛盾内容的负面度量。[^src-2]

[^src-1]: `data/raw/github_repo/repo-amazon-ragchecker/repo/README.md` -- "Run the Checking Pipeline with CLI" P1 -- "generator_metrics: { context_utilization: 87.5, noise_sensitivity_in_relevant: 22.5, noise_sensitivity_in_irrelevant: 0.0, hallucination: 4.2, self_knowledge: 25.0, faithfulness: 70.8 }"
[^src-2]: `data/raw/github_repo/repo-amazon-ragchecker/repo/README.md` -- "Run the Checking Pipeline with Python" P1 -- "generator_metrics: { context_utilization: 87.5, noise_sensitivity_in_relevant: 19.1, noise_sensitivity_in_irrelevant: 0.0, hallucination: 4.5, self_knowledge: 27.3, faithfulness: 68.2 }"
[^card-1]: ragchecker-claim-level-rag-evaluation-framework
