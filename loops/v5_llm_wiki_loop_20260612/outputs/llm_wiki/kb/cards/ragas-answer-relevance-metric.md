---
id: ragas-answer-relevance-metric
title: RAGAS Answer Relevance 指标：逆向问题生成
status: accepted
card_type: metric-definition
tags:
- answer-relevance
- reverse-question-generation
- embedding-similarity
- rag-evaluation
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ragas
evidence_basis: experimental_paper
justification: ../justification/ragas-answer-relevance-metric.md
canonical_concept: ragas-answer-relevance
aliases:
- Answer Relevance
- RAGAS answer relevancy
- 答案相关性指标
- AR
summary: RAGAS Answer Relevance 通过逆向问题生成 (reverse question generation) 计算：从答案生成 n 个潜在问题 q_i， 用 text-embedding-ada-002 取 embedding 后与原问题 q 计算 cosine similarity，AR = (1/n) * sum(sim(q, q_i))。 不评估事实性，惩罚不完整或含冗余信息的回答。WikiEval
  准确率 0.78。
related:
- ragas-framework-overview
- ragas-faithfulness-metric
- ragas-context-relevance-metric
- ares-three-dimensional-rag-evaluation
---

Answer Relevance 衡量生成答案是否直接回应了用户问题，不涉及事实性判断，但惩罚不完整或包含冗余信息的答案。[^src-1]

**计算方法**：

1. 给定答案 a_s(q)，prompt LLM "Generate a question for the given answer" 生成 n 个潜在问题 q_i。[^src-2]
2. 用 text-embedding-ada-002 模型对所有 q_i 和原始问题 q 取 embedding。[^src-3]
3. 计算 AR = (1/n) * sum_{i=1}^{n} sim(q, q_i)，其中 sim 为 cosine similarity。[^src-4]

**直觉**：如果答案充分回应了问题，那么从答案反向生成的问题应当与原始问题高度相似；如果答案不完整或冗余，逆向生成的问题将偏离原问题。[^card-1]

在 WikiEval 上 AR 与人工判断一致率为 0.78，论文指出这是因为候选答案间差异常非常微妙。[^src-5]

[^src-1]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Answer relevance" P298 -- "relevant if it directly addresses the question... does not take into account factuality"
[^src-2]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Answer relevance" P300-303 -- "Generate a question for the given answer"
[^src-3]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Answer relevance" P304 -- "obtain embeddings for all questions using the text-embedding-ada-002 model"
[^src-4]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Answer relevance" P307-309 -- "AR = 1/n sum sim(q, q_i)"
[^src-5]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Experiments" P418 -- "For answer relevance, the agreement is lower... differences between the two candidate answers are often very subtle"
[^card-1]: 见 [ragas-framework-overview] 三维度总述
