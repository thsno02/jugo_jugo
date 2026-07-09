---
id: compile-over-rag-wiki-pattern
title: 编译式知识库优于 RAG 模式
status: accepted
card_type: architectural-pattern
tags:
- llm-wiki
- RAG
- compile
- knowledge-base
- wiki
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-lewislulu-llm-wiki-skill
evidence_basis: code_implementation
justification: ../justification/compile-over-rag-wiki-pattern.md
canonical_concept: compile-over-rag-wiki-pattern
aliases:
- compile over RAG
- 编译式wiki
- Karpathy-style LLM knowledge base
- llm-wiki pattern
- 知识复利wiki
summary: compile-over-rag-wiki-pattern 编译式知识库优于RAG模式：与 RAG 每次查询重新检索原始文档不同， llm-wiki 让 LLM 将原始来源编译(compile)为持久化、交叉链接的 Markdown wiki， 通过 compile/ingest/query/lint/audit 五阶段迭代使知识复利积累(knowledge compounds over
  time)。 灵感来自 Andrej Karpathy 的 llm-wiki Gist。
related:
- olw-llm-as-compiler
- kb-compile-implementation
- llm-wiki-audit-shared-library
- llm-wiki-human-machine-division
---
llm-wiki 提出一种替代 RAG 的知识管理模式：不在每次查询时重新检索原始文档，而是让 LLM 将原始来源预先"编译"为持久化、交叉链接的 Markdown wiki。[^src-1]

该模式通过五个操作阶段——compile、ingest、query、lint、audit——使 wiki 持续富化，知识随时间复利积累(knowledge compounds over time)。[^src-2]

项目灵感来自 Andrej Karpathy 的 llm-wiki Gist，定位为 OpenClaw/Codex Agent Skill。[^src-3]

[^src-1]: `data/raw/github_repo/repo-lewislulu-llm-wiki-skill/repo/README.md` -- "What this is" P1 -- "Instead of RAG (re-retrieving raw docs on every query), this pattern has the LLM compile raw sources into a persistent, cross-linked Markdown wiki."
[^src-2]: `data/raw/github_repo/repo-lewislulu-llm-wiki-skill/repo/README.md` -- "What this is" P1 -- "Every compile, ingest, query, lint, and audit pass makes the wiki richer. Knowledge compounds over time."
[^src-3]: `data/raw/github_repo/repo-lewislulu-llm-wiki-skill/repo/README.md` -- "Title" P1 -- "An OpenClaw / Codex Agent Skill for building Karpathy-style LLM knowledge bases."
