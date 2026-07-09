---
id: wikieval-dataset
title: WikiEval 数据集：RAG 评测指标的人工标注基准
status: accepted
card_type: dataset-description
tags:
- wikieval
- benchmark
- human-annotation
- rag-evaluation
- wikipedia
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ragas
evidence_basis: experimental_paper
justification: ../justification/wikieval-dataset.md
canonical_concept: wikieval-dataset
aliases:
- WikiEval
- wikieval
summary: WikiEval 是 RAGAS 论文构建的 RAG 评测基准数据集，包含 50 个 2022 年后事件的 Wikipedia 页面生成的 question-context-answer 三元组，由两位标注者在 Faithfulness / Answer Relevance / Context Relevance 三维度做 pairwise comparison 标注，inter-annotator
  agreement 为 95%/90%/95%。
related:
- ragas-framework-overview
- ragas-faithfulness-metric
---

WikiEval 是为验证 RAGAS 指标有效性而构建的评测数据集，聚焦 RAG 系统的三维度质量评估。[^src-1]

**构建流程**：
1. 选取 50 个 Wikipedia 页面，覆盖 2022 年后事件（超出实验模型训练截止），优先选择近期编辑的页面。[^src-2]
2. 用 ChatGPT 从 intro section 生成适中难度的问题（6 条规则约束 prompt）。[^src-3]
3. 用 ChatGPT 基于 context 生成答案。[^src-4]

**标注设计**：
- Faithfulness: 对比有/无 context 生成的答案，标注哪个更忠实。[^src-5]
- Answer Relevance: 对比完整答案与 LLM 生成的 incomplete answer。[^src-6]
- Context Relevance: 通过添加 back-link 句子增加冗余，对比原始/扩展 context。[^src-7]

两位标注者 inter-annotator agreement: Faithfulness ~95%, Answer Relevance ~90%, Context Relevance ~95%。分歧通过讨论解决。[^card-1][^src-8]

[^src-1]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "The WikiEval Dataset" P348 -- "we created a new dataset, which we refer to as WikiEval"
[^src-2]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "The WikiEval Dataset" P348 -- "selected 50 Wikipedia pages covering events that have happened since the start of 2022"
[^src-3]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "The WikiEval Dataset" P350-358 -- prompt with 6 rules for question generation
[^src-4]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "The WikiEval Dataset" P359-363 -- "Answer the question using the information from the given context"
[^src-5]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "The WikiEval Dataset / Faithfulness" P367 -- "used ChatGPT to answer the question without access to any additional context"
[^src-6]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "The WikiEval Dataset / Answer relevance" P370-371 -- "Answer the given question in an incomplete manner"
[^src-7]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "The WikiEval Dataset / Context relevance" P376 -- "added additional sentences to the context by scraping back-links"
[^src-8]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "The WikiEval Dataset" P365 -- "agreed in around 95% of cases... For answer relevance, they agreed in around 90%"
[^card-1]: 见 [ragas-framework-overview] 三维度定义背景
