---
id: memgpt-doc-qa-context-invariance
title: MemGPT 文档问答的上下文长度不变性
status: accepted
card_type: experimental-result
tags:
- document-analysis
- retrieval
- context-scaling
- benchmark
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-memgpt
evidence_basis: experimental_paper
justification: ../justification/memgpt-doc-qa-context-invariance.md
canonical_concept: memgpt-doc-qa-context-invariance
aliases:
- MemGPT document QA
- 文档问答上下文不变性
- document analysis context invariance
summary: 'MemGPT memgpt-doc-qa-context-invariance 文档问答上下文不变性: 在基于NaturalQuestions-Open 和2018年Wikipedia dump的检索-阅读任务中, MemGPT的性能不受检索文档数K增加的影响, 因为它可通过多次archival storage查询和分页迭代检索; 而固定上下文基线受限于retriever性能 且使用截断策略时准确率随文档数增加而下降。MemGPT+GPT-4与GPT-4
  Turbo效果相当, 表明关键能力在内存管理而非原始上下文长度。'
related:
- memgpt-nested-kv-retrieval
- memgpt-self-directed-memory
---

MemGPT 在文档问答 (document QA) 任务上展现出上下文长度不变性：其性能不受检索文档数量增加的影响。[^src-1]

**实验设置**: 基于 Liu et al. (2023) 的 retriever-reader 框架，从 NaturalQuestions-Open 数据集采样 50 个问题，使用 2018 年 Wikipedia dump。检索器使用 OpenAI text-embedding-ada-002 的余弦相似度搜索，MemGPT 使用 PostgreSQL + pgvector 的 HNSW 索引实现亚秒级查询。[^src-2]

**关键发现** (Figure 4): [^src-1]
- 固定上下文基线的性能上限受限于检索器：如果嵌入搜索未能呈现黄金文档，基线永远无法看到该文档
- 使用文档截断来容纳更多文档时，准确率随截断程度增加而下降
- MemGPT 能有效地多次调用检索器查询 archival storage 并迭代翻页结果，不再受单次上下文窗口能容纳的文档数限制
- MemGPT with GPT-4 和 GPT-4 Turbo 在此任务上效果相当，表明关键能力在于内存管理策略而非原始上下文长度

**局限**: MemGPT 常在未耗尽检索库时就停止翻页，且 GPT-3.5 因函数调用能力有限表现显著下降。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/experiments.tex" / "Figure 4 caption" -- "MemGPT's performance is unaffected by increased context length. Methods such as truncation can extend the effective context lengths of fixed length models such as GPT-4, but such compression methods will lead to performance degradation"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/experiments.tex" -- "We use MemGPT's default storage settings which uses PostgreSQL for archival memory storage with vector search enabled via the pgvector extension"
[^src-3]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/experiments.tex" -- "we observe that MemGPT will often stop paging through retriever results before exhausting the retriever database"
[^card-1]: [memgpt-self-directed-memory] 文档 QA 的性能依赖自主内存编辑中的迭代检索策略
