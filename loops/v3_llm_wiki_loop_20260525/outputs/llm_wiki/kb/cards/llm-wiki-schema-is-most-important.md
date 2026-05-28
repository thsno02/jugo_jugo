---
id: llm-wiki-schema-is-most-important
title: schema.md 是 LLM Wiki 里最重要的文件——Karpathy gist 没说够
status: accepted
card_type: operational_rule
tags: [#karpathy-llm-wiki, #schema, #pitfalls, #rohit-v2]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T11:46:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
provenance_card: ../provenance/llm-wiki-schema-is-most-important.md
aliases: [schema-first, schema is the most important file, schema.md]
related: [karpathy-llm-wiki-three-layers, llm-wiki-mcp-design-boundary-mechanics-not-content, llm-wiki-tldr-load-bearing, llm-wiki-rohit-v2-improvements, robin-cartier-schema-as-product-doc, aillm-wiki-schema-as-bottleneck, agents-md-as-schema-layer]
---

## 经验主张

Jim Liu（独立开发者，悉尼，openaitoolshub.org 站长）在 Obsidian 上跑 Karpathy LLM Wiki 模式 6 个月、覆盖 35 页之后得到一个**反 Karpathy gist 强调比例**的结论：

> "The pattern works — far better than I expected — but only if you treat the schema file as the most important file, which Karpathy's original gist underplays."[^src1]

Rohit Ghumare 给出更直白的版本："Schema is the most important file."[^src2]

## 为什么 schema 比内容重要

- **schema 决定增量动作的语义**：frontmatter 字段名 / canonical slug 规则 / contradiction 解决协议 → 都是每次 ingest 时 LLM 必须遵从的规则。schema 不清，LLM 每次都用自己的"默认习惯"，半年后 wiki 内部不自洽。
- **schema 决定可寻址性**：slug 命名规则不统一 → 同一个人 / 概念出现两个 slug（如 `karpathy.md` 和 `andrej-karpathy.md`）→ LLM 当成两个实体处理 → 推荐 / 搜索失真（Jim 的 Pitfall #4）。
- **schema 是 onboarding 文档**：每个 skill 都在每次运行时重读 schema[^v3-1]；schema 写得清楚 = agent 行为可预测。

## Jim 的"schema first"实操

> "I wrote schema.md before I had 5 pages."[^src2]

即"先写规则，再写第一页"。具体定义的内容：

- frontmatter 字段（必备 + 可选）
- canonical slug 规则
- contradiction-resolution 协议
- aliases 字段（用于 dedup）
- 文件夹分类（concepts / tools / people / insights / originals / indexes）

## Karpathy gist 为什么"underplay"

Jim 的诊断：Karpathy gist 把 schema 定位为"三层之一"，与 raw / wiki 并列；但在实际部署中，缺 schema 比缺 raw / wiki 衰败得**更快、更隐蔽**。raw / wiki 缺会立刻报错；schema 缺只是慢慢退化，3 个月后才发现已经"a graveyard within two months"。

## 操作含义

- **任何 Karpathy LLM Wiki 实例的第一个文件应是 `schema.md` / `CLAUDE.md` / `AGENTS.md`**[^v3-2]。
- **任何工具切换前必须重读 schema.md**（Jim Pitfall #4：换 note app 时没带 aliases 字段，结果产生双 slug）[^src3]。
- 把 schema.md 当 Wiki 的 README + ARCHITECTURE.md 来维护，而不是当 "rule reference card"。
- 不写 schema 的 wiki 在 2 个月内会变成"graveyard"——Jim 在三个朋友身上看到过这种失败模式。

## 边界

- 这条经验来自 sample size = 1（35 页、6 个月、个人项目）；外推到团队 / 千页规模时 schema 的作用方式可能不同。
- "schema 比内容重要"是相对强调，不否认内容质量也重要；正确读法是"没有 schema，再多内容也会退化"。

## Footnotes

[^src1]: `data/raw/webpage/openaitoolshub-six-months/text.txt:14` — "The pattern works — far better than I expected — but only if you treat the schema file as the most important file, which Karpathy's original gist underplays."
[^src2]: 同文件 `text.txt:50` — "Schema first, content second. I wrote schema.md before I had 5 pages. It defines the frontmatter fields, the canonical slug rules, the contradiction-resolution protocol. This is the part most write-ups skip and the part that matters most. Rohit Ghumare put it bluntly: 'Schema is the most important file.' He's right."
[^src3]: 同文件 `text.txt:98`（Pitfall #4）— "I migrated from one note app to Obsidian and forgot that my schema specified aliases field for canonical slug deduplication... Result: two pages on the same person under different slugs (karpathy.md and andrej-karpathy.md), Claude treated them as different entities, recommendations got weird. Lesson: any tool change starts with re-reading schema.md and writing a migration plan."
[^v3-1]: [llm-wiki-mcp-skills-vs-tools-workflow](llm-wiki-mcp-skills-vs-tools-workflow.md) — skill 层每次运行重读 schema 的设计参考。
[^v3-2]: [agents-md-as-schema-layer](agents-md-as-schema-layer.md) — `AGENTS.md` 作为 schema 实例的展开。
