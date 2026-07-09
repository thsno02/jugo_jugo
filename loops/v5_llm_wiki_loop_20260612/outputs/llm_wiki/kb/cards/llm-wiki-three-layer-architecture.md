---
id: llm-wiki-three-layer-architecture
title: LLM Wiki 三层架构
status: accepted
card_type: architecture-structure
tags:
- llm-wiki
- three-layer
- raw-sources
- schema
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- marvin-hn-persistent-knowledge
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-three-layer-architecture.md
canonical_concept: llm-wiki-three-layer-architecture
aliases:
- three layers
- 三层结构
- raw sources / wiki / schema
summary: 'LLM Wiki 三层架构 (llm-wiki-three-layer-architecture): 第一层 raw sources 为不可变 ground truth（文章/论文/转录/图像/数据集）；第二层 wiki 为 LLM 撰写的 markdown 页面（摘要/概念/实体/比较/综合）；第三层 schema 为规则文档（AGENTS.md / CLAUDE.md）指导 agent
  如何结构化和维护 wiki。'
related:
- llm-wiki-pattern-overview
- llm-wiki-ingest-query-lint
- llm-wiki-three-layer-structure
- agents-md-instruction-file
- bttb-production-reference
- llm-wiki-compilation-analogy
- llm-wiki-compiled-artifact-analogy
- llm-wiki-ingest-loop
- llm-wiki-ingestion-workflow
- llm-wiki-setup-procedure
- llm-wiki-v2-agent-memory
---
Karpathy 将 LLM Wiki 系统构造为三个明确层次：[^src-1]

1. **Raw Sources（原始源）**：不可变的文章、论文、转录文本、图像或数据集，始终作为 ground truth 保留。

2. **Wiki（知识层）**：由 LLM 撰写的 markdown 页面目录，包含摘要、概念、实体、比较以及更广泛的综合分析。

3. **Schema（规则层）**：如 AGENTS.md 或 CLAUDE.md 这样的规则文档，告知 agent wiki 应如何被结构化和维护。

这种分层将不可变的事实来源、可变的知识编译产物、以及指导维护行为的元规则清晰分开。[^card-1]

[^src-1]: data/raw/webpage/marvin-hn-persistent-knowledge/markdown.md -- "The three layers and the operating loop" P1 -- "Karpathy frames the system in three layers. The first is raw sources: immutable articles, papers, transcripts, images, or datasets that remain the ground truth. The second is the wiki, a directory of LLM-authored markdown pages containing summaries, concepts, entities, comparisons, and broader syntheses. The third is the schema, a rules document such as AGENTS.md or CLAUDE.md that tells the agent how the wiki should be structured and maintained."
[^card-1]: llm-wiki-pattern-overview
