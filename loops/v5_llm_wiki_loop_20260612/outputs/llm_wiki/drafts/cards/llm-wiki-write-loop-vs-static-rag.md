---
id: llm-wiki-write-loop-vs-static-rag
title: LLM Wiki 的 Write Loop 区别于静态 RAG
status: draft
card_type: technical-distinction
tags: [llm-wiki, rag, write-loop, lint-pass, knowledge-synthesis, zettelkasten]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [hacker-news-original-thread]
evidence_basis: community_discussion
justification: ../justification/llm-wiki-write-loop-vs-static-rag.md
canonical_concept: llm-wiki-write-loop
aliases: [write loop, LLM wiki write loop, 写循环, knowledge synthesis loop, lint pass]
summary: >-
  LLM Wiki 与传统 RAG 的核心区别是 write loop：LLM 自己撰写维护 wiki、构建 backlinks、将输出回归系统，语料库动态演进而非静态。lint pass 执行不一致性审计、补全缺失数据、建议连接，更接近助理维护 zettelkasten 而非搜索引擎返回 top-k chunks。反对观点认为检索最相关知识片段的基本问题本质仍是 RAG。
related: [dual-audience-wiki-artifact, wiki-complexity-collapse-threshold]
---

LLM Wiki 与传统 RAG 的核心区别在于 write loop（写循环）：LLM 不仅检索，还自己撰写和维护 wiki 内容、构建 backlinks、将输出回归系统。在传统 RAG 中语料库是静态的，而在 LLM Wiki 中语料库动态自演进。[^src-1]

此外，lint pass 执行了传统 RAG 不具备的功能：审计不一致性、补全缺失数据、建议连接。这更接近一个助理维护 zettelkasten，而非搜索引擎返回 top-k chunks。[^src-1]

反对观点认为：无论通过 vector DB 还是结构化索引/文件系统检索最相关信息这一基本问题——即为 LLM context 获取最佳数据——本质仍是 RAG，且这是一个已被研究和评估多年的问题。[^src-2]

原帖设计还规定将 ground truth 源文件放入 /raw 目录，一切派生内容回链到源文件，这对警惕 staleness、正确性和 drift 是必要的。[^src-3]

[^src-1]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- "darkhanakh comment" -- "the interesting bit here is the write loop - the LLM is authoring and maintaining the wiki itself, building backlinks, filing its own outputs back in. thats not retrieval thats knowledge synthesis. in vanilla RAG your corpus is static, here it isnt"
[^src-2]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- "kenforthewin comment" -- "What I'm pushing back on specifically is the insistence that the core loop - retrieving the most relevant pieces of knowledge for wiki synthesis - is not RAG... that fundamental problem - retrieving the best data for the LLM's context - is RAG."
[^src-3]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- "hombre_fatal comment" -- "TFA prescribes putting ground truth source files into a /raw directory. Everything is derived from them and backlinks into them. Which is necessary to be vigilant about staleness, correctness, drift"
