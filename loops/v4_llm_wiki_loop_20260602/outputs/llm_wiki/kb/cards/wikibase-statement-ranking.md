---
id: wikibase-statement-ranking
title: Statement 三级排名机制
status: accepted
card_type: mechanism
tags: [wikibase, ranking, preferred, normal, deprecated, best-rank, filtering]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
justification: ../justification/wikibase-statement-ranking.md
canonical_concept: wikibase-statement-ranking
aliases: [StatementRank, 声明排名, Preferred/Normal/Deprecated, best rank]
summary: >-
  wikibase-statement-ranking（StatementRank / 声明排名 / best rank）Wikibase 为每条 Statement 赋予 Preferred（最重要/最新）、Normal（正确但次要）、Deprecated（不可靠/已知错误）三级排名，并据此定义 best rank（有 preferred 则取 preferred，否则取 normal），实现简洁的默认筛选
related: [wikibase-statement-structure]
---

Wikibase 为每条 Statement 赋予三级排名（StatementRank），作为简单的筛选和过滤标准 [^src-1]：

**Preferred**：最重要和最新的信息，默认在大多数场景中使用。例如只显示柏林最新人口数据。注意可以有多条 preferred 声明——这可能意味着多值属性（如一个人的多个子女），或来源分歧（不同来源给出不同的人口数字）[^src-2]。

**Normal**：被认为正确的相关信息，但可能过于丰富，不适合默认展示。例如柏林多年的历史人口数据 [^src-3]。

**Deprecated**：不可靠或已知包含错误的声明。例如某历史文献中记录的错误人口数字——声明本身并没有错（历史文献确实做了这个错误的断言），但该声明在大多数情况下不应被使用 [^src-4]。

文档明确指出，这个三级模型是"有意保持粗粒度和简单的"。三个级别对应数据访问、UI（默认显示什么）和导出（可只导出 preferred + normal）中的不同处理。更细粒度的排名"似乎没有如此清晰的解释，会不必要地增加 UI 复杂性"；而只有两级或没有排名"会使处理不可信或包含错误声明的情况更加困难" [^src-5]。

基于排名还派生出 **best rank** 概念：对于给定 Item 的给定 Property，如果存在至少一条 preferred 声明，则该属性的 best rank 为 preferred；否则 best rank 为 normal。"Best Statements"即具有 best rank 的那些声明 [^src-6]。

## Footnotes

[^src-1]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Ranks of Statements" section, lines 575-576 -- "The ranks provide a simple selection/filtering criterion in cases where there are many Statements for some property. There are three possible ranks"
[^src-2]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Ranks of Statements" section, lines 577-578 -- "Preferred statements refer to the most important and most up-to-date information... Note that there may be multiple preferred statements"
[^src-3]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Ranks of Statements" section, lines 579-580 -- "Normal statements contain relevant information that is believed to be correct but that may be too extensive for showing it by default"
[^src-4]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Ranks of Statements" section, lines 581-582 -- "Deprecated statements that may not be considered reliable or that are even known to contain errors"
[^src-5]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Ranks of Statements" section, lines 583-584 -- "This model is intentionally left coarse and simple... More fine-grained rankings do not seem to have such a clear interpretation"
[^src-6]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Ranks of Statements" section, lines 585-586 -- "the 'best rank' for the Statements about a given Property with respect to a given Item... the 'best Statements' about a given Property in the context of a given Item are the ones that have the best rank"
