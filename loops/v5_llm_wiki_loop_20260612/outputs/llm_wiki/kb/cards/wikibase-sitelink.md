---
id: wikibase-sitelink
title: Wikibase Sitelink 的约束与 Badge 扩展
status: accepted
card_type: mechanism
tags:
- wikibase
- sitelink
- badge
- cross-wiki
- interlanguage-link
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- wikibase-data-model
evidence_basis: documentation
justification: ../justification/wikibase-sitelink.md
canonical_concept: wikibase-sitelink
aliases:
- sitelink
- site link
- interlanguage link
- badge
summary: Wikibase Sitelink 将 Item 链接到外部 wiki 页面，主要用于 Wikipedia 跨语言版本关联。 约束：一个 Item 可有多个 sitelink（指向不同 wiki）但同一 wiki 至多一个。 Sitelink 可附带 badges 集合（如"featured article"），badges 本身由 Item 表示。
related:
- wikibase-item
- wikibase-entity-description
---

Sitelink 是 Wikibase 中将 Item 链接到外部 wiki 页面的机制，主要用于关联 Wikipedia 不同语言版本的同一主题文章（因不同语言的 Wikipedia 在技术上是独立 wiki）。

**约束规则**：
- 一个 Item 可以有多个 sitelink，指向不同的 wiki
- 同一个 wiki 至多只能有一个 sitelink（即不能将一个 Item 链接到同一 wiki 的两个页面）

**Badge 扩展**：
- Sitelink 可附带一组 "badges"
- Badge 表示页面的某种属性/荣誉（如 "featured article"）
- Badge 本身也用 Item 表示[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Sitelinks" P89-90 -- "An Item can be linked to pages on other wikis via sitelinks ... it cannot have multiple sitelinks to the same wiki"
[^card-1]: 参见 [wikibase-item] 了解 Sitelink 所属的 Item 概念
