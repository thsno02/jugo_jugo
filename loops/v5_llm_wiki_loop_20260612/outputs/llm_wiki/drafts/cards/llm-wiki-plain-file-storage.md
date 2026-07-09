---
id: llm-wiki-plain-file-storage
title: LLM Wiki 纯文本文件存储架构
status: draft
card_type: architectural-principle
tags: [llm-wiki, markdown, storage, portability]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [aillm-wiki-directory]
evidence_basis: documentation
justification: ../justification/llm-wiki-plain-file-storage.md
canonical_concept: llm-wiki-plain-file-storage
aliases: [plain markdown files, LLM Wiki storage, no vector DB]
summary: >-
  LLM Wiki 采用纯 markdown 文件存储，无向量 DB、无 embeddings、无需维护基础设施。兼容 Obsidian、Notion 或任意编辑器，可 grep 搜索、git diff 追踪、离线阅读。知识库的生命周期超越任何单一工具。
related: [llm-wiki-pattern-definition, llm-wiki-vs-rag]
---

LLM Wiki 的存储层采用纯 markdown 文件，置于普通文件夹中。[^card-1]

该设计选择带来以下特性：[^src-1]
- **零基础设施依赖**：无向量数据库、无 embeddings 计算、无需维护服务
- **工具无关**：兼容 Obsidian、Notion 或任何文本编辑器
- **可操作性**：支持 grep 搜索、git diff 版本追踪、离线阅读（如飞机上）

材料特别强调知识库的持久性——"The knowledge base outlives any tool you use to build it"——纯文件格式确保知识库生命周期不绑定于任何特定工具或服务。[^src-2]

[^card-1]: 参见 [[llm-wiki-pattern-definition]] LLM Wiki 模式的基本定义
[^src-1]: `data/raw/webpage/aillm-wiki-directory/markdown.md` -- "Value Props" P6 -- "Plain markdown files in a folder. No vector DB, no embeddings, no infrastructure to maintain. Works with Obsidian, Notion, or any editor"
[^src-2]: `data/raw/webpage/aillm-wiki-directory/markdown.md` -- "Value Props" P6 -- "The knowledge base outlives any tool you use to build it"
