---
id: full-context-vs-rag
title: 全量上下文策略对比 RAG
status: accepted
card_type: design-decision
tags:
- llm-wiki
- rag
- context-window
- architecture-decision
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- obsidian-community-plugin
evidence_basis: documentation
justification: ../justification/full-context-vs-rag.md
canonical_concept: full-context-vs-rag
aliases:
- full-context strategy
- non-RAG
- 全量上下文
- 非RAG策略
summary: Karpathy LLM Wiki 采用全量上下文策略而非 RAG：将完整 Wiki 内容喂给 LLM 而非分块检索。 理由是 RAG 将知识碎片化，破坏 LLM 跨知识图谱推理的能力。因此强烈推荐长上下文模型（1M+ tokens）。
related:
- karpathy-llm-wiki-concept
- llm-wiki-model-recommendations
- full-stack-locality-privacy-tradeoff
- llm-kb-vs-rag-comparison
- conversational-wiki-query
---
该插件遵循 Karpathy 的哲学：向 LLM 提供完整 Wiki 上下文，而非分块 RAG 检索。据材料所述，Karpathy 的原始批评认为 RAG 将知识碎片化并破坏了 LLM 跨完整知识图谱推理的能力。[^src-1]

因此强烈推荐长上下文模型——Wiki 越大，LLM 需要的上下文越多。材料推荐的模型多具有 1M+ tokens 上下文窗口。[^src-2] [^card-1]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Model Recommendations" P1 -- "feed the LLM full Wiki context, not chunked RAG retrieval. Long-context models are strongly recommended"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Why not RAG?" P1 -- "Karpathy's original critique argues that RAG fragments knowledge and breaks the LLM's ability to reason across the full knowledge graph"
[^card-1]: 参见 [[karpathy-llm-wiki-concept]] 了解整体设计理念
