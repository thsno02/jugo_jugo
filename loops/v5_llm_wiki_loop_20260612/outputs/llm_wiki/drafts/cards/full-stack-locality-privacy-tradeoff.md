---
id: full-stack-locality-privacy-tradeoff
title: 全栈本地化的隐私-便利性取舍
status: draft
card_type: tradeoff-analysis
tags: [privacy, data-governance, local-first, notion-ai, obsidian, tradeoff]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [kunal-local-knowledge-base]
evidence_basis: practitioner_report
justification: ../justification/full-stack-locality-privacy-tradeoff.md
canonical_concept: full-stack-locality-tradeoff
aliases: [full-stack locality, 全栈本地化, privacy-convenience tradeoff, data sovereignty, local-first AI]
summary: >-
  知识库工具在隐私-便利性频谱上分三档：Notion AI（零设置/数据在他方/检索不透明）、Obsidian+插件（本地存储/推理调外部API）、本地LLM wiki（全栈本地/高摩擦/低质量/无UI）。作者结论：敏感工作笔记用本地 wiki 不可替代，其余场景 Obsidian 更实用。
related: []
---

据作者对比分析，个人知识管理工具在隐私-便利性频谱上形成三个层次：[^src-1]

**Notion AI**：零设置开箱即用，但数据存于 Notion 服务器，由其模型处理，用户对检索逻辑无可见性。作者判断对个人杂项笔记可接受，但对工程架构决策和专有系统设计而言"non-starter for a lot of teams"。[^src-2]

**Obsidian + 社区插件**（如 Smart Connections、Copilot）：笔记以 markdown 保留在本地，但多数插件仍调用外部 API 进行 LLM 推理——"Local on storage, cloud on compute"。[^src-3]

**本地 LLM wiki**：全栈本地——数据在本机、模型在本机。代价是设置摩擦高、答案质量低于 GPT-4 级模型、无精美 UI、在终端操作。[^src-4]

作者的实践结论：本地 wiki 在"不能也不应发送至第三方 API 的敏感工作笔记"场景中胜出；其余场景 Obsidian + 好插件更实用——"the boring answer is actually the right one for most developers"。[^src-5]

[^card-1]: 与 [llm-wiki-definition-and-core-value] 关联——本卡展开其"数据不出机"价值主张的具体取舍维度。

[^src-1]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "LLM Wiki vs. Notion AI vs. Obsidian" P27 -- "Why not just use Notion AI or one of the dozen Obsidian plugins"
[^src-2]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "LLM Wiki vs. Notion AI vs. Obsidian" P28 -- "your data lives on Notion's servers...Non-starter for a lot of teams I've worked with"
[^src-3]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "LLM Wiki vs. Notion AI vs. Obsidian" P29 -- "Your notes stay local in markdown, but most plugins still call external APIs for the LLM inference"
[^src-4]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "LLM Wiki vs. Notion AI vs. Obsidian" P30 -- "A local LLM wiki gives you full-stack locality...The tradeoff is setup friction, lower answer quality"
[^src-5]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "LLM Wiki vs. Notion AI vs. Obsidian" P31 -- "the local wiki wins for one specific use case: querying sensitive work notes...the boring answer is actually the right one"
