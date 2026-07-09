---
id: llm-wiki-topic-wiki-isolation
title: Topic Wiki 隔离原则
status: superseded
superseded_by: hub-topic-wiki-isolation
card_type: design-principle
tags: [llm-wiki, isolation, topic-wiki]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-topic-wiki-isolation.md
canonical_concept: topic-wiki-isolation
aliases: [topic isolation, isolated wiki, topic wiki isolation]
summary: >-
  topic-wiki-isolation 隔离原则：每个 topic wiki 是独立研究区域，有自己的 sources articles outputs 和 Obsidian vault config，研究一个主题不会污染另一个 wiki，查询保持聚焦，跨 wiki 仅在相关时 peek overlap
related: [llm-wiki-hub-architecture, llm-wiki-archive-system]
---

llm-wiki 的核心设计原则之一是 topic wiki 隔离。每个 topic wiki（~/wiki/topics/<name>/）是完全独立的研究区域，拥有自己的源、文章、输出和 Obsidian vault 配置。[^src-1]

隔离意味着研究某个主题（如量子计算）不会污染另一个 wiki（如营养学）。查询保持聚焦于当前 topic。多 wiki 仅在相关时通过 peek 功能发现重叠。[^src-2]

跨 wiki 上下文可通过 --with <wiki> 参数在 query、output、plan 命令中显式引入。[^card-1]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Architecture" P196 -- "Topic wikis (~/wiki/topics/<name>/) are isolated research areas. Each has its own sources, articles, outputs, and Obsidian vault config."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Directory Structure" P116 -- "Each research area is isolated. No cross-topic noise. Queries stay focused. A multi-wiki peek finds overlap when relevant."
[^card-1]: [llm-wiki-hub-architecture]
