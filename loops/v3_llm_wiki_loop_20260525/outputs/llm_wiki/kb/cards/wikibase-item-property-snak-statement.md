---
id: wikibase-item-property-snak-statement
title: Wikibase 数据模型的四个核心结构——Item / Property / Snak / Statement
status: accepted
card_type: concept
tags: [#wikibase, #wikidata, #data-model, #knowledge-graph]
created_time: 2026-05-26T15:10:00+08:00
edited_time: 2026-05-28T12:10:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
provenance_card: ../provenance/wikibase-item-property-snak-statement.md
aliases: [Wikibase core model, Wikidata model]
related: [wikibase-three-snak-types, wikibase-statement-rank-and-references, wikibase-conceptual-not-serialization, graphrag-global-sensemaking-pipeline]
---

## 四层抽象

Wikibase（Wikidata 背后的引擎）的数据模型不是"主-谓-宾"三元组，而是四层结构[^src1]：

1. **Item**——对应"Wikipedia 一页可能描述的事物"，可以是 Berlin（城市）、Albert Einstein（个人）、Physicist（类）。Item 用 IRI 标识，典型 ID 形如 `Q1234567890`，稳定不变。
2. **Property**——描述两个实体（或 Item 与 DataValue）之间的关系，例如 `population`、`binomial name`、`capital of`、`author of`。ID 形如 `P123456789`，与 Item 用不同前缀避免混淆。Property 有一个 **Datatype** 提示常用值类型，但**模型不强制 strict typing**——Datatype 改了之后旧数据仍然合法[^src4]。
3. **Snak**——*"small, but more than a byte"* 的基本断言单位[^src2]，目前只有 `PropertySnak`（即 `PropertyValueSnak` / `PropertySomeValueSnak` / `PropertyNoValueSnak` 三种）；三者语义差与"未填 / 无值 / 未知值"的区分见三类 Snak 卡[^v3-1]。
4. **Statement**——以一个 Item 为 subject，包含**一个 main Snak**、零或多个 qualifier Snak、零或多个 ReferenceRecord、一个 Rank[^src3]。Statement 才是 Wikidata 实际"声明"的最小单位。

`Statement := 'Statement(' Entity Snak { PropertySnak } { ReferenceRecord } Rank ')'`

## 为什么不是简单的三元组

- **Qualifier 让一个声明可以带 contextual modifier**——"Obama 是 US Senator from Illinois"光这一句不够，需要 qualifier `in office: 2005-01-03 to 2008-11-16`。RDF 也能做，但要靠 reification；Wikibase 把它直接做进了 Statement 的结构。
- **Rank 让多个并存声明可被自动筛选**：preferred / normal / deprecated 三档；同一 Item 对同一 Property 可以有多个 preferred 声明（如 "Berlin 当前人口"与"Berlin 历史人口"分级）——详细机制见 Rank 与 ReferenceRecord 卡[^v3-2]。
- **References 与 Snak 平级**——每个 Statement 都可以挂任意条 ReferenceRecord，每条 reference 本身又是 Snak 集合（如"标题/作者/出版者/章节"）。这把"引用"从单一 URL 抬升为结构化对象。

## 边界

- Datatype 不是强类型——若一个 Property 的 Datatype 被改，旧值仍合法，所以系统必须接受"Value 与当前 Property Datatype 不匹配"的情形。
- Property 由用户自由创建（Item 也是），所以同一概念可能有多种 Property 表达；不要假设 Property 是封闭集合。
- Statement 的 subject 是 Item 而不是 Snak 内部——Snak 自己不含 subject 信息，要从所在 Statement 上下文获取。
- 这套四结构是 *conceptual model*，不规定底层存储或 JSON/RDF 序列化[^v3-3]。与 GraphRAG 抽取的 entity / relationship / claim 三元产物形成对照——后者面向 LLM 编译知识图，没有 Statement 这层 Rank/Reference 结构[^v3-4]。

## Footnotes

[^v3-1]: [wikibase-three-snak-types](wikibase-three-snak-types.md) — 三类 PropertySnak（Value/NoValue/SomeValue）的语义差
[^v3-2]: [wikibase-statement-rank-and-references](wikibase-statement-rank-and-references.md) — Rank 三级与 ReferenceRecord 的展开
[^v3-3]: [wikibase-conceptual-not-serialization](wikibase-conceptual-not-serialization.md) — 数据模型是 conceptual model 而非 binding / 序列化规范
[^v3-4]: [graphrag-global-sensemaking-pipeline](graphrag-global-sensemaking-pipeline.md) — GraphRAG 抽 entity / relationship / claim 三元产物，与 Wikibase 四层结构形成对照
[^src1]: `data/raw/webpage/wikibase-data-model/text.txt` 第 311-321 行（Overview）、第 423-447 行（Items + Properties）四结构总览
[^src2]: `data/raw/webpage/wikibase-data-model/text.txt` 第 319 行（Snak 名称解释）："any such basic assertion that one can make in Wikidata is called a Snak (which is small, but more than a byte). This term will not be relevant for using Wikidata (editors will not encounter it), but it is relevant for developers to avoid confusion with Statements or other claims." Snak 类型详见第 467–475 行
[^src3]: `data/raw/webpage/wikibase-data-model/text.txt` 第 528–545 行（Statement 完整结构）；第 545 行 BNF："Statement := 'Statement(' Entity Snak { PropertySnak } { ReferenceRecord } Rank ')'"
[^src4]: `data/raw/webpage/wikibase-data-model/text.txt` 第 480 行（Datatype 非强类型）："it is not required that Value belongs to the Datatype that is currently given to the Property in the system ... if the Datatype is changed, then it will not be possible to update all stored data immediately."
