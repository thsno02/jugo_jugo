---
id: llmwiki-two-phase-pipeline
title: llmwiki 两阶段编译管线
status: draft
card_type: mechanism
tags: [two-phase-pipeline, concept-extraction, page-generation, incremental-compilation, SHA-256]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-atomicstrata-llm-wiki-compiler]
evidence_basis: code_implementation
justification: ../justification/llmwiki-two-phase-pipeline.md
canonical_concept: llmwiki-two-phase-pipeline
aliases: [two-phase pipeline, 两阶段管线, concept extraction, page generation, incremental compile]
summary: >-
  llmwiki 编译采用两阶段管线：Phase 1 从所有源中提取全部概念，
  Phase 2 生成页面。消除顺序依赖、在写入前捕获失败、
  将多源共享概念合并为单页。增量编译通过 SHA-256 哈希检测变更，
  仅处理已变化的源。
related: [llmwiki-compile-first-architecture, llmwiki-epistemic-metadata]
---

llmwiki 的编译采用两阶段管线设计。Phase 1 从所有源中提取全部概念；Phase 2 根据提取结果生成 wiki 页面。[^src-1] [^card-1]

两阶段分离带来三个工程收益：消除源处理的顺序依赖、在任何写入发生前捕获失败、将多个源共享的概念合并为单个页面。[^src-2]

增量编译通过 SHA-256 哈希实现变更检测：仅已变化的源经过 LLM 处理，其余全部跳过。[^src-3]

整体流水线为：`sources/ → SHA-256 hash check → LLM concept extraction → wiki page generation → [[wikilink]] resolution → index.md`。[^src-4]

[^src-1]: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md -- "How it works" P200-201 -- "Two-phase pipeline. Phase 1 extracts all concepts from all sources. Phase 2 generates pages."
[^src-2]: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md -- "How it works" P201 -- "This eliminates order-dependence, catches failures before writing anything, and merges concepts shared across multiple sources into single pages."
[^src-3]: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md -- "How it works" P203 -- "Incremental. Only changed sources go through the LLM. Everything else is skipped via hash-based change detection."
[^src-4]: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md -- "How it works" P198 -- "sources/ → SHA-256 hash check → LLM concept extraction → wiki page generation → [[wikilink]] resolution → index.md"
[^card-1]: llmwiki-compile-first-architecture -- 两阶段管线是编译优先架构的具体实现机制
