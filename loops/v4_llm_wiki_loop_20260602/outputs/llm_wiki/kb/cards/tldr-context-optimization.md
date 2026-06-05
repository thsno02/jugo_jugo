---
id: tldr-context-optimization
title: TL;DR 摘要的上下文窗口优化作用
status: accepted
card_type: mechanism
tags: [llm-wiki, context-window, tldr, schema-enforcement]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
justification: ../justification/tldr-context-optimization.md
canonical_concept: tldr-context-optimization
aliases: [TL;DR 摘要优化, TL;DR enforcement, 摘要上下文压缩, TL;DR-on-top]
summary: >-
  tldr-context-optimization（TL;DR 摘要优化 / TL;DR enforcement / 摘要上下文压缩 / TL;DR-on-top）
  指在每个 wiki 页面顶部强制放置 <=50 字符 TL;DR 摘要，使 LLM 查询时扫描摘要而非全文，节省上下文窗口；实践中比索引更重要
related: [index-based-navigation, longmemeval-context-compression, schema-as-configuration]
---

在 LLM Wiki 的实际运行中，每个 wiki 页面顶部放置一行不超过 50 字符的 TL;DR 摘要，其对上下文窗口的节省效果**超过概念索引本身**[^src-1]。

这一机制的工作原理是：当用户提出跨页面查询时（如「关于 RAG vs LLM wiki 我之前怎么决定的？」），LLM 可以在**单次读取**中扫描全部 35 条 TL;DR 摘要，而不需要尝试压缩 35 个完整页面的内容[^src-2]。这将查询的上下文消耗从 O(全部页面长度) 降至 O(页面数 x 50 字符)。

Karpathy 原始 gist 仅提及 TL;DR-on-top 一次，但在六个月的实践中，作者发现它是「承重结构」（load-bearing）——即系统正常运行的必要条件，而非可选的格式约定[^src-3]。这一发现意味着 schema.md 中对 TL;DR 的格式要求应被视为核心配置而非风格偏好。

TL;DR 摘要代表了一种轻量级的上下文压缩策略（O(页面数x50字符)），而更重量级的记忆系统（如 Zep 的知识图谱管线）则通过结构化提取实现更激进的压缩（115K 至 1.6K token），两者在不同规模和复杂度下优化同一稀缺资源[^card-1]。

## Footnotes

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L38 -- "TL;DR enforcement saves your context window more than the index does"
[^src-2]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L38 -- "Every page in my wiki has a ≤50-character TL;DR at the top. When I ask Claude 'what did I decide about RAG vs LLM wiki?', it can scan 35 TL;DRs in a single read instead of trying to compress 35 full pages."
[^src-3]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L38 -- "Karpathy's gist mentions the TL;DR-on-top idea once; in practice it's load-bearing."
[^card-1]: [LongMemEval 上下文压缩与准确率提升](longmemeval-context-compression.md) -- 本卡聚焦轻量级 schema 层压缩（50字符 TL;DR），该卡展示重量级知识图谱管线压缩（115K->1.6K token），两者在不同复杂度层级优化上下文 token
