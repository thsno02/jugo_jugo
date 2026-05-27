---
schema: accepted_card_provenance.v3
card: ../cards/zep-hybrid-search-rerank.md
material_id: arxiv-zep
digest_id: digest_arxiv-zep
source_paths:
  - data/raw/arxiv/arxiv-zep/agent_source_bundle.txt
draft_card: ../../drafts/cards/zep-hybrid-search-rerank.md
draft_provenance: ../../drafts/provenance/zep-hybrid-search-rerank.md
similarity_result: ../../drafts/similarity/zep-hybrid-search-rerank.json
comparison_provenance: ../../drafts/comparison/zep-hybrid-search-rerank.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；f=χ(ρ(φ)) 形式化、三路 search 与五种 reranker、1.6k vs 115k tokens 实证均回到行 156–201 / 281–283。
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开 $f$ 组合 + 三路 search + 五种 rerank + constructor + 操作含义 + 边界。
  - 知识密度：形式化 + 三种相似性 + reranker 谱系 + 实证 token 数字。
  - 源支撑：source_ids 含 arxiv-zep；行 163 / 196 / 198 / 281–283 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：5 张 Zep / LongMemEval / GraphRAG 相邻卡。

## 备注

- 与 v2 可能已有的"RAG 多路检索"通用卡有边界重叠，但本卡是 Zep 专属机制。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/zep-hybrid-search-rerank.md`
- draft provenance: `../../drafts/provenance/zep-hybrid-search-rerank.md`
- similarity: `../../drafts/similarity/zep-hybrid-search-rerank.json`
- comparison provenance: `../../drafts/comparison/zep-hybrid-search-rerank.md`
