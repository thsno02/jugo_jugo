---
id: inventory-evidence-separation
title: 清单与证据的刻意分离
status: accepted
card_type: distinction
tags: [llm-wiki, inventory, evidence, operational-state]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
justification: ../justification/inventory-evidence-separation.md
canonical_concept: inventory-evidence-separation
aliases: [清单证据分离, inventory vs evidence, 操作状态与事实证据, inventory separation]
summary: >-
  inventory-evidence-separation（清单证据分离 / inventory vs evidence / 操作状态与事实证据 / inventory separation）
  是 LLM Wiki 的设计区分：inventory/ 存放操作状态（物品/来源候选/语料/实体/待办），
  刻意不作为事实主张的证据，与 raw/+wiki/ 的证据链保持边界
related: [audit-provenance-tracing, three-layer-architecture]
---

LLM Wiki 在 `inventory/` 和证据体系（`raw/` + `wiki/`）之间划定了**刻意的边界**[^src-1]。

**Inventory 的定位是操作状态（operational state）**，用于追踪持久性事物：实际物品（items）、来源候选（source candidates）、语料（corpora）、实体（entities）、待解问题（open questions）、监视项（watch items）和下一步行动（next actions）[^src-2]。

关键设计决策在于：inventory **刻意不是事实主张的证据**[^src-3]。这意味着当 wiki 文章引用来源支撑一个论点时，它追溯到 `raw/` 中的不可变来源，而不是 `inventory/` 中的操作记录。Inventory 的内容可以被列出和重访，但不会污染证据链。

同理，**dataset manifests** 也遵循类似的分离原则——它们索引大型外部数据而不将其复制进来源语料库，wiki 成为数据的接口而数据留在原处[^src-4]。

这一分离的实际意义在于：审计溯源机制仅需沿证据链（raw->wiki->output）工作，inventory 的操作状态不会干扰溯源路径[^card-1]。从架构视角看，inventory 是三层架构之外的第四种关注——它与 raw/wiki/schema 的证据层级平行存在但刻意不交叉[^card-2]。

## Footnotes

[^src-1]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Inventory is state" L154-156 -- "Parts, source queues, corpora, watch items, and next actions live under inventory/ so they can be listed and revisited without becoming evidence."
[^src-2]: `data/raw/webpage/llm-wiki-net/text.txt` -- "How the wiki works" L316-317 -- "Inventory (inventory/) is for durable operational state: actual items, source candidates, corpora, entities, open questions, tasks, watch items, and next actions. It is intentionally not evidence for factual claims."
[^src-3]: `data/raw/webpage/llm-wiki-net/text.txt` -- "How the wiki works" L317 -- "It is intentionally not evidence for factual claims."
[^src-4]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Datasets stay external" L158-160 -- "datasets/ stores manifests, samples, profiles, and query recipes for large data. The wiki indexes data without copying it into the source corpus."
[^card-1]: [审计与溯源追踪](audit-provenance-tracing.md) -- 本卡解释 inventory 被排除在证据体系之外，该卡描述仅沿证据链（raw->wiki->output）工作的审计机制
[^card-2]: [三层架构](three-layer-architecture.md) -- 本卡描述 inventory 作为操作状态的独立关注，该卡定义 raw/wiki/schema 三层证据架构，inventory 是三层之外的第四种关注
