# Justification: llm-wiki-multi-phase-query-pipeline

## 为什么产出此卡

多阶段查询管线是 LLM Wiki 区别于简单 RAG 检索的核心技术实现，包含精确的阶段划分、预算分配比例和性能数据。

## 证据来源

README Section "7. Optimized Query Retrieval Pipeline" 完整描述了 4 个阶段（含可选 1.5）、budget 比例和 recall 基准数据。

## evidence_basis 取值理由

`code_implementation`：给出了具体的 budget 比例（60/20/5/15）和基准数据（58.2% → 71.4%），属于已实现的工程管线。
