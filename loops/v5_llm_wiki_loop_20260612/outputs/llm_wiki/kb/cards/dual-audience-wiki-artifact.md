---
id: dual-audience-wiki-artifact
title: Wiki 作为人机双用知识界面
status: accepted
card_type: design-insight
tags:
- llm-wiki
- human-ai-interface
- obsidian
- knowledge-artifact
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- hacker-news-original-thread
evidence_basis: community_discussion
justification: ../justification/dual-audience-wiki-artifact.md
canonical_concept: dual-audience-wiki-artifact
aliases:
- same artifact two audiences
- 人机共用界面
- compiled wiki as interface
summary: compiled wiki 同时作为人类浏览界面和 AI 知识层：人可在 Obsidian 中打开浏览图谱和跟踪链接，AI 读取同样页面获得结构化交叉引用的答案，优于 RAG 的 raw chunk 检索。vector database 只对机器有用，wiki 对两种受众都有用。
related:
- llm-wiki-write-loop-vs-static-rag
- context-window-degradation-limits
---
LLM Wiki 的关键设计洞察是：compiled wiki 同时服务两种受众——人类和 AI。[^src-1]

Vector database（如 .faiss 文件）只对机器有用，人无法直接打开浏览。而 wiki 文件可以在 Obsidian 中打开、浏览图谱、跟踪链接，无需 AI 介入。当人向 AI 提问时，AI 读取同样的 wiki 页面，由于知识已被结构化和交叉引用，答案优于 RAG 从原始 chunks 检索的结果。[^src-1]

实证支持：对 3 本书（约 155K words，68 source files）的测试中，编译器产出 210 个概念页面、4,597 条交叉引用（平均每页 19.2 条链接），20+ 概念跨三本书被自动合成，其中一个概念从 11 个源文件中提取并发现了两本书之间的真实矛盾。[^src-2]

[^card-1]: 参见 [llm-wiki-write-loop-vs-static-rag] -- write loop 使 wiki 动态演进而非静态语料

[^src-1]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- "vbarsoum comment" -- "a vector database is only useful to machines. You can't open a .faiss file and browse it. A wiki is useful to both... The compiled wiki is the interface for humans AND the knowledge layer for AI. Same artifact, two audiences."
[^src-2]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- "vbarsoum comment" -- "The compiler produced 210 concept pages with 4,597 cross-references (19.2 avg links per page). 20+ concepts synthesized across all 3 books unprompted"
