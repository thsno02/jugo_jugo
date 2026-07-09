---
id: ripple-effect-ingest
title: Ingest 涟漪效应
status: draft
card_type: observed-phenomenon
tags: [llm-wiki, compounding, ingest, ripple-effect]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
evidence_basis: practitioner_report
justification: ../justification/ripple-effect-ingest.md
canonical_concept: ripple-effect-ingest
aliases: [ripple effect, 涟漪效应, 每次 ingest 触及多页, compounding behavior]
summary: >-
  Ingest 涟漪效应 ripple-effect-ingest 指每次向 LLM wiki 注入新文章时 Claude 会触及多个现有页面：添加 backlinks、更新概念索引、标记矛盾、精炼 TL;DR。作者报告中位数每次 ingest 触及 9 个文件（范围 4-23），基于最近 30 次 ingest 的 log.md 统计。此为 Karpathy 原始 gist 所称的 ripple effect 的实证验证。
related: []
---

每次向 LLM wiki 注入新文章时，Claude 平均触及 8-12 个现有页面 [^src-1]。具体操作包括：添加 backlinks、更新 concepts index、标记与旧笔记的矛盾、精炼 TL;DR。

作者基于 log.md 的统计：中位数每次 ingest 触及 9 个文件，范围为 4 到 23 [^src-1]。数据来源为最近 30 次 ingest。

这是 Karpathy 原始 gist 所称的"ripple effect"的实证验证。作者称"compounding behavior is real"——远超预期。

[^card-1]: 与 [llm-wiki-three-layer-structure] 相关——涟漪效应发生在三层结构的 wiki/ 层
[^card-2]: 与 [schema-first-principle] 相关——schema 规则指导 Claude 何时何处触及现有页面

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "What the Karpathy LLM Wiki Actually Looks Like" P29 -- "Claude touches an average of 8–12 existing pages...my log.md says the median ingest touches 9 files"
