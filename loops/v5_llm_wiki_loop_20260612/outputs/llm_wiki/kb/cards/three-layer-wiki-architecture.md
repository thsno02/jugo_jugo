---
id: three-layer-wiki-architecture
title: 三层分离架构
status: accepted
card_type: architecture-pattern
tags:
- llm-wiki
- architecture
- separation-of-concerns
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- obsidian-community-plugin
evidence_basis: documentation
justification: ../justification/three-layer-wiki-architecture.md
canonical_concept: three-layer-wiki-architecture
aliases:
- three-layer architecture
- 三层架构
- sources/wiki/schema
summary: Karpathy 三层分离架构：sources/（用户源文档，只读）→ wiki/（LLM 生成的实体/概念/索引页面）→ schema/（Wiki 结构配置，命名规范/模板/分类）。数据流为 ingest 从 sources 到 wiki， query/maintain 在 wiki 层，schema 与 wiki 共演化。插件不修改源文件。
related:
- karpathy-llm-wiki-concept
- wiki-page-generation-output
- karpathy-llm-wiki-three-layer-architecture
- raw-wiki-code-architecture
- three-layer-architecture
- extraction-granularity-levels
- smart-knowledge-fusion
---
该插件实现 Karpathy 的三层分离设计：[^src-1]

1. **sources/**：用户源文档，只读。插件从不修改源文件。
2. **wiki/**：LLM 生成的 Wiki 页面，包含 entities/（实体页）、concepts/（概念页）、index.md（自动索引）、log.md（操作日志）。
3. **schema/**：Wiki 结构配置（命名规范、模板、分类），与 wiki 层共演化（co-evolve）。

数据流为：sources → ingest → wiki → query/maintain。[^src-1] [^card-1]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Architecture" P1 -- "sources/ # Your source documents (read-only) ↓ ingest wiki/ # LLM-generated Wiki pages ↓ query / maintain schema/ # Wiki structure configuration"
[^card-1]: 参见 [[karpathy-llm-wiki-concept]] 了解设计理念背景
