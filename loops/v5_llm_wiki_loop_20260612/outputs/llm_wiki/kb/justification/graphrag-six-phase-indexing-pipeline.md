# Justification: graphrag-six-phase-indexing-pipeline

## 提取依据
材料 docs/index/default_dataflow.md 详细描述了 6 阶段流水线，包含完整的 mermaid 数据流图和每个阶段的具体操作说明。

## 原子性判断
本卡聚焦于索引流水线的整体架构和阶段划分。各阶段内部的深度机制（如 Leiden 算法细节、entity extraction prompt）可能在后续卡中进一步原子化。

## Evidence basis
code_implementation -- 描述的是实际运行的 pipeline workflow 代码实现的行为。
