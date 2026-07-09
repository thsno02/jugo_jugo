---
id: wiki-page-generation-output
title: Wiki 页面生成输出格式
status: accepted
card_type: specification
tags:
- llm-wiki
- page-format
- entity
- concept
- frontmatter
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- obsidian-community-plugin
evidence_basis: documentation
justification: ../justification/wiki-page-generation-output.md
canonical_concept: wiki-page-generation-output
aliases:
- wiki page format
- 页面生成格式
- entity page
- concept page
summary: 生成四类页面：wiki/sources/ 源摘要、wiki/entities/ 实体页（人物/组织/项目等）、 wiki/concepts/ 概念页（理论/方法/术语等）、wiki/index.md 自动索引。实体页 frontmatter 含 type/created/updated/sources/tags/aliases，正文含描述/相关概念/相关实体/源提及。 保留原语言引用（verbatim
  source mentions）并可选附翻译。
related:
- three-layer-wiki-architecture
- wiki-page-aliases
---

该插件生成四类 Wiki 页面：[^src-1]

- `wiki/sources/filename.md`：源文档摘要
- `wiki/entities/entity-name.md`：实体页（人物、组织、项目等）
- `wiki/concepts/concept-name.md`：概念页（理论、方法、术语等）
- `wiki/index.md`：自动生成的索引
- `wiki/log.md`：操作日志

实体页结构示例包含 frontmatter（type/created/updated/sources/tags/aliases）和正文节（Basic Information、Description、Related Concepts、Related Entities、Mentions in Source）。[^src-2]

特征：保留原语言引用（Verbatim Source Mentions）并可选附翻译，确保可追溯性。[^src-3] [^card-1]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Generated pages" P1 -- "wiki/sources/filename.md — Source summary; wiki/entities/entity-name.md — Entity pages; wiki/concepts/concept-name.md — Concept pages"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Example" P1 -- "type: entity; created: 2026-05-15; sources: [[sources/machine-learning]]; tags: [method]; aliases: ['监督学习', 'Supervised Learning']"
[^src-3]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Features" P1 -- "Verbatim Source Mentions — Original language quotes preserved with optional translation for traceability"
[^card-1]: 参见 [[three-layer-wiki-architecture]] 了解页面在架构中的位置
