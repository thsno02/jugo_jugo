---
id: wikibase-conceptual-data-model
title: Wikibase 概念数据模型的定位与边界
status: draft
card_type: architectural-principle
tags: [wikibase, data-model, conceptual-model, wikidata]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
evidence_basis: documentation
justification: ../justification/wikibase-conceptual-data-model.md
canonical_concept: wikibase-conceptual-data-model
aliases: [Wikibase data model, Wikibase DataModel, Wikibase conceptual model]
summary: >-
  Wikibase 数据模型（Wikibase DataModel）是概念层规范，回答"需要支持哪些信息"而非实现或序列化问题。
  序列化（JSON/RDF）和内部数据结构由独立文档规定。UML 类图描述结构但不要求实现照搬。
  模型可扩展但在任一时刻应记录系统中所有可能存储的信息。
related: [wikibase-design-goals-requirements]
---

Wikibase 数据模型是一份概念规范（conceptual model），其核心关切为"系统需要支持哪些信息"。它明确不规定：

1. **内部数据结构**——虽使用 UML 类图描述，但不要求实现中照搬类层次；具体场景可采用更优化的存储方式
2. **导出格式**——JSON 序列化和 RDF 映射分别由独立文档定义
3. **形式语义**——数据的精确形式化解释留给另外的文档

该模型具有可扩展性：在任一时间点，它应记录系统中所有可能存储的事物，但其定义集可随时间增长。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Goals and requirements" P2-4 -- "This document describes a conceptual model ('Which information do we have to support?') and does not specify how this data should be represented technically"
