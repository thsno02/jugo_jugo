---
id: sensemaking-vs-retrieval-query
title: 意义建构查询与检索查询的区分
status: accepted
card_type: distinction
tags: [sensemaking, retrieval, rag, query-type, qfs]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
justification: ../justification/sensemaking-vs-retrieval-query.md
canonical_concept: sensemaking-vs-retrieval-query
aliases: [sensemaking query, 全局查询与局部查询, 意义建构型问题]
summary: >-
  sensemaking-vs-retrieval-query（sensemaking query / 意义建构型问题）区分需要全局理解语料库的意义建构查询（如主题趋势）与可通过局部文本片段回答的检索查询，前者是 QFS 任务而非检索任务
related: [graphrag-global-sensemaking, graphrag-map-reduce-query, llm-wiki-rag-depth-distinction, query-and-answer-filing]
---

GraphRAG 论文明确区分了两类根本不同的查询类型。检索查询（retrieval query）可以通过检索少量局部相关的文本记录来回答，传统向量 RAG 在此类任务上表现良好 [^src-1]。

意义建构查询（sensemaking query）则要求对整个数据集的全局理解，例如"过去十年跨学科研究如何影响科学发现的关键趋势是什么？" [^src-2]。这类任务的本质是查询聚焦摘要（QFS），而非显式检索。

论文引用 Klein 等人对 sensemaking 的定义：需要推理"人、地点和事件之间的联系，以预测其轨迹并有效行动" [^src-3]。这一区分是 GraphRAG 存在的根本理由——向量 RAG 在局部检索上有效，但无法支持对整个语料库的 sensemaking。

这一区分具有实际架构意义：当系统主要面对检索型查询时，传统 RAG 已经足够；但当需要回答全局性、主题性、趋势性问题时，需要从局部到全局的摘要机制 [^src-4]。

LLM Wiki 从推理深度角度做出了类似的区分——wiki 的预综合知识使多跳推理自然可行，而 RAG 局限于局部片段检索[^card-1]。本卡所定义的 sensemaking 查询类型正是 GraphRAG map-reduce 流程的设计目标[^card-2]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Introduction (graph_rag.tex) -- "This conventional approach, which we collectively call vector RAG, works well for queries that can be answered with information localized within a small set of records."
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Introduction (graph_rag.tex) -- "vector RAG approaches do not support sensemaking queries, meaning queries that require global understanding of the entire dataset, such as 'What are the key trends in how scientific discoveries are influenced by interdisciplinary research over the past decade?'"
[^src-3]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Introduction (graph_rag.tex) -- "Sensemaking tasks require reasoning over 'connections (which can be among people, places, and events) in order to anticipate their trajectories and act effectively'"
[^src-4]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Abstract (graph_rag.tex) -- "this is inherently a query-focused summarization (QFS) task, rather than an explicit retrieval task"
[^card-1]: [LLM Wiki 与 RAG 的核心差异在于推理深度](llm-wiki-rag-depth-distinction.md) -- 本卡从查询类型区分 sensemaking 与 retrieval，该卡从推理深度论证 wiki 超越 RAG，两者共同指向局部检索对深层推理的不足
[^card-2]: [GraphRAG 查询时 Map-Reduce 应答流程](graphrag-map-reduce-query.md) -- 本卡定义 sensemaking 查询类型，该卡描述回答此类查询的具体 map-reduce 机制，构成问题定义与解决方案的互补
