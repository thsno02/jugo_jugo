---
id: wikibase-multilingual-text
title: Wikibase 多语言文本值的层次结构
status: draft
card_type: data-structure
tags: [wikibase, MonolingualTextValue, MultilingualTextValue, MultilingualMultiTextValue, i18n]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
evidence_basis: documentation
justification: ../justification/wikibase-multilingual-text.md
canonical_concept: wikibase-multilingual-text-values
aliases: [MonolingualTextValue, MultilingualTextValue, MultilingualMultiTextValue, multilingual text]
summary: >-
  Wikibase 多语言文本三层结构：MonolingualTextValue（language+value，单语言单短语）、
  MultilingualTextValue（MonolingualTextValue 列表，每语言至多一个，表示直接翻译关系）、
  MultilingualMultiTextValue（MonolingualMultiTextValue 列表，每语言可多个短语，无跨语言对应关系）。
  语言标识使用 UserLanguageCode（类似 BCP 47 但非完全相同）。
related: [wikibase-entity-description, wikibase-datatype]
---

Wikibase 定义了三层多语言文本值结构：

**MonolingualTextValue**——单语言单短语：
- 属性：language（UserLanguageCode）+ value（String）
- 内容可被发音、可关联音频
- WON：`MonolingualTextValue(UserLanguageCode String)`

**MultilingualTextValue**——多语言单短语（互为翻译）：
- 由 MonolingualTextValue 列表组成，每个 UserLanguageCode 至多一条
- 语义：所有条目是直接翻译关系
- 用于 EntityDescription 的 label 和 description
- WON：`MultilingualTextValue({MonolingualTextValue})`

**MultilingualMultiTextValue**——多语言多短语（无跨语言对应）：
- 由 MonolingualMultiTextValue 列表组成，每语言可有多个 String
- 各语言的短语列表之间无暗示对应关系
- 用于 EntityDescription 的 aliases
- WON：`MultilingualMultiTextValue({MonolingualMultiTextValue})`

**语言标识**：使用 UserLanguageCode（基于 Wikipedia 用户语言偏好设置，比 GlobalSiteIdentifier 更细粒度，类似 BCP 47 但不完全相同）。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Monolingual texts" / "Multilingual texts" / "Multilingual multi-texts" P251-264 -- "MultilingualTextValues are Values that represent a phrase in many languages"
[^card-1]: 参见 [wikibase-entity-description] 了解这些文本类型在 EntityDescription 中的使用
