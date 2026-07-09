---
id: llm-wiki-audit-shared-library
title: llm-wiki 审计共享库架构
status: draft
card_type: component-architecture
tags: [audit, typescript, shared-library, obsidian-plugin, web-viewer]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-lewislulu-llm-wiki-skill]
evidence_basis: code_implementation
justification: ../justification/llm-wiki-audit-shared-library.md
canonical_concept: llm-wiki-audit-shared-library
aliases: [audit-shared, audit-shared library, 审计共享库, TypeScript audit library]
summary: >-
  llm-wiki-audit-shared-library 审计共享库：audit-shared 是共享 TypeScript 库
  (schema/anchor/id/serialize/index)，确保 Obsidian 插件(plugins/obsidian-audit)
  与 web preview server(web/) 产出的审计文件字节级形状一致(byte-identical in shape)，
  实现跨工具审计格式统一。
related: [compile-over-rag-wiki-pattern, llm-wiki-human-machine-division]
---

llm-wiki 项目包含两个配套审计工具——Obsidian 插件和本地 web preview server——它们共享同一个 TypeScript 库 `audit-shared/`。[^src-1]

audit-shared 的设计目标是保证不同工具产出的审计文件"字节级形状一致"(byte-identical in shape)。其源码模块包括 schema、anchor、id、serialize、index 五个组件。[^src-2]

Obsidian 插件允许用户在 vault 中选中文本并附带严重度留下评论，评论被写入 `audit/` 目录。web viewer 则提供 Markdown 渲染(含 mermaid/KaTeX/wikilinks)并支持从浏览器中选中文本提交反馈。[^src-3] 两个工具的审计输出格式统一，据材料推测这是为了让 LLM 处理反馈时无需区分来源。[^card-1]

[^src-1]: `data/raw/github_repo/repo-lewislulu-llm-wiki-skill/repo/README.md` -- "What this is" P4 -- "Both tools share a single TypeScript library (audit-shared/) so audit files written from Obsidian and the web viewer are byte-identical in shape."
[^src-2]: `data/raw/github_repo/repo-lewislulu-llm-wiki-skill/repo/README.md` -- "Repo contents" P1 -- "audit-shared/ ← Shared TypeScript library └── src/{schema,anchor,id,serialize,index}.ts"
[^src-3]: `data/raw/github_repo/repo-lewislulu-llm-wiki-skill/repo/README.md` -- "What this is" P3 -- "plugins/obsidian-audit/ — an Obsidian plugin: select text in any page, leave a comment with severity"
[^card-1]: [[llm-wiki-human-machine-division]] — LLM 负责处理用户反馈(acting on feedback)，统一格式降低处理复杂度
