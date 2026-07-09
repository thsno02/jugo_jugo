# Justification: langgraph-tool-runtime-store-access

## 为什么产出此卡
材料中最核心的集成模式：agent tool 如何通过 ToolRuntime 读写 store。这是开发者实际使用 long-term memory 时最需要的 pattern。

## Evidence basis 选择
官方文档 documentation。

## 原子性检查
覆盖 ToolRuntime + context_schema 这一集成模式（读写均含），但不涉及 store 本身的数据模型或搜索细节。
