---
id: llm-wiki-three-step-workflow
title: LLM Wiki 三步工作流
status: draft
card_type: workflow
tags: [llm-wiki, workflow, schema, compilation]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [aillm-wiki-directory]
evidence_basis: documentation
justification: ../justification/llm-wiki-three-step-workflow.md
canonical_concept: llm-wiki-three-step-workflow
aliases: [LLM Wiki workflow, three-step workflow, Pick-Drop-Query]
summary: >-
  LLM Wiki 三步工作流：(1) Pick Your Schema 从模板选择或自建 schema.md；(2) Drop in Your Sources 将原始文件放入 raw/ 文件夹并指示 LLM compile；(3) Query & Compound 添加新源后 LLM 更新已有页面而非创建孤立页，wiki 逐周增强。
related: [llm-wiki-pattern-definition, llm-wiki-schema-templates]
---

LLM Wiki 的操作分为三步：[^card-1]

**第一步：Pick Your Schema**——从 5 个 battle-tested schema.md 模板（general, research, engineering, product, SEO）中选择，或在熟悉模式后从零构建。每个模板配有 CLAUDE.md 伴随文件。[^src-1]

**第二步：Drop in Your Sources**——将原始文件（PDF、截图、会议笔记、论文等）放入 raw/ 文件夹，指向 Claude 或 Gemini 并配合 schema.md 说"compile"。LLM 读取 schema 并在 wiki/ 文件夹中写出结构化 wiki，不触碰源文件。[^src-2]

**第三步：Query & Compound**——随新源到来，LLM 更新已有页面而非创建孤立页（orphans）。数周后 wiki 成为该领域所学内容中信号最强的草稿。[^src-3]

[^card-1]: 参见 [[llm-wiki-pattern-definition]] LLM Wiki 模式的基本定义
[^src-1]: `data/raw/webpage/aillm-wiki-directory/markdown.md` -- "Three Steps" P12-13 -- "Start from one of our five battle-tested schema.md templates — general, research, engineering, product, or SEO"
[^src-2]: `data/raw/webpage/aillm-wiki-directory/markdown.md` -- "Three Steps" P14-15 -- "Raw files live in a raw/ folder — PDFs, screenshots, meeting notes, research papers, whatever. Claude reads the schema and writes a structured wiki alongside in wiki/"
[^src-3]: `data/raw/webpage/aillm-wiki-directory/markdown.md` -- "Three Steps" P16-17 -- "As new sources arrive, the LLM updates existing pages rather than creating orphans. After a few weeks your wiki becomes the highest-signal draft"
