---
id: parallel-page-generation
title: 并行页面生成与容错
status: draft
card_type: mechanism
tags: [llm-wiki, concurrency, error-handling, performance]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
evidence_basis: documentation
justification: ../justification/parallel-page-generation.md
canonical_concept: parallel-page-generation
aliases: [parallel generation, 并行生成, page generation concurrency, Promise.allSettled]
summary: >-
  并行页面生成：可配置 1-5 并发（默认 3），2-3 倍加速。使用 Promise.allSettled 隔离错误——
  单页失败不影响其他页面，失败页以指数退避重试。Rate Limit Guardian 自动检测限速并建议
  降低并发/增加延迟/切换提供商。Smart Batch Skip 跳过已处理文件。
related: [content-truncation-protection, extraction-granularity-levels]
---

并行页面生成（v1.7.3+）支持可配置的 1-5 并发页面创建（默认 3），对含 10+ 实体的源可加速 2-3 倍。[^src-1]

容错设计：
- 使用 `Promise.allSettled` 实现错误隔离——单页失败不影响其他页面继续生成。[^src-2]
- 失败页面以指数退避（exponential backoff）单独重试。
- Rate Limit Guardian：当并行生成触发限速时自动检测，建议降低并发、增加批次延迟或切换提供商。[^src-3]
- Smart Batch Skip（v1.7.7）：自动检测已 ingest 的文件并跳过，节省时间和 API 成本。[^src-4]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Features" P1 -- "Parallel Page Generation — Configurable 1–5 concurrent pages, default 3 (parallel), 2–3× faster for large sources, error isolation per page"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Safety" P1 -- "Parallel generation uses Promise.allSettled — if one page fails, others continue. Failed pages are retried individually with exponential backoff"
[^src-3]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Features" P1 -- "Rate Limit Guardian — When parallel generation triggers rate limits, auto-detects and suggests: lower concurrency, increase batch delay, switch provider"
[^src-4]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Features" P1 -- "Smart Batch Skip automatically detects already-ingested files to save time and API costs"
