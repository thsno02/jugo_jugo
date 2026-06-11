---
id: wikibase-sitelink-badge-model
title: Sitelink 的一对一约束与 Badge 扩展
status: accepted
card_type: mechanism
tags: [wikibase, sitelink, interwiki, badge, wikipedia, item-identity]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
justification: ../justification/wikibase-sitelink-badge-model.md
canonical_concept: wikibase-sitelink-badge-model
aliases: [Sitelink, 站点链接, 跨语言链接, Badge 标记]
summary: >-
  wikibase-sitelink-badge-model（Sitelink / 站点链接 / Badge 标记）Wikibase 的 Item 通过 Sitelink 连接到外部 wiki 页面，核心约束是每个 Item 对同一 wiki 至多一条 Sitelink（一对一映射），并可附加 Badge（如"优良条目"标记，以 Item 表示）；Item 代表"维基页面讨论的事物"而非页面本身
related: [wikibase-entity-value-hierarchy, wikibase-entity-description]
---

Wikibase 的 Item 通过 Sitelink 机制连接到外部 wiki（如各语言维基百科）上的页面 [^src-1]。这一机制有三个关键设计特征：

**一对一约束**：一个 Item 可以有多条 Sitelink 指向不同的 wiki，但对同一个 wiki 至多只能有一条 Sitelink [^src-2]。这反映了 Wikidata 的核心设计原则——维基百科使用 Sitelink 来链接同一文章的不同语言版本（因为不同语言的维基百科在技术上是独立的 wiki）。

**Badge 附加**：每条 Sitelink 可以关联一组 Badge（如"优良条目"、"特色条目"标记）。Badge 本身也以 Item 表示 [^src-3]。

**Item 与页面的语义区分**：Item 代表"维基页面所讨论的事物"，而非维基页面本身 [^src-4]。例如柏林的 Item 代表柏林这座城市，而非英语维基百科中关于柏林的文章。Wikidata 关心的是记录文章**主题**的事实。

这一语义区分还延伸到数据的归属原则：一个 Item 应完整表示一个事物的所有信息，不应将关于同一主题的数据分散到多个 Item [^src-5]。例如"柏林历史"的 Item 应存储关于该历史的数据（如果有的话），而不是关于柏林（城市）的数据。这也有助于跨语言数据整合——许多语言没有关于柏林历史的独立文章，但大多数有关于柏林的文章。

## Footnotes

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Sitelinks" section, line 89 -- "An Item can be linked to pages on other wikis via sitelinks"
[^src-2]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Sitelinks" section, line 90 -- "while an Item can have multiple sitelinks to different wikis, it cannot have multiple sitelinks to the same wiki"
[^src-3]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Sitelinks" section, line 90 -- "Sitelinks can additionally have a set of 'badges' associated with the page (such as 'featured article'). Badges are also represented as Items"
[^src-4]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Overview" section, line 27 -- "The Wikidata Item for Berlin would represent the thing that the Wikipedia article is about, not the Wikipedia article itself"
[^src-5]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Items" section, line 88 -- "It is not intended that data about one subject is distributed across multiple Wikidata Items: each Item fully represents one thing"
