---
id: wikibase-quantity-value-uncertainty
title: QuantityValue 的不确定区间与单位模型
status: accepted
card_type: mechanism
tags: [wikibase, quantity, uncertainty-interval, unit, decimal, measurement]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
justification: ../justification/wikibase-quantity-value-uncertainty.md
canonical_concept: wikibase-quantity-value-uncertainty
aliases: [QuantityValue, 数量值不确定区间, 物理量表示, lowerBound/upperBound]
summary: >-
  wikibase-quantity-value-uncertainty（QuantityValue / 数量值不确定区间）Wikibase 的 QuantityValue 由 amount（主值）、可选的 lowerBound/upperBound（不确定区间）和 unit（以 IRI 表示的物理单位）四字段组成，使用 XML Schema decimal 的字符串词法形式以保留任意精度，不确定区间的精确解释（硬限 vs 正态分布百分位）故意不做规定
related: [wikibase-entity-value-hierarchy, wikibase-flexible-typing, wikibase-timevalue-precision-model]
---

Wikibase 使用 QuantityValue 表示带有不确定性信息和物理单位的十进制数值。其结构由四个字段组成 [^src-1]：

- **amount**（decimal）：数量的主值。
- **lowerBound**（decimal，可选）：真实值可能的下界。
- **upperBound**（decimal，可选）：真实值可能的上界。
- **unit**（IRI 或字面量 "1"）：物理量的单位，以 IRI 标识。

数值使用 XML Schema decimal 的词法形式（字符串表示），支持任意大小和任意精度。文档明确指出 float 或 double 等技术格式"不适合准确表示用户输入" [^src-2]。对于数据访问（如数值排序），可以使用 double 近似值。

**不确定区间的语义**：lowerBound 和 upperBound 表示真实值相对于 amount 可能的偏差范围（如"12300 +/- 50"）。关键设计决定是：不确定区间的精确解释被**故意留为未规定** [^src-3]——根据上下文，它可能表示硬限值，也可能描述正态分布的 66 或 95 百分位区间。如果不提供上下界，则不确定性为"未指定"。

**UI 输入模式**：用户界面中数量和边界作为字符串一起输入，例如"4~"会被解析为 amount=4, lowerBound=3.5, upperBound=4.5。系统使用正则表达式解析输入 [^src-4]：
```
^\s*((?:[-+]\s*)?(?:[\d,]+\.\d*|\.?\d+)(?:[eE][-+]?\d+)?)\s*(?:([~!])|(?:\+/?-|±)\s*((?:[-+]\s*)?(?:[\d,]+\.\d*|\.?\d+)(?:[eE][-+]?\d+)?)|)\s*$
```

**单位表示**：单位使用 IRI 而非字符串，因为如"m"之类的缩写在不同上下文可能代表不同单位。实践中可以是指向 Wikidata Item 的 IRI，也可以取自 QUDT 等标准单位词汇表 [^src-5]。

## Footnotes

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Quantities" section, lines 198-203 -- "amount: decimal the quantity's main value; lowerBound: decimal the quantity's lower bound (optional); upperBound: decimal the quantity's upper bound (optional); unit: IRI or '1'"
[^src-2]: `data/raw/webpage/wikibase-data-model/markdown.md` -- lines 53 -- "technical formats such as float or double are not appropriate to represent user input accurately"
[^src-3]: `data/raw/webpage/wikibase-data-model/markdown.md` -- lines 205 -- "The exact interpretation of the uncertainty interval provided with lowerBound and upperBound is unspecified. Depending on context, it may represent hard limits on the value, or the interval may just describe the 66 or 95 percentile interval of a normal distribution"
[^src-4]: `data/raw/webpage/wikibase-data-model/markdown.md` -- lines 206-207 -- regex for parsing quantity input in UI
[^src-5]: `data/raw/webpage/wikibase-data-model/markdown.md` -- lines 208 -- "It is represented as a IRI rather than as a String, since a string like 'm' might represent different units in different contexts"
