---
id: llm-wiki-index-derived-cache
title: _index.md 派生缓存机制
status: draft
card_type: mechanism
tags: [llm-wiki, index, derived-cache, navigation]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-index-derived-cache.md
canonical_concept: index-derived-cache
aliases: [_index.md, directory index, derived index cache]
summary: >-
  index-derived-cache 机制：每个目录都有 _index.md 作为从文件 frontmatter 派生的缓存，自动重建，agent 首先读取索引永不盲扫目录
related: [llm-wiki-hub-architecture]
---

llm-wiki 中每个目录都存在 _index.md 文件，作为从文件 frontmatter 派生的缓存。这些索引自动重建，agent 在探索内容时首先读取索引，永远不进行盲目目录扫描。[^src-1]

这种设计使 agent 能快速定位相关内容而无需遍历大量文件，提升了系统在大规模 wiki 下的可扩展性。[^card-1]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Architecture" P206 -- "Indexes (_index.md) exist in every directory. They're derived caches — rebuilt automatically from file frontmatter. The agent reads indexes first and never scans blindly."
[^card-1]: [llm-wiki-hub-architecture]
