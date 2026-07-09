---
id: llm-wiki-4-signal-relevance-model
title: LLM Wiki 四信号知识图谱相关性模型
status: draft
card_type: algorithm
tags: [knowledge-graph, relevance-model, llm-wiki, adamic-adar, wikilink, graph]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-nashsu-llm-wiki]
evidence_basis: code_implementation
justification: ../justification/llm-wiki-4-signal-relevance-model.md
canonical_concept: llm-wiki-4-signal-relevance-model
aliases: [4-Signal Relevance Model, 四信号相关性模型, knowledge graph relevance, 4-signal knowledge graph]
summary: >-
  LLM Wiki 四信号相关性模型（4-Signal Relevance Model）：Direct link ×3.0（wikilinks 直接链接）、
  Source overlap ×4.0（共享同一原始来源，权重最高）、Adamic-Adar ×1.5（共享邻居按邻居度加权）、
  Type affinity ×1.0（同类型页面加分）。用于知识图谱可视化和查询检索的 graph expansion 阶段。
  附带 Louvain 社区检测和 Graph Insights（surprising connections + knowledge gaps）。
related: []
---

LLM Wiki 在 Karpathy 原始设计的 `[[wikilinks]]` 交叉引用基础上，构建了完整的知识图谱可视化和相关性引擎，采用四信号加权模型：

| 信号 | 权重 | 描述 |
|------|------|------|
| Direct link | ×3.0 | 通过 `[[wikilinks]]` 直接链接的页面 |
| Source overlap | ×4.0 | 共享同一原始来源（通过 frontmatter `sources[]` 匹配），权重最高 |
| Adamic-Adar | ×1.5 | 共享共同邻居的页面（按邻居度反比加权） |
| Type affinity | ×1.0 | 同类型页面间的加分（entity-entity, concept-concept） |

图可视化使用 sigma.js + graphology + ForceAtlas2 布局，节点按类型或社区着色，边的粗细和颜色反映相关性权重。[^src-1]

系统还集成了 Louvain 算法进行自动社区检测（基于链接拓扑发现知识聚类），以及 Graph Insights 功能（发现跨社区的意外连接、孤立页面、稀疏社区和桥接节点）。[^src-2] [^card-1]

[^src-1]: `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md` -- "4. Knowledge Graph with Relevance Model" P138-144 -- "4-Signal Relevance Model: Direct link ×3.0 / Source overlap ×4.0 / Adamic-Adar ×1.5 / Type affinity ×1.0"
[^src-2]: `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md` -- "5. Louvain Community Detection" P156-162 -- "Automatic discovery of knowledge clusters using the Louvain algorithm"
[^card-1]: 参见 [[llm-wiki-multi-phase-query-pipeline]] 了解该模型在 Phase 2 Graph Expansion 中的应用
