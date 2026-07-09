# Justification: graphrag-community-hierarchy-leiden

## 提取依据
材料 docs/index/default_dataflow.md Phase 4 详述了 Leiden 层次聚类的执行方式，docs/index/outputs.md 描述了 communities 和 community_reports 的完整 schema，docs/query/global_search.md 指出层级选择对查询质量的影响，docs/config/yaml.md 给出了配置参数。

## 原子性判断
社区检测+社区报告生成是紧密耦合的一对机制（检测产出社区结构，报告消费该结构），作为一个原子 idea 成卡合理。

## Evidence basis
code_implementation -- Leiden 聚类和社区报告生成均为实际实现的 workflow 步骤。
