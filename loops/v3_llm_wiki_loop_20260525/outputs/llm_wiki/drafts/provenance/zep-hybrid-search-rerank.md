---
schema: draft_card_provenance.v3
draft_card: ../cards/zep-hybrid-search-rerank.md
material_id: arxiv-zep
digest_id: digest_arxiv-zep
source_paths:
  - data/raw/arxiv/arxiv-zep/agent_source_bundle.txt
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-26T11:10:00+08:00
edited_entity: llm
---

## 源证据

- main.tex 行 156–163：定义 $f, \varphi, \rho, \chi$ 与组合关系。
- main.tex 行 193–198：三路 search（cosine、BM25、BFS）以及每种检索字段。
- main.tex 行 196：「breadth-first search over knowledge graphs has received limited attention in the RAG domain」+ BFS 可接节点为参数、用 recent episodes 当 seed。
- main.tex 行 198：「full-text search identifies word similarities, cosine similarity captures semantic similarities, and breadth-first search reveals contextual similarities」——三种相似性的明确分工。
- main.tex 行 200–201：五种 reranker（RRF, MMR, episode-mentions, node distance, cross-encoder）。
- main.tex 行 281–283：表 2 数据 Avg Context Tokens 1.6k vs Full-context 115k；延迟 2.58–3.20 s vs 28.9–31.3 s。

## 卡片范围是否成立

本卡聚焦"检索/重排流水线"这一独立机制，把三层图、bi-temporal 这些已经独立成卡的内容只一笔带过。"小上下文高精度"的结论引用了 §4.3 LongMemEval 实验表（行 281–283 数据），属于把检索机制与实验结果做最小桥接，仍是论文自身主张。BFS 与 community search 的局限引述了 §3.1 与论文未来工作段。

## 发表门控结果

本轮未运行。

## 备注

- 与 v2 可能已有的"RAG 多路检索"通用卡有边界重叠，但本卡是 Zep 专属机制，应保留 Zep 视角，不要被通用化卡吞并。
