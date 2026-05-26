---
id: wikibase-timevalue-uncertain-dates
title: Wikibase 的 TimeValue 用 precision + before/after 表达不确定日期
status: draft
card_type: mechanism
tags: [#wikibase, #wikidata, #temporal, #datatype]
created_time: 2026-05-26T15:25:00+08:00
edited_time: 2026-05-26T15:25:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
provenance_card: ../provenance/wikibase-timevalue-uncertain-dates.md
aliases: [TimeValue precision, uncertain date Wikibase]
related: [wikibase-three-snak-types]
---

## TimeValue 的字段结构

Wikibase 的日期数据类型不是简单的 ISO 8601 字符串，而是一个 6 字段结构（datatype IRI `http://wikidata.org/vocabulary/datatype_time`）：

| 字段 | 含义 |
|---|---|
| `time` | 类 ISO 8601 timestamp，年份永远带符号、1-16 位，例如 `+2013-01-01T00:00:00Z`；月/日/时若未知填 0 |
| `precision` | 0=billion years, 6=millennium, 7=century, 8=decade, 9=year, 10=month, 11=day, 12=hour, 13=minute, 14=second |
| `before` | 不确定时，"实际可能比 time 早多少个 precision 单位" |
| `after` | 不确定时，"实际可能比 time 晚多少个 precision 单位" |
| `timezone` | UTC 偏移分钟数；1972 年前用经度 ×4 替代 |
| `calendarmodel` | 显示用日历模型（Gregorian / Julian）的 IRI；**存储永远是 proleptic Gregorian** |

## 不确定日期的标准表达

要表达"between 1846 and 1855"，做法是：

```
time: "+00000001850-00-00T00:00:00Z"
precision: 9   // year-level
before: 4
after: 5
```

含义：主值 1850（用于排序与默认显示），下界比主值早 4 年（→1846），上界比主值晚 5 年（→1855）。`before` / `after` 的单位由 `precision` 决定。

## 为什么这种设计

- **显示与存储分离**：内部永远存 proleptic Gregorian + 数值字段，让排序/查询稳定；显示时再根据 `calendarmodel` 渲染（Julian 历史日期不需要"转换"原数据）。
- **precision 是"语义粒度"而非"显示粒度"**：如果只知道"18 世纪"，应当存 `time = +00000001750-...` + `precision = 7`，而不是猜一个具体年——下游可以识别这是世纪级数据，避免假精度。
- **历史日期边界细节**：century / millennium 不与最高位数字对齐——18 世纪从 1701 到 1800，公元前 2 千年从 -2000 到 -1001；decade 才与最高位对齐（1980s = 1980-1989）。
- **年份 0 存在**：年 0 即"公元前 1 年"——与 ISO 8601 一致，但不少现实系统不这样做，混用会出 off-by-one。

## 边界

- 不支持"1347 或 1348"这种 disjunction——只能用 precision=9 + before/after 表达一个区间，无法精确表达"两个具体可选值"。
- TimeValue 与 Calendar 现在只覆盖 Gregorian / Julian；其他历法（如农历）目前不在 schema 内。
- `timezone` 字段含义在 1972 年（UTC 现代实现）前后不同，跨年代查询要按字段语义而非简单做减法。

## References

- TimeValue 字段定义：`data/raw/webpage/wikibase-data-model/text.txt` 第 692-712 行（Dates and times）。
- 不确定日期例子：第 717-721 行。
- "1347 或 1348" 限制：第 526 行（SomeValueSnak 章节末尾）。

## Footnotes

- 字段表原文："time: timestamp in a format resembling ISO 8601 ... precision: shortint. The numbers have the following meaning: 0 - billion years, 1 - hundred million years, ..., 14 - second ... after: integer. If the date is uncertain, how many units before the given time could it be? ... before: integer. ... timezone: signed integer."（第 696-704 行）
- "1846 and 1855" 完整例子："time: '+00000001850-00-00T00:00:00Z', precision: 9, before: 4, after: 5 / This means the 'main' value is 1850, given as a year, with a lower bound four years before and an upper bound 5 years after the 'main' value (before and after are given in the unit specified by the precision value)."（第 717-719 行）
- 18 世纪边界："centuries and millennia begin on years 1 modulo 100/1000 and end on years 0 modulo 100/1000 ... For example, the 18th century begins in the year 1701 and ends in the year 1800"（第 698 行）
