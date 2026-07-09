## Justification: graphiti-episode-subgraph

**提取理由**: Episode 子图是 Graphiti 三层架构的数据基础层，其 non-lossy 设计和 reference timestamp 机制是论文的重要技术贡献。Section 2.1 专门论述。

**原子性判断**: 聚焦于 episode 层的数据模型和双向索引特性，不涉及其上的 semantic entity 提取逻辑（独立卡）。

**Evidence basis**: experimental_paper。
