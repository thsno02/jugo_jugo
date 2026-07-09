# Justification: pin-llm-wiki-agent-consumption-protocol

## 提取理由
材料 "Agent behavior" 和 "Limits" 两节定义了 agent 消费 wiki 的具体协议和工具的自我定位边界。这是 pin-llm-wiki 区别于普通文档生成工具的关键——它不仅生成内容，还规范了 agent 如何与内容交互。

## 证据强度
- evidence_basis: code_implementation — AGENTS.md 是工具实际生成的文件，行为规则为其内容
- "Limits" 节为作者明确声明的设计边界

## 原子性检验
- 单一主题：agent 消费协议 + 工具定位边界
- 不涉及架构层次（卡1）或 ingest pipeline（卡2）

## 来源段落
- "Agent behavior" (L116-123)
- "Limits" (L126-128)
