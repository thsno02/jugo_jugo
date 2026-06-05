---
id: adaptive-benchmarking-persona-generation
title: 基于 LLM 人设生成的自适应基准测试
status: accepted
card_type: mechanism
tags: [evaluation, benchmarking, persona-generation, sensemaking, question-generation]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
justification: ../justification/adaptive-benchmarking-persona-generation.md
canonical_concept: adaptive-benchmarking-persona-generation
aliases: [adaptive benchmarking, 自适应基准测试, persona-based question generation, 人设驱动问题生成]
summary: >-
  adaptive-benchmarking-persona-generation（adaptive benchmarking / 自适应基准测试）用 LLM 从语料库描述推断潜在用户人设、任务和全局理解问题（K*N*M 组合），为缺乏标准答案的 sensemaking 查询生成领域特定评估基准
related: [sensemaking-vs-retrieval-query, graphrag-comprehensiveness-diversity-result]
---

GraphRAG 论文提出了一种自适应基准测试方法，用于为全局 sensemaking 任务生成语料库特定的评估问题。该方法的核心思想是：由于全局 sensemaking 问题没有标准答案，需要根据语料库的实际内容和用途动态生成评估基准 [^src-1]。

问题生成采用三层级的 LLM 提示流程（Algorithm 1）[^src-2]：

1. 给定语料库的高级描述和目的，LLM 推断 K 个潜在用户人设（persona）
2. 对每个用户，LLM 生成 N 个该用户会使用 RAG 系统完成的任务
3. 对每个用户-任务组合，LLM 生成 M 个需要理解整个语料库的问题

生成的问题需满足两个约束：要求对整个语料库的理解，且不需要检索特定的低层事实 [^src-3]。

论文评估中设定 K=M=N=5，生成每个数据集 125 个测试问题。该方法的一个重要设计选择是避免直接从语料库本身生成问题，以确保公平评估 [^src-4]。

结合 LLM-as-a-judge 的头对头比较方法，该自适应基准测试框架提供了一种在缺乏黄金标准答案时评估 RAG 系统性能的实用路径。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 1.2 (graph_rag.tex) -- "Adaptive benchmarking refers to the process of dynamically generating evaluation benchmarks tailored to specific domains or use cases."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Algorithm 1 (graph_rag.tex) -- "1. Describe personas of K potential users of the dataset. 2. For each user, identify N tasks relevant to the user. 3. Specific to each user & task pair, generate M high-level questions"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Algorithm 1 (graph_rag.tex) -- "generate M high-level questions that: Require understanding of the entire corpus. Do not require retrieval of specific low-level facts."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 2.3 (graph_rag.tex) -- "in order to produce a fair evaluation, our method avoids generating the questions directly from the corpus itself"
