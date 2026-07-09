---
id: wikibase-quantity-value
title: Wikibase QuantityValue 的结构与不确定性表示
status: draft
card_type: data-structure
tags: [wikibase, quantity, uncertainty, unit, decimal, QuantityValue]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
evidence_basis: documentation
justification: ../justification/wikibase-quantity-value.md
canonical_concept: wikibase-quantity-value
aliases: [QuantityValue, quantity, numeric value with uncertainty]
summary: >-
  Wikibase QuantityValue 包含 amount（decimal 主值）、可选 lowerBound/upperBound（不确定区间）、
  unit（IRI 或"1"表无单位）。不确定区间语义故意未精确规定（可能是硬限或概率区间）。
  单位用完整 IRI 表示以避免歧义，通常指向 Wikidata Item 或标准词汇表如 QUDT。
related: [wikibase-datatype, wikibase-time-value]
---

QuantityValue 表示带不确定性信息和单位的十进制数，结构如下：

| 属性 | 类型 | 含义 |
|------|------|------|
| amount | decimal | 主值 |
| lowerBound | decimal（可选） | 下界 |
| upperBound | decimal（可选） | 上界 |
| unit | IRI 或 "1" | 计量单位 |

**不确定性表示**：lowerBound/upperBound 指定真值可能偏离主值的正负范围（如 12300 +/- 50）。若未提供则不确定性未指定。不确定区间的精确解释故意未规定——可能是硬限，也可能是正态分布的 66% 或 95% 区间。

**单位表示**：使用完整 IRI 而非字符串（因 "m" 在不同上下文可能指不同单位）。实践中通常指向表示该单位的 Wikidata ItemDescription 的 IRI，或取自标准单位词汇表如 QUDT。"1" 表示无量纲。

**UI 输入**：如 "4~" 生成 amount=4, lowerBound=3.5, upperBound=4.5。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Quantities" P197-209 -- "A QuantityValue represents a decimal number, together with information about the uncertainty interval of this number, and a unit of measurement"
[^card-1]: 参见 [wikibase-datatype] 了解 Datatype 体系
