---
schema: accepted_card_provenance.v3
card: ../cards/wikibase-timevalue-uncertain-dates.md
material_id: wikibase-data-model
digest_id: digest_wikibase-data-model
source_paths:
  - data/raw/webpage/wikibase-data-model/text.txt
draft_card: ../../drafts/cards/wikibase-timevalue-uncertain-dates.md
draft_provenance: ../../drafts/provenance/wikibase-timevalue-uncertain-dates.md
similarity_result: ../../drafts/similarity/wikibase-timevalue-uncertain-dates.json
comparison_provenance: ../../drafts/comparison/wikibase-timevalue-uncertain-dates.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；6 字段表 + 1846–1855 例子 + 18 世纪边界 + disjunction 不支持均回到 L692–721 / L526。
created_time: 2026-05-26T15:25:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开 TimeValue 6 字段表 + 不确定日期编码示例 + 设计动机 + 历史边界 + 限制。
  - 知识密度：字段语义 + 示例 + 边界。
  - 源支撑：source_ids 含 wikibase-data-model；L696–704 / L717–719 / L698 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：5 张 Wikibase / zep / longmemeval 相邻卡。

## 备注

- TimeValue 的"precision + before/after"对 LLM 系统处理用户给出的模糊时间（"上周末"、"几年前"）有结构借鉴价值。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/wikibase-timevalue-uncertain-dates.md`
- draft provenance: `../../drafts/provenance/wikibase-timevalue-uncertain-dates.md`
- similarity: `../../drafts/similarity/wikibase-timevalue-uncertain-dates.json`
- comparison provenance: `../../drafts/comparison/wikibase-timevalue-uncertain-dates.md`
