---
id: graphrag-query-modes
title: GraphRAG 四种查询模式
status: draft
card_type: query-architecture
tags: [query, global-search, local-search, drift-search, basic-search, map-reduce]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
evidence_basis: code_implementation
justification: ../justification/graphrag-query-modes.md
canonical_concept: graphrag-query-modes
aliases: [GraphRAG query engine, 查询引擎, Global Search, Local Search, DRIFT Search, Basic Search]
summary: >-
  GraphRAG 提供四种查询模式：Global Search 使用社区报告 map-reduce 回答全局综合性问题；Local Search 通过实体嵌入匹配后 fan-out 到邻居实体/关系/文本块回答特定实体问题；DRIFT Search（Dynamic Reasoning and Inference with Flexible Traversal）融合社区信息与局部搜索扩展查询广度；Basic Search 为标准 top-k 向量检索基线。query modes global local drift basic map-reduce entity fan-out。
related: [graphrag-knowledge-graph-augmented-rag, graphrag-six-phase-indexing-pipeline]
---

GraphRAG 查询引擎在完成索引后提供四种检索模式：[^src-1]

**Global Search**：针对需要理解整个数据集的全局性问题（如"数据中的主要主题是什么"）。采用 map-reduce 策略：先将社区报告分批输入 LLM 获得带重要性评分的中间响应点（map），再筛选最重要的点聚合为最终回答（reduce）。社区层级的选择影响回答质量——低层级报告更详细但消耗更多资源。[^src-2]

**Local Search**：针对需要理解特定实体的问题（如"某植物的药用价值"）。通过实体描述嵌入匹配语义相关实体，然后 fan-out 到关联实体、关系、社区报告、文本块和 covariates，经排序过滤后在单一上下文窗口中生成回答。[^src-3]

**DRIFT Search**（Dynamic Reasoning and Inference with Flexible Traversal）：融合全局与局部搜索的方法。三阶段：Primer 阶段将查询与 top-K 语义相关社区报告比较生成初始回答和后续问题；Follow-Up 阶段使用 local search 细化查询；Output 阶段输出按相关性排序的问答层次结构。[^src-4]

**Basic Search**：标准 top-k 向量检索基线实现，用于方便与其他搜索模式对比效果。[^src-5]

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/query/overview.md" P1019-1029 -- query engine overview listing four methods
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/query/global_search.md" P1065-1110 -- "global search method uses a collection of LLM-generated community reports... in a map-reduce manner"
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/query/local_search.md" P1140-1180 -- "identifies a set of entities from the knowledge graph that are semantically-related to the user input"
[^src-4]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/query/drift_search.md" P1206-1218 -- "DRIFT search (Dynamic Reasoning and Inference with Flexible Traversal)... combining characteristics of both global and local search"
[^src-5]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/query/overview.md" P1049-1051 -- "rudimentary implementation of basic vector RAG"
[^card-1]: [graphrag-knowledge-graph-augmented-rag](graphrag-knowledge-graph-augmented-rag.md) -- 查询模式利用该卡所述的知识图谱结构
[^card-2]: [graphrag-six-phase-indexing-pipeline](graphrag-six-phase-indexing-pipeline.md) -- 查询依赖索引阶段产出的 artifacts
