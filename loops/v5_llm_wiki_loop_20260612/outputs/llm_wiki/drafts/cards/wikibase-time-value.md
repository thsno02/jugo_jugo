---
id: wikibase-time-value
title: Wikibase TimeValue 的精度编码与不确定日期表示
status: draft
card_type: data-structure
tags: [wikibase, time, precision, calendar, TimeValue, proleptic-gregorian]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
evidence_basis: documentation
justification: ../justification/wikibase-time-value.md
canonical_concept: wikibase-time-value
aliases: [TimeValue, time value, date value, temporal precision]
summary: >-
  Wikibase TimeValue 包含 time（类 ISO 8601 时间戳）、precision（0-14 整数，0=十亿年到14=秒）、
  before/after（以 precision 为单位的不确定范围）、timezone（UTC 偏移分钟）、calendarmodel（显示用
  日历 URI）。存储始终用儒略前推格里历，calendarmodel 指定显示日历。世纪/千年不严格对齐最高位。
related: [wikibase-datatype, wikibase-quantity-value]
---

TimeValue 表示可能不精确的时间点，结构如下：

| 属性 | 类型 | 含义 |
|------|------|------|
| time | 时间戳 | 类 ISO 8601 格式，年份始终带符号且 1-16 位 |
| precision | 0-14 整数 | 精度级别 |
| before | integer | 不确定范围：主值之前多少单位 |
| after | integer | 不确定范围：主值之后多少单位 |
| timezone | signed integer | UTC 偏移（分钟） |
| calendarmodel | URI | 显示用日历模型 |

**Precision 编码**：0=十亿年, 1=亿年, ..., 6=千年, 7=世纪, 8=十年, 9=年, 10=月, 11=日, 12=时, 13=分, 14=秒。

**世纪/千年对齐特殊规则**：正年份世纪从 xx01 始到 xx00 止（18 世纪 = 1701-1800），但十年对齐最高位（1980s = 1980-1989）。

**不确定日期示例**："between 1846 and 1855" 可表示为 time=1850, precision=9(年), before=4, after=5。

**日历模型**：数据始终以前推格里历（proleptic Gregorian）存储，calendarmodel 字段指定显示时应使用的日历（可能是儒略历）。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Dates and times" P210-226 -- "A TimeValue represents a point in time that might be imprecise"
[^card-1]: 参见 [wikibase-quantity-value] 了解另一种带不确定性的 DataValue
