---
id: llm-wiki-definition-and-core-value
title: LLM Wiki 的定义与核心价值
status: draft
card_type: concept-definition
tags: [llm-wiki, personal-knowledge-management, natural-language-query]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [kunal-local-knowledge-base]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-definition-and-core-value.md
canonical_concept: llm-wiki-concept
aliases: [LLM wiki, LLM 维基, personal queryable knowledge base, 可对话的个人知识库]
summary: >-
  LLM wiki (LLM 维基) 是一种可对话的个人知识库，用户以自然语言提问而非关键词搜索，系统通过本地 RAG 管线从自有文档中合成回答。核心价值在于从"定位文档"升级为"合成答案"，且数据全程不出本机。
related: []
---

LLM wiki 被定义为"a personal knowledge base you can talk to"——一种可以用自然语言对话的个人知识库。[^src-1]

与传统关键词搜索的本质区别在于：用户不再搜索文档再人工阅读，而是直接提出问题，系统从自有文档中检索相关片段并由本地 LLM 合成回答。[^src-2]

该概念的核心价值主张是全栈本地化——检索增强生成（RAG）完全运行在本机，无数据外泄。据材料描述，开发者"don't just want AI assistants that know the internet. They want AI assistants that know their stuff"。[^src-3]

[^src-1]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "What Is an LLM Wiki" P3 -- "a personal knowledge base you can talk to. Instead of searching your notes by keyword, you ask natural-language questions and get synthesized answers drawn from your own documents"
[^src-2]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "What Is an LLM Wiki" P6 -- "An LLM wiki takes a collection of text documents...chunks them into smaller pieces, creates vector embeddings for each chunk, and then uses a local LLM to find and synthesize answers"
[^src-3]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "What Is an LLM Wiki" P8 -- "Developers don't just want AI assistants that know the internet. They want AI assistants that know their stuff"
