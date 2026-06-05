---
id: graphrag-map-reduce-query
title: GraphRAG 查询时 Map-Reduce 应答流程
status: accepted
card_type: mechanism
tags: [graphrag, map-reduce, query-answering, summarization]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
justification: ../justification/graphrag-map-reduce-query.md
canonical_concept: graphrag-map-reduce-query
aliases: [GraphRAG map-reduce, 社区摘要 map-reduce 应答, 分步聚合回答]
summary: >-
  graphrag-map-reduce-query（GraphRAG map-reduce / 社区摘要 map-reduce 应答）在查询时将社区摘要随机分块后并行生成带有用性评分的中间回答（map），再按评分降序聚合为最终全局回答（reduce）
related: [graphrag-community-hierarchy, graphrag-global-sensemaking]
---

GraphRAG 在查询时使用三步 map-reduce 流程将预生成的社区摘要转化为全局回答 [^src-1]：

**1. 准备（Prepare）**：社区摘要被随机打乱并分割为预设 token 大小的块。随机打乱确保相关信息分布在多个块中，而不是集中（并可能丢失）在单个上下文窗口中 [^src-2]。

**2. 映射（Map）**：对每个块并行生成中间回答。LLM 同时被要求生成一个 0-100 的评分，表示该中间回答对目标问题的有用程度。评分为 0 的回答被过滤掉 [^src-3]。

**3. 归约（Reduce）**：中间回答按有用性评分降序排列，迭代添加到新的上下文窗口中直至 token 上限。该最终上下文被用来生成返回给用户的全局回答 [^src-4]。

该流程的一个重要设计选择是可以使用不同层级的社区摘要来回答问题——不同层级在摘要细节与覆盖范围之间提供不同的平衡。论文的评估探索了根层级（C0）到低层级（C3）四个层级，以确定哪个层级最适合一般性 sensemaking 问题 [^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 1.1.6 (graph_rag.tex) -- "Given a user query, the community summaries generated in the previous step can be used to generate a final answer in a multi-stage process."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 1.1.6 (graph_rag.tex) -- "Community summaries are randomly shuffled and divided into chunks of pre-specified token size. This ensures relevant information is distributed across chunks, rather than concentrated (and potentially lost) in a single context window."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 1.1.6 (graph_rag.tex) -- "Intermediate answers are generated in parallel. The LLM is also asked to generate a score between 0-100 indicating how helpful the generated answer is in answering the target question. Answers with score 0 are filtered out."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 1.1.6 (graph_rag.tex) -- "Intermediate community answers are sorted in descending order of helpfulness score and iteratively added into a new context window until the token limit is reached."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 1.1.6 (graph_rag.tex) -- "The hierarchical nature of the community structure also means that questions can be answered using the community summaries from different levels, raising the question of whether a particular level in the hierarchical community structure offers the best balance of summary detail and scope"
