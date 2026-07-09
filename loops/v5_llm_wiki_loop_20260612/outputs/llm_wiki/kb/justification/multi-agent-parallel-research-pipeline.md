# Justification: multi-agent-parallel-research-pipeline

## 抽卡理由
多 Agent 研究管线是 llm-wiki 最复杂的子系统，集成了并行调度、信誉评分、进度追踪、反确认偏差等多个机制。作为一个完整的管线设计，它展示了如何在 LLM agent 框架下组织大规模信息获取。

## 证据强度
- research.md 完整定义所有模式和协议
- research-infrastructure.md 定义信誉评分、进度公式、gap 评分
- README Research Modes 表格概述
- evidence_basis: code_implementation

## 原子性检验
虽然内容丰富，但核心 idea 是统一的：多角度并行 agent swarm + 独立信誉评估 + 进度驱动终止。Thesis/Question 是同一管线的模式变体而非独立系统。
