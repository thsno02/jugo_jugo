---
id: graphrag-comprehensiveness-diversity-result
title: GraphRAG 全面性与多样性大幅优于向量 RAG 的实证结果
status: accepted
card_type: source_claim
tags: [graphrag, evaluation, comprehensiveness, diversity, directness, empirical-result]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
justification: ../justification/graphrag-comprehensiveness-diversity-result.md
canonical_concept: graphrag-comprehensiveness-diversity-result
aliases: [GraphRAG evaluation results, GraphRAG 评估结果, GraphRAG vs naive RAG 胜率]
summary: >-
  graphrag-comprehensiveness-diversity-result（GraphRAG 评估结果）在百万 token 数据集上 GraphRAG 全面性胜率 72-83%、多样性 62-82%（p<.001），但向量 RAG 在直接性上占优；全面性与直接性存在内在对立
related: [graphrag-community-level-tradeoff, graphrag-global-sensemaking, sensemaking-vs-retrieval-query]
---

GraphRAG 论文通过两个实验在两个百万 token 级数据集（Podcast 转录和新闻文章）上评估了性能，使用 LLM-as-a-judge 方法和基于事实声明的指标。

**全面性（Comprehensiveness）**：全局方法显著优于向量 RAG（SS），Podcast 数据集胜率 72-83%（p<.001），News 数据集 72-80%（p<.001） [^src-1]。

**多样性（Diversity）**：全局方法同样显著领先，Podcast 胜率 75-82%（p<.001），News 62-71%（p<.01） [^src-2]。

**直接性（Directness）**：作为对照指标，向量 RAG 在所有比较中产生最直接的回答。这一结果被设计为有效性验证——因为直接性与全面性和多样性本质上是对立的，没有方法应当在所有四个指标上获胜 [^src-3]。

**赋能性（Empowerment）**：该指标的结果混合。LLM 分析表明，提供具体示例、引用和引证被认为是帮助用户达成知情理解的关键能力——这些细节可能在 GraphRAG 索引构建过程中丢失 [^src-4]。

基于事实声明的验证实验（实验 2）确认：所有全局搜索条件的声明数量均多于 SS（p<.05），声明聚类分析在大多数条件下也显示更高的多样性 [^src-5]。LLM 判断与声明指标的一致率为全面性 78%，多样性 69-70% [^src-6]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Results Section (graph_rag.tex) -- "global approaches achieved comprehensiveness win rates between 72-83% (p<.001) for Podcast transcripts and 72-80% (p<.001) for News articles"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Results Section (graph_rag.tex) -- "diversity win rates ranged from 75-82% (p<.001) and 62-71% (p<.01) respectively"
[^src-3]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 1.3 (graph_rag.tex) -- "Since directness is effectively in opposition to comprehensiveness and diversity, we would not expect any method to win across all four criteria."
[^src-4]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Results Section (graph_rag.tex) -- "the ability to provide specific examples, quotes, and citations was judged to be key to helping users reach an informed understanding. Tuning element extraction prompts may help to retain more of these details in the GraphRAG index."
[^src-5]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Experiment 2 Results (graph_rag.tex) -- "all global search conditions (C0-C3) and source text summarization (TS) had greater comprehensiveness than vector RAG (SS). The differences were statistically significant (p<.05) in all cases."
[^src-6]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Experiment 2 Results (graph_rag.tex) -- "the aggregated LLM label matched the claim-based label in 78% of pairwise comparisons for comprehensiveness and 69-70% for diversity"
