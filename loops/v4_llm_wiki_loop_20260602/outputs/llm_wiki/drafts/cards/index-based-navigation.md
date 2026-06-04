---
id: index-based-navigation
title: 基于索引文件的 Wiki 导航
status: draft
card_type: mechanism
tags: [llm-wiki, index, navigation, scaling]
created_time: 2026-06-04T22:30:00+08:00
edited_time: 2026-06-04T22:30:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/index-based-navigation.md
canonical_concept: index-based-navigation
aliases: [索引文件导航, index.md, wiki 导航, 索引机制]
summary: >-
  index-based-navigation 是 LLM Wiki 的导航机制：index.md 按类别列出所有页面及摘要，
  LLM 查询时先读索引再深入具体页面，在中等规模（~100 资料、数百页面）下运作良好，
  避免了 embedding RAG 基础设施的需要；超出规模后可用 qmd 等本地搜索工具
related: []
---

LLM Wiki 使用 **index.md** 作为内容导航的核心机制。index.md 是一份目录型文件——列出 wiki 中的每个页面，附带链接、一行摘要和可选元数据（如日期、资料计数），按类别组织（实体、概念、资料等）。LLM 在每次摄入时更新索引[^src-1]。

查询时，LLM 先读取索引找到相关页面，再深入阅读具体页面。这种方法在中等规模下（约 100 份资料、数百个页面）「出人意料地好用」，避免了 embedding RAG 基础设施的需要[^src-2]。

当 wiki 增长超出索引文件的承载能力时，可引入正式的搜索工具。材料推荐 **qmd**——一个本地 markdown 搜索引擎，结合 BM25/向量混合搜索和 LLM 重排序，全部在本地设备运行，同时提供 CLI 和 MCP server 接口[^src-3]。也可自行构建更简单的搜索脚本。

另一个辅助文件是 **log.md**——按时间顺序记录的 append-only 日志，记录摄入、查询和巡检事件，可用 grep 等 unix 工具解析[^src-4]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Indexing and logging > index.md" -- "It's a catalog of everything in the wiki — each page listed with a link, a one-line summary, and optionally metadata like date or source count."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Indexing and logging > index.md" -- "This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure."
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Optional: CLI tools" -- "qmd is a good option: it's a local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking, all on-device"
[^src-4]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Indexing and logging > log.md" -- "It's an append-only record of what happened and when — ingests, queries, lint passes."
