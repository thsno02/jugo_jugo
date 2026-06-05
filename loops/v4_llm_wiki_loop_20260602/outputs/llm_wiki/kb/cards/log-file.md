---
id: log-file
title: 活动日志文件
status: accepted
card_type: mechanism
tags: [llm-wiki, log, chronological, navigation]
created_time: 2026-06-05T00:00:00+08:00
edited_time: 2026-06-05T00:00:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/log-file.md
canonical_concept: log-file
aliases: [活动日志, log.md, append-only log, 时间线日志]
summary: >-
  log-file（活动日志 / log.md / append-only log / 时间线日志）是 LLM Wiki 的时间线记录：
  按时间顺序 append-only 记录摄入/查询/巡检事件，可用 grep 等 unix 工具解析，
  帮助 LLM 理解最近发生了什么
related: []
---

**log.md** 是 LLM Wiki 的时间线记录文件，与 index.md（内容目录）互补[^card-1]。它是一个 append-only 的按时间顺序记录——摄入、查询和巡检事件[^src-1]。

实用技巧：如果每条记录以统一前缀开头（如 `## [2026-04-02] ingest | Article Title`），日志就可用简单的 unix 工具解析——`grep "^## \[" log.md | tail -5` 即可获取最近 5 条记录[^src-2]。

log.md 给出 wiki 演化的时间线，帮助 LLM 理解最近做了什么[^src-3]。这使其成为跨会话连续性的辅助组件[^card-2]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Indexing and logging > log.md" P1 -- "It's an append-only record of what happened and when — ingests, queries, lint passes."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Indexing and logging > log.md" P1 -- "if each entry starts with a consistent prefix... the log becomes parseable with simple unix tools"
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Indexing and logging > log.md" P1 -- "The log gives you a timeline of the wiki's evolution and helps the LLM understand what's been done recently"
[^card-1]: [索引文件导航机制](index-based-navigation.md) -- index.md 是内容目录，本卡的 log.md 是时间线
[^card-2]: [跨会话连续性机制](cross-session-continuity.md) -- log.md 帮助新会话 LLM 理解最近发生了什么
