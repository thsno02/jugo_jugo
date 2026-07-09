# Justification: llm-wiki-agent-compile-once-architecture

## 抽取理由
该卡片捕获 LLM Wiki Agent 的核心架构模式——编译式知识管理。这是该项目最根本的设计决策，所有其他功能（entity 自动创建、矛盾标记、graph 构建）都是该模式的衍生。

## 证据强度
- evidence_basis: `code_implementation` — CLAUDE.md 中包含完整的 10 步 ingest workflow 定义，README 中有目录结构展示
- 材料同时提供了 README（面向用户的说明）和 CLAUDE.md（面向 agent 的实际 workflow schema），两者一致

## 边界标注
- 卡片描述的是设计意图和 config 层面的 workflow 定义，未直接验证运行时行为
- "编译式"是提取者对架构模式的概括命名，材料原文用 "compiles once, keeps current"
