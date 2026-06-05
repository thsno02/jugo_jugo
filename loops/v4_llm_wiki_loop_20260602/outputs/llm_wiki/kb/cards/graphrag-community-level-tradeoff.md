---
id: graphrag-community-level-tradeoff
title: GraphRAG 社区层级的 token 效率与回答质量权衡
status: accepted
card_type: distinction
tags: [graphrag, community-level, token-efficiency, tradeoff, scalability]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
justification: ../justification/graphrag-community-level-tradeoff.md
canonical_concept: graphrag-community-level-tradeoff
aliases: [C0 vs C3 tradeoff, 社区层级选择权衡, root vs leaf community tradeoff]
summary: >-
  graphrag-community-level-tradeoff（C0 vs C3 tradeoff / 社区层级选择权衡）根层级社区摘要 C0 仅需最大 token 量的 2.3-2.6%，但仍保持对向量 RAG 72% 全面性和 62% 多样性的胜率；低层级 C3 更详细但需 67-74% token
related: [graphrag-community-hierarchy, graphrag-comprehensiveness-diversity-result, graphrag-map-reduce-query]
---

GraphRAG 的层级社区结构带来一个重要的实践权衡：不同层级的社区摘要在 token 消耗与回答质量之间提供不同的平衡点。

根层级社区摘要（C0）数量最少但覆盖最广——Podcast 数据集仅 34 个社区，News 数据集仅 55 个社区，分别占最大 token 量的 2.6% 和 2.3% [^src-1]。尽管如此，C0 仍在全面性（72% 胜率）和多样性（62% 胜率）上显著优于向量 RAG [^src-2]。

低层级社区摘要（C3）数量最多且最具体——Podcast 1,310 个社区，News 2,142 个社区，分别占最大 token 量的 73.5% 和 66.8% [^src-3]。C3 在两个数据集的全面性胜率达 79%，多样性达 69-81%。

关键发现是，对 C3 相比 C0 的边际增益（约 7-19 个百分点的胜率提升）而言，token 消耗增加了约 25-30 倍 [^src-4]。因此，对于需要对同一数据集进行多次全局查询的迭代式意义建构活动，根层级 GraphRAG 提供了高效的方案 [^src-5]。

没有单一层级在所有情况下都是最优的——中间层级在某些数据集上比 C0 和 C3 都好。例如 Podcast 数据集上 C2 在全面性上最优（57% vs TS），而 News 数据集上 C3 最优（64% vs TS） [^src-6]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- community_table.tex -- C0: Podcast 34 units/26657 tokens/2.6%, News 55 units/39770 tokens/2.3%
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Results Section (graph_rag.tex) -- "root-level GraphRAG offers a highly efficient method for the iterative question answering that characterizes sensemaking activity, while retaining advantages in comprehensiveness (72% win rate) and diversity (62% win rate) over vector RAG"
[^src-3]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- community_table.tex -- C3: Podcast 1310 units/746100 tokens/73.5%, News 2142 units/1140266 tokens/66.8%
[^src-4]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Results Section (graph_rag.tex) -- "for low-level community summaries (C3), GraphRAG required 26-33% fewer context tokens, while for root-level community summaries (C0), it required over 97% fewer tokens"
[^src-5]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Conclusion (graph_rag.tex) -- "For situations requiring many global queries over the same dataset, summaries of root-level communities in the entity-based graph index provide a data index that is both superior to vector RAG and achieves competitive performance to other global methods at a fraction of the token cost."
[^src-6]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Results Section (graph_rag.tex) -- "Intermediate-level summaries in the Podcast dataset and low-level community summaries in the News dataset achieved comprehensiveness win rates of 57% (p<.001) and 64% (p<.001), respectively."
