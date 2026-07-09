---
id: wikibase-statement-structure
title: Wikibase Statement 的完整结构
status: accepted
card_type: data-structure
tags:
- wikibase
- statement
- claim
- mainSnak
- qualifier
- reference
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- wikibase-data-model
evidence_basis: documentation
justification: ../justification/wikibase-statement-structure.md
canonical_concept: wikibase-statement-structure
aliases:
- Statement
- Wikibase Statement
- claim
summary: 'Wikibase Statement 的完整结构：subject（Entity）+ mainSnak + rank（StatementRank）+ referenceRecords（ReferenceRecord 列表）+ qualifierSnaks（PropertySnak 列表）。 mainSnak 是核心断言，qualifierSnaks 修饰主断言（时间范围/角色等），referenceRecords
  提供来源。 WON: Statement(Entity Snak {PropertySnak} {ReferenceRecord} Rank)。'
related:
- wikibase-snak-types
- wikibase-statement-rank
- wikibase-reference-record
- wikibase-qualifier-snaks
---

Statement 是 Wikibase 中表达事实性数据的主要结构，由以下组件构成：

| 组件 | 类型 | 含义 |
|------|------|------|
| subject | Entity | Statement 所描述的实体 |
| mainSnak | Snak | 核心断言 |
| rank | StatementRank | 用于简化选择/过滤的优先级标记 |
| referenceRecords | ReferenceRecord 列表 | 来源证据（可为空，顺序有意义） |
| qualifierSnaks | PropertySnak 列表 | 修饰主断言的附加信息 |

WON 表示：`Statement(Entity Snak {PropertySnak} {ReferenceRecord} Rank)`

Statement 由两部分组成概念：一个 claim（声称某事为真）和一组 references（为该声称提供证据）。referenceRecords 列表允许为空——类似 Wikipedia，编辑者可先添加无来源的 Statement，后由他人补充。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Statements" P132-140 -- "Statements describe the claim of a statement and list references for this claim"
[^card-1]: 参见 [wikibase-snak-types] 了解 Statement 内 Snak 的类型
