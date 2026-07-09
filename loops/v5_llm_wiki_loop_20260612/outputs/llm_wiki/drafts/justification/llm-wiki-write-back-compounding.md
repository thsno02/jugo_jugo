# Justification: llm-wiki-write-back-compounding

## 为什么产出此卡
Write-back 是 LLM Wiki 概念中"compounding artifact"设计意图的具体实现机制，具有独立的原子性——描述一种知识系统如何随使用而增长的模式。

## 证据强度
- evidence_basis = documentation：材料为 PyPI 项目描述，对 write-back 命令的说明属于一手文档
- 具体命令语法和行为描述直接来自项目 README

## 边界决策
- 与工具概览卡分离：工具卡描述 what it is，此卡描述 how it grows
- 与三层架构卡分离：架构卡描述理论设计，此卡描述具体的增长机制
- SHA256 cache 与 write-back 紧密相关（都关于增量更新），故在此卡中提及
