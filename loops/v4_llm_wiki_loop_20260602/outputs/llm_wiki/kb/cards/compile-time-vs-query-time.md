---
id: compile-time-vs-query-time
title: 编译时与查询时知识装配
status: accepted
card_type: distinction
tags: [llm-wiki, rag, architecture, knowledge-assembly]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [atlan-llm-wiki-vs-rag-dynamic-20260524]
justification: ../justification/compile-time-vs-query-time.md
canonical_concept: compile-time-vs-query-time
aliases: [编译时vs查询时, compile-time vs query-time, 编译时知识装配, 查询时知识装配]
summary: >-
  compile-time-vs-query-time（编译时vs查询时 / compile-time vs query-time）是 LLM wiki
  与 RAG 的根本架构区分轴：wiki 在编译时将结构化索引加载到上下文中（LLM 预先读取全部相关内容），
  RAG 在查询时从向量库动态检索语义相关片段
related: []
---

LLM wiki 与 RAG 知识库的核心架构差异可以用一个轴来表达：**编译时（compile-time）与查询时（query-time）知识装配**[^src-1]。

LLM wiki 将结构化索引直接加载到上下文窗口中——LLM 预先读取所有相关内容，无需向量数据库或检索管线。RAG 则在查询时从向量存储中动态检索语义相关的文档片段，LLM 从未加载完整语料[^src-2]。

这一区分不关乎"智能"差异，而关乎**规模假设的不同**。Wiki 假设知识是有界的、稳定的——一个个人研究者策展的约 100 篇文章可以舒适地装入上下文。RAG 假设知识是大规模的、动态的、多领域的——没有任何单一索引文件可以容纳[^src-3]。

MindStudio 的分析表明，在小规模下编译时方案可将 token 消耗减少多达 95%（相比于将所有源文档一次性加载到上下文中），但这一优势在面对优化过的 RAG 管线时会缩小，超出单个上下文窗口后完全消失[^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L230 -- "The key distinction is compile-time versus query-time knowledge assembly."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L275-276 -- "An LLM wiki loads a structured index directly into context - the LLM reads everything relevant upfront. A RAG knowledge base retrieves chunks dynamically from a vector store at query time. The distinction is compile-time versus query-time knowledge assembly, not intelligence."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L280-281 -- "The LLM wiki assumes knowledge is bounded and stable... RAG assumes knowledge is large, dynamic, and multi-domain"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L247 -- "the wiki approach can cut token usage by up to 95% compared to loading all source documents into context at once, an advantage that narrows against optimized RAG pipelines and disappears entirely beyond one context window"
