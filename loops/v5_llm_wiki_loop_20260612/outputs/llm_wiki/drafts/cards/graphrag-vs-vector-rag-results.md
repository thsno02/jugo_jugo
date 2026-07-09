---
id: graphrag-vs-vector-rag-results
title: GraphRAG 对比 Vector RAG 的实验结果
status: draft
card_type: empirical-finding
tags: [graphrag, vector-rag, experiment-results, win-rate, statistical-significance, comprehensiveness, diversity, directness]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
evidence_basis: experimental_paper
justification: ../justification/graphrag-vs-vector-rag-results.md
canonical_concept: graphrag-vs-vector-rag-results
aliases: [GraphRAG vs vector RAG, GraphRAG experimental results, GraphRAG win rates, 实验结果对比]
summary: >-
  GraphRAG graphrag-vs-vector-rag-results 实验在两个约 1M token 语料上（Podcast 1669 chunks, News 3197 chunks）评估六种条件。全局方法（C0-C3, TS）在 comprehensiveness 上 win rate 72-83% (p<.001) 和 diversity 上 62-82% (p<.01) 显著优于 vector RAG (SS)。Vector RAG 在 directness 上最优（控制准则验证）。Empowerment 结果混合——vector RAG 和源文本能提供具体引用和例证。知识图 Podcast 含 8564 nodes 20691 edges，News 含 15754 nodes 19520 edges。
related: [graphrag-community-hierarchy-cost-performance, graphrag-adaptive-benchmarking]
---

GraphRAG 在两个真实世界数据集上进行了系统性实验评估。

**数据集**:
- Podcast transcripts (Behind the Tech): 1669 chunks x 600 token, ~1M tokens
- News articles (MultiHop-RAG benchmark): 3197 chunks x 600 token, ~1.7M tokens

**图索引规模**:
- Podcast: 8,564 nodes, 20,691 edges
- News: 15,754 nodes, 19,520 edges

**核心结果（Experiment 1, LLM-as-judge）**:

| 指标 | 全局方法 vs SS (Podcast) | 全局方法 vs SS (News) |
|------|------------------------|---------------------|
| Comprehensiveness | 72-83% win (p<.001) | 72-80% win (p<.001) |
| Diversity | 75-82% win (p<.001) | 62-71% win (p<.01) |
| Empowerment | 混合结果 | 混合结果 |
| Directness | SS 胜出（符合预期） | SS 胜出（符合预期） |

**Empowerment 分析**: LLM 评估发现，提供具体例证、引用和引语是帮助读者做出知情判断的关键。GraphRAG 的抽取过程据材料推测可能丢失了这些细节。微调抽取 prompt 似乎有助于保留更多此类信息。

**统计方法**: 数据非正态分布（Shapiro-Wilk 检验），使用 Wilcoxon signed-rank tests + Holm-Bonferroni 校正。

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Results" (Section 4.1) -- "global approaches achieved comprehensiveness win rates between 72-83% (p<.001) for Podcast transcripts"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Results" (Section 4.1) -- "Using an LLM to analyze LLM reasoning for this measure indicated that the ability to provide specific examples, quotes, and citations was judged to be key"
[^card-1]: [graphrag-community-hierarchy-cost-performance] 各层级的具体 win rate 对比
[^card-2]: [graphrag-adaptive-benchmarking] 评估使用的方法论
