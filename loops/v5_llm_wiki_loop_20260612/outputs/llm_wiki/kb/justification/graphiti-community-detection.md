## Justification: graphiti-community-detection

**提取理由**: 社区检测选择 label propagation 而非 Leiden 的设计决策及其动态扩展机制是论文的工程贡献，直接影响系统延迟和成本。Section 2.3 专门论述。

**原子性判断**: 聚焦于社区检测算法选择和动态更新逻辑，不涉及检索阶段如何利用 community（属于 retrieval pipeline 卡）。

**Evidence basis**: experimental_paper。
