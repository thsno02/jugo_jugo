---
id: rag-evaluation-tri-dimension
title: RAG 评估三维度分解
status: accepted
card_type: distinction
tags: [rag, evaluation, retrieval-quality, faithfulness, generation-quality, evaluation-dimensions]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragas]
justification: ../justification/rag-evaluation-tri-dimension.md
canonical_concept: rag-evaluation-tri-dimension
aliases: [RAG评估三维度, RAG evaluation dimensions, 检索-忠实性-生成质量三维度]
summary: >-
  rag-evaluation-tri-dimension（RAG评估三维度 / RAG evaluation dimensions / 检索-忠实性-生成质量三维度）RAGAS 将 RAG 管道评估分解为三个独立维度：检索系统识别相关且聚焦的上下文段落的能力、LLM 忠实利用上下文的能力、生成输出本身的质量。
related:
  - ragas-reference-free-rag-evaluation
  - citation-quality-tri-dimension
  - rag-retrieval-generation-dual-condition
  - retrieval-snr-tradeoff
---

RAGAS 框架将 RAG 管道的评估挑战分解为三个独立维度，论文指出"评估 RAG 架构是具有挑战性的，因为有多个维度需要考虑" [^src-1]：

**维度一：检索质量（Context Relevance）**——"检索系统识别相关且聚焦的上下文段落的能力" [^src-2]。注意论文同时强调了"相关（relevant）"和"聚焦（focused）"两个属性，暗示检索不仅要召回相关内容，还要避免返回过于宽泛或噪声过多的段落。这与检索信噪比（SNR）的权衡直接相关。

**维度二：忠实性（Faithfulness）**——"LLM 忠实利用这些段落的能力" [^src-3]。这一维度衡量的是生成模型是否真正基于检索到的上下文来回答问题，而非依赖自身参数化知识或产生幻觉。忠实性（faithfulness）是 RAG 区别于纯 LLM 生成的关键评估维度。

**维度三：生成质量（Answer Quality）**——"生成本身的质量" [^src-4]。这一维度关注最终回答的整体可用性，独立于检索和忠实性之外。

三维分解的价值在于：它揭示了 RAG 管道的故障可能独立发生在不同组件上——检索可能召回了正确内容但 LLM 未能忠实使用，或 LLM 忠实使用了检索内容但检索本身返回了不相关的段落。单一维度的评估无法区分这些不同的失败模式。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragas/text.txt` -- Abstract L37 -- "Evaluating RAG architectures is, however, challenging because there are several dimensions to consider"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragas/text.txt` -- Abstract L37 -- "the ability of the retrieval system to identify relevant and focused context passages"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragas/text.txt` -- Abstract L37 -- "the ability of the LLM to exploit such passages in a faithful way"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragas/text.txt` -- Abstract L37 -- "the quality of the generation itself"
