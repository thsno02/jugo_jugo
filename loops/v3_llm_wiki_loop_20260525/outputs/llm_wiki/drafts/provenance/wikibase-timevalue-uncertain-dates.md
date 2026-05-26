---
schema: draft_card_provenance.v3
draft_card: ../cards/wikibase-timevalue-uncertain-dates.md
material_id: wikibase-data-model
digest_id: digest_wikibase-data-model
source_paths:
  - data/raw/webpage/wikibase-data-model/text.txt
created_time: 2026-05-26T15:25:00+08:00
edited_time: 2026-05-26T15:25:00+08:00
edited_entity: llm
---

## 源证据

- 第 692-712 行（§9.2 Dates and times）：6 字段（time / precision / before / after / timezone / calendarmodel）完整定义、ISO 8601 解读、year 0 存在、世纪边界、十年代对齐。
- 第 717-721 行（§9.2.1 Examples）："between 1846 and 1855" 的完整字段示例。
- 第 526 行（PropertySomeValueSnak 章节末）："William of Ockham died in 1347 or 1348" 不支持的明示。

## 卡片范围是否成立

- 字段定义、precision 等级表、世纪边界、不确定日期例子、disjunction 限制——全部直接来自文档。
- "存储 vs 显示 分离" 是对 calendarmodel 字段描述的合理归纳；文档明确说 "time is always saved in proleptic Gregorian, this URI states how the value should be displayed"。
- "其他历法不在 schema 内" 是文档第 710 行"future extension"暗示的边界提示。

## 发表门控结果

本轮未运行。

## 备注

- TimeValue 的"precision + before/after"对 LLM 系统处理用户给出的模糊时间（"上周末"、"几年前"）有结构借鉴价值，可在后续与 LongMemEval 的 time-aware query expansion 对照。
