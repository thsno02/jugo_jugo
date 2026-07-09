# Justification: olw-rejection-feedback-loop

## 为何产卡
Rejection feedback loop 是 olw 独有的质量控制机制，有明确的触发条件、数据流路径和终止规则（5 次 auto-block），构成独立原子概念。

## 证据来源
- README "Rejection feedback loop" 一节完整描述机制
- "Features" 一节中 "Rejection feedback" 条目确认功能存在
- CLAUDE.md 提及 state.py 中存储 rejections

## evidence_basis 选择
选择 `code_implementation`：这是已实现的软件功能，有明确的 CLI 命令和 DB 存储。

## 边界决策
- 与三阶段管线卡交叉引用（rejection feedback 是管线的子机制）
- 未将 draft annotations（低置信度注释）合并入此卡——它们是独立的质量信号，非反馈闭环的一部分
