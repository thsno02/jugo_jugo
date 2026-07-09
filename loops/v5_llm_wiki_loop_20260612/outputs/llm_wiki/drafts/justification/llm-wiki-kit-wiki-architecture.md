# Justification: llm-wiki-kit-wiki-architecture

## 为什么产出此卡

wiki 的三层目录结构（concepts/sources/synthesis + index + log）加上不可变 raw 层是该工具的核心设计决策，决定了知识如何组织和关联。这是一个独立的架构知识单元。

## evidence_basis 选择: code_implementation

架构图出自可运行代码的 README，描述的目录结构是实际文件系统布局，由代码生成和维护。

## 卡片边界

本卡聚焦"结构是什么"（目录组成、职责分工、互联方式、图谱可视化）。不涉及为什么需要持久记忆（见 persistent-agent-memory 卡）或具体工具接口（见 mcp-tool-surface 卡）。

## 材料覆盖度

覆盖 README 的 How It Works 架构图、Knowledge Graph 章节。
