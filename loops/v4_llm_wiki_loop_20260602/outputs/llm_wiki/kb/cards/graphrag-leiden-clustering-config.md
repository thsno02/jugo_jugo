---
id: graphrag-leiden-clustering-config
title: GraphRAG Leiden 社区检测实现参数与图修剪
status: accepted
card_type: mechanism
tags: [graphrag, leiden, community-detection, clustering, graph-pruning, implementation]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
justification: ../justification/graphrag-leiden-clustering-config.md
canonical_concept: graphrag-leiden-clustering-config
aliases: [GraphRAG Leiden 配置, cluster_graph 参数, 图修剪优化模块性]
summary: >-
  graphrag-leiden-clustering-config（GraphRAG Leiden 配置）实现中通过 cluster_graph 配置控制 Leiden 聚类行为（max_cluster_size/use_lcc/seed），并提供 prune_graph 前置步骤按度数/频率/权重百分位裁剪噪声节点以优化模块性
related: [graphrag-community-hierarchy, graphrag-community-level-tradeoff, graphrag-indexing-pipeline-six-phases]
---

GraphRAG 开源实现中，Leiden 层级社区检测通过 `cluster_graph` 和 `prune_graph` 两组配置精细控制聚类质量[^card-1]。

**cluster_graph 参数** [^src-1]：
- `max_cluster_size`：导出的最大社区尺寸上限——Leiden 递归分区时以此为阈值判断是否继续向下分割
- `use_lcc`：是否仅对最大连通分量执行聚类（丢弃孤立子图）
- `seed`：随机种子，保证跨 run 的聚类稳定性（默认提供固定种子）

**prune_graph 前置修剪** [^src-2]：在社区检测前可选地裁剪图结构以优化 Leiden 模块性：
- `min_node_freq`：最小节点出现频率（出现太少的实体可能是噪声）
- `max_node_freq_std`：节点频率标准差上限（过于泛化的 hub 节点）
- `min_node_degree`：最小节点度数
- `max_node_degree_std`：节点度数标准差上限
- `min_edge_weight_pct`：最小边权重百分位（过滤弱连接）
- `remove_ego_nodes`：移除 ego 节点（过度中心化的节点）
- `lcc_only`：仅保留最大连通分量

关系表中的 `weight` 字段由 LLM 对每个关系实例派生的 "strength" 度量值求和而来，是 Leiden 正确计算社区的关键输入 [^src-3]。

Gephi 可视化指南中也展示了等价的参数选择：使用 Modularity 质量函数、resolution=1 的 Leiden 配置 [^src-4]，与代码实现中的默认行为一致。

这些参数控制的是论文中描述的 Leiden 层级社区检测[^card-hierarchy]的工程实现细节——论文描述"递归检测直到叶节点"的行为对应 `max_cluster_size` 的阈值判断。

## Footnotes

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/yaml.md -- "cluster_graph: max_cluster_size int - The maximum cluster size to export. use_lcc bool - Whether to only use the largest connected component. seed int - A randomization seed"
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/yaml.md -- "prune_graph: min_node_freq, max_node_freq_std, min_node_degree, max_node_degree_std, min_edge_weight_pct, remove_ego_nodes, lcc_only"
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/byog.md -- "the weight field is important because it is used to properly compute Leiden communities"
[^src-4]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/visualization_guide.md -- "For the Leiden Algorithm: Quality function: Modularity, Resolution: 1"
[^card-hierarchy]: [GraphRAG 层级社区检测与摘要机制](graphrag-community-hierarchy.md) -- 本卡描述 Leiden 聚类的工程配置参数，该卡描述论文中层级社区检测的概念与自底向上摘要算法
[^card-1]: [GraphRAG 层级社区检测与摘要机制](graphrag-community-hierarchy.md) -- 论文中"递归检测直到叶节点"对应实现中 max_cluster_size 阈值
