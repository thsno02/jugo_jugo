---
id: llm-wiki-knowledge-system
title: LLM Wiki 知识系统的核心定义与架构
status: accepted
card_type: concept-definition
tags:
- llm-wiki
- knowledge-system
- wiki-architecture
- compounding-knowledge
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-astro-han-karpathy-llm-wiki
evidence_basis: code_implementation
justification: ../justification/llm-wiki-knowledge-system.md
canonical_concept: llm-wiki-knowledge-system
aliases:
- LLM wiki
- LLM Wiki
- llm wiki knowledge system
summary: LLM wiki 是一种知识系统，LLM 维护结构化 wiki 页面而非每次查询重新搜索原始文档。 架构为 raw/（不可变源材料）+ wiki/（LLM 维护的 curated markdown pages）+ index.md（全局目录）+ log.md（追加操作日志）。新源可更新多个页面、强化 cross-references 交叉引用、记录 contradictions 矛盾。知识随时间复合增长
  (compounding knowledge)。
related:
- llm-wiki-vs-rag
- karpathy-llm-wiki-skill
- karpathy-llm-wiki-concept
- karpathy-llm-wiki-pattern
- karpathy-llm-wiki-three-layer-architecture
- llm-knowledge-base-pattern
- llm-wiki-definition-and-core-value
- llm-wiki-pattern
- llm-wiki-pattern-definition
- llm-wiki-pattern-overview
- llm-wiki-three-folder-architecture
- olw-llm-as-compiler
- llm-wiki-vs-rag-ingest-time-synthesis
---
LLM wiki 是一种知识系统，其中 LLM 维护结构化的 wiki 页面，而非在每次提问时重新搜索原始文档。新源材料被编译为持久的 markdown 页面，交叉引用随时间更新，回答引用已包含综合知识的 wiki 页面。[^src-1]

## 目录结构

```
project/
├── raw/            ← 不可变源材料
│   └── topic/
│       └── 2026-04-03-source-article.md
├── wiki/           ← LLM 维护的编译知识页面
│   ├── topic/
│   │   └── concept-name.md
│   ├── index.md    ← 全局目录
│   └── log.md      ← 追加操作日志
```

[^src-2]

## 复合增长机制

每个新源可以更新多个页面、强化交叉引用（cross-references）、并记录矛盾（contradictions）。这使得 wiki 随时间复合增长（compound over time）。[^src-3]

## 核心设计理念

LLM 维护 wiki，人类专注于选择源材料和提出好问题。[^src-4]

---
[^src-1]: data/raw/github_repo/repo-astro-han-karpathy-llm-wiki/repo/README.md -- "What Is an LLM Wiki?" P1 -- "An LLM wiki is a knowledge system where the LLM maintains structured wiki pages instead of re-searching raw documents on every question."
[^src-2]: data/raw/github_repo/repo-astro-han-karpathy-llm-wiki/repo/README.md -- "How the Workflow Works" P1 -- "your-project/ ├── raw/ ... ├── wiki/ ..."
[^src-3]: data/raw/github_repo/repo-astro-han-karpathy-llm-wiki/repo/README.md -- "How the Workflow Works" P2 -- "Each new source can update multiple pages, strengthen cross-references, and record contradictions. That is what makes the wiki compound over time."
[^src-4]: data/raw/github_repo/repo-astro-han-karpathy-llm-wiki/repo/README.md -- "How the Workflow Works" P1 -- "the LLM maintains the wiki while the human focuses on choosing sources and asking good questions."
