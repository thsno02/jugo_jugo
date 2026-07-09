---
id: rag-three-stage-pipeline
title: RAG 三阶段检索管道
status: draft
card_type: architecture_pattern
tags: [rag, vector-database, embedding, chunking, retrieval-pipeline]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [atlan-llm-wiki-vs-rag-dynamic-20260524]
evidence_basis: practitioner_report
justification: ../justification/rag-three-stage-pipeline.md
canonical_concept: rag-three-stage-pipeline
aliases: [RAG pipeline, retrieval-augmented generation pipeline, RAG 管道, 向量检索管道]
summary: >-
  RAG three-stage pipeline 包含：(1) 文档切分为可检索片段(chunking)，(2) embedding model 将片段转为向量表示，(3) 向量存入向量数据库(Pinecone/Weaviate/pgvector)建索引。查询时：用户问题向量化→top-K 相似度检索→片段作为 context 交给 LLM 合成回答。chunking 策略直接影响检索质量，embedding 漂移需持续维护。
related: [compile-time-vs-query-time-knowledge-assembly]
---

检索增强生成(RAG)知识库将向量索引文档存储与检索层结合，在查询时检索语义相关片段。LLM 从不加载完整语料——仅基于检索到的 context 生成回答。[^src-1]

**三阶段工作流**：

1. **Chunking**：文档切分为可检索片段——切分策略直接影响检索质量
2. **Embedding**：每个片段由 embedding model（如专用向量化模型）转为向量表示进行语义索引
3. **向量索引**：向量存入向量数据库（Pinecone、Weaviate、pgvector）进行快速相似度搜索 [^src-2]

**查询时流程**：用户查询 → 转为向量 → 检索 top-K 最相似片段 → 片段作为 context 传递给 LLM → LLM 从检索证据（非预加载索引）合成回答。[^src-3]

**工程开销**：chunking 和 embedding 策略显著影响检索质量，为每次部署增加有意义的工程开销。[^src-4] [^card-1]

[^src-1]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is a RAG knowledge base?" P33 -- "A RAG knowledge base combines a vector-indexed document store with a retrieval layer that surfaces semantically relevant chunks at query time."
[^src-2]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is a RAG knowledge base?" P34 -- "Documents are chunked into retrievable segments, each chunk is converted into a vector embedding by an embedding model, and those embeddings are indexed in a vector database"
[^src-3]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is a RAG knowledge base?" P34 -- "the system converts the user's query into a vector, retrieves the top-K most semantically similar chunks, and passes them as context to the LLM"
[^src-4]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is a RAG knowledge base?" P36 -- "Chunking and embedding strategies significantly affect retrieval quality, adding meaningful engineering overhead to every deployment."
[^card-1]: 参见 [[compile-time-vs-query-time-knowledge-assembly]] — RAG 属 query-time assembly 模式
