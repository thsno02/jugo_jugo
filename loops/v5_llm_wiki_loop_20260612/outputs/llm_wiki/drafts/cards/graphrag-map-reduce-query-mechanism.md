---
id: graphrag-map-reduce-query-mechanism
title: GraphRAG Map-Reduce 查询机制
status: draft
card_type: technique
tags: [graphrag, map-reduce, query-time, global-answer, helpfulness-score, parallel-generation]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
evidence_basis: experimental_paper
justification: ../justification/graphrag-map-reduce-query-mechanism.md
canonical_concept: graphrag-map-reduce-query-mechanism
aliases: [GraphRAG map-reduce, community answers to global answer, map-reduce summarization, GraphRAG 查询时机制]
summary: >-
  GraphRAG graphrag-map-reduce-query-mechanism 查询时 map-reduce 机制：社区摘要随机打乱分为预设 token 大小的 chunks 确保相关信息分散；map 阶段对每 chunk 并行生成中间答案并输出 helpfulness score 0-100 过滤 0 分答案；reduce 阶段按得分降序迭代添加中间答案到新 context window 直至 token limit 后生成最终全局答案。此设计使不同社区层级的摘要均可用于回答同一问题。
related: [graphrag-pipeline-architecture, graphrag-community-summary-generation]
---

GraphRAG 的查询时（query time）通过 map-reduce 模式将分散在多个社区摘要中的信息聚合为全局答案。

**三步机制**:

1. **Prepare（准备）**: 所选层级的社区摘要随机打乱后分割为预设 token 大小的 chunk。随机打乱确保相关信息分散于多个 chunk 中，避免集中在单个窗口中被"lost in the middle"。

2. **Map（映射）**: 对每个 chunk 独立且并行地生成中间答案。LLM 同时输出 helpfulness score (0-100)，表示该中间答案对目标问题的帮助程度。Score=0 的答案被过滤。

3. **Reduce（归约）**: 将通过过滤的中间答案按 helpfulness score 降序排列，迭代添加到新的 context window 中，直至 token limit。以此最终上下文生成返回给用户的全局答案。

**设计特性**:
- 层级选择灵活：同一问题可用 C0-C3 任何层级回答
- 并行化：map 阶段完全并行，可利用高并发 LLM API
- 信息过滤：helpfulness score 机制自动排除不相关社区的贡献
- 与 TS 条件共享相同框架：区别仅在输入是社区摘要还是源文本

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Community Summaries → Community Answers → Global Answer" (Section 3.1.6) -- "Intermediate answers are generated in parallel. The LLM is also asked to generate a score between 0-100 indicating how helpful the generated answer is"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Global Answer Generation" (Appendix E) -- "generate an integer score between 0-100 that indicates how helpful is this response"
[^card-1]: [graphrag-pipeline-architecture] map-reduce 是流水线最终查询步骤
[^card-2]: [graphrag-community-summary-generation] map 步骤的输入来自社区摘要
