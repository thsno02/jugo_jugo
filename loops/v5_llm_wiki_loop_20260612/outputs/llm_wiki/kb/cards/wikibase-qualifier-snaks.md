---
id: wikibase-qualifier-snaks
title: Wikibase Qualifier Snaks 的功能与用法
status: accepted
card_type: mechanism
tags:
- wikibase
- qualifier
- snak
- statement
- context-annotation
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- wikibase-data-model
evidence_basis: documentation
justification: ../justification/wikibase-qualifier-snaks.md
canonical_concept: wikibase-qualifier-snaks
aliases:
- qualifier Snaks
- qualifiers
- qualifier
summary: Qualifier Snaks 是 Statement 中附加的 PropertySnak 列表，修饰 mainSnak 但不直接描述 subject。 典型用途：时间范围（任期）、角色关系（饰演角色）、比例修饰（百分比）。Qualifier 可选省略。 例如 Obama 担任参议员的时间段、Emma Watson 饰演的角色。
related:
- wikibase-statement-structure
- wikibase-snak-types
---

Qualifier Snaks（限定符）是附加在 Statement mainSnak 之后的零个或多个 PropertySnak，用于对主断言进行细化修饰。它们存储的附加信息不直接描述 Statement 的 subject，而是描述 Statement 本身的上下文。

**典型用例**：

1. **时间范围**——"Obama 于 2005-01-03 至 2008-11-16 担任来自 Illinois 的参议员"
   - mainSnak: PropertyValueSnak(US Senator from, Illinois)
   - qualifier: PropertyIntervalSnak(in office, 2005-01-03 to 2008-11-16)

2. **角色关系**——"Harry Potter 中 Emma Watson 饰演 Hermione Granger"
   - mainSnak: PropertyValueSnak(starring, Emma Watson)
   - qualifier: PropertyValueSnak(played character, Hermione Granger)

3. **比例修饰**——"奥地利 1.6% 居民为土耳其人"
   - mainSnak: PropertyValueSnak(ethnic group, Turks)
   - qualifier: PropertyValueSnak(percentage, 1.6%)

**设计灵活性**：qualifier 可选省略——如已知某民族存在但比例未知时。同一信息可有多种表达方式，由社区协商统一。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Statements" P141-157 -- "qualifier Snaks (or 'qualifiers' for short) store additional information that does not directly refer to the subject"
[^card-1]: 参见 [wikibase-statement-structure] 了解 qualifier 在 Statement 中的位置
