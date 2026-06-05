---
id: structured-queryability-gap
title: 结构化可查询性缺口
status: accepted
card_type: distinction
tags: [llm-wiki, structured-data, markdown, queryability, ADR, work-items]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [hacker-news-original-thread]
justification: ../justification/structured-queryability-gap.md
canonical_concept: structured-queryability-gap
aliases: [结构化可查询性, queryability gap, markdown查询局限]
summary: >-
  structured-queryability-gap（结构化可查询性 / queryability gap / markdown查询局限）指纯 markdown wiki 在混入结构化数据（工作项、ADR）后暴露的查询局限：agent 无法回答"显示阻塞此 epic 的未完成任务"而不扫描散文或维护并行索引；AGENTS.md 教 LLM 文件夹约定只在数据简单时有效；需要同时提供人类可读文件和 agent 可查询的结构化接口
related: [index-based-navigation, schema-as-configuration, wiki-as-git-repo]
---

一位评论者指出了 LLM Wiki 模式在实践中遇到的一个具体摩擦点：当 wiki 中混入结构化数据（如工作项或架构决策记录 ADR）时，**纯 markdown 的查询能力不足**[^src-1]。

具体表现：agent 无法回答「显示阻塞此 epic 的未完成任务」这样的结构化查询，除非扫描散文文本或维护一个并行索引。AGENTS.md 的方式（教 LLM 文件夹约定）在数据简单时有效，但随着迭代次数增多会退化[^src-2]。

该评论者提出的解决方案是**双接口设计**：数据存储在结构化数据库中，但渲染为纯 markdown 并支持双向同步。LSP 为编辑器提供自动补全和验证，agent 和脚本通过 CLI 或 MCP 访问同一数据[^src-3]。

这一观察揭示了 LLM Wiki 模式（以 markdown 为中心的文件系统）在特定使用场景下的架构限制：markdown 对人类阅读友好，但对程序化查询不友好。当知识库需要同时支持叙述性文档和结构化数据时，纯文件系统方案需要增强。

## Footnotes

[^src-1]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- mpazik 评论 -- "The friction shows up once you mix docs with structured things like work items or ADRs. Flat markdown doesn't query well and gets inconsistent."
[^src-2]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- mpazik 评论 -- "The AGENTS.md approach papers over this by teaching the LLM the folder conventions. Works until the data gets complex but gets worse after many iterations."
[^src-3]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- mpazik 评论 -- "Both are needed: files that open in any editor, and a structured interface the agent can actually query... Data lives in a structured DB but renders to plain markdown with bi-directional sync. LSP gives editors autocomplete and validation. Agents and scripts get the same data through CLI or MCP."
