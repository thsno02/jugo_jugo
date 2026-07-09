---
id: ragas-framework-overview
title: RAGAS 无参考答案 RAG 评测框架
status: draft
card_type: framework-overview
tags: [rag-evaluation, reference-free, automated-metrics, llm-as-judge]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragas]
evidence_basis: experimental_paper
justification: ../justification/ragas-framework-overview.md
canonical_concept: ragas-framework
aliases: [RAGAS, Retrieval Augmented Generation Assessment, ragas]
summary: >-
  RAGAS (Retrieval Augmented Generation Assessment) 是一个 reference-free 的 RAG pipeline 自动评测框架，
  提出三维度指标 Faithfulness / Answer Relevance / Context Relevance，通过 LLM prompting 实现无需 ground truth
  的评测；在 WikiEval 数据集上与人工判断一致性优于 GPT Score 和 GPT Ranking 基线。
related: [ragas-faithfulness-metric, ragas-answer-relevance-metric, ragas-context-relevance-metric, wikieval-dataset]
---

RAGAS (Retrieval Augmented Generation Assessment) 是面向 RAG pipeline 的自动化评测框架，核心设计目标为 **reference-free**——无需人工标注的 ground truth 或参考答案即可评估 RAG 系统质量。[^src-1]

框架覆盖三个正交维度：Faithfulness（答案是否有 context 根据）、Answer Relevance（答案是否回应问题）、Context Relevance（检索结果是否聚焦）。三指标均通过 LLM prompting 实现，不依赖 token probability 或模型内部权重，适用于仅通过 API 访问的 closed-model (如 ChatGPT/GPT-4)。[^src-2]

RAGAS 集成 llama-index 与 LangChain，可直接嵌入开发者工作流。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Abstract" P234 -- "a framework for reference-free evaluation of Retrieval Augmented Generation (RAG) pipelines"
[^src-2]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies" P266-269 -- "We therefore focus on metrics that are fully self-contained and reference-free"
[^src-3]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Introduction" P245 -- "provides an integration with both llama-index and Langchain"
