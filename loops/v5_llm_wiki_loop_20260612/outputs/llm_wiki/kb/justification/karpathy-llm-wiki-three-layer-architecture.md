# Justification: karpathy-llm-wiki-three-layer-architecture

## 为什么产出此卡
材料核心叙事围绕 Karpathy LLM Wiki 概念展开，三层架构是整个 my-llm-wiki 项目的理论基础。该概念具有独立的原子性：描述一种知识系统的设计模式。

## 证据强度
- evidence_basis = documentation：材料为 PyPI 项目描述页面，对 Karpathy 概念的转述属于二手文档记录
- 材料直接引述了 Karpathy 的原话和概念定义，信息密度高

## 边界决策
- 未将 my-llm-wiki 的实现细节混入此卡——实现属于另一张卡 (my-llm-wiki-tool-overview)
- 未将 write-back 机制混入——那是概念的应用层 (llm-wiki-write-back-compounding)
