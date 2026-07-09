---
id: tldr-enforcement-context-window
title: TL;DR 强制与 Context Window 管理
status: draft
card_type: technique
tags: [llm-wiki, context-window, tldr, retrieval-optimization]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
evidence_basis: practitioner_report
justification: ../justification/tldr-enforcement-context-window.md
canonical_concept: tldr-enforcement-context-window
aliases: [TL;DR enforcement, TL;DR-on-top, TL;DR 置顶, context window 节省]
summary: >-
  TL;DR 强制 tldr-enforcement-context-window 指每个 wiki 页面顶部放置 ≤50 字符摘要，使 LLM 可在单次 read 中扫描所有页面摘要而非压缩全文。作者称此为"load-bearing"——比 index 更节省 context window。Karpathy 原始 gist 仅提及一次，但实践中此机制是负载承重件。
related: []
---

每个 wiki 页面顶部放置 ≤50 字符的 TL;DR [^src-1]。

作用机制：当提问"what did I decide about X?"时，Claude 可在单次 read 中扫描 35 条 TL;DR，而非尝试压缩 35 个全页。这比 index 文件更有效地节省 context window。

作者将其描述为"load-bearing"（负载承重）——Karpathy gist 仅提及一次，但六个月实践表明这是系统关键组件而非可选装饰 [^src-1]。

[^card-1]: 与 [llm-wiki-three-layer-structure] 相关——TL;DR 是 wiki/ 页面的必需结构元素

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "What the Karpathy LLM Wiki Actually Looks Like" P30 -- "TL;DR enforcement saves your context window more than the index does...it's load-bearing"
