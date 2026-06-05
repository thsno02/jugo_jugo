---
id: wikibase-statement-structure
title: Statement 的复合结构
status: accepted
card_type: mechanism
tags: [wikibase, statement, snak, qualifier, reference, provenance]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
justification: ../justification/wikibase-statement-structure.md
canonical_concept: wikibase-statement-structure
aliases: [Wikibase Statement 组合, 声明结构, 主Snak+限定+引用+排名]
summary: >-
  wikibase-statement-structure（Wikibase Statement 组合 / 声明结构）一条 Statement 由 subject（主语实体）、mainSnak（核心断言）、qualifierSnaks（限定上下文如时间/角色）、referenceRecords（来源证据的 Snak 集合列表）和 rank（排名）五部分组成，实现了"断言+限定+溯源"的完整知识记录
related: [wikibase-qualifier-mechanism, wikibase-snak-triple-epistemology, wikibase-statement-ranking]
---

Wikibase 的 Statement 是表示事实性数据的核心结构，由五个组件组成 [^src-1]：

1. **subject**：Statement 所描述的 Entity（主语）。
2. **mainSnak**：Statement 最重要的部分，通常是一个 PropertyValueSnak，如"柏林的人口是 3,499,879"。
3. **qualifierSnaks**：零个或多个 PropertySnak，用于补充不直接指向主语的附加信息。例如时间范围（"奥巴马从 2005 年 1 月 3 日到 2008 年 11 月 16 日担任伊利诺伊州参议员"）或角色限定（"艾玛·沃特森饰演赫敏·格兰杰"）[^src-2]。
4. **referenceRecords**：来源引用的有序列表，每条 ReferenceRecord 是一组 Snak 的集合。最简单的情况下可以是一个 URL，也可以包含书名、作者、出版社、章节和页码等多个 Snak [^src-3]。引用列表允许为空——与维基百科一样，编辑者可以先添加无来源的声明，后续由他人补充 [^src-4]。
5. **rank**：StatementRank，用于简化 Statement 的筛选（详见排名机制卡片）。

这种复合结构的设计使得一条 Statement 不仅记录"什么是什么"，还能记录"在什么条件下是什么"（通过 qualifier）以及"根据什么来源知道的"（通过 reference）。Snak 本身不包含主语——主语由 Statement 的上下文提供 [^src-5]。

## Footnotes

[^src-1]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Statements" section, lines 530-545 -- "subject: the Entity that the statement is about; mainSnak: the main Snak of the statement; rank: a StatementRank...; referenceRecords: the list of references; qualifierSnaks: optional list of additional PropertySnaks"
[^src-2]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Statements" section, lines 548-570 -- examples of qualifier Snaks with Obama, Harry Potter, and Austria
[^src-3]: `data/raw/webpage/wikibase-data-model/text.txt` -- "ReferenceRecords" section, lines 590-592 -- "In the simplest case, the source can be represented by a single Snak, e.g. providing a URL. But SourceRecords can also be more complex"
[^src-4]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Overview" section, lines 312-313 -- "the list of references is allowed to be empty (like in Wikipedia, editors can add Statements without a reference)"
[^src-5]: `data/raw/webpage/wikibase-data-model/text.txt` -- "PropertyValueSnak" section, lines 497-498 -- "Snaks do not mention the subject to which they refer; this is given by the context in which a Snak is used"
