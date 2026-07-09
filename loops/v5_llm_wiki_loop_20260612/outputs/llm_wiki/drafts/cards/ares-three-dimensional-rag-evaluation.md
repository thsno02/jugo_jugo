---
id: ares-three-dimensional-rag-evaluation
title: RAG 三维评估指标体系
status: draft
card_type: concept-definition
tags: [context-relevance, answer-faithfulness, answer-relevance, rag-evaluation, evaluation-metrics]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ares]
evidence_basis: experimental_paper
justification: ../justification/ares-three-dimensional-rag-evaluation.md
canonical_concept: ares-three-dimensional-rag-evaluation
aliases: [context relevance, answer faithfulness, answer relevance, C.R., A.F., A.R., RAG evaluation criteria]
summary: >-
  ARES 定义 RAG 系统三维评估：context relevance（检索段落是否与 query 相关）、answer faithfulness（生成答案是否忠实于检索段落、无幻觉/外推）、answer relevance（答案是否与 query+段落相关）。每个维度由独立的二分类 judge 评估 query-passage-answer 三元组。此三维分解使开发者能定位 RAG 管线中具体瓶颈组件。
related: []
---

ARES 将 RAG 评估分解为三个独立维度，每个维度由专门的 LLM judge 评估：[^src-1]

1. **Context Relevance** -- 检索返回的段落是否与给定 query 相关？评估检索器质量。
2. **Answer Faithfulness** -- 生成的答案是否忠实于检索段落？是否包含幻觉或超出段落的外推陈述？评估生成器的接地能力。
3. **Answer Relevance** -- 给定 query 和检索段落，生成的答案是否相关？评估端到端回答质量。

此三维分解允许开发者分别评估 RAG 管线各组件，创建针对性解决方案。[^src-2]

每个 judge 对连接后的 query-document-answer 三元组做正/负二分类。[^src-3]

[^card-1]: [^ref→ares-llm-judge-finetuning] 三个 judge 的微调

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "methods.tex" P730-734 -- "Context Relevance...Answer Faithfulness...Answer Relevance"
[^src-2]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "introduction.tex" P626 -- "ARES reports three evaluation scores...A good RAG system finds relevant contexts and generates answers that are both faithful and relevant"
[^src-3]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "methods.tex" P737 -- "For each concatenated query-document-answer, a single LLM judge must classify the triple"
