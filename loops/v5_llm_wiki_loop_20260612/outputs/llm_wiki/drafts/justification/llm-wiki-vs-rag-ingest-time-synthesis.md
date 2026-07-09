# Justification: llm-wiki-vs-rag-ingest-time-synthesis

## 为什么提取这张卡

材料中有一个独立的 "LLM Wiki vs RAG" 章节，给出了明确的表格对比。这是一个独立的原子观点：两种范式在综合时机上的根本区别。

## 为什么用 llm-wiki-vs-rag-ingest-time-synthesis 而非 llm-wiki-vs-rag

同 loop 中已有另一位 worker 从不同源（marvin-hn-persistent-knowledge）产出了 `llm-wiki-vs-rag` 卡。本卡从 karpathy-llm-wiki 仓库 README 的角度提供补充视角（具体的表格对比和 "optimized for the wiki model" 的明确声明），使用更具体的 id 以避免文件冲突。治理阶段可决定合并或保留。

## Evidence basis 选择: code_implementation

来源是实际代码项目的 README，描述的对比直接指导了该项目的设计决策。

## 原子性判断

聚焦于 LLM wiki vs RAG 的综合时机对比这一单一论断，不涉及架构细节或工具实现。
