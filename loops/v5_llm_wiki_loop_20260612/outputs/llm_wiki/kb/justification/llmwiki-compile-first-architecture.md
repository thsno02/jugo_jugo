# Justification: llmwiki-compile-first-architecture

## 提取依据

材料 README.md 开篇即阐明项目灵感来源（Karpathy LLM Wiki pattern）及核心设计哲学（compile once vs query-time retrieval）。"Why not just RAG?" 段落明确对比两种范式，并给出 RAG 与 llmwiki 的流程对比图。

## 原子性判断

本卡聚焦"编译优先"这一架构级设计决策及其与 RAG 的关系定位。具体的编译机制（两阶段管线）拆分为独立卡片。

## Evidence basis 选择

选 `code_implementation`：该工具已发布为 npm 包（`npm install -g llm-wiki-compiler`），README 描述的是已实现功能而非论文提案。

## Hedge 审查

"complementary to RAG, not a replacement" 为源材料原话，直接保留。
