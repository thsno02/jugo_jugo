---
id: wikibase-three-snak-types
title: 三种 Snak——区分"未填"、"无值"、"未知值"
status: accepted
card_type: distinction
tags: [#wikibase, #wikidata, #knowledge-representation, #missing-data]
created_time: 2026-05-26T15:15:00+08:00
edited_time: 2026-05-28T12:20:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
provenance_card: ../provenance/wikibase-three-snak-types.md
aliases: [PropertyNoValueSnak, PropertySomeValueSnak, PropertyValueSnak]
related: [wikibase-item-property-snak-statement, wikibase-statement-rank-and-references, wikibase-timevalue-uncertain-dates]
---

## 三种 Snak 的语义差

Wikibase 显式把"一个 Item 对某 Property 的取值情况"分成三种 Snak[^src1]，且它们语义彼此不可替换。Snak 是 Wikibase 数据模型四层抽象里的基本断言单位[^v3-1]：

| Snak 类型 | 语义 | 经典例子 |
|---|---|---|
| `PropertyValueSnak(P, V)` | 该 Item 对 P 有具体值 V | "Berlin 的 population 是 3,499,879" |
| `PropertyNoValueSnak(P)` | 该 Item 对 P **不存在值**（不是没填，是真没有） | "Circle has no angle"、"Mount Everest has no parent peak"[^src2] |
| `PropertySomeValueSnak(P)` | 该 Item 对 P **有某个值，但未知** | "Ambrose Bierce 有 date of death（他不在世），但具体日期不详"[^src3] |

这三者与"Wikidata 还没人填这条数据"（信息缺失，根本没建 Statement）是第四种状态，互相**不冲突也不可合并**。

## 为什么这种细分有意义

- 知识库最容易出 bug 的地方就是"missing vs absent vs unknown"被混为一谈：搜索"圆的内角"如果回退 "无信息"，用户没法判断是 Wikidata 漏录还是几何上就不存在；明确用 `NoValueSnak` 后，下游系统就知道这是 *肯定否定*。
- `SomeValueSnak` 解决"我们知道他死了，但不知道哪一天"这种事实——对历史人物、生物分类、天文观测等领域常用。具体的日期不确定性还由 TimeValue 的 precision/before/after 字段表达[^v3-3]。
- 文档明确指出 `NoValueSnak` **只应在"否则会被误以为不完整"时使用**——不要写"Pacific Ocean has no angle"这种泛滥的否定[^src4]。

## 边界

- 目前所有 Snak 都属 `PropertySnak` 大类；未来"非 Property 的 Snak"是预留可能性，尚未启用。
- 模型支持"多个矛盾值同时存在"（不同 source 给出不同人口数），不强制单值；`Rank` 才是处理冲突的机制（preferred / normal / deprecated）[^v3-2]，不是用 Snak 类型解决。
- `SomeValueSnak` 不带 precision 信息；要表达"William of Ockham 死于 1347 或 1348"这种 disjunction 模型层面不支持，只能用 TimeValue 的 precision 字段近似（"死于 1340s"）[^src5]。

## Footnotes

[^v3-1]: [wikibase-item-property-snak-statement](wikibase-item-property-snak-statement.md) — Snak 是四层抽象的基本断言单位，本卡是其子类型展开
[^v3-2]: [wikibase-statement-rank-and-references](wikibase-statement-rank-and-references.md) — Rank 三级机制处理多值冲突，与 Snak 类型分工
[^v3-3]: [wikibase-timevalue-uncertain-dates](wikibase-timevalue-uncertain-dates.md) — TimeValue 的 precision/before/after 表达不确定日期，与 SomeValueSnak 互补
[^src1]: `data/raw/webpage/wikibase-data-model/text.txt` 第 471-526 行（三 Snak 类型定义：PropertyValueSnak / PropertyNoValueSnak / PropertySomeValueSnak 三节）
[^src2]: `data/raw/webpage/wikibase-data-model/text.txt` 第 509-511 行（NoValueSnak 例子原文）："Circle (subject) has no angle (property). / Mount Everest (subject) has no parent peak (property)."
[^src3]: `data/raw/webpage/wikibase-data-model/text.txt` 第 524 行（SomeValueSnak 例子原文）："Ambrose Bierce (subject) has an unknown date of death (property), yet we can be certain that he is not among the living persons."
[^src4]: `data/raw/webpage/wikibase-data-model/text.txt` 第 513 行（不滥用警示）："Such statements should only be made in cases where one could otherwise expect an incompleteness. It is not intended that Wikidata stores all things that are not the case (e.g., 'The Pacific Ocean has no angle')."
[^src5]: `data/raw/webpage/wikibase-data-model/text.txt` 第 526 行（SomeValueSnak 章节末尾的 "1347 或 1348" 限制）
