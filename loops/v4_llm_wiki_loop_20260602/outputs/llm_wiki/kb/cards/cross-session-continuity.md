---
id: cross-session-continuity
title: 跨会话连续性机制
status: accepted
card_type: mechanism
tags: [llm-wiki, session, persistence, continuity]
created_time: 2026-06-04T22:45:00+08:00
edited_time: 2026-06-04T22:45:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/cross-session-continuity.md
canonical_concept: cross-session-continuity
aliases: [跨会话连续性, session continuity, 会话持久化]
summary: >-
  cross-session-continuity（跨会话连续性 / session continuity / 会话持久化）是 LLM Wiki
  通过三个持久化组件（raw sources、wiki、schema）加 log.md 实现跨会话连续性的机制
related: [schema-as-configuration]
---

[编者注]LLM 的每个会话从零开始，没有先前会话的记忆。LLM Wiki 通过**三个持久化到磁盘的组件**解决跨会话连续性：

1. **Raw sources**——不可变的原始文件
2. **Wiki 文件**——LLM 生成的 markdown 页面，在会话间保持不变
3. **Schema**——告知 LLM 结构和约定的配置文件[^src-1]

此外，**log.md** 提供了 wiki 演化的时间线，帮助新会话的 LLM 理解最近发生了什么[^src-2]。Schema 被明确期望编码足够的意图供未来会话使用——用户开发出的工作流应 「记录在 schema 中供后续会话使用」[^src-3]。

材料未讨论哪些具体信息会在会话边界丢失（如 ingest 对话中的上下文、人类的偏好指引、正在进行的分析思路），也未讨论 schema + log 的组合是否足以实现无缝衔接。Schema 的配置角色详见专题卡[^card-1]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture > The schema" -- "tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow"
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Indexing and logging > log.md" -- "The log gives you a timeline of the wiki's evolution and helps the LLM understand what's been done recently"
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Ingest" P1 -- "It's up to you to develop the workflow that fits your style and document it in the schema for future sessions"
[^card-1]: [Schema 文件的配置角色](schema-as-configuration.md) -- Schema 是跨会话持久化的核心组件，该卡展开其配置角色
