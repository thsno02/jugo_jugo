---
id: wikibase-entity-description
title: Wikibase EntityDescription 的多语言结构
status: draft
card_type: data-structure
tags: [wikibase, EntityDescription, ItemDescription, PropertyDescription, label, description, alias, multilingual]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
evidence_basis: documentation
justification: ../justification/wikibase-entity-description.md
canonical_concept: wikibase-entity-description
aliases: [EntityDescription, ItemDescription, PropertyDescription, entity description]
summary: >-
  Wikibase EntityDescription 聚合 Entity 的全部信息，支持 labels（MultilingualTextValue，主显示名）、
  descriptions（MultilingualTextValue，消歧简介）、aliases（MultilingualMultiTextValue，搜索用）、
  Statements。ItemDescription 唯一键为 label+description（单语言），PropertyDescription 唯一键为
  label（单语言）。PropertyDescription label 亦称 property 的"name"。
related: [wikibase-item, wikibase-property, wikibase-multilingual-text]
---

EntityDescription 是关于某个 Entity 的全部信息集合，主要作为数据容器。分为 ItemDescription 和 PropertyDescription 两个子类型。

**多语言支持三层结构**：

| 信息类型 | 数据类型 | 基数（每语言） | 用途 |
|---------|---------|-------------|------|
| label | MultilingualTextValue | 至多 1 个 | 主显示名称 |
| description | MultilingualTextValue | 至多 1 个 | 消歧简介（与 label 并列显示） |
| aliases | MultilingualMultiTextValue | 0 或多个 | 搜索用替代名称 |

**唯一键规则**：
- ItemDescription：label + description 组合为单语言唯一键（两者都存在时）
- PropertyDescription：label 为单语言唯一键（因此 label 也被称为 Property 的 "name"）
- 计划功能：PropertyDescription 的任何 alias 也将成为唯一键

**结构**：
- `ItemDescription(Item [label] [description] [aliases] {Statement})`
- `PropertyDescription(Property [label] [description] [aliases] {Statement})`

所有 Statement 的 subject 必须为对应的 Item 或 Property。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "EntityDescriptions of Items and Properties" P168-181 -- "EntityDescriptions are collections of information about an entity"
[^card-1]: 参见 [wikibase-item] 和 [wikibase-property] 了解两种 Entity 类型
