---
id: wikibase-entity-description
title: EntityDescription 的多语言数据容器
status: accepted
card_type: mechanism
tags: [wikibase, entity-description, label, alias, multilingual, disambiguation]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
justification: ../justification/wikibase-entity-description.md
canonical_concept: wikibase-entity-description
aliases: [EntityDescription, ItemDescription, PropertyDescription, 实体描述容器]
summary: >-
  wikibase-entity-description（EntityDescription / ItemDescription / PropertyDescription / 实体描述容器）EntityDescription 为每个实体聚合 Statements 和多语言词汇信息（label/description/aliases），其中 label+description 在 Item 中构成给定语言下的唯一键，label 在 Property 中即为该属性的"名称"
related: [wikibase-entity-value-hierarchy, wikibase-statement-structure]
---

EntityDescription 是 Wikibase 中聚合实体所有信息的数据容器，分为 ItemDescription 和 PropertyDescription 两个子类型 [^src-1]。它包含两部分内容：

**Statements 集合**：关于该实体的所有声明，其中每条 Statement 的主语必须是该 EntityDescription 对应的 Entity [^src-2]。

**多语言词汇信息**，包括三种类型 [^src-3]：
- **label**：实体在各语言中的主要标签，如英语的"Georgia"。每种语言至多一个。
- **description**：用于消歧义的简短描述，如"a country in the Caucasus"。主要用途是在多个同名实体间帮助用户选择。每种语言至多一个。
- **aliases**：各语言的替代标签，主要用于按名称搜索。每种语言可以有任意数量。

label 和 description 使用 MultilingualTextValue 表示，aliases 使用 MultilingualMultiTextValue 表示。

这些词汇信息还可以用作唯一键 [^src-4]：
- 对于 ItemDescription：label + description 的组合在给定语言下构成唯一键（前提是两者都已定义）。
- 对于 PropertyDescription：label 本身即为给定语言下的唯一键，因此 label 也被称为该 Property 的"名称"。

文档还列出了多项 PropertyDescription 的计划扩展功能，包括：长描述、"自明性"标志（标记不需要引用的声明类型如 IMDB URL）、IRI 前缀映射、与 Dublin Core / FOAF 等标准词汇的等价映射、以及 qualifier Snaks 的推荐提示 [^src-5]。

## Footnotes

[^src-1]: `data/raw/webpage/wikibase-data-model/text.txt` -- "EntityDescriptions" section, lines 596-598 -- "EntityDescriptions are collections of information about an entity, and they mainly serve as data containers"
[^src-2]: `data/raw/webpage/wikibase-data-model/text.txt` -- "EntityDescriptions" section, lines 599-600 -- "all Statements of an ItemDescription must use the expected Item as the subject of their main Snak"
[^src-3]: `data/raw/webpage/wikibase-data-model/text.txt` -- "EntityDescriptions" section, lines 609-616 -- "label: the main label... description: a brief description to clarify the meaning of the label... alias: alternative labels in various languages"
[^src-4]: `data/raw/webpage/wikibase-data-model/text.txt` -- "EntityDescriptions" section, lines 617-622 -- "For ItemDescriptions, the combination of label and description is a key... For PropertyDescriptions, the label is a key"
[^src-5]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Planned Feature" section, lines 629-643 -- 计划扩展的 PropertyDescription 功能列表
