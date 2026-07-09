---
id: wikibase-entity-identity
title: Wikibase Entity 与 DataValue 的标识差异
status: accepted
card_type: concept-definition
tags:
- wikibase
- entity
- datavalue
- IRI
- identity
- value
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- wikibase-data-model
evidence_basis: documentation
justification: ../justification/wikibase-entity-identity.md
canonical_concept: wikibase-entity-datavalue-distinction
aliases:
- Entity vs DataValue
- Value types
- Entity identity
summary: Wikibase Value 分为 Entity（有全局唯一 IRI，可作 Snak subject）和 DataValue（无 IRI，靠内容/哈希标识， 不能作 Snak subject）。Entity 包括 Item/Property/Datatype；DataValue 包括 QuantityValue/TimeValue/ StringValue 等。Wikidata 不打算对数据值本身（如数字/字符串）存储
  Statement。
related:
- wikibase-item
- wikibase-property
- wikibase-datatype
---

Wikibase 将 Value（值）分为两大类，其核心区别在于标识方式和可寻址性：

**Entity**（实体）：
- 以全局唯一 IRI 标识（如 `https://www.wikidata.org/entity/Q{n}`）
- 可作为 Snak 的 subject（即可以"关于它"做出断言）
- 包括：Item、Property、Datatype
- 不同 Entity 不共享 IRI

**DataValue**（数据值）：
- 无 IRI，靠内容本身（或其哈希）标识
- 不能作为 Snak 的 subject
- 包括：QuantityValue、TimeValue、GlobeCoordinateValue、StringValue、MonolingualTextValue、MultilingualTextValue 等

**设计意图**：Wikidata 不打算对单个数据值（如字符串、数字）存储 Statement。但如果某个数字作为 Wikipedia 页面讨论的概念存在，则该概念可由一个 Item 表示（此时 Item 代表的是该概念，而非数字本身）。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Values" P74-82 -- "Various kinds of Values can be the subject of basic statements (Snaks): they are called Entities. Entities are identified in a uniform way using ... IRIs"
[^card-1]: 参见 [wikibase-item] 和 [wikibase-property] 了解具体 Entity 类型
