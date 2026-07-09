---
id: olw-three-stage-pipeline
title: olw 三阶段管线架构
status: accepted
card_type: architecture-pattern
tags:
- llm-pipeline
- obsidian
- knowledge-management
- local-first
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-kytmanov-obsidian-local
evidence_basis: code_implementation
justification: ../justification/olw-three-stage-pipeline.md
canonical_concept: olw-three-stage-pipeline
aliases:
- obsidian-llm-wiki pipeline
- olw pipeline
- ingest-compile-review
summary: obsidian-llm-wiki (olw) 采用三阶段管线架构将原始笔记编译为结构化 wiki： ingest 阶段使用 fast model (3B-8B) 提取 concept 并生成 source summary page， compile 阶段使用 heavy model (7B-14B) 汇聚源笔记生成带 wikilinks 的 draft article， review/approve
  阶段由人工交互审阅后发布。三阶段管线 pipeline architecture ingest compile review approve draft。
related:
- olw-rejection-feedback-loop
- olw-knowledge-item-candidates
- olw-llm-as-compiler
---

obsidian-llm-wiki (olw) 的核心架构是一条三阶段管线，将 Obsidian 原始笔记编译为互相链接的知识 wiki [^src-1]：

**Ingest（摄入）**：使用 fast model（推荐 3B-8B，如 gemma4:e4b）读取原始笔记，提取 concept 名称，将质量评分与摘要写入 state.db，并生成 `wiki/sources/` 下的 source summary page。

**Compile（编译）**：使用 heavy model（推荐 7B-14B，如 qwen2.5:14b）对每个 concept 汇聚所有提及它的源笔记，注入先前的 rejection feedback，写出带 `[[wikilinks]]` 的 wiki article 至 `wiki/.drafts/`。编译是增量的——仅与变更源笔记关联的 article 被重新编译 [^src-2]。

**Review/Approve（审阅/发布）**：人工通过 `olw review` 交互式审阅 draft，approve 后 article 发布至 `wiki/`，rejection feedback 存入 state DB 供下次 compile 使用。

该管线刻意不使用 vector database 或 embedding，而以 `wiki/index.md` 作为 query routing layer [^src-3]。

[^src-1]: `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` -- "How it works" P335-363 -- "The pipeline has three stages, each using the LLM for a different purpose"
[^src-2]: `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` -- "Features" P57 -- "Each concept gets its own article. When you change a source note, only the articles tied to that note recompile, not the whole vault."
[^src-3]: `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` -- "How it works" P364 -- "No vector databases, no embeddings. wiki/index.md acts as the routing layer for olw query."
