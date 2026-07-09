---
id: schema-first-principle
title: Schema First 原则
status: draft
card_type: design-principle
tags: [llm-wiki, schema, governance]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
evidence_basis: practitioner_report
justification: ../justification/schema-first-principle.md
canonical_concept: schema-first-principle
aliases: [schema first content second, schema 优先, schema.md 最重要文件]
summary: >-
  Schema first 原则 schema-first-principle 指 schema.md 是 LLM wiki 中最重要的文件，应在内容产生前先写好。schema 定义 frontmatter 字段、canonical slug 规则、矛盾解决协议。无 schema 的 wiki 两个月内退化为 graveyard。优先级排序为 schema first, content second, tooling third。Rohit Ghumare 明确表述"Schema is the most important file"。
related: []
---

Schema.md 是 LLM wiki 中最重要的文件 [^src-1]。作者在仅有 5 页时即先写 schema.md，定义 frontmatter 字段、canonical slug 规则和矛盾解决协议。

此原则的优先级排序：schema first → content second → tooling third [^src-2]。

据材料报告，不写 schema.md 的 wiki 两个月内退化为"graveyard"——作者观察到朋友的失败案例验证了此规律 [^src-3]。

schema 的核心功能是作为人向 LLM 传达维护规则的唯一通道：LLM 负责编辑但需要明确指令。

[^card-1]: 与 [llm-wiki-three-layer-structure] 相关——schema.md 是三层结构的规则层

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "How I Set Mine Up" P36 -- "Schema first, content second. I wrote schema.md before I had 5 pages."
[^src-2]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "4 Pitfalls I Hit" P61 -- "Schema first, content second, tooling third."
[^src-3]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "Who Should (and Shouldn't) Try This Pattern" P81 -- "You won't write a schema.md. Without it, the wiki devolves into a graveyard within two months."
