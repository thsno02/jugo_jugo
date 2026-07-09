---
id: llm-knowledge-base-pattern
title: LLM 知识库模式（Karpathy pattern）
status: draft
card_type: architecture-pattern
tags: [llm-wiki, karpathy-pattern, personal-knowledge-management, markdown-wiki, zero-infrastructure]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [robin-cartier-llm-knowledge-bases]
evidence_basis: practitioner_report
justification: ../justification/llm-knowledge-base-pattern.md
canonical_concept: llm-knowledge-base-pattern
aliases: [LLM Knowledge Bases, Karpathy pattern, LLM wiki, LLM-maintained wiki, personal knowledge base pattern]
summary: >-
  LLM 知识库模式（Karpathy pattern）：LLM 增量构建和维护持久化、互链的 markdown wiki，替代查询时的 RAG。三层架构：raw/（不可变源文件）、wiki/（LLM 生成的 markdown 页面含交叉引用）、schema file（如 CLAUDE.md，治理规则）。附带 index.md（分类目录）和 log.md（操作日志）。工作流：投入源→LLM 一次性产出 10-15 页 wiki。零基础设施：无 embedding model、无 vector database、无 chunking pipeline。Token 成本每次 ingest ~$2-5。
related: []
---

LLM 知识库模式（又称 Karpathy pattern）是一种个人知识管理架构：LLM 增量构建和维护一个持久化、互链的 markdown wiki，替代查询时的检索增强生成（RAG）。[^src-1]

**三层架构设计**：
1. **raw/**——不可变源文件（PDF、文章、转录稿），永不编辑
2. **wiki/**——LLM 生成的 markdown 页面，含交叉引用、摘要、概念图。LLM 拥有这些文件
3. **Schema file**（如 CLAUDE.md）——治理文件夹结构、引用规则、ingest 工作流、linting 约定

附带两个承重元文件：index.md（按分类组织的目录，每次 ingest 更新）和 log.md（每次操作的时序记录）。

**工作流**：将源文件投入 raw/ → 告知 LLM ingest → LLM 在 wiki/ 下一次创建或更新 10-15 个 markdown 页（提取实体、概念、关系、交叉引用）→ 查询时 LLM 读取 index 循链接回答，不走向量相似度检索。

**零基础设施**：无 embedding model、无 vector database、无 chunking pipeline。仅 markdown 文件在文件夹中。Token 成本：主要 session ~$2-5（10-15 页）；linting <$1；查询可忽略。任何编辑器可用，Obsidian 仅提供可选的图视图。[^src-1]

[^src-1]: `data/raw/webpage/robin-cartier-llm-knowledge-bases/markdown.md` -- "Key points" P1 -- "Three layers by design... drop a source into raw/, tell the LLM to ingest it, and it creates or updates 10–15 wiki pages in one pass"
