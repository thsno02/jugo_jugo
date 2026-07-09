---
id: schema-file-as-innovation
title: Schema File 是 LLM Wiki 的真正创新点
status: draft
card_type: design-insight
tags: [schema-file, claude-md, operational-knowledge, llm-autonomy, governance]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [robin-cartier-llm-knowledge-bases]
evidence_basis: practitioner_report
justification: ../justification/schema-file-as-innovation.md
canonical_concept: schema-file-as-innovation
aliases: [schema file innovation, CLAUDE.md as PRD, living product requirements document for AI]
summary: >-
  Schema file（如 CLAUDE.md）被视为 LLM wiki pattern 的真正创新——而非 wiki 本身。将其视为"AI 同事的活产品需求文档"（living product requirements document for an AI colleague），编码文件夹结构、引用规则、ingest 工作流、linting 约定。该模式可推广到任何需要操作知识（operational knowledge）编码供 LLM 自主执行的工作流。
related: [llm-knowledge-base-pattern]
---

据源材料，schema file 被视为 LLM wiki pattern 的真正创新，而非 wiki 本身：[^src-1] [^card-1]

将 CLAUDE.md 视为"AI 同事的活产品需求文档"（a living product requirements document for an AI colleague），它编码了：
- 文件夹结构
- 引用规则
- Ingest 工作流
- Linting 约定

该洞察的关键推广意义：schema file 模式远超知识管理范畴，可应用于任何需要操作知识（operational knowledge）编码供 LLM 自主执行的工作流。它本质上是将人类的工作流规范转化为 LLM 可解析、可遵循的治理文件。

[^src-1]: `data/raw/webpage/robin-cartier-llm-knowledge-bases/markdown.md` -- "Key points" P1 -- "The schema file is the real innovation, not the wiki itself. Treating CLAUDE.md as 'a living product requirements document for an AI colleague' scales far beyond knowledge management"
[^card-1]: 参见 [[llm-knowledge-base-pattern]] 了解该 pattern 的完整三层架构
