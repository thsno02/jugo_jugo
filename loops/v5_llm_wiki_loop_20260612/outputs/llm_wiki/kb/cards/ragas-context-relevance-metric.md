---
id: ragas-context-relevance-metric
title: RAGAS Context Relevance 指标：句子提取比
status: accepted
card_type: metric-definition
tags:
- context-relevance
- sentence-extraction
- retrieval-quality
- rag-evaluation
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ragas
evidence_basis: experimental_paper
justification: ../justification/ragas-context-relevance-metric.md
canonical_concept: ragas-context-relevance
aliases:
- Context Relevance
- RAGAS context relevancy
- 上下文相关性指标
- CR
summary: RAGAS Context Relevance 通过 LLM 从 context 中提取回答问题所需的关键句子子集 S_ext， CR = |S_ext| / total_sentences_in_context。惩罚检索结果中的冗余信息。WikiEval 准确率 0.70， 是三维度中最难评测的——ChatGPT 在长 context 下提取关键句子时表现不稳定。
related:
- ragas-framework-overview
- ragas-faithfulness-metric
- ragas-answer-relevance-metric
- lost-in-the-middle-effect-on-rag
- ares-three-dimensional-rag-evaluation
---

Context Relevance 衡量检索到的上下文是否聚焦，即是否仅包含回答问题所需的信息，惩罚冗余内容。[^src-1]

**计算方法**：

1. 给定问题 q 和 context c(q)，prompt LLM 提取对回答问题至关重要的句子子集 S_ext（若无相关句则返回 "Insufficient Information"）。[^src-2]
2. CR = |S_ext| / total_sentences_in_c(q)。[^src-3]

**设计动机**：长 context 增加 LLM token 成本，且 LLM 对中间位置信息的利用效率下降（"lost in the middle" 现象）。[^card-1][^src-4]

在 WikiEval 上 CR 准确率 0.70，论文承认这是最难评测的维度——ChatGPT 在长 context 下提取关键句子时常出错。[^src-5]

[^src-1]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Context relevance" P320 -- "considered relevant to the extent that it exclusively contains information that is needed to answer the question"
[^src-2]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Context relevance" P321-325 -- "extract relevant sentences from the provided context that can potentially help answer the following question"
[^src-3]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Context relevance" P327-329 -- "CR = number of extracted sentences / total number of sentences in c(q)"
[^src-4]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Context relevance" P267 -- "LLMs are often less effective in exploiting that context, especially for information that is provided in the middle"
[^src-5]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Experiments" P418-419 -- "We found context relevance to be the hardest quality dimension to evaluate"
[^card-1]: 见 [lost-in-the-middle-effect-on-rag] 关于长 context 问题的描述
