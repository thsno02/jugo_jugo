---
id: llm-wiki-immutable-raw-sources
title: Raw Sources 不可变性原则
status: draft
card_type: design-principle
tags: [llm-wiki, immutability, audit-trail, raw-sources]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-immutable-raw-sources.md
canonical_concept: immutable-raw-sources
aliases: [immutable sources, raw source immutability, 不可变源]
summary: >-
  immutable-raw-sources 原则：一旦源被摄取到 raw/ 就永不修改，这构成审计追踪，每条声明可追溯到源，wiki articles 在 raw 之上合成，retract 命令同时清理源和下游引用
related: [llm-wiki-hub-architecture, llm-wiki-compilation-process, llm-wiki-audit-trust-verification]
---

llm-wiki 的数据完整性建立在 raw sources 不可变性原则之上：一旦论文、文章或数据文件被摄取，就永远不被修改。这构成了审计追踪——每篇编译文章中的每条声明都可追溯回某个原始源。[^src-1]

Wiki articles 是在 raw sources 之上的 LLM 编译合成，带交叉引用和置信度评分。当需要撤回时，retract 命令会同时清理源和下游引用。[^src-2]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Architecture" P197 -- "Raw sources (raw/) are immutable. Once a paper, article, or data file is ingested, it's never modified. This is the audit trail — every claim in every article traces back to a source."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "How It Works" P118 -- "Once a source is ingested it is never modified. Articles synthesize on top. Retraction removes both cleanly."
