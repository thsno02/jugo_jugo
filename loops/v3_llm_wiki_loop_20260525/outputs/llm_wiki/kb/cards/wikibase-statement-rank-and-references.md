---
id: wikibase-statement-rank-and-references
title: Statement 的 Rank 与 ReferenceRecord——并存多值的筛选机制
status: accepted
card_type: mechanism
tags: [#wikibase, #wikidata, #rank, #citation]
created_time: 2026-05-26T15:20:00+08:00
edited_time: 2026-05-28T12:15:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
provenance_card: ../provenance/wikibase-statement-rank-and-references.md
aliases: [preferred / normal / deprecated rank, best rank]
related: [wikibase-item-property-snak-statement, wikibase-three-snak-types, wikibase-conceptual-not-serialization, llm-wiki-karpathy-lint-grounding-trail, llm-wiki-contradictions-are-assets, zep-bi-temporal-edges]
---

## Rank 的三级与"best rank"

Wikibase 允许同一 Item 对同一 Property 有多条 Statement（不同来源、不同时间点的人口数据）。**Rank** 用于在不修改任何 Statement 的前提下做筛选：

- **preferred**：最重要、最新的信息，下游默认采用（Wikipedia infobox 通常只显示 preferred）。一个 property 可以有多个 preferred（如人的多个孩子、不同来源的不同人口数）。
- **normal**：相关、可信、但因数量多而不默认显示（如 Berlin 历年人口）。
- **deprecated**：已知不可靠或有错的（如沿用一个被证伪的历史文献的人口数）。注意：deprecated 不代表 statement 本身错——它表示"那个历史文献确实这样写了，但今天不该用"。

**Best rank 规则**：对某个 Property，若至少有一条 preferred，则该 property 的 best rank 是 preferred；否则是 normal。"Best statements" = 取 best rank 的所有 statements。Wikidata API 输出"当前值"时通常用这条规则筛选。

Rank 设计**故意只有三级**——更细只会让 UI 更复杂；少于三级又无法同时表达"有错"与"可疑"。

## ReferenceRecord：结构化的引用

每条 Statement 还可挂任意条 `ReferenceRecord`：

`ReferenceRecord := 'ReferenceRecord(' Snak { Snak } ')'`

也就是说**每条 reference 本身就是一组 Snak**——可以只放一个"source URL" Snak，也可以放"title / author / publisher / chapter / page" 多个 Snak。这把"引用"从一段自由文本提升到结构化数据，使下游能把"未引用 vs 引用了哪本书第几页" 区分得清清楚楚。

Reference 列表允许为空——Wikipedia 风格的"先记下，等别人补 ref"。

## 边界

- Rank 不是访问权限——但维护界面通常只保护 preferred / normal statements，deprecated 允许更自由修改。
- 同时有两个 preferred 值不是"冲突未解决"——可能表达"多值属性"（孩子）或"存在多个权威来源给不同数"（公开未达成共识）。下游应处理而不是默认取一个。
- 第 7.2 节末尾标记的"Best Rank"概念在 RDF/JSON 序列化里不一定显式存在，需 API 计算。

## References

- Rank 三级 + best rank：`data/raw/webpage/wikibase-data-model/text.txt` 第 575-585 行（§7.1）。
- Reference 结构 BNF + 允许为空：第 588-592 行（§7.2）+ 第 313 行（Overview 提到 "the list of references is allowed to be empty"）。

## Footnotes

- Preferred 多值定义："Note that there may be multiple preferred statements. This may imply a multi-valued property (e.g. a person's children), or a disagreement (diverging population figures given by different sources)."（第 577 行）
- Deprecated 不代表 statement 错："Deprecated statements that may not be considered reliable or that are even known to contain errors (example: a statement that documents a wrong population figure that was published in some historic document; in this case the statement is not wrong – the historic document that is given as a reference really made the erroneous claim – yet the statement should not be used in most cases)."（第 581 行）
- 故意只有三级的设计意图："This model is intentionally left coarse and simple. ... More fine-grained rankings do not seem to have such a clear interpretation and would thus increase the UI complexity unnecessarily."（第 583 行）
