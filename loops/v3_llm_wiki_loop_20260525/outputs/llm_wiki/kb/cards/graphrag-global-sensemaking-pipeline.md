---
id: graphrag-global-sensemaking-pipeline
title: GraphRAG 把 RAG 改造成"全局意义建构"的两阶段流水线
status: accepted
card_type: mechanism
tags: [#graphrag, #rag, #knowledge-graph, #sensemaking]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T11:10:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
provenance_card: ../provenance/graphrag-global-sensemaking-pipeline.md
aliases: ["GraphRAG pipeline", "From Local to Global"]
related: [graphrag-leiden-community-hierarchy, graphrag-root-community-token-efficiency, graphrag-context-window-8k-optimal, graphrag-pipeline-formalism, mem0-graph-memory-variant, zep-graphiti-three-tier-graph, karpathy-llm-wiki-vs-rag]
---

GraphRAG（Edge et al., Microsoft Research, NeurIPS 2024）针对的是传统 vector RAG 答不出的一类问题——"What are the main themes in the dataset?"这种需要对整个语料做意义建构（sensemaking）的查询。论文给出的解法是把流水线拆成**索引时**与**查询时**两个阶段，并在二者之间放一个"分层社群摘要"的中间产物。

**索引阶段（一次性、可离线跑完）：**

1. `Source Documents → Text Chunks`：原文档被切成固定大小的 chunk（论文实验用 600 token），chunk 越小召回越好但 LLM 调用越多。
2. `Text Chunks → Entities & Relationships`：用 LLM 在每个 chunk 上抽实体（名字、类型、简短描述）、抽关系（源/目标实体 + 关系描述）；可选再抽 *claims*（关于实体的可验证事实陈述）。
3. `Entities & Relationships → Knowledge Graph`：跨 chunk 把同一实体的多次出现合并成单节点；关系出现次数变成边权重；实体匹配在论文里用 exact string，但可换更软的匹配。
4. `Knowledge Graph → Communities`：跑分层 Leiden 社群检测（用 graspologic 实现），得到一棵从根（C0，最大、最少）到叶的社群树。
5. `Communities → Community Summaries`：自底向上为每个社群生成报告式摘要——叶社群按"节点度数优先"把 element 摘要塞进 8k 上下文；高层社群在塞不下时把子社群摘要替换掉其底层 element 摘要。

**查询阶段（map-reduce）：**

- 选定一个社群层级，把该层所有社群摘要**洗牌**后切成等长 chunk（防止信息集中而被"lost in the middle"）；
- Map：每个 chunk 并行生成局部答案，并自评 0–100 的"是否回答了问题"分数，0 分被丢弃；
- Reduce：按分数降序把局部答案塞进新上下文，生成最终全局答案。

边界与误用：GraphRAG 不是为"What is the capital of France?"这类事实型查询设计的——评测里它在 *directness* 指标上输给 vector RAG (SS)。它的强项是 *comprehensiveness* 和 *diversity*：对 ~100 万 token 量级的播客转写和新闻语料，全局方法相对 vector RAG 在两项上的胜率分别是 72–83% 和 62–82%（p<0.001 / 0.01）。

## References

- Edge et al., "From Local to Global: A GraphRAG Approach to Query-Focused Summarization"，NeurIPS 2024。论文正文摘要与 §3.1 Methods（`data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt`，行 671–860）。

## Footnotes

- 索引五步骤的小节标题见 `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` 行 769、776、808、821、829。
- 查询时 map-reduce 的三步（Prepare/Map/Reduce）见行 853–857。
- "shuffled and divided into chunks ... ensures relevant information is distributed across chunks, rather than concentrated (and potentially lost) in a single context window" 来自行 854。
- 评测胜率与统计显著性见行 987–989；directness 反向结果见行 989。
