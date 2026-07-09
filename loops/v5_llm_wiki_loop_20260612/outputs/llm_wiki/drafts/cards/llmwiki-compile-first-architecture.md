---
id: llmwiki-compile-first-architecture
title: llmwiki 编译优先架构
status: draft
card_type: architectural-pattern
tags: [knowledge-compilation, compile-first, RAG-alternative, compounding-knowledge]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-atomicstrata-llm-wiki-compiler]
evidence_basis: code_implementation
justification: ../justification/llmwiki-compile-first-architecture.md
canonical_concept: llmwiki-compile-first-architecture
aliases: [llmwiki, llm-wiki-compiler, compile-first wiki, LLM Wiki pattern, Karpathy LLM Wiki]
summary: >-
  llmwiki 实现 Karpathy 的 LLM Wiki 模式：将原始源编译为持久化互链 wiki，
  而非 RAG 式查询时检索。概念获得独立页面、页面互相 wikilink、
  query --save 将回答写回 wiki 使后续查询上下文更丰富，知识随使用累积。
  与 RAG 互补而非替代。
related: [llmwiki-two-phase-pipeline]
---

llmwiki 实现 Karpathy 提出的"LLM Wiki"模式：不在查询时重新发现知识，而是将原始源一次性编译为持久、可浏览的 wiki 产物，使知识随时间累积。[^src-1]

与 RAG 的核心区别在于知识是否积累：RAG 在查询时检索 chunk 并生成答案，每个问题从头重新发现相同关系，nothing accumulates；llmwiki 将源编译为 wiki，概念获得独立页面，页面通过 wikilink 互链。[^src-2]

`llmwiki query --save` 实现复合效应：答案被保存为新 wiki 页面，未来查询将该页面作为上下文使用，探索过程自身变为知识资产。[^src-3]

该工具明确定位为与 RAG 互补而非替代——RAG 适合对大语料库的临时检索，llmwiki 提供结构化的持久产物作为检索目标。[^src-4]

[^src-1]: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md -- "Header" P3 -- "Inspired by Karpathy's LLM Wiki pattern: instead of re-discovering knowledge at query time, compile it once into a persistent, browsable artifact that compounds over time."
[^src-2]: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md -- "Why not just RAG?" P183-188 -- "RAG retrieves chunks at query time. Every question re-discovers the same relationships from scratch. Nothing accumulates. llmwiki compiles your sources into a wiki."
[^src-3]: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md -- "Why not just RAG?" P188 -- "When you ask a question with --save, the answer becomes a new page, and future queries use it as context. Your explorations compound."
[^src-4]: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md -- "Why not just RAG?" P189 -- "This is complementary to RAG, not a replacement."
