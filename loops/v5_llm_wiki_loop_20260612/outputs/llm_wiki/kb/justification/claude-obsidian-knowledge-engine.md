# Justification: claude-obsidian-knowledge-engine

## 为何建卡
这是 claude-obsidian 项目的顶层架构卡，概括其核心循环（ingest/query/lint）、工程特性（multi-agent/6 modes/跨项目/DragonScale）和定位（knowledge engine vs chat interface）。作为该源的 anchor card。

## 拆卡说明
- hot cache 独立为 claude-obsidian-hot-cache（独立机制，可跨项目引用）
- 竞品对比独立为 claude-obsidian-differentiation（evidence_basis 不同：author_claim vs code_implementation）

## evidence_basis 选择
code_implementation：README 描述的 skills/agents/hooks/file-structure 均为仓库中实际存在的代码实现。
