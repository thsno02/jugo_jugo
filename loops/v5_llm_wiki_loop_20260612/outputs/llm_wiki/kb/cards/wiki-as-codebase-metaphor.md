---
id: wiki-as-codebase-metaphor
title: Wiki-as-Codebase 类比：LLM 是程序员，Obsidian 是 IDE
status: accepted
card_type: conceptual_metaphor
tags:
- llm-wiki
- metaphor
- software-engineering-analogy
- obsidian
- development-workflow
created_time: 2026-06-12 15:08:00+08:00
edited_time: 2026-06-12 15:08:00+08:00
edited_entity: llm
source_ids:
- karpathy-gist-llm-wiki
evidence_basis: practitioner_report
justification: ../justification/wiki-as-codebase-metaphor.md
canonical_concept: wiki-as-codebase-metaphor
aliases:
- IDE-programmer-codebase analogy
- Obsidian as IDE
- wiki 即代码库
summary: wiki-as-codebase-metaphor 是 Karpathy 描述 LLM Wiki 工作模式的三重类比：Obsidian 是 IDE（浏览/导航环境）、LLM 是 programmer（唯一写入者）、wiki 是 codebase（持续维护的活代码）；人类角色类似 code reviewer
related:
- human-llm-cognitive-division
- three-layer-architecture
- llm-wiki-maintenance-engine-analogy
- obsidian-as-llm-ide
---

Karpathy 用软件工程三重类比描述 LLM Wiki 的工作模式："Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."[^src-1]

这一类比传达了多层设计意图：

1. **Wiki 是活代码**：不是写完就放的静态文档，而是需要持续维护、重构、更新的活系统——类似生产代码。[^card-1]
2. **LLM 是唯一写入者**：拥有完全的"代码所有权"——"the LLM makes edits based on our conversation, and I browse the results in real time"。[^src-2]
3. **Obsidian 是观察环境**：用户"following links, checking the graph view, reading the updated pages"——角色类似 code reviewer 而非 coder。[^src-3]

作者的实际工作流："I have the LLM agent open on one side and Obsidian open on the other"——双屏并行，LLM 执行写入，人类实时浏览审查。[^src-4] [^card-2]

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P4 -- "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P4 -- "The LLM makes edits based on our conversation, and I browse the results in real time"
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P4 -- "following links, checking the graph view, reading the updated pages"
[^src-4]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P4 -- "I have the LLM agent open on one side and Obsidian open on the other."
[^card-1]: [persistent-compounding-artifact](persistent-compounding-artifact.md) -- "活代码"性质正是 persistent compounding artifact 的实践体现
[^card-2]: [human-llm-cognitive-division](human-llm-cognitive-division.md) -- 类比中的角色分配映射了认知分工原则
