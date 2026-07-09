---
id: wikibase-property
title: Wikibase Property 的定义与特征
status: accepted
card_type: concept-definition
tags:
- wikibase
- property
- entity
- P-identifier
- datatype
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- wikibase-data-model
evidence_basis: documentation
justification: ../justification/wikibase-property.md
canonical_concept: wikibase-property
aliases:
- Property
- Wikidata Property
- P-property
summary: Wikibase Property 是 Entity 子类型，描述 Entity 与 Value 之间的关系。以 IRI（形如 P{n}）标识。 Property 通常无对应 Wikipedia 页面。Property 可指定 Datatype 约束值的形式，但数据模型不强制 Snak 中的 Value 匹配 Property 当前 Datatype。PropertyDescription
  中 label 是单语言唯一键。
related:
- wikibase-item
- wikibase-datatype
- wikibase-property-weak-typing
- wikibase-entity-description
- wikibase-entity-identity
- wikibase-snak-types
---
Property 是 Wikibase 中的 Entity 子类型，描述 Entity（通常是 Item）与 Value 之间的关系。典型 Property 如 population（值为数字）、binomial name（值为字符串）、has father（值为 Item）。

**与 Item 的区别**：
1. Property 通常无对应 Wikipedia 页面——Wikipedia 的 "population" 页面讨论名词含义，不描述区域与居民数之间的关系
2. Property 可附带 Datatype 指定用户通常应输入的值类型
3. Property 的 ID 使用不同命名方案（如 "P123456789"），避免与 Item 混淆

**由用户定义**：Property 由用户创建，任何 Property 均可被定义。Property 的 ID 创建后应保持稳定。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Properties" P92-95 -- "Properties are Entities that describe a relationship between Items (or other Entities) and Values of the property"
[^card-1]: 参见 [wikibase-item] 了解与 Property 对比的 Item 概念
