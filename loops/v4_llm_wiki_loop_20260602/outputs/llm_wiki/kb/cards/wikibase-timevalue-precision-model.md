---
id: wikibase-timevalue-precision-model
title: TimeValue 的 15 级精度与不确定性模型
status: accepted
card_type: mechanism
tags: [wikibase, time, precision, calendar, proleptic-gregorian, uncertainty, temporal]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
justification: ../justification/wikibase-timevalue-precision-model.md
canonical_concept: wikibase-timevalue-precision-model
aliases: [TimeValue, 时间值精度, 15级时间精度, 日历模型, proleptic Gregorian]
summary: >-
  wikibase-timevalue-precision-model（TimeValue / 15级时间精度）Wikibase 的 TimeValue 使用 6 字段结构：ISO 8601 时间戳 + 15 级精度（0=十亿年到14=秒）+ before/after 不确定单元 + 时区偏移 + 日历模型 IRI；数据始终以外推格里历存储，日历模型仅控制显示；世纪/千年的精度对齐规则与十年不同
related: [wikibase-quantity-value-uncertainty, wikibase-entity-value-hierarchy]
---

Wikibase 的 TimeValue 是处理可能不精确的时间点的核心数据结构，由六个字段组成 [^src-1]：

1. **time**：类 ISO 8601 格式的时间戳，年份始终带符号且有 1-16 位数字，如 `+2013-01-01T00:00:00Z`。未知的月、日、时间部分设为零；精度字段决定哪些数字有意义。
2. **precision**（shortint）：15 级精度系统，数值含义为：
   - 0 = 十亿年
   - 1 = 一亿年
   - ...
   - 6 = 千年
   - 7 = 世纪
   - 8 = 十年
   - 9 = 年
   - 10 = 月
   - 11 = 日
   - 12 = 小时
   - 13 = 分钟
   - 14 = 秒
3. **before**（integer）：不确定性下限，表示真实时间可能比给定时间早多少个精度单位。
4. **after**（integer）：不确定性上限，表示真实时间可能比给定时间晚多少个精度单位。
5. **timezone**（signed integer）：相对 UTC 的分钟偏移；1972 年前为相对世界时的偏移；时区实施前为事件地点经度 x4（转换为分钟）。
6. **calendarmodel**（URI）：标识用于**显示**此时间值的日历模型。

**关键设计决定**：数据始终以外推格里历（proleptic Gregorian）存储，日历模型 URI 仅控制显示方式，不影响存储 [^src-2]。

**世纪与千年的对齐规则**：十年与时间戳最高位对齐（1980s = 1980-1989），但世纪和千年不是如此——正时间戳中世纪和千年从模 100/1000 余 1 的年份开始（18 世纪 = 1701-1800），负时间戳相反（公元前第 2 千年 = -2000 到 -1001）[^src-3]。

**不确定日期示例**："1846 年到 1855 年之间"可表示为 [^src-4]：
- time: "+00000001850-00-00T00:00:00Z"
- precision: 9（年）
- before: 4（主值前 4 年）
- after: 5（主值后 5 年）

主值用于默认显示和排序；before/after 允许精确描述不确定性。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/wikibase-data-model/markdown.md` -- "Dates and times" section, lines 212-218 -- TimeValue 的六个字段定义
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/wikibase-data-model/markdown.md` -- lines 211 -- "The calendar model used for saving the data is always the proleptic Gregorian calendar... but the Calendar model used for displaying the data is given by the saved Calendar model"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/wikibase-data-model/markdown.md` -- lines 214 -- "centuries and millennia do not strictly align with the most significant digits... the 18th century begins in the year 1701 and ends in the year 1800"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/wikibase-data-model/markdown.md` -- "Examples" section, lines 223-225 -- "between 1846 and 1855" 示例
