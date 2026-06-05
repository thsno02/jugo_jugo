---
id: schema-as-configuration
title: Schema 文件的配置角色
status: accepted
card_type: mechanism
tags: [llm-wiki, schema, configuration]
created_time: 2026-06-04T22:30:00+08:00
edited_time: 2026-06-04T22:30:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/schema-as-configuration.md
canonical_concept: schema-as-configuration
aliases: [Schema 文件, CLAUDE.md, AGENTS.md, wiki schema, 配置文件]
summary: >-
  schema-as-configuration（Schema 文件 / CLAUDE.md / AGENTS.md / wiki schema / 配置文件）
  指 LLM Wiki 中 schema 的配置角色：使 LLM 成为有纪律的 wiki 维护者，由人机共同演化
related: [cross-session-continuity, documentation-shared-ownership, three-layer-architecture]
---

Schema 文件是 LLM Wiki 三层架构中的第三层，承担**关键配置角色**——它告诉 LLM wiki 的结构、约定和工作流程，包括如何摄入资料、回答问题和维护 wiki[^src-1]。

Schema 的核心价值在于：它使 LLM 成为「有纪律的 wiki 维护者而非通用聊天机器人」[^src-2]。具体实例包括 Claude Code 的 CLAUDE.md 或 OpenAI Codex 的 AGENTS.md。

Schema 是一个**共同演化的制品**——不是纯人工编写也不是纯 LLM 生成，而是「你和 LLM 随着摸索出领域适用方案而共同演化」[^src-3]。用户开发适合自己风格的工作流后，将其记录在 schema 中供未来会话使用[^src-4]。Schema 作为三层架构的第三层[^card-1]，也是实现跨会话连续性的核心持久化组件[^card-2]。

Schema 的共同演化特质与 Docs as Code 社区提倡的文档共同所有权文化形成平行：前者是人-LLM 边界上的协作，后者是人-人（写作者与开发者）边界上的协作，两者各自在不同协作边界上实践了知识制品的共有模式[^card-3]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture > The schema" -- "a document... that tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow when ingesting sources, answering questions, or maintaining the wiki"
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture > The schema" -- "it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot"
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture > The schema" -- "You and the LLM co-evolve this over time as you figure out what works for your domain"
[^src-4]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Ingest" P1 -- "It's up to you to develop the workflow that fits your style and document it in the schema for future sessions"
[^card-1]: [三层架构](three-layer-architecture.md) -- Schema 是三层架构的第三层，本卡展开其配置角色
[^card-2]: [跨会话连续性机制](cross-session-continuity.md) -- Schema 是跨会话持久化的核心组件之一
[^card-3]: [文档共同所有权文化](documentation-shared-ownership.md) -- 本卡聚焦人-LLM 之间的 schema 共同演化，该卡聚焦人-人之间的文档共同所有权，两者平行展示了不同协作边界上的知识共有模式
