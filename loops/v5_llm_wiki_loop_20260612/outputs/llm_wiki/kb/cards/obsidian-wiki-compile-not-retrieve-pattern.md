---
id: obsidian-wiki-compile-not-retrieve-pattern
title: obsidian-wiki 编译式知识管理模式
status: accepted
card_type: design-philosophy
tags:
- llm-wiki-pattern
- compile-knowledge
- karpathy
- obsidian
- knowledge-management
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-ar9av-obsidian-wiki
evidence_basis: code_implementation
justification: ../justification/obsidian-wiki-compile-not-retrieve-pattern.md
canonical_concept: compile-not-retrieve-llm-wiki
aliases:
- LLM Wiki pattern
- compile don't retrieve
- Karpathy wiki pattern
- 编译式知识管理
summary: obsidian-wiki 实现 Karpathy 提出的 LLM Wiki 模式（compile-not-retrieve-llm-wiki）： 不重复向 LLM 问同样问题或每次做 RAG，而是将知识一次性编译到互联 markdown 文件中并保持更新。 Obsidian 作为 viewer，LLM 作为 maintainer。框架在此基础上包装了 skill 文件体系， 让任何
  AI 编码代理可读取并执行知识管理操作。核心原则："Compile, don't retrieve"。
related:
- karpathy-llm-wiki-pattern
- karpathy-llm-wiki-pattern-automation
- llm-compilation-paradigm
- llm-wiki-agent-compile-once-architecture
- llm-wiki-pattern
- llm-wiki-pattern-definition
- llm-wiki-pattern-overview
- llmwiki-compile-first-architecture
- obsidian-wiki-agent-agnostic-skill-framework
- obsidian-wiki-four-stage-pipeline
- obsidian-wiki-tiered-retrieval
---
obsidian-wiki 是一个受 Andrej Karpathy 发表的 gist 启发的知识管理系统[^src-1]，实现了"LLM Wiki"模式的核心理念：

**核心洞察**：不重复向 LLM 问同样的问题（或每次都做 RAG），而是将知识一次性编译（compile）到互联的 markdown 文件中，并保持它们持续更新[^src-2]。

**角色分工**：Obsidian 作为 viewer（人类浏览界面），LLM 作为 maintainer（知识的摄入、提取、合并和维护者）[^src-3]。

**框架化实现**：该项目在 Karpathy 的原始模式上构建了完整框架——一组 markdown skill 文件，任何 AI 编码代理（Claude Code、Cursor、Windsurf、Pi 等）均可读取并执行[^src-4]。用户将代理指向 Obsidian vault 并告诉它做什么即可。

**设计原则**（据 CLAUDE.md）："Compile, don't retrieve. The wiki is pre-compiled knowledge. Update existing pages — don't append or duplicate."[^src-5]

[^src-1]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "Header" P1 -- "A knowledge mgmt system inspired by gist published by Andrej Karpathy about maintaining a personal knowledge base with LLMs : the 'LLM Wiki' pattern."
[^src-2]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "Header" P1 -- "Instead of asking an LLM the same questions over over (or doing RAG every time), you compile knowledge once into interconnected markdown files and keep them current."
[^src-3]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "Header" P1 -- "In this case Obsidian is the viewer and the LLM is the maintainer."
[^src-4]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "Header" P2 -- "We took that and built a framework around it. The whole thing is a set of markdown skill files that any AI coding agent...can read and execute."
[^src-5]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/CLAUDE.md -- "Core Principles" P1 -- "Compile, don't retrieve. The wiki is pre-compiled knowledge. Update existing pages — don't append or duplicate."
