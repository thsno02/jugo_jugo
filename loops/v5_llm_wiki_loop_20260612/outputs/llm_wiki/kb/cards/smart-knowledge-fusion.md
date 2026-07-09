---
id: smart-knowledge-fusion
title: 智能知识融合
status: accepted
card_type: mechanism
tags:
- llm-wiki
- knowledge-fusion
- incremental-update
- multi-source
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- obsidian-community-plugin
evidence_basis: documentation
justification: ../justification/smart-knowledge-fusion.md
canonical_concept: smart-knowledge-fusion
aliases:
- Smart Knowledge Fusion
- 智能知识融合
- incremental merge
- 增量合并
summary: 多源增量更新合并新信息而不引入冗余。重复 ingest 同一源执行增量更新（新信息合并至 entity/concept 页面）。矛盾被保留并附带归因。reviewed:true 页面受保护不被覆盖。 Summary 页面则重新生成。
related:
- contradiction-state-machine
- three-layer-wiki-architecture
---

该插件的知识融合机制支持多源增量更新：[^src-1]

- 重复 ingest 同一源时，对 entity/concept 页面执行增量更新（新信息合并），而非全量覆盖。Summary 页面则重新生成。[^src-2]
- 合并新信息时不引入冗余。
- 矛盾被保留并附带归因（attribution）。
- 用户标记 `reviewed: true` 的页面受保护不被覆盖。[^src-1]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Features" P1 -- "Smart Knowledge Fusion — Multi-source updates merge new info without redundancy, contradictions preserved with attribution, reviewed: true pages protected from overwrite"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Usage" P1 -- "Re-ingesting the same source does incremental updates on entity/concept pages (new info merged in). Summary pages are regenerated"
