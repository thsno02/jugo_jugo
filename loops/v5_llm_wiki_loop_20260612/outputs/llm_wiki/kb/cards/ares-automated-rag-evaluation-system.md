---
id: ares-automated-rag-evaluation-system
title: ARES 自动化 RAG 评估系统
status: accepted
card_type: framework-overview
tags:
- rag-evaluation
- automated-evaluation
- llm-judge
- ppi
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ares
evidence_basis: experimental_paper
justification: ../justification/ares-automated-rag-evaluation-system.md
canonical_concept: ares-automated-rag-evaluation-system
aliases:
- ARES
- Automated RAG Evaluation System
summary: ARES (Automated RAG Evaluation System) 是首个为 RAG 管线各组件生成定制化 LLM judge 的自动化评估框架。通过三阶段流程——合成数据生成、轻量
  LLM judge 微调、PPI 置信区间排序——仅需约 150 人工标注即可准确评估 RAG 系统的 context relevance、answer faithfulness、answer
  relevance。来自 Stanford/Databricks，代码开源于 GitHub。
related:
- ares-three-dimensional-rag-evaluation
- prediction-powered-inference-for-rag-ranking
- ares-synthetic-data-generation
---

ARES 是一个自动化 RAG 评估系统，解决传统 RAG 评估依赖大量人工标注的问题。[^src-1]

系统接受三个输入：领域内段落集、约 150 个人工标注的 human preference validation set、5+ 个 few-shot 示例（用于 LLM 合成数据生成的 prompt）。[^src-2]

ARES 通过三阶段流程运作：(1) LLM 生成合成 query-answer 对，(2) 微调轻量 LLM judge 做三维评估分类，(3) 用 PPI 产出置信区间和系统排名。[^src-3]

在 KILT、SuperGLUE、AIS 共八个知识密集型任务上，ARES 准确评估 RAG 系统，同时仅使用数百个人工标注。[^src-4]

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "introduction.tex" P621 -- "we propose ARES, the Automated RAG Evaluation System"
[^src-2]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "methods.tex" P690-694 -- "three required inputs: an in-domain passage set, a human preference validation set of approximately 150 annotated datapoints (or more), and few-shot examples"
[^src-3]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "methods.tex" P690-696 -- "ARES proceeds in three stages"
[^src-4]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "abstract.tex" P207-213 -- "Across eight different knowledge-intensive tasks in KILT, SuperGLUE, and AIS, ARES accurately evaluates RAG systems"
