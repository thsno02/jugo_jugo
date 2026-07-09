---
id: maintenance-inversion-llm-wiki
title: 维护倒置——LLM 维护人提问
status: accepted
card_type: core-insight
tags:
- llm-wiki
- maintenance
- knowledge-management
- system-survival
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- openaitoolshub-six-months
evidence_basis: practitioner_report
justification: ../justification/maintenance-inversion-llm-wiki.md
canonical_concept: maintenance-inversion-llm-wiki
aliases:
- maintenance inversion
- 维护倒置
- LLM maintains human inputs
- the LLM maintains the wiki the human investments are inputs and questions
summary: 维护倒置 maintenance-inversion-llm-wiki 是 Karpathy LLM wiki 模式的核心设计哲学：LLM 负责维护（添加
  backlinks、修复 stale claims、标记矛盾），人只负责输入和提问。此单一倒置是作者坚持使用超过三个月的根本原因——相对于 PARA/Notion/Roam
  等要求人做维护的系统。BASB asks you to do the maintenance work, LLM wiki asks Claude to do
  it, that single inversion changes whether the system survives month three.
related:
- maintenance-loop-as-core-innovation
- retrieval-does-not-fix-maintenance
- llm-wiki-maintenance-engine-analogy
---

LLM wiki 模式的核心倒置 [^src-1]：

- **传统系统**（Notion/Roam/PARA/BASB）：人负责添加 backlinks、修复 stale claims、标记矛盾 → 维护负担导致三个月内放弃
- **LLM wiki**：LLM 负责维护，人只负责输入（articles/transcripts）和提问 → 系统存活

作者称这是"the single inversion"——唯一使此系统在尝试 Notion 一年、plain Obsidian 一年均失败后存活下来的设计选择 [^src-1]。

对比 BASB（Building a Second Brain / Tiago Forte's PARA）："BASB asks you to do the maintenance work. The LLM wiki asks Claude to do it. That single inversion changes whether the system survives month three." [^src-2]

[^card-1]: 与 [schema-first-principle] 相关——schema 是人向 LLM 传达维护规则的通道
[^card-2]: 与 [ripple-effect-ingest] 相关——涟漪效应是 LLM 执行维护的具体表现

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "Who I Am, and Why I Run an LLM Wiki" P11 -- "the LLM maintains the wiki, the human investments are inputs and questions. That single inversion is why this stuck when nothing else did."
[^src-2]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "FAQ" P88 -- "BASB asks you to do the maintenance work. The LLM wiki asks Claude to do it. That single inversion changes whether the system survives month three."
