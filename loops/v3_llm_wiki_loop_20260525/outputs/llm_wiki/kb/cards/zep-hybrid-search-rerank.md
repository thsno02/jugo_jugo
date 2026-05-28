---
id: zep-hybrid-search-rerank
title: Zep 的检索把 cos+BM25+BFS 三路覆盖三种"相似性"，再叠多种重排器
status: accepted
card_type: mechanism
tags: [#zep, #retrieval, #reranking, #graph-rag]
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-28T11:34:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
provenance_card: ../provenance/zep-hybrid-search-rerank.md
aliases: [Zep memory retrieval, Graphiti BFS rerank]
related: [zep-graphiti-three-tier-graph, longmemeval-key-expansion-with-facts, zep-bi-temporal-edges, zep-dmr-benchmark-critique]
---

Zep 把图检索抽象为 $f: S \to S$，输入查询字符串 $\alpha$，输出可直接喂给 agent 的上下文字符串 $\beta$。整条链路是 $f(\alpha) = \chi(\rho(\varphi(\alpha)))$[^src1]，由 search、reranker、constructor 三步组成。检索底层是 Graphiti 三层图[^v3-1]。

**Search $\varphi$ 同时跑三路、覆盖三种相似性：**

- 余弦语义相似 $\varphi_\text{cos}$：抓"语义相似"——对实体名 embedding（1024 维）和 fact embedding 做向量检索；
- Okapi BM25 全文检索 $\varphi_\text{bm25}$：抓"词形/词面相似"——查 fact 字段、entity name、community name；
- 广度优先搜索 $\varphi_\text{bfs}$：抓"上下文相似"——在图上做 n-hop 邻域扩散，并且可以**接受节点作为参数**[^src2]，所以可以拿"最近的几条 episode"当种子做扩散，把当前对话里刚出现的实体/关系塞进检索池。

前两路在 RAG 圈是标配；第三路（图上的 BFS）在 RAG 文献中很少出现，Zep 把它列为关键差异化。三路覆盖的"相似性维度"完全正交，最大化 candidate recall。LongMemEval 的 K = V + fact 做的是同一目标在 key 侧的另一种实现[^v3-2]。

**Reranker $\rho$ 提供五种实现：**

- 经典 RRF（Reciprocal Rank Fusion）、MMR（Maximal Marginal Relevance）；
- 自研 graph-based 重排：按"实体/事实在最近对话中被提及的频次"提升排序——把频繁出现的信息推到前面；
- node distance 重排：以某个 centroid 节点为中心，按图距离重排——给出"局部话题相关"的语境收敛；
- Cross-encoder（用 LLM 跨注意力打分）——质量最高但代价最大。

**Constructor $\chi$ 是确定性格式化器**：对 $\mathcal{E}_s$ 返回 fact + $t_\text{valid}/t_\text{invalid}$（来自 bi-temporal edges[^v3-3]）；对 $\mathcal{N}_s$ 返回 name + summary；对 $\mathcal{N}_c$ 返回 community summary。这一步没有 LLM，纯模板，可解释、可压缩、可审计。

操作含义：实验中 Zep 把"top 20 facts + entities"格式化为 1.6k tokens 的上下文，相比 115k tokens 的 full-context baseline 既降了 token 又提升精度[^src3]。**多路 search + 多种 rerank 的组合是这种"小上下文高精度"的工程基础**——任何一路单独使用都会丢回忆。这也是为什么 Zep 论文呼吁用 LongMemEval 而非 DMR 作为长程记忆评估基准[^v3-4]。

边界：BFS 的 seed 选择很影响结果，目前依赖"recent episodes"启发；社区检索方式与 LightRAG 高层 key 检索类似，论文也提到 "hybridization … presents a promising direction"——目前还没融合。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` — main.tex 行 156–164（§3 "Memory Retrieval" 整节定义 $f, \varphi, \rho, \chi$）+ 行 163 — "we can express $f$ as a composition of these three components: $f(\alpha)=\chi(\rho(\varphi(\alpha)))=\beta$."
[^src2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` — main.tex 行 193–201（§3.1 三路 search 与 §3.2 五种 reranker）+ 行 196 — "breadth-first search over knowledge graphs has received limited attention in the RAG domain ... can accept nodes as parameters for the search ... allowing the system to incorporate recently mentioned entities and relationships into the retrieved context."
[^src3]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` — main.tex 行 281–283（表 2）— "Avg Context Tokens ... Zep & gpt-4o & ... & 1.6k"，对比 Full-context 的 115k。
[^v3-1]: [zep-graphiti-three-tier-graph](zep-graphiti-three-tier-graph.md) — 三路 search 的底层数据载体。
[^v3-2]: [longmemeval-key-expansion-with-facts](longmemeval-key-expansion-with-facts.md) — 同目标在 key 侧的另一实现。
[^v3-3]: [zep-bi-temporal-edges](zep-bi-temporal-edges.md) — constructor 输出的 fact 时间区间来自 bi-temporal edges。
[^v3-4]: [zep-dmr-benchmark-critique](zep-dmr-benchmark-critique.md) — Zep 推荐 LongMemEval 替代 DMR 的理由。
