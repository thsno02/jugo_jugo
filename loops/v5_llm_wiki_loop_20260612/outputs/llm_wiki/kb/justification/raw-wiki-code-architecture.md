# Justification: raw-wiki-code-architecture

## 为什么产出此卡
三层架构（raw/wiki/code）是 LLM Wiki 的核心数据模型，在 README 中以代码块和多处引用明确定义，具有独立描述价值。

## 证据强度
- 材料以 ASCII 图展示三层流向
- 各层约束在多个 section 反复强化（The Idea / Don't Do These Things / How Do I Know It's Working）
- 配套工具链（ingest_raw, stale_report, delta_compile, wiki_size_report）均围绕此架构设计
- evidence_basis 取 code_implementation：架构在 bootstrap 脚本中被物理实现为目录结构

## 边界决策
- 与编译范式分离：范式是认知主张，架构是实现结构
- 与五条规则分离：规则约束行为，架构定义拓扑
- 未单独为工具链出卡：工具是架构的辅助而非独立概念（且材料中描述深度不足以支撑独立卡）
