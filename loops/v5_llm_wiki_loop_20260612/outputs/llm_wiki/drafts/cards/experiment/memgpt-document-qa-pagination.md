---
id: memgpt-document-qa-pagination
title: MemGPT 文档问答中的迭代检索优势
status: draft
card_type: empirical-result
tags: [memgpt, document-qa, pagination, retrieval, embedding-search]
created_time: 2026-06-12T10:16:00+08:00
edited_time: 2026-06-12T10:16:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-document-qa-pagination.md
canonical_concept: document-qa-iterative-retrieval
aliases: [文档问答迭代检索, document QA, pagination retrieval, archival search]
summary: >-
  MemGPT document-qa-iterative-retrieval 在文档QA中性能不受文档数增加影响：通过 pagination 迭代检索 archival storage，理论上不受 retriever 单次排名限制；但实践中 MemGPT 常在耗尽结果前停止翻页。
related: [memgpt-archival-vs-recall-storage, memgpt-function-chaining, memgpt-premature-stopping]
---

MemGPT 在文档 QA 任务中展示了迭代检索对 fixed-context 方法的结构性优势：

**实验设置**：两者使用相同 retriever（cosine similarity on text-embedding-ada-002 embeddings）。Baseline 一次性将 top-K 文档放入上下文窗口；MemGPT 将全部文档存入 archival storage（PostgreSQL + pgvector HNSW 索引），通过函数调用按需检索。[^src-1]

**关键差异**：Baseline 性能受 retriever 质量和上下文容量双重约束——若 gold document 不在 top-K 内则永远无法找到。MemGPT 可通过 pagination 翻页浏览更多结果，且可用不同查询词重新检索。因此 MemGPT 性能不随文档数 K 增加而下降。[^src-2]

**Baseline 扩展策略的代价**：为让 fixed-context baseline 处理更多文档，论文采用 document truncation（截断文档以塞入更多条目）。但截断降低了命中关键片段的概率，性能随之下降。[^src-2]

然而，MemGPT 的理论优势在实践中有折扣：论文观察到 MemGPT "will often stop paging through retriever results before exhausting the retriever database"——即 LLM 在应该继续翻页时提前停止。这意味着 MemGPT 的实际性能上界由 LLM 的搜索持久性（而非系统架构）决定。[^src-2]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Multi-document QA -- "MemGPT's default storage settings which uses PostgreSQL for archival memory storage with vector search enabled via the pgvector extension"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Multi-document QA -- "MemGPT is effectively able to make multiple calls to the retriever by querying archival storage, allowing it to scale to larger effective context lengths... we observe that MemGPT will often stop paging through retriever results before exhausting the retriever database"
[^card-1]: -> memgpt-premature-stopping -- 本卡描述迭代检索的结构性优势，该卡深入分析 MemGPT 提前停止的失败模式
[^card-2]: -> memgpt-archival-vs-recall-storage -- 本卡展示 archival storage 在文档 QA 中的应用，该卡描述 archival 和 recall 的通用区别
