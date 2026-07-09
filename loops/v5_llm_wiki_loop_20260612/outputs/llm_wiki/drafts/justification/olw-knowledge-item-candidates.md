# Justification: olw-knowledge-item-candidates

## 为何产卡
Knowledge item candidates 是 olw 独有的子系统，体现了"保守性提取"的设计原则——有独立的数据结构（ledger）、独立的 CLI 命令（olw items）、独立的接受规则。

## 证据来源
- README "Knowledge item candidates" 一节完整描述机制
- "Quality principles" 一节确认 "Preserve weak entity references as knowledge item candidates rather than generating unsupported concept articles"

## evidence_basis 选择
选择 `code_implementation`：这是已实现的软件功能，有 CLI 命令和 DB 存储（CLAUDE.md 提及 state.py 中的 items 表）。

## 边界决策
- 未合并入三阶段管线卡：knowledge item 是管线之外的平行数据通路，非管线的子步骤
- 未合并入 rejection feedback 卡：两者虽都是质量控制手段，但运作层面完全不同（item 在 ingest 时产生，rejection 在 review 时产生）
