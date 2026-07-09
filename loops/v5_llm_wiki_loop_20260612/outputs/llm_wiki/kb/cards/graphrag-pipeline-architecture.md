---
id: graphrag-pipeline-architecture
title: GraphRAG 流水线架构
status: accepted
card_type: system-architecture
tags:
- graphrag
- rag
- knowledge-graph
- pipeline
- community-detection
- map-reduce
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-graphrag
evidence_basis: experimental_paper
justification: ../justification/graphrag-pipeline-architecture.md
canonical_concept: graphrag-pipeline-architecture
aliases:
- GraphRAG pipeline
- GraphRAG workflow
- Graph RAG pipeline
- GraphRAG 流水线
summary: GraphRAG graphrag-pipeline-architecture 流水线架构由六阶段组成：Source Documents 分块为 Text Chunks（600 token, 100 overlap）；LLM 从 chunk 抽取 entities relationships claims；聚合为 Knowledge Graph（实体描述摘要化、关系重复数作边权）；Leiden
  层级社区检测划分 Graph Communities（互斥全覆盖）；生成 Community Summaries（按节点度优先级填充 context window）；查询时 map-reduce 产出 Global Answer（并行 map 各社区摘要生成中间答案+打分 0-100 过滤排序后 reduce）。
related:
- graphrag-community-hierarchy-cost-performance
- graphrag-community-summary-generation
- graphrag-context-window-lost-in-middle
- graphrag-entity-extraction-self-reflection
- graphrag-global-sensemaking
- graphrag-knowledge-poisoning-attack-surface
- graphrag-map-reduce-query-mechanism
- graphrag-relationship-fine-tuning
---
GraphRAG 流水线包含索引时（indexing time）和查询时（query time）两个阶段共六步。

**索引时**：
1. **Source Documents → Text Chunks**: 语料分割为固定大小文本块（默认 600 token, 100 token 重叠）
2. **Text Chunks → Entities & Relationships**: LLM 提取实体（名称/类型/描述）、关系（源/目标/描述/强度）和 claims（可验证事实陈述）。提示可通过领域特定 few-shot exemplars 定制。
3. **Entities & Relationships → Knowledge Graph**: 多次抽取的同一实体实例聚合为单个节点（描述合并摘要），关系聚合为边（重复数成为边权）。
4. **Knowledge Graph → Graph Communities**: 使用 Leiden 算法递归层级社区检测，直到叶社区不可再分。每级提供互斥全覆盖的节点分区。
5. **Graph Communities → Community Summaries**: 叶级社区按边的源/目标节点度降序优先级迭代填充 LLM context window 生成摘要；高层级以子社区摘要替代过长的元素摘要以适应窗口。

**查询时**：
6. **Community Summaries → Community Answers → Global Answer**: 社区摘要随机打乱分块；LLM 并行生成中间答案并打分（0-100 helpfulness）；过滤 0 分答案后按得分降序填入最终 context window 生成全局答案。

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "GraphRAG Workflow" (Section 3.1) -- "Graph RAG pipeline using an LLM-derived graph index of source document text"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Community Summaries → Community Answers → Global Answer" (Section 3.1.6) -- "Community summaries are randomly shuffled and divided into chunks of pre-specified token size"
