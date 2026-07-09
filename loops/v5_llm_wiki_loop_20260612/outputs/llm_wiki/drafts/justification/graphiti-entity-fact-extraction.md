## Justification: graphiti-entity-fact-extraction

**提取理由**: 实体和事实的提取/消解是 KG 构建的核心流程，论文在 Section 2.2 详细描述了多步骤 pipeline。含 reflexion 技术、向量空间消解、hyper-edge 等有价值的工程细节。

**原子性判断**: 将 entity extraction + resolution + fact extraction + dedup 视为一个紧密耦合的流程，作为单卡记录。Temporal extraction 和 edge invalidation 独立成卡。

**Evidence basis**: experimental_paper。
