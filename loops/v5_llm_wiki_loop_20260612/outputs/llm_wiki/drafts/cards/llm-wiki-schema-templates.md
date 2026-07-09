---
id: llm-wiki-schema-templates
title: LLM Wiki Schema 模板体系
status: draft
card_type: tooling
tags: [llm-wiki, schema, templates, claude-md]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [aillm-wiki-directory]
evidence_basis: documentation
justification: ../justification/llm-wiki-schema-templates.md
canonical_concept: llm-wiki-schema-templates
aliases: [schema.md templates, LLM Wiki schemas, CLAUDE.md templates]
summary: >-
  LLM Wiki schema 模板体系包含 5 种 battle-tested 模板：general、research、engineering、product、SEO。每种模板由 schema.md 与 CLAUDE.md 配对组成，指导 LLM 在首次尝试即产出清洁 entity pages。选择匹配思维方式的 schema 是最难决策点。
related: [llm-wiki-three-step-workflow, llm-wiki-pattern-definition]
---

LLM Wiki 的模板体系围绕 schema.md + CLAUDE.md 配对构建。[^card-1]

该站提供 5 种 battle-tested 模板，覆盖最常见用例：[^src-1]
- **general**——通用知识管理
- **research**——研究与文献
- **engineering**——工程技术
- **product**——产品
- **SEO**——搜索引擎优化

每个模板的设计目标是让 LLM 在首次尝试（first try）即产出清洁的 entity pages，避免与模糊 prompt 的反复拉扯。[^src-2]

据材料描述，选择匹配个人思维方式的 schema 是整个流程中最难的决策点（"The hardest part is picking a schema that matches how you actually think"）。一旦 schema 确定，后续每个新源材料都以相同可预测形状自行编译。[^src-3]

[^card-1]: 参见 [[llm-wiki-three-step-workflow]] 三步工作流的第一步
[^src-1]: `data/raw/webpage/aillm-wiki-directory/markdown.md` -- "Templates" P10 -- "Download battle-tested CLAUDE.md and schema.md templates for general, research, engineering, product, and SEO use cases"
[^src-2]: `data/raw/webpage/aillm-wiki-directory/markdown.md` -- "Templates" P10 -- "Each template ships with the exact schema.md and CLAUDE.md combo that gets an LLM to produce clean entity pages on the first try"
[^src-3]: `data/raw/webpage/aillm-wiki-directory/markdown.md` -- "How It Works" P11 -- "The hardest part is picking a schema that matches how you actually think — once that is locked in, every new source compiles itself in the same predictable shape"
