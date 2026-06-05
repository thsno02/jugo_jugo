---
id: topic-isolation
title: 主题隔离原则
status: accepted
card_type: concept
tags: [llm-wiki, architecture, isolation, topic-wiki]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
justification: ../justification/topic-isolation.md
canonical_concept: topic-isolation
aliases: [主题隔离, topic isolation, one topic one wiki, 话题隔离]
summary: >-
  topic-isolation（主题隔离 / topic isolation / one topic one wiki / 话题隔离）是 LLM Wiki
  的设计原则：每个研究领域是独立 wiki，拥有独立的来源/文章/产出/Obsidian 配置，
  避免跨主题噪声，需要时可通过 multi-wiki peek 发现交叉
related: []
---

LLM Wiki 的核心设计原则之一是**一个主题一个 wiki（one topic, one wiki）**[^src-1]。作为 LLM Wiki 模式的架构组成部分[^card-1]，主题隔离有效管理了个人规模下的内容复杂度。每个研究领域作为独立的 topic wiki 存在于 `~/wiki/topics/<name>/` 下，拥有自己独立的来源、文章、产出和 Obsidian vault 配置[^src-2]。

隔离带来的直接好处是**无跨主题噪声**——研究量子计算不会污染营养学 wiki，查询保持聚焦[^src-3]。

当确实需要跨主题视角时，有两种机制突破隔离边界：
- **multi-wiki peek**：在相关时发现主题间的交叉[^src-4]
- **`--with` 参数**：`query`、`output`、`plan` 命令支持 `--with <wiki>` 从另一个 wiki 引入上下文[^src-5]

Hub 层（`~/wiki/`）只是注册表——没有内容，只有 `wikis.json`、`_index.md` 和 `log.md`。所有内容都在 topic 子 wiki 中[^src-6]。

## Footnotes

[^src-1]: `data/raw/webpage/llm-wiki-net/text.txt` -- "One topic, one wiki" L142-144 -- "Each research area is isolated. No cross-topic noise. Queries stay focused. A multi-wiki peek finds overlap when relevant."
[^src-2]: `data/raw/webpage/llm-wiki-net/text.txt` -- "How the wiki works" L302-303 -- "Topic wikis (~/wiki/topics/<name>/) are isolated research areas. Each has its own sources, articles, outputs, and Obsidian vault config."
[^src-3]: `data/raw/webpage/llm-wiki-net/text.txt` -- "How the wiki works" L303 -- "Isolation means researching quantum computing can't pollute your nutrition wiki."
[^src-4]: `data/raw/webpage/llm-wiki-net/text.txt` -- "One topic, one wiki" L144 -- "A multi-wiki peek finds overlap when relevant."
[^src-5]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Commands" L172 -- "query, output, and plan also accept --with <wiki> for cross-wiki context."
[^src-6]: `data/raw/webpage/llm-wiki-net/text.txt` -- "How the wiki works" L300 -- "The hub (~/wiki/) is just a registry. No content — only wikis.json, _index.md, and log.md."
