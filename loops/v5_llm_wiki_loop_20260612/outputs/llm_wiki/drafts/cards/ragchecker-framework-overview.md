---
id: ragchecker-framework-overview
title: RAGChecker 细粒度 RAG 诊断评估框架
status: draft
card_type: framework-definition
tags: [rag-evaluation, fine-grained-metrics, claim-entailment, neurips-2024]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
evidence_basis: experimental_paper
justification: ../justification/ragchecker-framework-overview.md
canonical_concept: ragchecker-framework
aliases: [RAGChecker, RagChecker, ragchecker]
summary: >-
  RAGChecker 是基于 claim-level entailment checking 的 RAG 评估框架，将评估分解为 overall metrics（precision/recall/F1）、retriever metrics（claim recall/context precision）和 generator metrics（faithfulness/noise sensitivity/hallucination/self-knowledge/context utilization）三层诊断指标。该框架处理 user query、retrieved context、model response 和 ground truth answer 四项输入，通过 text-to-claim extractor 和 claim-entailment checker 两个组件实现细粒度评估。
related: []
---

RAGChecker 是一个面向 Retrieval-Augmented Generation 系统的细粒度评估框架，基于 claim-level entailment checking 实现对 RAG 系统的诊断式评估。[^src-1]

框架将 RAG 系统形式化为 RAG = {R, G}，其中 R 为 retriever，G 为 generator。给定 query q 和文档集 D，先检索 top-k 相关 context chunks，再由 generator 生成回答。[^src-2]

RAGChecker 的核心设计包含两个组件：(1) text-to-claim extractor 将文本分解为 claim 集合；(2) claim-entailment checker 判断 claim 是否被 reference text 蕴含。[^src-3]

框架输出三层指标：Overall Metrics 提供系统全局视角，Diagnostic Retriever Metrics 评估检索有效性，Diagnostic Generator Metrics 诊断生成器的上下文利用、噪声处理和忠实度。[^src-4]

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "Abstract" -- "we propose a fine-grained evaluation framework, RagChecker, that incorporates a suite of diagnostic metrics for both the retrieval and generation modules"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex Formulation" -- "Define a modular RAG system as RAG = {R, G}, where R is the retriever and G is the generator"
[^src-3]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex Fine-grained Evaluation with Claim Entailment" -- "we introduce two components: 1) a text-to-claim extractor that decomposes a given text T into a set of claims {c_i}, and 2) a claim-entailment checker"
[^src-4]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/introduction.tex" -- "Overall Metrics to provide a holistic view...Diagnostic Retriever Metrics to evaluate the effectiveness...Diagnostic Generator Metrics to assess the performance"
