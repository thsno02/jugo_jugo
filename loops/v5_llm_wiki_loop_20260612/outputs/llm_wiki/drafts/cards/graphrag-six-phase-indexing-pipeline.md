---
id: graphrag-six-phase-indexing-pipeline
title: GraphRAG 六阶段索引流水线
status: draft
card_type: data-pipeline
tags: [indexing, pipeline, text-chunking, graph-extraction, community-detection, embedding]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
evidence_basis: code_implementation
justification: ../justification/graphrag-six-phase-indexing-pipeline.md
canonical_concept: graphrag-six-phase-indexing-pipeline
aliases: [GraphRAG indexing pipeline, GraphRAG 索引管线, default dataflow, 默认数据流]
summary: >-
  GraphRAG 默认索引流水线分六阶段：Phase 1 文档切分为 TextUnit（默认1200 token）、Phase 2 文档-TextUnit 关联、Phase 3 LLM 提取实体/关系/声明、Phase 4 Leiden 层次社区检测、Phase 5 社区报告生成与摘要、Phase 6 文本嵌入写入向量存储。indexing pipeline six-phase TextUnit extraction community detection embedding。
related: [graphrag-knowledge-graph-augmented-rag]
---

GraphRAG 的默认配置索引流水线由六个阶段组成，将原始文本文档转化为 GraphRAG Knowledge Model：[^src-1]

**Phase 1 - 构成 TextUnit**：将输入文档切分为 TextUnit（默认 1200 token），作为后续图提取的分析单元和溯源引用基础。较大的 chunk 可加速处理但降低输出精细度。[^src-2]

**Phase 2 - 文档处理**：建立文档与 TextUnit 之间的双向关联，输出 Documents 表。

**Phase 3 - 图提取**：对每个 TextUnit 使用 LLM 提取实体（title, type, description）和关系（source, target, description），合并同名实体/关系的描述后由 LLM 摘要为单一描述。可选的 Claim Extraction 提取时间限定的事实性声明（Covariates）。[^src-3]

**Phase 4 - 图增强**：使用 Hierarchical Leiden Algorithm 对实体图进行递归社区聚类，直到达到社区大小阈值，输出 Communities 表。[^src-4]

**Phase 5 - 社区摘要**：为每个社区层级生成 LLM 报告，包含执行概述和关键实体/关系/声明引用，再对报告做二次摘要。

**Phase 6 - 文本嵌入**：为实体描述、TextUnit 文本、社区报告文本生成嵌入，写入配置的向量存储（默认 LanceDB）。

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/default_dataflow.md" P377-429 -- "Dataflow Overview" mermaid diagram
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/default_dataflow.md" P433-436 -- "The chunk size (counted in tokens), is user-configurable. By default this is set to 1200 tokens."
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/default_dataflow.md" P486-493 -- "we process each text-unit to extract entities and relationships out of the raw text using the LLM"
[^src-4]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/default_dataflow.md" P513-515 -- "we generate a hierarchy of entity communities using the Hierarchical Leiden Algorithm"
[^card-1]: [graphrag-knowledge-graph-augmented-rag](graphrag-knowledge-graph-augmented-rag.md) -- 本卡描述的流水线实现了该卡定义的 GraphRAG 方法论
