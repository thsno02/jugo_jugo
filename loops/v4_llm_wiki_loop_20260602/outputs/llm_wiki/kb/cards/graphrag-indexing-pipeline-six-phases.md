---
id: graphrag-indexing-pipeline-six-phases
title: GraphRAG 索引管线六阶段数据流
status: accepted
card_type: mechanism
tags: [graphrag, indexing-pipeline, data-pipeline, workflow, implementation]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
justification: ../justification/graphrag-indexing-pipeline-six-phases.md
canonical_concept: graphrag-indexing-pipeline-six-phases
aliases: [GraphRAG 索引六阶段, indexing dataflow phases, 图RAG管线阶段]
summary: >-
  graphrag-indexing-pipeline-six-phases（GraphRAG 索引六阶段）将非结构化文本通过六个顺序阶段转化为知识模型：TextUnit 分块 -> 文档处理 -> 图提取(实体/关系/声明) -> 图增强(Leiden社区检测) -> 社区摘要 -> 文本嵌入，输出为 Parquet 表
related: [graphrag-community-hierarchy, graphrag-self-reflection-gleaning, graphrag-map-reduce-query, graphrag-fastgraphrag-nlp-extraction, graphrag-leiden-clustering-config]
---

GraphRAG 开源实现将索引过程分为六个明确阶段，每个阶段对应一组可配置的 workflow 步骤 [^src-1]：

**Phase 1 - Compose TextUnits**：输入文档按可配置的 token 大小（默认 1200 tokens）切分为 TextUnit。TextUnit 既是图提取的分析单元，也是下游知识项的来源引用锚点，支持面包屑式溯源 [^src-2]。

**Phase 2 - Document Processing**：建立 Document 与 TextUnit 的双向链接表，导出 Documents Parquet 表。

**Phase 3 - Graph Extraction**：对每个 TextUnit 使用 LLM 提取实体（title + type + description）和关系（source + target + description），同名实体/同对关系合并描述数组后再调用 LLM 做描述摘要。可选的 claim extraction 提取时间约束的事实声明 [^src-3]。

**Phase 4 - Graph Augmentation**：对合并后的实体-关系图执行 Hierarchical Leiden 社区检测，生成层级社区结构，导出 Entities、Relationships、Communities 三张 Parquet 表 [^src-4]。

**Phase 5 - Community Summarization**：对每个社区使用 LLM 生成报告（executive overview + key entities/relationships/claims），再做报告摘要，导出 Community Reports 表。

**Phase 6 - Text Embeddings**：对 entity descriptions、text unit text、community report text 生成向量嵌入并写入配置的向量存储（默认 LanceDB）[^src-5]。

整个管线的 workflow 列表可通过 `settings.yaml` 的 `workflows` 字段精确指定——用户可以跳过不需要的步骤（如仅运行 `[create_communities, create_community_reports]` 即可支持 Global Search）[^src-6]。此设计也支持 Bring-Your-Own-Graph 场景：用户提供自己的 entities/relationships parquet，仅运行社区检测和摘要步骤。

实际管线中的 LLM 交互由缓存层保护——相同输入参数的 completion 请求返回缓存结果，使索引器具备幂等性和网络容错性[^card-graphrag-llm-caching]。

## Footnotes

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/default_dataflow.md -- Dataflow Overview 流程图展示六阶段: Phase 1 Compose TextUnits -> Phase 2 Document Processing -> Phase 3 Graph Extraction -> Phase 4 Graph Augmentation -> Phase 5 Community Summarization -> Phase 6 Text Embeddings
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/default_dataflow.md -- "A TextUnit is a chunk of text that is used for our graph extraction techniques. They are also used as source-references by extracted knowledge items in order to empower breadcrumbs and provenance"
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/default_dataflow.md -- "any entities with the same title and type are merged by creating an array of their descriptions. Similarly, any relationships with the same source and target are merged"
[^src-4]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/default_dataflow.md -- "we generate a hierarchy of entity communities using the Hierarchical Leiden Algorithm. This method will apply a recursive community-clustering to our graph until we reach a community-size threshold"
[^src-5]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/default_dataflow.md -- "By default we embed entity descriptions, text unit text, and community report text"
[^src-6]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/byog.md -- "workflows: [create_communities, create_community_reports]"
[^card-graphrag-llm-caching]: [GraphRAG LLM 缓存幂等机制](graphrag-llm-caching-idempotency.md) -- 管线的网络容错和幂等性依赖于缓存层设计
