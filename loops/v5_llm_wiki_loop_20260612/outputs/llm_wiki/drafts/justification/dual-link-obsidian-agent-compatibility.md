# Justification: dual-link-obsidian-agent-compatibility

## 抽卡理由
双链接格式是 llm-wiki 确保工具无关性的核心约定——同一行兼容 Obsidian 图视图和 agent markdown 导航。这是一个简洁但影响深远的设计决策。

## 证据强度
- wiki-structure.md Dual-Link Convention 段定义格式
- README "Linking: Works Everywhere" 段解释动机
- AGENTS.md Core Principles #4 声明原则
- compilation.md 在写入协议中强制要求
- lint C4 检查双向性
- evidence_basis: code_implementation

## 原子性检验
单一核心 idea：在同一行使用双链接格式实现多工具兼容。
