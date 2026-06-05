---
id: full-stack-locality
title: 全栈本地性
status: accepted
card_type: distinction
tags: [llm-wiki, privacy, data-governance, locality-spectrum]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [kunal-local-knowledge-base]
justification: ../justification/full-stack-locality.md
canonical_concept: full-stack-locality
aliases: [全栈本地, full-stack local, 本地存储本地计算, 数据隐私架构, 三层本地性谱系]
summary: >-
  full-stack-locality（全栈本地 / full-stack local / 本地存储本地计算 / 数据隐私架构）是个人知识库的三层本地性谱系：Notion AI = 云存储+云计算，Obsidian+插件 = 本地存储+云计算，本地 LLM wiki = 存储与计算均在本地；全栈本地的核心价值不是速度而是敏感数据永不离机
related: [llm-wiki-pattern, obsidian-tooling]
---

在个人知识库工具的比较中，「本地」并非一个二元属性，而是一个**三层谱系**[^src-1]：

1. **Notion AI**——打磨精良、零配置，但数据存储在 Notion 服务器上、由其模型处理，用户对检索机制零可见性。对于个人杂货清单可以接受，对于工程架构决策和专有系统设计，在许多团队中是"非起步项"（non-starter）[^src-2]。

2. **Obsidian + 社区插件**（如 Smart Connections、Copilot）——笔记以 markdown 形式保留在本地，但大多数插件仍调用外部 API 进行 LLM 推理。**本地存储，云端计算**[^src-3]。

3. **本地 LLM wiki**——**全栈本地性**：数据在本机、模型在本机。代价是搭建摩擦、相比 GPT-4 级模型的回答质量差距、以及没有精美 UI（只在终端中工作）[^src-4]。

全栈本地的核心价值不是速度，而是隐私。作者明确指出："你的专有笔记、半成形的想法、敏感的架构文档永远不会接触他人的服务器。"[^src-5]在企业场景中，作者曾多次见证数据治理顾虑扼杀了基于云的 RAG 系统的采纳——完全本地的系统从根本上绕过了这一整个对话[^src-6]。

作者的诚实评估是：本地 wiki 仅在一个特定场景胜出——查询**不能也不应该发送给第三方 API 的敏感工作笔记**。对于其他所有场景，"Obsidian 配一个好插件今天更实用"[^src-7]。

## Footnotes

[^src-1]: `data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L105-116 "LLM Wiki vs. Notion AI vs. Obsidian + Plugins" -- 三者对比的完整段落
[^src-2]: `data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L109 -- "For personal grocery lists, fine. For engineering architecture decisions and proprietary system designs? Non-starter for a lot of teams I've worked with."
[^src-3]: `data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L111 -- "Your notes stay local in markdown, but most plugins still call external APIs for the LLM inference. Local on storage, cloud on compute."
[^src-4]: `data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L113 -- "Your data stays on your machine. Your model runs on your machine. The tradeoff is setup friction, lower answer quality compared to GPT-4 class models, and no slick UI."
[^src-5]: `data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L102 -- "your proprietary notes, your half-formed ideas, your sensitive architecture docs never touch someone else's server"
[^src-6]: `data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L103 -- "I've watched data governance concerns kill adoption in enterprise teams more than once. A fully local system sidesteps that entire conversation."
[^src-7]: `data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L115 -- "For everything else, I'll be honest — Obsidian with a good plugin is more practical today."
