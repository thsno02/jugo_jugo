# Justification: olw-three-stage-pipeline

## 为何产卡
README 详细描述了 olw 的三阶段管线架构（ingest/compile/review），这是该工具的核心设计模式，构成一个独立的原子概念。

## 证据来源
- README "How it works" 一节完整描述了三阶段流程图及各阶段 LLM 职责
- "Features" 一节确认增量编译特性
- 明确声明无 vector DB / embedding

## evidence_basis 选择
选择 `code_implementation`：README 描述的是已实现的软件架构，非理论论述。CLAUDE.md 进一步确认了 pipeline/ 目录下的 ingest.py / compile.py 等模块实现。

## 边界决策
- rejection feedback 机制单独成卡（有独立生命周期和规则）
- knowledge item candidates 单独成卡（独立子系统）
- query synthesis / compare 功能未单独成卡（相对次要，且材料描述不构成独立原子 idea 的充分密度）
