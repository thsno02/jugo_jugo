---
id: wikibase-reference-record
title: Wikibase ReferenceRecord 的结构与语义
status: draft
card_type: data-structure
tags: [wikibase, reference, ReferenceRecord, provenance, source]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
evidence_basis: documentation
justification: ../justification/wikibase-reference-record.md
canonical_concept: wikibase-reference-record
aliases: [ReferenceRecord, SourceRecord, reference]
summary: >-
  Wikibase ReferenceRecord 存储来源信息，由一组 Snak 组成。最简形式为一个提供 URL 的 Snak，
  复杂形式可含书名/作者/出版商/章节/页码等多个 Snak。Statement 的 referenceRecords 列表可为空，
  顺序在显示主参考时有意义。WON: ReferenceRecord(Snak {Snak})。
related: [wikibase-statement-structure, wikibase-snak-types]
---

ReferenceRecord 是 Wikibase 中存储来源/证据信息的结构，本质上是一组 Snak 的集合。

**结构**：`ReferenceRecord(Snak {Snak})`——至少包含一个 Snak，可包含多个。

**复杂度光谱**：
- 最简单：单个 Snak 提供一个 URL
- 复杂：多个 Snak 分别表示书名、作者、出版商、章节、页码等

**在 Statement 中的角色**：
- Statement 的 referenceRecords 列表允许为空（编辑者可先添加无来源的 Statement）
- 列表顺序有意义——尤其在显示主参考时
- 类比 Wikipedia：他人可后续补充合适的参考[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "ReferenceRecords" P165-167 -- "ReferenceRecords are intended to store information about some source, represented as a set of Snaks"
[^card-1]: 参见 [wikibase-statement-structure] 了解 ReferenceRecord 在 Statement 中的位置
