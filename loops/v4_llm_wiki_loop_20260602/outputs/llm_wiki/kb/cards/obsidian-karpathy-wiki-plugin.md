---
id: obsidian-karpathy-wiki-plugin
title: Obsidian 社区插件 Karpathy LLM Wiki
status: accepted
card_type: example_pattern
tags: [llm-wiki, obsidian, plugin, implementation, community]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
justification: ../justification/obsidian-karpathy-wiki-plugin.md
canonical_concept: obsidian-karpathy-wiki-plugin
aliases: [Karpathy LLM Wiki Plugin, karpathywiki, Greener-Dalii 插件]
summary: >-
  obsidian-karpathy-wiki-plugin（Karpathy LLM Wiki Plugin / karpathywiki / Greener-Dalii 插件）
  是 Karpathy LLM Wiki 概念的 Obsidian 社区插件实现：v1.10.2，94/100 评分，
  实现三层架构 + 六大命令（摄入/查询/巡检/索引/Schema 建议），支持 10+ LLM 供应商
related: [mcp-tool-skill-layering, my-llm-wiki-implementation]
  - obsidian-tooling
  - three-layer-architecture
  - llm-wiki-pattern
---

**Karpathy LLM Wiki** 是由开发者 Greener-Dalii 发布的 Obsidian 社区插件，实现了 Andrej Karpathy 提出的 LLM Wiki 概念[^src-1]。截至材料收录时，该插件版本为 v1.10.2，Obsidian 官方评分 94/100，累计 781 次下载，4 周内发布 27 个版本[^src-2]。

插件实现了 Karpathy 三层架构设计：`sources/`（只读源文档）-> `wiki/`（LLM 生成的 Wiki 页面）-> `schema/`（Wiki 结构配置）[^src-3]。生成的页面包括五种类型：源摘要页（`wiki/sources/`）、实体页（`wiki/entities/`）、概念页（`wiki/concepts/`）、自动索引（`wiki/index.md`）和操作日志（`wiki/log.md`）[^src-4]。

插件提供六大命令[^src-5]：
1. **Ingest single source** -- 选择单个笔记，提取实体和概念生成 Wiki 页面
2. **Ingest from folder** -- 批量摄入整个文件夹
3. **Query wiki** -- 会话式问答，流式响应带 [[wiki-links]]
4. **Lint wiki** -- 健康扫描：重复页、死链、空页、孤立页、缺失别名、矛盾
5. **Regenerate index** -- 重建 wiki/index.md
6. **Suggest schema updates** -- LLM 分析 Wiki 并提出 schema 改进建议

插件支持 10+ LLM 供应商（Anthropic、Gemini、OpenAI、DeepSeek、Kimi、GLM、Ollama、OpenRouter 等），支持 8 种语言的 UI 和 Wiki 输出，Wiki 输出语言可独立于 UI 语言设置[^src-6]。代码库由 13 个模块组成，包含 wiki 引擎、查询引擎、源分析器、页面工厂、巡检控制器等[^src-7]。my-llm-wiki 以 CLI+pip 路线提供了互补的实现方式，强调代码仓库级知识图谱构建和 19 语言代码支持[^card-1]。llm-wiki-mcp 则将同类操作拆分为 MCP 工具层与 Claude Code 技能层，实现跨客户端可移植性[^card-2]。

## Footnotes

[^card-1]: [my-llm-wiki PyPI 实现](my-llm-wiki-implementation.md) -- 两个独立的 LLM Wiki 三层架构实现：本插件走 Obsidian GUI 路线（6 大命令、10+ LLM 供应商），my-llm-wiki 走 CLI+pip 路线（Tree-sitter 代码提取、SHA256 增量缓存、CLI 回写），体现同一模式在不同工具生态中的具体化
[^card-2]: [MCP 工具与技能的双层设计](mcp-tool-skill-layering.md) -- 本插件将 ingest/query/lint 封装为 6 个 Obsidian 命令，该卡将同类操作拆分为 4 个 MCP 工具原语 + 4 个 Claude Code 技能编排，走跨客户端可移植路线

[^src-1]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "What is LLM-Wiki?" L96 -- "AI-powered structured knowledge base that ingests your notes and generates a connected Wiki — based on Andrej Karpathy's LLM Wiki concept"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "Overview" L82-98 -- "Greener-Dalii 781 downloads" "Obsidian official score 94/100" "27 releases"
[^src-3]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "Architecture" L378-379 -- "Karpathy's three-layer separation design: sources/ # Your source documents (read-only) → wiki/ # LLM-generated Wiki pages → schema/ # Wiki structure configuration"
[^src-4]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "Generated pages" L383-393 -- "wiki/sources/filename.md — Source summary; wiki/entities/entity-name.md — Entity pages; wiki/concepts/concept-name.md — Concept pages"
[^src-5]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "Commands" L322-335 -- "Ingest single source... Ingest from folder... Query wiki... Lint wiki... Regenerate index... Suggest schema updates"
[^src-6]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "LLM & Language" L296-304 -- "Multi-Provider — Anthropic, Anthropic Compatible, Gemini, OpenAI, DeepSeek, Kimi, GLM, OpenRouter, Ollama, custom endpoints" "Wiki Output Language — 8 languages independent of UI"
[^src-7]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "Codebase" L381 -- "Modular Codebase — 13 focused modules in src/"
