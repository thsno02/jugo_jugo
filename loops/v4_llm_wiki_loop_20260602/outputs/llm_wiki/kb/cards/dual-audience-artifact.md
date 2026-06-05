---
id: dual-audience-artifact
title: 双受众制品
status: accepted
card_type: mechanism
tags: [llm-wiki, dual-audience, human-readable, AI-queryable, vector-db]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [hacker-news-original-thread]
justification: ../justification/dual-audience-artifact.md
canonical_concept: dual-audience-artifact
aliases: [双受众制品, 双用途产物, same artifact two audiences]
summary: >-
  dual-audience-artifact（双受众制品 / 双用途产物 / same artifact two audiences）指编译后的 wiki 同时是人类浏览界面（Obsidian 打开、跟踪链接、阅读概念页）和 AI 知识层（结构化、交叉引用的上下文）；与 RAG 向量数据库（.faiss 文件人类无法阅读）形成对比——同一制品服务两类受众
related: [obsidian-tooling, rag-wiki-synthesis-distinction, wiki-compounding-artifact]
---

一位实现了 LLM Wiki 编译器的评论者基于实际数据提出了一个关键洞察：编译后的 wiki 是同时服务于人类和 AI 的**双受众制品（dual-audience artifact）**[^src-1]。

具体实现数据：将 3 本书（约 155K 词、68 个源文件）编译为 wiki，产出 210 个概念页面、4,597 条交叉引用（平均每页 19.2 条链接）。20 多个概念在未被提示的情况下跨三本书综合——其中一个概念拉取了 11 个源文件，并发现了两本书之间一个作者未明确指出的真实矛盾[^src-2]。

这与 RAG 的核心区别在于：**向量数据库只对机器有用**——你无法打开一个 .faiss 文件来浏览它。而 wiki 对两类受众都有用。人类在 Obsidian 中打开这些文件、浏览图谱、跟随链接、阅读概念页面，不需要 AI。当你确实需要问 AI 问题时，AI 读取的是同一套 wiki 页面，而且因为知识已经被结构化和交叉引用（而非作为原始片段被检索），回答质量更高[^src-3]。

该评论者还报告了**源粒度的关键效应**：将每本书作为一个文件的朴素版本产生了典型的"slop"；切换为章节级文件后，相同的模型、相同的提示词，输出发生了质的变化。唯一变量是源文件粒度[^src-4]。

## Footnotes

[^src-1]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- vbarsoum 评论 -- "The compiled wiki is the interface for humans AND the knowledge layer for AI. Same artifact, two audiences."
[^src-2]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- vbarsoum 评论 -- "The compiler produced 210 concept pages with 4,597 cross-references (19.2 avg links per page). 20+ concepts synthesized across all 3 books unprompted — one pulled from 11 source files and found a genuine contradiction between two books"
[^src-3]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- vbarsoum 评论 -- "a vector database is only useful to machines. You can't open a .faiss file and browse it. A wiki is useful to both."
[^src-4]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- vbarsoum 评论 -- "The naive version (each book as 1 file) produced exactly the slop... But splitting into chapter-level files and recompiling changed the output categorically. Same model, same prompts — the only variable was source granularity."
