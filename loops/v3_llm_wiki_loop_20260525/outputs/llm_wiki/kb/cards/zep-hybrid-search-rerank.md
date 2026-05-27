---
id: zep-hybrid-search-rerank
title: Zep 的检索把 cos+BM25+BFS 三路覆盖三种"相似性"，再叠多种重排器
status: accepted
card_type: mechanism
tags: [#zep, #retrieval, #reranking, #graph-rag]
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
provenance_card: ../provenance/zep-hybrid-search-rerank.md
aliases: [Zep memory retrieval, Graphiti BFS rerank]
related: [zep-graphiti-three-tier-graph, zep-bi-temporal-edges, zep-dmr-benchmark-critique, longmemeval-key-expansion-with-facts, graphrag-leiden-community-hierarchy]
---

Zep 把图检索抽象为 $f: S \to S$，输入查询字符串 $\alpha$，输出可直接喂给 agent 的上下文字符串 $\beta$。整条链路是 $f(\alpha) = \chi(\rho(\varphi(\alpha)))$，由 search、reranker、constructor 三步组成。

**Search $\varphi$ 同时跑三路、覆盖三种相似性：**

- 余弦语义相似 $\varphi_\text{cos}$：抓"语义相似"——对实体名 embedding（1024 维）和 fact embedding 做向量检索；
- Okapi BM25 全文检索 $\varphi_\text{bm25}$：抓"词形/词面相似"——查 fact 字段、entity name、community name；
- 广度优先搜索 $\varphi_\text{bfs}$：抓"上下文相似"——在图上做 n-hop 邻域扩散，并且可以**接受节点作为参数**，所以可以拿"最近的几条 episode"当种子做扩散，把当前对话里刚出现的实体/关系塞进检索池。

前两路在 RAG 圈是标配；第三路（图上的 BFS）在 RAG 文献中很少出现，Zep 把它列为关键差异化。三路覆盖的"相似性维度"完全正交，最大化 candidate recall。

**Reranker $\rho$ 提供五种实现：**

- 经典 RRF（Reciprocal Rank Fusion）、MMR（Maximal Marginal Relevance）；
- 自研 graph-based 重排：按"实体/事实在最近对话中被提及的频次"提升排序——把频繁出现的信息推到前面；
- node distance 重排：以某个 centroid 节点为中心，按图距离重排——给出"局部话题相关"的语境收敛；
- Cross-encoder（用 LLM 跨注意力打分）——质量最高但代价最大。

**Constructor $\chi$ 是确定性格式化器**：对 $\mathcal{E}_s$ 返回 fact + $t_\text{valid}/t_\text{invalid}$；对 $\mathcal{N}_s$ 返回 name + summary；对 $\mathcal{N}_c$ 返回 community summary。这一步没有 LLM，纯模板，可解释、可压缩、可审计。

操作含义：实验中 Zep 把"top 20 facts + entities"格式化为 1.6k tokens 的上下文，相比 115k tokens 的 full-context baseline 既降了 token 又提升精度。**多路 search + 多种 rerank 的组合是这种"小上下文高精度"的工程基础**——任何一路单独使用都会丢回忆。

边界：BFS 的 seed 选择很影响结果，目前依赖"recent episodes"启发；社区检索方式与 LightRAG 高层 key 检索类似，论文也提到 "hybridization … presents a promising direction"——目前还没融合。

## References

Zep 论文 §3 "Memory Retrieval" 整节定义 $f, \varphi, \rho, \chi$；§3.1 列三路 search；§3.2 列五种 reranker。

- 源路径：`data/raw/arxiv/arxiv-zep/agent_source_bundle.txt`（main.tex 行 156–164 三阶段函数；行 193–201 三路 search 与 reranker；行 281–283 Zep 的 1.6k vs 115k 上下文数据）。

## Footnotes

- 三阶段定义原文（行 163）："we can express $f$ as a composition of these three components: $f(\alpha)=\chi(\rho(\varphi(\alpha)))=\beta$."
- BFS 差异化（行 196）："breadth-first search over knowledge graphs has received limited attention in the RAG domain ... can accept nodes as parameters for the search ... allowing the system to incorporate recently mentioned entities and relationships into the retrieved context."
- 上下文降到 1.6k（表 2 行 281–283）："Avg Context Tokens ... Zep & gpt-4o & ... & 1.6k"，对比 Full-context 的 115k。
