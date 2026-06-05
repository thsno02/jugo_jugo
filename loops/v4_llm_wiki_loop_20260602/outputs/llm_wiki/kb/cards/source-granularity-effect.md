---
id: source-granularity-effect
title: 源文件粒度效应
status: accepted
card_type: mechanism
tags: [llm-wiki, granularity, source-files, quality, slop]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [hacker-news-original-thread]
justification: ../justification/source-granularity-effect.md
canonical_concept: source-granularity-effect
aliases: [源粒度效应, source granularity, 文件切分粒度]
summary: >-
  source-granularity-effect（源粒度效应 / source granularity / 文件切分粒度）指源文件的切分粒度对 wiki 编译质量有决定性影响：整本书作为单文件产出"slop"，章节级切分则质的提升；相同模型、相同提示词，唯一变量是源粒度
related: [chunk-size-tradeoff, dual-audience-artifact, extraction-granularity-control, ingest-operation, three-layer-architecture]
---

一位 LLM Wiki 编译器的实现者报告了一个关键的实证发现：**源文件粒度是 wiki 编译质量的决定性变量**。

在处理 3 本书（约 155K 词）时，将每本书作为一个文件（朴素版本）产出了评论者所描述的典型「slop」。但将源文件切分为章节级粒度后，**相同的模型、相同的提示词**，输出发生了质的变化（categorically different）。唯一改变的变量就是源文件粒度[^src-1]。

切分到章节级粒度后，编译器从 68 个源文件生成了 210 个概念页面、4,597 条交叉引用。20 多个概念在未被提示的情况下跨三本书综合。最终输出 173K 词，从 155K 词输入中产出——这不是压缩，而是综合[^src-2]。

这一发现对 LLM Wiki 的三层架构（raw sources 层）有直接的实践指导意义：raw sources 的组织粒度不仅是文件管理问题，更是影响整个 wiki 质量的关键设计决策。该发现与 RAG 管线中的分块权衡形成跨域呼应——朴素固定分块同样因丢弃文档结构而降低检索质量，语义分块是共同的改进方向[^card-1]。此外，提取粒度（从源文档中提取多少实体）构成了与源文件粒度正交的另一质量维度[^card-2]。

## Footnotes

[^src-1]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- vbarsoum 评论 -- "The naive version (each book as 1 file) produced exactly the slop people are describing here. But splitting into chapter-level files and recompiling changed the output categorically. Same model, same prompts — the only variable was source granularity."
[^src-2]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- vbarsoum 评论 -- "The compiler produced 210 concept pages with 4,597 cross-references (19.2 avg links per page). 20+ concepts synthesized across all 3 books unprompted... 173K words of output from 155K input. It's not compression — it's synthesis."
[^card-1]: [分块大小权衡](chunk-size-tradeoff.md) -- 本卡聚焦 wiki 编译场景中源文件切分粒度的质量效应，该卡聚焦 RAG 管线中分块大小的检索精度权衡，共同印证语义边界切分优于朴素固定切分
[^card-2]: [提取粒度控制](extraction-granularity-control.md) -- 本卡聚焦输入侧的源文件切分粒度，该卡聚焦产出侧的实体提取深度（5 级可配置），两者是 wiki 编译质量的正交维度
