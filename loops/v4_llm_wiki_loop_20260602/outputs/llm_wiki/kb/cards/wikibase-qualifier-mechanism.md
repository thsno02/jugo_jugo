---
id: wikibase-qualifier-mechanism
title: Qualifier Snaks 的上下文限定机制
status: accepted
card_type: mechanism
tags: [wikibase, qualifier, snak, context, temporal-scope, role]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
justification: ../justification/wikibase-qualifier-mechanism.md
canonical_concept: wikibase-qualifier-mechanism
aliases: [qualifier Snaks, 限定修饰, 声明限定词, qualifierSnaks]
summary: >-
  wikibase-qualifier-mechanism（qualifier Snaks / 限定修饰 / 声明限定词）Wikibase 中 Statement 的 qualifierSnaks 是对 mainSnak 的上下文限定，用于附加"不直接指向主语"的信息如时间范围、角色、比例等，使单一 Property-Value 断言能表达复合事实
related: [wikibase-snak-triple-epistemology, wikibase-statement-structure]
---

Wikibase 的 Statement 支持在 mainSnak 之外添加零个或多个 qualifier Snaks（也简称"qualifiers"），用于补充"不直接指向主语"的附加上下文信息 [^src-1]。

qualifier Snaks 解决的核心问题是：Property-Value 对虽然能表达许多基本断言，但现实世界中的事实往往需要附加条件或限定。文档给出三个典型场景 [^src-2]：

**时间范围限定**："奥巴马从 2005 年 1 月 3 日到 2008 年 11 月 16 日担任伊利诺伊州参议员"——mainSnak 为 PropertyValueSnak（属性"US Senator from"，值"Illinois"），qualifier 用 PropertyIntervalSnak 指定"in office"的时间区间。

**角色限定**："《哈利波特与魔法石》主演艾玛·沃特森饰演赫敏·格兰杰"——mainSnak 的属性是"starring"，值是"Emma Watson"，qualifier 用 PropertyValueSnak 指定"played character"为"Hermione Granger"。

**比例限定**："奥地利 1.6% 的居民是土耳其人"——mainSnak 的属性是"ethnic group"，值是"Turks"，qualifier 用 PropertyValueSnak 指定"percentage"为"1.6%"。

qualifier 的一个重要特征是其可省略性：如果某信息未知（如知道一个国家有某民族但不知比例），可以简单省略该 qualifier [^src-3]。选择何种表示方式由社区协商决定，正如维基百科中对信息呈现方式的协商一样 [^src-4]。

## Footnotes

[^src-1]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Statements" section, lines 531-532 -- "there can be zero or more additional PropertySnaks that describe the Statement in more detail. These qualifier Snaks... store additional information that does not directly refer to the subject"
[^src-2]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Statements" section, lines 548-569 -- 奥巴马参议员、哈利波特和奥地利民族的三个示例
[^src-3]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Statements" section, lines 570-571 -- "there are cases where a country is known to have inhabitants of some ethnic group, while the percentage of that group is not known; then the qualifier Snak could simply be omitted"
[^src-4]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Statements" section, lines 569-570 -- "Like in Wikipedia, it is left to the community to agree on uniform ways of expressing such things"
