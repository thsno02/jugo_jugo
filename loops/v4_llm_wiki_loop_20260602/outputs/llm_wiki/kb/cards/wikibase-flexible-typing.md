---
id: wikibase-flexible-typing
title: Property 的非严格类型设计
status: accepted
card_type: concept
tags: [wikibase, typing, property, datatype, schema-evolution, flexibility]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
justification: ../justification/wikibase-flexible-typing.md
canonical_concept: wikibase-flexible-typing
aliases: [非严格类型, Property 弹性类型, Wikibase 类型灵活性]
summary: >-
  wikibase-flexible-typing（非严格类型 / Property 弹性类型）Wikibase 数据模型有意不要求 Snak 中的 Value 严格匹配 Property 声明的 Datatype：UI/API 层面强制类型一致，但底层模型允许不匹配，以应对 Datatype 变更后旧数据无法即时全量更新的现实
related: [wikibase-entity-value-hierarchy, wikibase-snak-triple-epistemology]
---

Wikibase 数据模型在 Property 的类型约束上做了一个重要的灵活性设计：虽然每个 Property 可以声明一个 Datatype 来指定其值的类型和格式，但在 Snak 层面，并不要求 Value 严格属于该 Property 当前声明的 Datatype [^src-1]。

这一设计的核心理由是实际运维中的类型变更场景。文档给出两点论证 [^src-2]：

1. **变更后的存量数据问题**：如果一个 Property 的 Datatype 被修改，已经存储的数据不可能立即全部更新为新类型。
2. **回滚兼容性**：如果 Datatype 随后被改回原来的值，原有的未被修改的数据可以继续使用。

在实际操作中，Wikidata 的 UI 和 API 通常只允许输入匹配当前 Datatype 的值 [^src-3]，因此类型一致性在用户界面层面得到保证。模型层面的灵活性是一种"安全网"设计。

文档进一步指出，数据模型实际上"并未为每个 Property 定义唯一的 Datatype"——它只规定了 Datatype 分配如何被表示；只有在一个封闭系统中，每个 Property 拥有全局唯一的 Datatype 分配时，才能获得唯一的 Datatype [^src-4]。

## Footnotes

[^src-1]: `data/raw/webpage/wikibase-data-model/text.txt` -- "PropertyValueSnak" section, line 480 -- "it is not required that Value belongs to the Datatype that is currently given to the Property in the system"
[^src-2]: `data/raw/webpage/wikibase-data-model/text.txt` -- "PropertyValueSnak" section, lines 480-482 -- "if the Datatype is changed, then it will not be possible to update all stored data immediately. Moreover, if the Datatype is changed back to its earlier value, it might be possible to continue using existing data"
[^src-3]: `data/raw/webpage/wikibase-data-model/text.txt` -- "PropertyValueSnak" section, line 480 -- "the UI and API of Wikidata will only allow Values that match the given Datatype"
[^src-4]: `data/raw/webpage/wikibase-data-model/text.txt` -- "PropertyValueSnak" section, lines 482-483 -- "the data model does not actually define a unique Datatype for each Property: it just specifies how Datatype assignments would be represented"
