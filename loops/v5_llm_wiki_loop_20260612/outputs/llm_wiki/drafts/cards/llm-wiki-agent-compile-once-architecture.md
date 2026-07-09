---
id: llm-wiki-agent-compile-once-architecture
title: 编译式知识管理架构
status: draft
card_type: architecture-pattern
tags: [knowledge-management, wiki, incremental-compilation, ingest-workflow]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-samuraigpt-llm-wiki-agent]
evidence_basis: code_implementation
justification: ../justification/llm-wiki-agent-compile-once-architecture.md
canonical_concept: compile-once-knowledge-management
aliases: [compile once, 编译式知识管理, incremental wiki compilation, LLM Wiki Agent ingest]
summary: >-
  LLM Wiki Agent 采用 compile-once-knowledge-management 架构：每次 ingest 是增量编译，
  wiki 是编译产物。源文档经 10 步 ingest workflow 转化为结构化 wiki 页面(source/entity/concept pages)，
  同时更新 index、overview、标记矛盾、追加 log。与 RAG 的"每次查询重新推导"相对，
  知识只编译一次并持续维护。Knowledge graph 通过两遍构建(deterministic wikilink 解析 + semantic 推断)
  生成 EXTRACTED/INFERRED/AMBIGUOUS 边，Louvain 聚类，SHA256 缓存增量处理。
related: []
---

LLM Wiki Agent 的核心设计模式是"编译式知识管理"：将原始文档视为源码，wiki 视为编译产物，每次 ingest 执行增量编译。[^src-1]

完整的 ingest workflow 包含 10 个步骤：(1) 全文读入源文档 → (2) 读取现有 index 和 overview 获取上下文 → (3) 写 source 页 → (4) 更新 index → (5) 修订 overview → (6) 创建/更新 entity 页 → (7) 创建/更新 concept 页 → (8) 标记矛盾 → (9) 追加 log → (10) post-ingest 验证（检查 broken wikilinks、确认新页面在 index 中）。[^src-2]

产出物分为多层：source pages（每个源文档一页摘要）、entity pages（人物/公司/项目自动创建）、concept pages（概念/框架自动创建）、overview.md（跨所有源的活态综述，每次 ingest 修订）、以及 knowledge graph。[^src-3]

Knowledge graph 采用两遍构建：Pass 1 确定性解析所有 `[[wikilinks]]` 生成 EXTRACTED 边；Pass 2 由 agent 推断隐式关系生成带置信度的 INFERRED 边或 AMBIGUOUS 边。Louvain community detection 聚类节点，SHA256 缓存确保只重处理变化页面。[^src-4]

矛盾在 ingest 时即被标记，而非等到 query 时才浮现——这是与 RAG 系统的关键行为差异之一。[^src-5]

[^src-1]: `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md` -- "Introduction" P1 -- "it reads them, extracts knowledge, and builds a persistent interlinked wiki. Every new source makes the wiki richer."
[^src-2]: `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/CLAUDE.md` -- "Ingest Workflow" -- "Steps (in order): 1. Read the source document fully..."
[^src-3]: `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md` -- "What You Get" -- "Persistent wiki...Entity pages...Concept pages...Living overview"
[^src-4]: `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md` -- "The Graph" -- "Two-pass build: 1. Deterministic — parses all [[wikilinks]]... 2. Semantic — agent infers implicit relationships..."
[^src-5]: `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md` -- "What You Get" -- "when a new source contradicts an existing claim, it's flagged at ingest time, not buried until query time."
