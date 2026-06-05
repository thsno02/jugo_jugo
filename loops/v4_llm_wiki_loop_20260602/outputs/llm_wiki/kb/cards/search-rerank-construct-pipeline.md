---
id: search-rerank-construct-pipeline
title: 搜索-重排-构造三步检索管线
status: accepted
card_type: mechanism
tags: [retrieval_pipeline, agent_memory, reranking, Zep, search]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
justification: ../justification/search-rerank-construct-pipeline.md
canonical_concept: search-rerank-construct-pipeline
aliases: [三步检索管线, search-rerank-construct, phi-rho-chi pipeline]
summary: >-
  search-rerank-construct-pipeline（三步检索管线, search-rerank-construct）Zep 的记忆检索形式化为 f(alpha)=chi(rho(phi(alpha)))=beta，即搜索（召回候选边/节点）、重排（提升精度）、构造（转为文本上下文）三步组合
related:
  - hybrid-triple-search-complementarity
  - temporal-knowledge-graph-three-tier
---

Zep 将记忆检索形式化为一个三步组合函数 f: S -> S，接受文本查询 alpha 作为输入，返回文本上下文 beta 作为输出 [^src-1]：

**搜索 (phi)**：识别可能包含相关信息的候选节点和边。输出为一个三元组：语义边列表、实体节点列表、社区节点列表。该步骤追求高召回率 [^src-2]。

**重排器 (rho)**：对搜索结果重新排序以提升精度。Zep 支持多种重排方法：互惠排名融合（RRF）、最大边际相关性（MMR）、基于图的 episode-mentions 重排器（按实体/事实在对话中的提及频率优先排序）、节点距离重排器（基于与指定中心节点的图距离排序）、以及 cross-encoder 重排器（使用 LLM 交叉注意力生成相关性评分，计算成本最高）[^src-3]。

**构造器 (chi)**：将相关节点和边转换为文本上下文。对语义边返回 fact 及其 t_valid/t_invalid 字段；对实体节点返回名称和摘要；对社区节点返回摘要 [^src-4]。

最终检索函数表示为组合：f(alpha) = chi(rho(phi(alpha))) = beta [^src-5]。

Mem0^g 的知识图谱检索采用了类似的多路策略（实体锚定 + 语义三元组双路检索），从不同系统设计角度印证了多路检索在知识图谱场景中的必要性 [^card-1]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 3 (Memory Retrieval) -- "the Zep graph search API implements a function f: S->S that accepts a text-string query alpha as input and returns a text-string context beta as output"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 3 -- "The process begins by identifying candidate nodes and edges potentially containing relevant information."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 3.2 (Reranker) -- "Zep supports existing reranking approaches such as Reciprocal Rank Fusion (RRF) and Maximal Marginal Relevance (MMR). Additionally, Zep implements a graph-based episode-mentions reranker..."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 3 -- "For each e_i in E_s, chi returns the fact and t_valid, t_invalid fields; for each n_i in N_s, the name and summary fields; and for each n_i in N_c, the summary field."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 3 -- "we can express f as a composition of these three components: f(alpha)=chi(rho(phi(alpha)))=beta"
[^card-1]: [双路检索策略（实体锚定 + 语义三元组）](dual-retrieval-entity-semantic.md) -- Mem0^g 的双路知识图谱检索展示了另一种多路策略设计，与 Zep 的三步管线形成跨系统比较
