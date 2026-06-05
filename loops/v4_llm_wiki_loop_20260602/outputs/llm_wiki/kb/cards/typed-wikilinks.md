---
id: typed-wikilinks
title: 类型化 Wiki 链接
status: accepted
card_type: mechanism
tags: [llm-wiki, wikilinks, knowledge-graph, relationship-types]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
justification: ../justification/typed-wikilinks.md
canonical_concept: typed-wikilinks
aliases: [类型化链接, typed relationships, 有类型的 wikilink, 关系类型标注]
summary: >-
  typed-wikilinks（类型化链接 / typed relationships / 有类型的 wikilink / 关系类型标注）指在
  wiki 链接后附加关系类型标注（共 6 种，如 uses / alternative-to / contradicts），使知识图从
  "X 连接 Y" 升级为 "X 以何种方式关联 Y"，显著提升 LLM 回答精度
related: [wiki-compounding-artifact, schema-as-configuration]
---

类型化 Wiki 链接是 Rohit v2 引入的机制：将普通的 `[[obsidian]]` 链接升级为带关系类型的 `[[obsidian]] (uses)` 或 `[[gbrain]] (alternative-to)` 形式[^src-1]。共定义**六种关系类型**，使页面间的知识图谱从「X 与 Y 相关」升级为「X 使用 Y」「X 与 Y 矛盾」等具体语义[^src-2]。

这一机制的实践效果在使用约两个月后显现：LLM 能够给出「明显更精确的回答」（much sharper answers），因为它在遍历图谱时不仅知道节点间有连接，还能理解连接的性质[^src-3]。

作者承认该机制初始感觉「过于琐碎」（feels fussy at first），但两个月的使用经验证明了其价值[^src-4]。类型化链接本质上是将关系语义从隐含的页面内容提升到了显式的结构化元数据层面。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L56 -- "instead of plain [[obsidian]] , I write [[obsidian]] (uses) or [[gbrain]] (alternative-to)"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L56 -- "Six relationship types total."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L56 -- "by month two it lets Claude give much sharper answers because the graph isn't just 'X is connected to Y' but 'X uses Y' or 'X contradicts Y'."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L56 -- "It feels fussy at first"
