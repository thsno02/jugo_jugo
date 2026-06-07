---
schema: justification_journal.v1
card: ../cards/graphrag-leiden-clustering-config.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：从 repo-microsoft-graphrag material_bundle.txt 提取实现细节
来源：`data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt`
源证据：
- docs/config/yaml.md — cluster_graph 参数（max_cluster_size, use_lcc, seed）
- docs/config/yaml.md — prune_graph 参数（min_node_freq, max_node_degree_std, remove_ego_nodes 等）
- docs/index/byog.md — weight 字段对 Leiden 计算的重要性
- docs/visualization_guide.md — Gephi 中 Leiden 参数（Modularity, Resolution=1）
范围论证：现有 graphrag-community-hierarchy 卡描述论文中 Leiden 层级检测的概念，此卡聚焦实现中的具体可调参数和图修剪前置步骤，是工程实践层的补充。
