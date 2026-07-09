---
id: llm-wiki-pattern
title: LLM Wiki 模式
status: draft
card_type: 架构模式
tags: [knowledge-compilation, kv-cache, inference-architecture]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
evidence_basis: experimental_paper
justification: ../justification/llm-wiki-pattern.md
canonical_concept: llm-wiki-pattern
aliases: [LLM Wiki, LLM Wiki pattern, Karpathy LLM Wiki, wiki-memory pattern]
summary: >-
  LLM Wiki pattern 是 Karpathy 2026 提出的三层架构: raw sources -> compiled wiki -> structured schemas。核心思想是知识编译一次后持续维护而非每次查询重新派生。实现方式为将编译后文档集加载至模型上下文窗口并持久化 KV cache 状态(如 llama.cpp --cache-prompt)，后续查询以亚秒延迟服务。与 RAG 的根本区别在于消除了查询时检索步骤和检索失败风险。
related: []
---

LLM Wiki 模式（Karpathy 2026）提出一种三层知识架构：

1. **原始源文档层**：未处理的领域文档集合
2. **编译 Wiki 层**：经 LLM 编译器蒸馏的结构化知识制品
3. **结构化 Schema 层**：进一步压缩的摘要与模式

核心原则为"知识编译一次后持续维护，不在每次查询时重新派生"。[^src-1]

实际实现路径为：将编译后的领域知识集（约 100K tokens 对应约 100 篇文章）加载进 LLM 上下文窗口，通过 KV cache 持久化（如 llama.cpp 的 `--cache-prompt` 功能），使后续每次查询仅需处理问题后缀（约 30-50 tokens），实现亚秒级 TTFT。[^src-2]

该模式从根本上区别于 RAG：RAG 在查询时嵌入问题并检索 top-k 文档块，虽减少了每次查询的 token 消耗，但存在检索失败风险；LLM Wiki 模式则让模型对全部知识库进行推理，消除检索失败但要求知识适配上下文窗口。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Introduction" P285-286 -- "knowledge is compiled once and then kept current, not re-derived on every query"
[^src-2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Introduction" P331-338 -- "loading a curated document collection into a model's context window and persisting the KV cache states"
[^src-3]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Introduction" P339-345 -- "embeds queries and retrieves the top-k most relevant document chunks...risks missing relevant information when retrieval fails"
