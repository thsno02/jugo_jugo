---
id: graphrag-community-hierarchy-leiden
title: GraphRAG Leiden 层次社区检测与报告
status: draft
card_type: algorithm-mechanism
tags: [leiden-algorithm, community-detection, hierarchical-clustering, community-reports, graph-augmentation]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
evidence_basis: code_implementation
justification: ../justification/graphrag-community-hierarchy-leiden.md
canonical_concept: graphrag-community-hierarchy-leiden
aliases: [Leiden hierarchical clustering, 层次社区检测, community hierarchy, Leiden algorithm in GraphRAG, 社区层级报告]
summary: >-
  GraphRAG 使用 Hierarchical Leiden Algorithm 对实体图进行递归社区聚类，产生严格层次化的社区结构。每个社区由 LLM 生成包含执行概述和关键实体/关系引用的报告。顶层社区报告描述全图概况，底层社区报告描述局部集群。社区 ID 跨层级唯一递增，支持 max_cluster_size 和 seed 配置。Leiden community detection hierarchy reports graph augmentation。
related: [graphrag-six-phase-indexing-pipeline, graphrag-query-modes]
---

GraphRAG 在实体/关系图构建完成后，使用 Hierarchical Leiden Algorithm 进行社区检测。该算法递归地对图进行社区聚类，直至达到社区大小阈值（通过 `max_cluster_size` 配置）。社区结构严格层次化——父社区细分为子社区。[^src-1]

社区层次结构的核心作用是支撑社区报告生成。对每个社区层级，将社区内的实体描述、关系描述和可选的 claims 收集后输入 LLM 生成一份结构化报告。报告包含：LLM 生成的标题、执行摘要（summary）、完整报告内容（full_content）、相关性排名（rank）、以及 5-10 个关键发现（findings）。报告再经 LLM 二次摘要用于简短引用。[^src-2]

社区层级的选择对查询质量有直接影响——低层级社区报告更详细，倾向产出更全面的回答，但也增加 LLM 处理量。[^src-3]

配置方面，`cluster_graph` 块支持 `max_cluster_size`（最大导出簇大小）、`use_lcc`（是否仅用最大连通分量）、`seed`（随机种子确保可重复性）。[^src-4]

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/default_dataflow.md" P513-515 -- "we generate a hierarchy of entity communities using the Hierarchical Leiden Algorithm. This method will apply a recursive community-clustering"
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/outputs.md" P869-885 -- community_reports table schema with title, summary, full_content, rank, findings
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/query/global_search.md" P1110 -- "Lower hierarchy levels, with their detailed reports, tend to yield more thorough responses"
[^src-4]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/config/yaml.md" P1746-1752 -- cluster_graph config with max_cluster_size, use_lcc, seed
[^card-1]: [graphrag-six-phase-indexing-pipeline](graphrag-six-phase-indexing-pipeline.md) -- Leiden 社区检测是 Phase 4 的核心操作
[^card-2]: [graphrag-query-modes](graphrag-query-modes.md) -- Global Search 直接消费社区报告
