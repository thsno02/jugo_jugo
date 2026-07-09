---
id: wikibase-property-weak-typing
title: Wikibase Property 弱类型设计决策
status: draft
card_type: design-rationale
tags: [wikibase, property, datatype, weak-typing, schema-evolution]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
evidence_basis: documentation
justification: ../justification/wikibase-property-weak-typing.md
canonical_concept: wikibase-property-weak-typing
aliases: [Property weak typing, non-strict typing, Datatype flexibility]
summary: >-
  Wikibase 数据模型不强制 Snak 中的 Value 匹配 Property 当前声明的 Datatype。原因：Datatype 可能
  被更改，无法立即更新所有已存储数据；若 Datatype 改回则旧数据可继续使用。UI/API 通常仅允许匹配
  当前 Datatype 的值，但模型层面不做限制。模型也不为每个 Property 定义唯一 Datatype。
related: [wikibase-property, wikibase-datatype]
---

Wikibase 数据模型在 Property 类型约束上采取弱类型（non-strict typing）设计：

**核心规则**：PropertyValueSnak 不要求其 Value 属于 Property 当前声明的 Datatype。

**设计理由**：
1. Datatype 可能被更改——此时无法立即更新所有已存储数据
2. 若 Datatype 被改回原值——未被修改的旧数据可继续使用而不丢失

**层次分离**：
- **数据模型层**：不限制 Value 类型
- **UI/API 层**：通常仅允许用户输入匹配当前 Datatype 的值

**进一步说明**：数据模型实际上并不为每个 Property 定义唯一的 Datatype——它仅规定 Datatype 赋值如何表示。唯一的 Datatype 仅在封闭系统中（每个 Property 都有全局唯一 Datatype 赋值时）才成立。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "PropertyValueSnak" P109-110 -- "it is not required that Value belongs to the Datatype that is currently given to the Property ... if the Datatype is changed, then it will not be possible to update all stored data immediately"
[^card-1]: 参见 [wikibase-property] 了解 Property 的基本定义
