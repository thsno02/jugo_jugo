---
id: graphrag-community-summary-generation
title: GraphRAG 社区摘要生成策略
status: draft
card_type: technique
tags: [graphrag, community-summary, hierarchical-summarization, context-window-packing, prioritization]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
evidence_basis: experimental_paper
justification: ../justification/graphrag-community-summary-generation.md
canonical_concept: graphrag-community-summary-generation
aliases: [community summary generation, 社区摘要生成, hierarchical community summarization, community report]
summary: >-
  GraphRAG graphrag-community-summary-generation 社区摘要生成分两级策略：叶级社区按边的源目标节点度（prominence）降序排列，迭代添加节点描述、边描述和 claims 直到 token limit；高层级社区若元素摘要超出 token limit 则以子社区摘要（更短）替换元素摘要（更长）直到适配窗口。生成的报告包含 title/summary/impact severity rating/detailed findings。摘要独立可用于理解语料全局结构。
related: [graphrag-pipeline-architecture, graphrag-community-hierarchy-cost-performance]
---

GraphRAG 的社区摘要生成是连接索引时图结构与查询时回答能力的关键步骤。

**叶级社区摘要策略**:
1. 对社区内每条边按源+目标节点度（overall prominence）降序排列
2. 按此优先级迭代向 LLM context window 添加：源节点描述 → 目标节点描述 → 边描述 → 相关 claims
3. 直至 token limit 到达

**高层级社区摘要策略**:
1. 若所有元素摘要可纳入 token limit → 同叶级处理
2. 否则：对子社区按元素摘要 token 数降序排列，迭代用子社区摘要（更短）替换其对应的元素摘要（更长），直到总量适配 context window

**报告结构**:
- TITLE: 代表关键实体的简短标题
- SUMMARY: 社区整体结构的执行摘要
- IMPACT SEVERITY RATING: 0-10 重要性评分
- RATING EXPLANATION: 一句解释
- DETAILED FINDINGS: 5-10 个关键洞察（含数据引用）

**独立价值**: 这些摘要本身可用于理解语料全局结构——用户可浏览某层级摘要寻找主题，再阅读低层级链接报告获取细节，无需特定查询。

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Graph Communities → Community Summaries" (Section 3.1.5) -- "Leaf-level communities. The element summaries...are prioritized and then iteratively added to the LLM context window until the token limit is reached"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Community Summary Generation" (Appendix E) -- "Write a comprehensive report of a community...TITLE...SUMMARY...IMPACT SEVERITY RATING...DETAILED FINDINGS"
[^card-1]: [graphrag-pipeline-architecture] 社区摘要是流水线第五步
[^card-2]: [graphrag-community-hierarchy-cost-performance] 不同层级摘要的 token 消耗来源于此策略
