---
id: three-layer-architecture
title: LLM Wiki 三层架构
status: accepted
card_type: architecture_pattern
tags:
- llm-wiki
- architecture
- raw-sources
- wiki-layer
- schema
created_time: 2026-06-12 15:01:00+08:00
edited_time: 2026-06-12 15:01:00+08:00
edited_entity: llm
source_ids:
- karpathy-gist-llm-wiki
evidence_basis: practitioner_report
justification: ../justification/three-layer-architecture.md
canonical_concept: three-layer-architecture
aliases:
- 三层架构
- raw-wiki-schema layers
- LLM wiki layers
summary: three-layer-architecture 描述 LLM Wiki 的三层权责分离：Raw sources（不可变真相源）→ Wiki（LLM 完全拥有的 markdown 页面层）→ Schema（约束 LLM 行为的配置文件，人机共同演进）
related:
- persistent-compounding-artifact
- raw-wiki-code-architecture
- three-layer-wiki-architecture
- human-llm-cognitive-division
- index-as-navigation
- ingest-operation
- wiki-as-codebase-metaphor
---
LLM Wiki 由三个明确分层构成，各层权责边界清晰：[^src-1]

**Raw sources（原始来源层）**：用户策展的源文档集合——文章、论文、图片、数据文件。此层不可变，LLM 只读不写，作为事实真相源 (source of truth)。[^src-2]

**Wiki（知识层）**：由 LLM 生成的 markdown 文件目录——摘要、实体页、概念页、对比、综述、综合。LLM 完全拥有此层，负责创建页面、在新 source 到达时更新、维护交叉引用、保持一致性。用户只读不写。[^src-3]

**Schema（配置层）**：一份告诉 LLM wiki 结构、约定和工作流的文档（如 CLAUDE.md 或 AGENTS.md）。这是使 LLM 成为"disciplined wiki maintainer rather than a generic chatbot"的关键配置。用户与 LLM 共同演进此层。[^src-4] [^card-1]

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture" P1 -- "There are three layers"
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture" P2 -- "These are immutable — the LLM reads from them but never modifies them. This is your source of truth."
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture" P3 -- "The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references"
[^src-4]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture" P4 -- "tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow"
[^card-1]: [persistent-compounding-artifact](persistent-compounding-artifact.md) -- 三层架构服务于持久性复合制品这一核心目标
