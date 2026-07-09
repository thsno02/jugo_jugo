# Justification: llmwiki-two-phase-pipeline

## 提取依据

"How it works" 段落明确描述 two-phase pipeline 及其设计动机，并给出完整流水线图。incremental compilation 通过 hash-based change detection 实现亦在同段说明。

## 原子性判断

本卡聚焦编译的具体机制：两阶段分离 + 增量哈希检测。与上层的"编译优先"设计哲学分卡，与下游的"认识论元数据"分卡。

## Evidence basis 选择

选 `code_implementation`：描述的是已实现的工程管线，非提案或假设。

## Hedge 审查

源材料对此部分使用确定性陈述，无需添加 hedge。
