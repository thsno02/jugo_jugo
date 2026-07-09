---
id: llm-compilation-paradigm
title: LLM 编译范式
status: draft
card_type: paradigm
tags: [llm-wiki, compilation, karpathy, knowledge-management]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-ss1024ss-llm-wiki]
evidence_basis: code_implementation
justification: ../justification/llm-compilation-paradigm.md
canonical_concept: llm-compilation-paradigm
aliases: [LLM compilation, LLM Wiki pattern, 编译范式, compile-first paradigm]
summary: >-
  LLM 编译范式 (llm-compilation-paradigm): 源自 Andrej Karpathy 的 LLM Wiki pattern，
  主张 LLM 正确用法不是 Q&A 而是 compilation（编译）。将非结构化源材料编译为结构化 wiki，
  再从 wiki 生成代码。LLM+filesystem+markdown 构成引擎，工具可换范式不可换。
related: [raw-wiki-code-architecture, llm-wiki-five-rules]
---

LLM Wiki 的核心理念源自 Andrej Karpathy 的 LLM Wiki pattern：LLM 的正确用法不是问答（Q&A），而是**编译（compilation）**。[^src-1]

这一范式主张：
- 非结构化知识（对话、文档、决策）应被 LLM 编译为结构化 wiki 页面
- wiki 是"当前共识"的唯一权威表达
- 代码是从 wiki 生成的制品（artifact），而非真相本身
- 引擎的本质是 LLM + filesystem + markdown，具体工具（Obsidian、Notion 等）可以替换，但编译范式不可替换

该范式解决的核心问题是：AI 对话记忆蒸发、知识散落多处无法定位、聊天历史不等于记忆。[^src-2]

[^src-1]: `data/raw/github_repo/repo-ss1024ss-llm-wiki/repo/README.md` -- "The Idea" P1 -- "Baseline from Andrej Karpathy's LLM Wiki pattern: the correct way to use LLMs is not Q&A, it's compilation."
[^src-2]: `data/raw/github_repo/repo-ss1024ss-llm-wiki/repo/README.md` -- "LLM Wiki" P1 -- "New session. AI remembers nothing. You spend 20 minutes re-explaining."
