---
id: wikibase-snak-triple-epistemology
title: Snak 的三种认识论状态
status: accepted
card_type: distinction
tags: [wikibase, snak, epistemology, open-world-assumption, data-completeness]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
justification: ../justification/wikibase-snak-triple-epistemology.md
canonical_concept: wikibase-snak-triple-epistemology
aliases: [Snak 三类型, PropertyValueSnak/NoValue/SomeValue, 三值断言模型]
summary: >-
  wikibase-snak-triple-epistemology（Snak 三类型 / 三值断言模型）Wikibase 用三种 Snak 编码不同的认识论状态：PropertyValueSnak（已知值）、PropertyNoValueSnak（明确无值，区别于"尚未录入"）、PropertySomeValueSnak（存在值但未知），使系统能区分数据缺失与事实缺失
related: [wikibase-entity-value-hierarchy, wikibase-statement-structure]
---

Snak 是 Wikibase 中描述实体的基本信息单元。模型定义了三种 PropertySnak 类型，每种编码一种不同的认识论状态 [^src-1]：

**PropertyValueSnak**：声明某实体对某属性有一个确定的值。例如"柏林的人口是 3,499,879" [^src-2]。值得注意的是，此 Snak 中的值不要求属于该 Property 当前声明的 Datatype——这是有意的灵活性设计 [^src-3]。

**PropertyNoValueSnak**：声明某实体对某属性明确没有值。这与"属性值尚未录入"有本质区别。例如"圆没有角"、"珠穆朗玛峰没有母峰" [^src-4]。文档特别指出，这类声明应仅在"否则可能被认为是不完整"的情况下使用，不应用于陈述所有不成立的事情（如"太平洋没有角"）[^src-5]。

**PropertySomeValueSnak**：声明某实体对某属性有值，但具体值未知。例如"安布罗斯·比尔斯有一个未知的死亡日期，但可以确定他不在世" [^src-6]。这使系统能在不知道具体值的情况下记录"值存在"这一事实。

这三种 Snak 的设计使 Wikidata 能在开放世界假设下精确区分三种状态：已知值、已知无值、以及已知有值但值未知。Snak 这个术语本身不会面向编辑者，但对开发者区分 Snak 与 Statement 至关重要 [^src-7]。

## Footnotes

[^src-1]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Snaks" section, lines 464-475 -- "Snaks are the basic information structures used to describe Entities in Wikidata... PropertySnak := PropertyValueSnak | PropertySomeValueSnak | PropertyNoValueSnak"
[^src-2]: `data/raw/webpage/wikibase-data-model/text.txt` -- "PropertyValueSnak" section, lines 490-498 -- "Berlin (subject) has a population (property) of 3499879 (value)"
[^src-3]: `data/raw/webpage/wikibase-data-model/text.txt` -- "PropertyValueSnak" section, lines 480-482 -- "it is not required that Value belongs to the Datatype that is currently given to the Property in the system"
[^src-4]: `data/raw/webpage/wikibase-data-model/text.txt` -- "PropertyNoValueSnak" section, lines 508-510 -- "Circle (subject) has no angle (property). Mount Everest (subject) has no parent peak (property)"
[^src-5]: `data/raw/webpage/wikibase-data-model/text.txt` -- "PropertyNoValueSnak" section, lines 511-513 -- "Such statements should only be made in cases where one could otherwise expect an incompleteness. It is not intended that Wikidata stores all things that are not the case"
[^src-6]: `data/raw/webpage/wikibase-data-model/text.txt` -- "PropertySomeValueSnak" section, lines 523-525 -- "Ambrose Bierce (subject) has an unknown date of death (property), yet we can be certain that he is not among the living persons"
[^src-7]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Overview" section, line 319 -- "any such basic assertion that one can make in Wikidata is called a Snak... This term will not be relevant for using Wikidata (editors will not encounter it), but it is relevant for developers"
