---
id: wikibase-statement-rank
title: Wikibase Statement 三级 Rank 系统
status: draft
card_type: mechanism
tags: [wikibase, rank, preferred, normal, deprecated, best-rank]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
evidence_basis: documentation
justification: ../justification/wikibase-statement-rank.md
canonical_concept: wikibase-statement-rank
aliases: [StatementRank, Rank, preferred rank, normal rank, deprecated rank, best rank]
summary: >-
  Wikibase Statement 三级 Rank：Preferred（最重要/最新，默认展示）、Normal（正确但不宜默认全部展示）、
  Deprecated（不可靠/已知错误）。"Best rank"机制：若存在 Preferred 则 best=Preferred，否则 best=Normal。
  设计故意简洁——三级对应不同的数据访问、UI 展示和导出处理。
related: [wikibase-statement-structure]
---

Wikibase 为每条 Statement 分配一个 Rank，用于提供简单的选择/过滤标准。三个级别：

1. **Preferred**——最重要和最新的信息，默认应使用
   - 可有多条 Preferred（可能表示多值属性或来源分歧）
   - 示例：Berlin 当前人口数字

2. **Normal**——被认为正确的相关信息，但可能过多不宜默认全部展示
   - 示例：Berlin 多年历史人口数据

3. **Deprecated**——不被信任或已知含错误的声明
   - Statement 本身可能不"错"（如历史文献确实做出了错误声称），但其内容不应在多数场景使用
   - 示例：某历史文献中的错误人口数字

**"Best rank" 机制**：对给定 Item 的给定 Property，若存在至少一条 Preferred 语句则 best rank 为 Preferred，否则为 Normal。"Best Statements" 即该 Property 下拥有 best rank 的语句集合。

设计故意保持粗粒度——三级分别对应不同的数据访问、UI 展示和导出策略。更细的分级缺乏明确解释且增加 UI 复杂度；更少的分级则难以处理不可信/错误声明。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Ranks of Statements" P158-164 -- "The ranks provide a simple selection/filtering criterion in cases where there are many Statements for some property"
[^card-1]: 参见 [wikibase-statement-structure] 了解 Rank 在 Statement 结构中的位置
