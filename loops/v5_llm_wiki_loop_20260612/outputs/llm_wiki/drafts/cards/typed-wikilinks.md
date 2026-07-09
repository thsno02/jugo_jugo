---
id: typed-wikilinks
title: Typed Wikilinks 类型化链接
status: draft
card_type: mechanism
tags: [llm-wiki, rohit-v2, wikilinks, knowledge-graph]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
evidence_basis: practitioner_report
justification: ../justification/typed-wikilinks.md
canonical_concept: typed-wikilinks
aliases: [typed wikilinks, 类型化链接, typed relationships, 六种关系类型]
summary: >-
  Typed wikilinks 类型化链接 typed-wikilinks 是 Rohit v2 引入的机制，将 plain [[link]] 升级为 [[target]] (relationship-type) 格式，共 6 种关系类型（如 uses、alternative-to、contradicts）。初期感觉繁琐但两个月后使 Claude 能给出更精确的回答——图不再仅是"X 连接 Y"而是"X uses Y"或"X contradicts Y"。
related: []
---

Rohit v2 将 plain wikilinks 升级为 typed wikilinks [^src-1]：

格式：`[[target]] (relationship-type)`

共 6 种关系类型（材料举例 uses、alternative-to；implied 还有 contradicts 等）。

作者初始感受："feels fussy at first"。但两个月后发现此机制让 Claude 能给出"much sharper answers"——因为知识图不再仅是"X is connected to Y"而是语义化的"X uses Y"或"X contradicts Y" [^src-1]。

[^card-1]: 与 [memory-lifecycle-fields] 相关——同属 Rohit v2 三项核心改进
[^card-2]: 与 [ripple-effect-ingest] 相关——typed links 是涟漪效应中 backlink 添加的具体形式

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "What I added from Rohit's v2" P39 -- "Typed wikilinks: instead of plain [[obsidian]], I write [[obsidian]] (uses) or [[gbrain]] (alternative-to). Six relationship types total."
