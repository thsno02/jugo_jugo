---
id: local-rag-three-stage-pipeline
title: 本地 RAG 三阶段管线架构
status: draft
card_type: architecture-pattern
tags: [rag, pipeline, chunking, embedding, generation, vector-search]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [kunal-local-knowledge-base]
evidence_basis: practitioner_report
justification: ../justification/local-rag-three-stage-pipeline.md
canonical_concept: local-rag-pipeline
aliases: [RAG pipeline, three-stage RAG, 检索增强生成管线, ingestion-embedding-generation]
summary: >-
  本地 RAG 管线由三阶段构成：Ingestion（文档分块 256-512 tokens）、Embedding（向量化语义指纹）、Generation（top-k 相关块拼入 prompt 由本地 LLM 合成答案）。chunk size 选择关键——过小丢失上下文，过大引入噪声。
related: []
---

据材料描述，LLM wiki 的 RAG 管线分为三个阶段：[^src-1]

1. **Ingestion（摄入）**：文档被切分为 chunks，典型大小为 256-512 tokens。作者强调 chunk size 的重要性超出多数教程所述——"too small and you lose context, too large and your retrieval gets noisy"。[^src-2]

2. **Embedding（向量化）**：每个 chunk 被转换为向量 embedding，作为捕获语义含义的"数学指纹"。用户查询以相同方式向量化，系统找到向量距离最近的 chunks。[^src-3]

3. **Generation（生成）**：top-k 最相关 chunks 与用户问题一同拼入 prompt，由本地 LLM 合成回答。[^src-4]

[^card-1]: 与 [llm-wiki-definition-and-core-value] 互补——该卡定义"是什么"，本卡展开"怎么做"。

[^src-1]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "How the LLM Wiki Architecture Actually Works" P12 -- "The pipeline has three stages"
[^src-2]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "How the LLM Wiki Architecture Actually Works" P13 -- "Your documents get split into chunks (typically 256-512 tokens each). Chunk size matters more than most tutorials admit"
[^src-3]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "How the LLM Wiki Architecture Actually Works" P14 -- "Each chunk gets converted into a vector embedding. Think of it as a mathematical fingerprint capturing semantic meaning"
[^src-4]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "How the LLM Wiki Architecture Actually Works" P15 -- "The top-k most relevant chunks get stuffed into a prompt alongside your question, and the local LLM synthesizes an answer"
