---
id: wikibase-item
title: Wikibase Item 的定义与语义
status: draft
card_type: concept-definition
tags: [wikibase, item, entity, wikidata, Q-identifier]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
evidence_basis: documentation
justification: ../justification/wikibase-item.md
canonical_concept: wikibase-item
aliases: [Item, Wikidata Item, Q-item]
summary: >-
  Wikibase Item 是 Entity 子类型，代表 Wikipedia 页面所描述的事物（非页面本身）。
  以 IRI（形如 Q{n}）全局唯一标识。Item 的确切含义由编辑社区决定，可有多重语义面向。
  核心原则：每个 Item 完整代表一个事物，信息不跨 Item 分散。
related: [wikibase-property, wikibase-entity-identity, wikibase-sitelink]
---

Item 是 Wikibase 中的 Entity 子类型，代表 Wikipedia 页面所描述的事物——是页面的主题而非页面本身。Item 可以是：

- 个体事物（如 Albert Einstein）
- 事物的类（如所有物理学家的类）
- 任何作为 Wikipedia 页面主题的概念（如 History of Berlin）

**标识**：Item 以 IRI 标识，形如 `https://www.wikidata.org/entity/Q{n}`，内部使用短 ID 字符串如 "Q1234567890"。ID 创建后应保持稳定。

**语义模糊性**：Item 的确切含义不由系统捕获，而由编辑社区讨论决定。一个 Item 可有多重"面向"——例如 Orca 既可视为所有虎鲸的类，又可作为关于该物种的个体概念。

**主题原则**：Item 存储的信息应关于其主题本身。History of Berlin 应存历史相关数据而非柏林城市数据。每个 Item 完整代表一个事物，不将数据分散至多个 Item。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Items" P85-88 -- "Items are Entities that are typically represented by a Wikipage ... it is intended that the information stored in Wikidata is generally about the topic of the Item"
[^card-1]: 参见 [wikibase-property] 了解与 Item 对比的 Property 概念
