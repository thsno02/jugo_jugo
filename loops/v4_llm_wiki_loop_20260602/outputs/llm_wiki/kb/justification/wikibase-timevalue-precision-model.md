---
card_id: wikibase-timevalue-precision-model
decision: accepted
confidence: high
---

## 提取理由

TimeValue 是 Wikibase 数据模型中处理时间的核心机制，具有独特的 15 级精度系统（从十亿年到秒）、before/after 不确定性编码、以及"始终以外推格里历存储、日历模型仅控制显示"的分离设计。这些结构化细节在已有 9 张卡片中完全没有覆盖。

本卡片的原子性知识点是：如何在单一数据结构中同时编码时间点、时间精度、时间不确定性、时区和日历显示模型。世纪/千年与十年的对齐规则差异（1701-1800 vs 1980-1989）是一个容易出错的实现细节，值得作为独立知识记录。

## 与已有卡片的区分

- entity-value-hierarchy 只列出 DataValue 存在，不描述具体结构
- 没有任何现有卡片涉及时间表示或日历模型
