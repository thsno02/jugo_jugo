---
id: wikibase-datatype
title: Wikibase Datatype 的定义与系统可扩展性
status: accepted
card_type: concept-definition
tags:
- wikibase
- datatype
- entity
- system-defined
- extensibility
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- wikibase-data-model
evidence_basis: documentation
justification: ../justification/wikibase-datatype.md
canonical_concept: wikibase-datatype
aliases:
- Datatype
- Wikibase Datatype
- data type
summary: Wikibase Datatype 是 Entity 子类型，以固定 IRI 标识，决定 Property Value 的格式和形状。 Datatype 集合为系统定义，仅开发者可扩展（编辑者不能在站点上添加）。每种 Datatype 需软件 专门处理（如 UI 区别）。多数 Datatype 非原始类型，具有内部结构（如地理坐标含经纬度）。
related:
- wikibase-property
- wikibase-property-weak-typing
- wikibase-quantity-value
- wikibase-time-value
- wikibase-entity-identity
- wikibase-globe-coordinate-value
- wikibase-multilingual-text
---
Datatype 是 Wikibase 中的 Entity 子类型，决定可赋给 Property 的值的类型和形状。

**关键特征**：
- 以系统定义的固定 IRI 标识
- 集合仅由开发者扩展（编辑者不能在站点上添加新 Datatype）
- 每种 Datatype 需软件专门处理（如不同 UI、不同验证逻辑）
- 可能允许在关联 Property 时做一定定制（如限制仅接受整数）

**非原始性**：多数 Datatype 的值不是单个编程语言原始类型。例如地理坐标具有内部结构（经度、纬度、可能的海拔），QuantityValue 包含主值、上下界和单位。

**已定义的 DataValue 类型**：QuantityValue、StringValue、TimeValue、GeoCoordinateValue、GeoShapeValue、MediaValue、IriValue、MonolingualTextValue、MultilingualTextValue。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Datatypes" P96-99 -- "A Datatype is an Entity that determines the type and shape of the values that can be assigned to a Property"
[^card-1]: 参见 [wikibase-property] 了解 Datatype 与 Property 的关系
