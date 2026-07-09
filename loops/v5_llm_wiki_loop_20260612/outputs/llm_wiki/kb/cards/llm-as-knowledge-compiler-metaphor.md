---
id: llm-as-knowledge-compiler-metaphor
title: LLM 作为知识编译器的核心隐喻
status: accepted
card_type: design-philosophy
tags:
- llm-wiki
- knowledge-management
- compiler-metaphor
- agent-architecture
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-nvk-llm-wiki
evidence_basis: code_implementation
justification: ../justification/llm-as-knowledge-compiler-metaphor.md
canonical_concept: llm-as-knowledge-compiler
aliases:
- LLM compiler metaphor
- LLM wiki compiler
- knowledge compiler
- LLM-compiled knowledge base
summary: llm-wiki 的核心设计隐喻将 LLM 视为知识编译器：raw sources 是源代码，LLM agent 是编译器，wiki articles 是可执行文件。原始材料一经 ingest 即不可变（immutable），所有综合工作发生在 wiki/ 层。LLM 同时充当编译引擎和查询接口。该隐喻源自 Karpathy 的 LLM wiki 概念。
related:
- hub-topic-wiki-isolation
- derived-index-concurrency-protocol
- llm-as-knowledge-compiler
- claude-first-multi-runtime-packaging
- collection-ingestion-adapter-system
- dual-link-obsidian-agent-compatibility
- multi-agent-parallel-research-pipeline
---
llm-wiki 项目的基础设计哲学将大语言模型定位为"知识编译器"：

- **raw sources 是源代码**：一旦 ingest 进入 `raw/` 目录即不可变，作为原始证据的永久记录
- **LLM agent 是编译器**：从多个源提取、综合、上下文化，产出结构化知识制品
- **wiki articles 是可执行文件**：编译后的综合文章，可被查询、交叉引用、持续更新

该隐喻据材料推测源自 Andrej Karpathy 的 LLM wiki 概念[^src-1]，由 nvk 实现为一个完整的 Claude Code 插件系统。

核心原则包括：文章是综合而非复制（"think textbook, not clipboard"）；增量编译为默认模式；诚实地承认知识缺口而非幻觉填补。[^src-2]

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "README.md Credits" -- "Andrej Karpathy — the LLM wiki concept"
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "AGENTS.md Core Principles" -- "Articles are synthesized, not copied. Draw from multiple sources, contextualize, connect. Think textbook, not clipboard."
