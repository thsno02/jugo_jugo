---
id: ragchecker-claim-level-rag-evaluation-framework
title: RAGChecker 基于 claim-level entailment 的 RAG 评估框架
status: superseded
superseded_by: ragchecker-framework-overview
card_type: framework-overview
tags: [rag-evaluation, claim-level-entailment, diagnostic-metrics, retriever, generator]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-amazon-ragchecker]
evidence_basis: code_implementation
justification: ../justification/ragchecker-claim-level-rag-evaluation-framework.md
canonical_concept: ragchecker-claim-level-rag-evaluation-framework
aliases: [RAGChecker, ragchecker, RAGChecker framework, Fine-grained Framework For Diagnosing RAG]
summary: >-
  RAGChecker 是 Amazon Science 开发的自动 RAG 评估诊断框架，核心方法论为
  claim-level entailment：将回答分解为原子 claims 后通过 entailment 判断其与
  ground truth 及 retrieved context 的关系。提供三层 metrics 体系——overall
  (precision/recall/f1)、retriever diagnostics (claim_recall/context_precision)、
  generator diagnostics (context_utilization/noise_sensitivity/hallucination/
  self_knowledge/faithfulness)。发表于 NeurIPS 2024 Dataset and Benchmark Track。
related: []
---

RAGChecker 是一个细粒度 RAG 系统自动评估与诊断框架，其核心技术路线为 claim-level entailment 操作：先用 extractor（LLM）将文本分解为原子 claims，再用 checker（LLM）判断各 claim 与参考文本之间的蕴含关系。[^src-1]

框架提供三层 metrics 体系用于全面诊断 RAG pipeline：[^src-2]

1. **Overall Metrics**: precision / recall / f1 — 对整个 RAG pipeline 的端到端评估
2. **Retriever Diagnostic Metrics**: claim_recall / context_precision — 诊断检索组件质量
3. **Generator Diagnostic Metrics**: context_utilization / noise_sensitivity_in_relevant / noise_sensitivity_in_irrelevant / hallucination / self_knowledge / faithfulness — 诊断生成组件质量

该框架通过将评估粒度从答案级别细化到 claim 级别，使开发者能精确定位 RAG 系统的薄弱环节（检索不足 vs 生成幻觉 vs 噪声敏感等），实现针对性优化。[^src-3]

[^src-1]: `data/raw/github_repo/repo-amazon-ragchecker/repo/README.md` -- "Highlighted Features" P1 -- "Fine-grained Evaluation: Utilizes claim-level entailment operations for fine-grained evaluation."
[^src-2]: `data/raw/github_repo/repo-amazon-ragchecker/repo/README.md` -- "Highlighted Features" P1 -- "Holistic Evaluation: RAGChecker offers Overall Metrics... Diagnostic Retriever Metrics... Diagnostic Generator Metrics..."
[^src-3]: `data/raw/github_repo/repo-amazon-ragchecker/repo/README.md` -- "RAGChecker: A Fine-grained Framework For Diagnosing RAG" P1 -- "RAGChecker empowers developers and researchers to thoroughly evaluate, diagnose, and enhance their RAG systems with precision and depth."
