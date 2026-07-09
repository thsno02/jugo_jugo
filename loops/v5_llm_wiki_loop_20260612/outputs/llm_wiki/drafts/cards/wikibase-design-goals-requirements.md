---
id: wikibase-design-goals-requirements
title: Wikibase 数据模型的六大设计目标
status: draft
card_type: design-rationale
tags: [wikibase, design-goals, requirements, extensibility, coverage]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
evidence_basis: documentation
justification: ../justification/wikibase-design-goals-requirements.md
canonical_concept: wikibase-design-goals
aliases: [Wikibase design goals, Wikibase requirements]
summary: >-
  Wikibase 数据模型的六大设计目标：Coverage（覆盖 Wikipedia 重要数据）、Simplicity（不过度复杂）、
  Extensibility（允许未来扩展）、Flexibility（支持多用途复用）、Exchange（系统外数据语义明确）、
  Technical support（可在 JSON/RDF/OWL 中充分表示）。这些目标有时互相冲突，需平衡取舍。
related: [wikibase-conceptual-data-model]
---

Wikibase 数据模型在设计时需平衡以下六大目标（有时互相冲突）：

1. **Coverage**——以自然方式捕获 Wikipedia 中的重要数据
2. **Simplicity**——避免过度复杂
3. **Extensibility**——允许未来扩展
4. **Flexibility**——支持数据的多用途访问和复用，不限于单一系统上下文
5. **Exchange**——数据（或其部分）可交换，且在 Wikidata 系统外仍有明确含义
6. **Technical support**——允许在 JSON、RDF/OWL 等既有格式中充分表示

此外，文档还有两个主要的元目标：概念清晰性（明确 Wikibase 能和不能捕获什么）和技术文档化（为开发者提供对数据的共识理解）。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Goals and requirements" P13-19 -- "There are a number of (sometimes conflicting) requirements that the data model should address in a balanced fashion"
[^card-1]: 参见 [wikibase-conceptual-data-model] 了解模型整体定位
