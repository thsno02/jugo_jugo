## Justification: zep-reranker-strategies

**提取理由**: Zep 实现了五种 reranker 策略，其中 episode-mentions reranker 和 node distance reranker 是 graph-specific 的创新。对理解 KG-based retrieval 的精度优化有独立价值。

**原子性判断**: 聚焦于 reranker 组件及其策略枚举，不涉及搜索阶段（独立卡）。

**Evidence basis**: experimental_paper。
