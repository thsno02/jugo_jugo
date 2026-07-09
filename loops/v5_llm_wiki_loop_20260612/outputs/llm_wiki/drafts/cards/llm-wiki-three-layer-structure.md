---
id: llm-wiki-three-layer-structure
title: LLM Wiki 三层目录结构
status: draft
card_type: architecture
tags: [llm-wiki, directory-structure, raw, wiki, schema]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-three-layer-structure.md
canonical_concept: llm-wiki-three-layer-structure
aliases: [three-layer markdown repo, 三层结构, raw/ wiki/ schema.md, 三文件夹结构]
summary: >-
  LLM wiki 三层目录结构 llm-wiki-three-layer-structure：raw/（不可变输入，原始文章/gist/转录，never edited）、wiki/（LLM 编译页面，含 concepts/tools/people/insights/originals/indexes/ 子文件夹）、schema.md（规则文件）。设计原则是 Claude 而非人做几乎所有编辑。顶层文件夹越少越好（3个而非14个）以减少分类决策。附 log.md 为 append-only 操作日志。
related: []
---

Karpathy LLM wiki 的三层 markdown 仓库结构 [^src-1]：

1. **raw/**：不可变输入层。存放原始文章、gists、转录，never edited。作者有 80 篇。
2. **wiki/**：LLM 编译层。Claude 维护的页面。作者有 35 页，子目录含 concepts/(14)、tools/(8)、people/(4)、insights/(5)、originals/(4)、indexes/。
3. **schema.md**：规则层。定义 frontmatter 字段、canonical slug 规则、lint 协议、矛盾解决协议。

辅助文件：`log.md`——append-only 操作日志，每次 ingest/lint/edit 带 UNIX 时间戳前缀。作者报告每周 grep 此文件约两次 [^src-2]。

设计选择：顶层仅 3 个文件夹（非 GBrain 的 14 个），"fewer folders = fewer 'where does this go?' decisions" [^src-2]。

核心约束："Claude — not me — does almost all the editing" [^src-1]。

[^card-1]: 与 [schema-first-principle] 相关——schema.md 是三层中的规则层
[^card-2]: 与 [maintenance-inversion-llm-wiki] 相关——三层结构的设计服务于维护倒置

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "What the Karpathy LLM Wiki Actually Looks Like" P14 -- "a three-layer markdown repo (raw/ for immutable inputs, wiki/ for LLM-compiled pages, schema.md for the rules) where Claude — not me — does almost all the editing."
[^src-2]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "How I Set Mine Up" P34-35 -- "Three folders only at the top of wiki/...Fewer folders = fewer 'where does this go?' decisions."
