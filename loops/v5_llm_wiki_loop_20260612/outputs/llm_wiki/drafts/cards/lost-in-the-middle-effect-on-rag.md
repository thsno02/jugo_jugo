---
id: lost-in-the-middle-effect-on-rag
title: Lost in the Middle 效应对 RAG Context 设计的影响
status: draft
card_type: empirical-finding
tags: [lost-in-the-middle, long-context, context-relevance, retrieval-design, attention-bias]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragas]
evidence_basis: experimental_paper
justification: ../justification/lost-in-the-middle-effect-on-rag.md
canonical_concept: lost-in-the-middle-rag-impact
aliases: [lost in the middle, 中间信息丢失, position bias in long context]
summary: >-
  LLM 在长 context 中对中间位置信息的利用效率下降（"lost in the middle" 现象），
  这为 RAG 系统的 Context Relevance 评测提供了实践动机：检索结果应尽量精简聚焦，
  避免长冗余 context 导致关键信息被 LLM 忽略。RAGAS 据此将 Context Relevance 作为核心维度之一。
related: [ragas-context-relevance-metric, ragas-framework-overview]
---

Liu et al. (2023) 发现 LLM 在处理长 context 时，对中间位置信息的利用效率显著下降——头尾位置的信息被更好地利用，而中间部分容易被忽略（"lost in the middle" 现象）。[^src-1]

RAGAS 论文引用该发现作为 Context Relevance 维度的实践动机：当 context 段落过长时，LLM 不仅增加 token 成本，还可能因位置偏差而无法有效利用关键信息。因此 RAG 系统的检索结果应尽量精简聚焦。[^card-1][^src-2]

这一观察强化了 "retrieval quality 不仅是 recall 问题，也是 precision 问题" 的观点——检索到相关但冗余的 context 可能反而损害生成质量。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies" P267 -- "LLMs are often less effective in exploiting that context, especially for information that is provided in the middle of the context passage (Liu et al. 2023)"
[^src-2]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Context relevance" P267 -- "This is important given the cost associated with feeding long context passages to LLMs"
[^src-3]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Context relevance" P320 -- "aims to penalise the inclusion of redundant information"
[^card-1]: 见 [ragas-context-relevance-metric] CR 指标的具体计算方法
