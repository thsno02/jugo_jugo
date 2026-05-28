---
id: aillm-wiki-schema-as-bottleneck
title: 在 LLM Wiki 三步工作流里，"挑 schema"才是真正的瓶颈
status: accepted
card_type: operational_rule
tags: [#llm-wiki, #schema, #operations, #workflow]
created_time: 2026-05-26T11:50:00+08:00
edited_time: 2026-05-28T10:42:00+08:00
edited_entity: llm
source_ids: [aillm-wiki-directory]
provenance_card: ../provenance/aillm-wiki-schema-as-bottleneck.md
aliases: ["LLM Wiki 3-step build", "schema picking"]
related: [aillm-wiki-four-defining-properties, llm-wiki-schema-is-most-important, robin-cartier-schema-as-product-doc, llm-wiki-mcp-design-boundary-mechanics-not-content, karpathy-gist-three-layers, agents-md-as-schema-layer]
---

aillm.wiki 把搭建 LLM Wiki 简化为三步：

1. **Pick Your Schema**：从 5 个预置模板（general / research / engineering / product / SEO）选一个 `schema.md` + `CLAUDE.md` 组合[^src2]，或自己写。
2. **Drop in Your Sources**：把原始材料丢到 `raw/` 目录，让 Claude/Gemini 按 schema 编译成 `wiki/`。
3. **Query & Compound**：提问、补源、修页面；新源会"波及"已有页面[^src3]，wiki 一周比一周更聪明。

这个流程表面上无差别，但站方明确提出一个值得记住的工程判断：

> *"The hardest part is picking a schema that matches how you actually think — once that is locked in, every new source compiles itself in the same predictable shape."*[^src1]

也就是说：**真正消耗时间的不是工具集成，不是模型选择，而是选/定义 schema**。原因可以拆成三层：

- **schema 决定输出形状**：同一份论文按"research"和按"engineering"编译，会拆出完全不同的实体页与互链；选错就要在 wiki 长大后回头大改。
- **schema 决定可压缩性**：LLM 把 raw 编译进 wiki 时，是按 schema 决定"保留什么/丢什么/连到哪"。schema 越贴合自己的思维模型，长期 token 成本越低，跨会话一致性越好。
- **schema 决定可重复性**：当下次新源进来，LLM 必须沿用既有 schema 才能"自动把页面写成同一形状"；schema 不稳定，wiki 就退化成不一致 markdown 堆。

操作含义：

- 不要急着搭工具栈。先用现有材料的一个真子集，跑 2-3 次"raw → wiki"循环，确认 schema 抓的是你真的会去查的字段。
- 如果发现自己经常手改 wiki 的 frontmatter / 标题层级，那是 schema 不匹配的信号，不是 LLM "听不懂"。
- 从预置模板入手是合理起点；按 aillm.wiki 的说法，"start from scratch once you have seen the pattern a few times"。

边界与误读：

- 这是站方的工程判断 + 营销话术（卖 Starter Kit 与 Schema Library），不是被同行评议过的实证结论；引用时应注明。
- "三步走"也是简化叙事，真实流程通常需要在第 3 步反馈到第 1 步迭代 schema。

## References

- "Build Your LLM Wiki in 3 Steps" 章节（`data/raw/webpage/aillm-wiki-directory/text.txt`，第 53–73 行）。
- "hardest part is picking a schema" 原句见同节引言（L53–55）。
- 五个 schema 模板说明见 "Ready-to-Use Templates" 章节（L46–48）以及 "Schema Library"（L83–86）。

## Footnotes

- L55：*"The hardest part is picking a schema that matches how you actually think — once that is locked in, every new source compiles itself in the same predictable shape."*
- L59–61：*"Start from one of our five battle-tested schema.md templates — general, research, engineering, product, or SEO."*
- L72–73：*"As new sources arrive, the LLM updates existing pages rather than creating orphans."*
