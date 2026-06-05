---
id: wiki-rag-hybrid-pattern
title: Wiki-RAG 混合架构模式
status: accepted
card_type: mechanism
tags: [llm-wiki, rag, hybrid, architecture, enterprise]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [atlan-llm-wiki-vs-rag-dynamic-20260524]
justification: ../justification/wiki-rag-hybrid-pattern.md
canonical_concept: wiki-rag-hybrid-pattern
aliases: [wiki-rag混合, hybrid wiki-RAG, 混合架构, wiki+RAG]
summary: >-
  wiki-rag-hybrid-pattern（wiki-rag混合 / hybrid wiki-RAG / 混合架构）LLM wiki 与 RAG
  并非互斥，可以形成混合架构：wiki 提供策展过的高置信度上下文作为"种子"锚定 RAG 检索，
  实现两层分离——wiki 层承载"我们确定知道的"，RAG 层承载"语料库中当前有的"
related: []
---

LLM wiki 和 RAG 管线并非互斥。在混合架构中，wiki 提供策展过的高置信度上下文来锚定 RAG 检索——降低噪声、改善 grounding、使 LLM 回复在查询间更一致[^src-1]。

**模式一：Wiki 作为策展上下文层覆盖 RAG。** Wiki 的结构化摘要文章作为高质量"种子"上下文，在 RAG 检索开始之前传递给 LLM。LLM 不是冷启动进入原始语料库，而是先获得可靠的解释框架：关键概念、稳定定义、已知关系。RAG 随后为具体查询检索支撑证据。组合效果：比单独 RAG 有更高的回复一致性和更少的幻觉[^src-2]。

**模式二：两层分离——策展层与检索层。** Wiki 处理"我们确定知道的"层——经过认证的概念、稳定定义、变化缓慢的内部框架。RAG 处理"语料库中当前有的"层——实时文档搜索、证据检索、大规模动态数据集的广覆盖。这种分离避免了策展知识层被广泛检索的噪声和方差污染[^src-3]。

**模式三：Wiki 层即受治理的元数据层。** 最强大的混合形式出现在"wiki"不是 markdown 文件夹而是**受治理的数据目录**时——策展的、认证的、有访问控制的元数据。目录回答"我们对数据了解什么"；RAG 从数据本身检索。一个在查询数据集之前就了解其结构、认证状态和血缘关系的 LLM agent 是一个根本性更可靠的 agent[^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L363 -- "In hybrid architectures, the wiki provides curated, high-confidence context that anchors RAG retrieval - reducing noise, improving grounding, and making LLM responses more consistent across queries."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L367-368 -- "Combined outcome: higher response consistency and fewer hallucinations than RAG alone, because the LLM is grounding against curated knowledge before it reaches into dynamic retrieval."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L373 -- "This separation avoids contaminating the curated knowledge layer with the noise and variance of broad retrieval."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L378 -- "An LLM agent that knows the shape, certification status, and lineage of a dataset before it queries it is a fundamentally more reliable agent than one that retrieves blindly."
