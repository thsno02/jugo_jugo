---
id: wikibase-snak-types
title: Wikibase Snak 的三种类型与语义
status: accepted
card_type: concept-definition
tags:
- wikibase
- snak
- PropertyValueSnak
- PropertyNoValueSnak
- PropertySomeValueSnak
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- wikibase-data-model
evidence_basis: documentation
justification: ../justification/wikibase-snak-types.md
canonical_concept: wikibase-snak-types
aliases:
- Snak
- PropertySnak
- PropertyValueSnak
- PropertyNoValueSnak
- PropertySomeValueSnak
summary: Snak 是 Wikibase 的基本信息单元。三种类型：PropertyValueSnak（断言 Entity 对某 Property 有特定值）、 PropertyNoValueSnak（断言确实无值，区别于"尚未录入"）、PropertySomeValueSnak（断言存在某值但未知）。 当前所有 Snak 均为 PropertySnak，未来可能扩展其他类型。术语 Snak
  仅对开发者相关，编辑者不会接触。
related:
- wikibase-statement-structure
- wikibase-property
- wikibase-qualifier-snaks
- wikibase-reference-record
---
Snak 是 Wikibase 数据模型中描述 Entity 的基本信息结构，是 Statement 的组成部件。"Snak" 一词仅对开发者有意义（"小于一个 byte"的双关），编辑者不会接触此术语。

当前所有 Snak 均为 PropertySnak，分三种子类型：

1. **PropertyValueSnak**——断言 Entity 对某 Property 持有特定 Value
   - 示例："Berlin 的 population 为 3,499,879"
   - WON：`PropertyValueSnak(Property Value)`

2. **PropertyNoValueSnak**——断言 Entity 对某 Property 确实没有值
   - 关键区别：不同于"值尚未录入"
   - 示例："Circle 没有 angle"
   - 仅在否则可能被误解为不完整时使用

3. **PropertySomeValueSnak**——断言 Entity 对某 Property 存在某值但该值未知
   - 示例："Ambrose Bierce 有死亡日期但不明"
   - 仅在无具体值可给出时使用

Snak 本身不指定 subject——subject 由使用 Snak 的上下文（通常是 Statement）给出。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Snaks" P102-131 -- "Snaks are the basic information structures used to describe Entities in Wikidata"
[^card-1]: 参见 [wikibase-statement-structure] 了解 Snak 在 Statement 中的组合方式
