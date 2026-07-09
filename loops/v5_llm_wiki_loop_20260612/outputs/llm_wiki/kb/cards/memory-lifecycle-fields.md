---
id: memory-lifecycle-fields
title: Memory Lifecycle Frontmatter 字段
status: accepted
card_type: mechanism
tags:
- llm-wiki
- rohit-v2
- frontmatter
- staleness-detection
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- openaitoolshub-six-months
evidence_basis: practitioner_report
justification: ../justification/memory-lifecycle-fields.md
canonical_concept: memory-lifecycle-fields
aliases:
- Memory Lifecycle
- lifecycle fields
- last_verified
- confidence
- superseded_by
- 生命周期字段
summary: Memory Lifecycle frontmatter 字段 memory-lifecycle-fields 是 Rohit v2 引入的机制，每页添加
  last_verified（日期）、confidence（high/medium/low）、superseded_by（指向替代页）、contradicts（指向矛盾声明）。解决
  v1 的 stale claims 问题——三个月后新旧定价声明并存且均自信断言。此为 Rohit Ghumare v2 三项核心改进之一。
related:
- llmwiki-epistemic-metadata
- typed-wikilinks
---

Rohit Ghumare 的 v2 在每个 wiki 页面的 frontmatter 中引入 Memory Lifecycle 字段 [^src-1]：

- `last_verified`: 最后验证日期（如 2026-05-01）
- `confidence`: high | medium | low
- `superseded_by`: 指向替代页面（如 another-page.md）
- `contradicts`: 指向矛盾声明页面

此机制解决的问题：v1 缺乏这些字段，三个月后会出现 stale ChatGPT pricing claims 与新声明并存、均被自信断言的状况 [^src-1]。

[^card-1]: 与 [schema-first-principle] 相关——lifecycle 字段在 schema.md 中定义
[^card-2]: 与 [contradiction-as-asset] 相关——contradicts 字段是矛盾标记的实现载体

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "What I added from Rohit's v2" P38 -- "Memory Lifecycle frontmatter: every page has last_verified...confidence...superseded_by...contradicts"
