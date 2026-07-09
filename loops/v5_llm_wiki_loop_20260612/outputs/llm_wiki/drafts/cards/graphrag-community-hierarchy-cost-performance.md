---
id: graphrag-community-hierarchy-cost-performance
title: GraphRAG 社区层级的成本-性能权衡
status: draft
card_type: empirical-finding
tags: [graphrag, community-level, token-cost, scalability, comprehensiveness, diversity]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
evidence_basis: experimental_paper
justification: ../justification/graphrag-community-hierarchy-cost-performance.md
canonical_concept: graphrag-community-hierarchy-cost-performance
aliases: [GraphRAG community levels, C0 C1 C2 C3, 社区层级权衡, GraphRAG scalability]
summary: >-
  GraphRAG graphrag-community-hierarchy-cost-performance 社区层级 C0-C3 在成本与性能间呈现明确权衡。C0 根级社区摘要仅消耗 source text summarization 2.3-2.6% 的 token 但仍以 72% comprehensiveness 和 62% diversity win rate 优于 vector RAG。C3 叶级消耗 66.8-73.5% token 但在 News 数据集达 comprehensiveness 79% diversity 69% win rate。C1-C3 相比 TS 有小幅但一致的改善（57-64% win rate）。对迭代 sensemaking 活动 C0 提供高效方案。
related: [graphrag-pipeline-architecture, graphrag-global-sensemaking]
---

GraphRAG 支持在不同社区层级回答查询，形成成本-性能连续体。

**Token 消耗**（占 source text summarization 的比例）:
| 层级 | Podcast | News |
|------|---------|------|
| C0 (根级) | 2.6% | 2.3% |
| C1 | 22.2% | 20.7% |
| C2 | 55.8% | 57.4% |
| C3 (叶级) | 73.5% | 66.8% |
| TS (全文) | 100% | 100% |

**性能（vs vector RAG SS, comprehensiveness win rate）**:
- C0: 72% (Podcast), 72% (News)
- C1: 75%, 75%
- C2: 78%, 79%
- C3: 79%, 79%
- TS: 83%, 80%

**GraphRAG vs TS**: C2 在 Podcast 达 57% (p<.001) comprehensiveness win rate; C3 在 News 达 64% (p<.001)。C0 与 TS 基本持平。

**实用意义**: 对需要迭代问答的 sensemaking 场景，C0 以 9x-43x 更少的 token 消耗提供远优于 vector RAG 的答案质量。

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "community_table.tex" -- "Root-level community summaries (C0) require dramatically fewer tokens per query (9x-43x)"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Results" (Section 4.1) -- "root-level GraphRAG offers a highly efficient method...while retaining advantages in comprehensiveness (72% win rate) and diversity (62% win rate) over vector RAG"
[^card-1]: [graphrag-pipeline-architecture] 层级来源于 Leiden 递归社区检测
[^card-2]: [graphrag-global-sensemaking] 成本效率支撑迭代 sensemaking 场景
