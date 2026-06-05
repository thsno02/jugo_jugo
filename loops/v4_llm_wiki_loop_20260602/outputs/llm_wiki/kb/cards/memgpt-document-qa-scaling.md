---
id: memgpt-document-qa-scaling
title: MemGPT 文档问答的上下文无关扩展性
status: accepted
card_type: source_claim
tags: [LLM, evaluation, document_analysis, retrieval, context_scaling, MemGPT]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
justification: ../justification/memgpt-document-qa-scaling.md
canonical_concept: memgpt-document-qa-scaling
aliases: [文档问答扩展性, document QA scaling, 多文档问答]
summary: >-
  memgpt-document-qa-scaling（文档问答扩展性, document QA scaling）在基于 NaturalQuestions-Open 的文档 QA 任务中，MemGPT 性能不受文档数量增加影响，而固定上下文基线受限于检索器性能和截断降质；MemGPT 通过多次查询 archival storage 并迭代分页突破单次检索限制，但有时会提前停止分页
related: [memgpt-function-chaining, memgpt-nested-kv-retrieval, virtual-context-management]
---

MemGPT 论文在文档问答任务上展示了虚拟上下文管理的扩展性优势 [^src-1]。

**实验设计**：基于 NaturalQuestions-Open 数据集，使用 2018 年 Wikipedia 转储，采样 50 个问题。检索器使用 OpenAI text-embedding-ada-002 嵌入的余弦距离相似度搜索，MemGPT 使用 PostgreSQL + pgvector 作为 archival storage [^src-2]。

**核心发现**：
- **MemGPT 性能不受上下文长度影响**：MemGPT 能够通过多次调用检索器查询 archival storage 并迭代分页浏览结果，使可用文档数量不再受限于上下文窗口容量 [^src-3]。
- **固定上下文基线性能受限**：基线性能受检索器上限约束；文档截断会降低准确率，因为相关片段被省略的概率增加 [^src-4]。
- **局限性**：尽管理论上 MemGPT 不受次优检索器限制（只要完整排序中包含金标准文档就能通过足够多的分页找到），实践中 MemGPT 常在耗尽检索器数据库之前就停止翻页 [^src-5]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Figure 3 caption -- "MemGPT's performance is unaffected by increased context length."
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/experiments.tex -- "We use MemGPT's default storage settings which uses PostgreSQL for archival memory storage with vector search enabled via the pgvector extention."
[^src-3]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/experiments.tex -- "MemGPT actively retrieves documents from its archival storage (and can iteratively page through results), so the total number of documents available to MemGPT is no longer limited by the number of documents that fit within the LLM processor's context window."
[^src-4]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/experiments.tex -- "document truncation reduces accuracy as documents shrink as the chance of the relevant snippet (in the gold document) being omitted grows"
[^src-5]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/experiments.tex -- "we observe that MemGPT will often stop paging through retriever results before exhausting the retriever database."
