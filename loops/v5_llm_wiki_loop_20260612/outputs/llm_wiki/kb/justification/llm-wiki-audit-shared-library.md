# Justification: llm-wiki-audit-shared-library

## 为什么产出此卡

audit-shared 是 llm-wiki 项目的关键架构组件，保证跨工具格式一致性。作为独立组件，有独立的设计目标和实现方式，值得单卡记录。

## Evidence basis 选择

`code_implementation` — 材料描述的是实际已实现的 TypeScript 库，列出了具体模块名(schema/anchor/id/serialize/index)。

## 拆卡决策

audit-shared 是具体技术组件，与上层模式(compile-over-rag)和设计原则(人机分工)属不同抽象层次，独立成卡。

## Hedge 使用

卡片中对"让 LLM 处理反馈时无需区分来源"使用"据材料推测"，因为 README 只说明格式统一的事实，未显式说明其对 LLM 处理的便利性。
