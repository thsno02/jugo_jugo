---
id: graphrag-knowledge-model-schema
title: GraphRAG Knowledge Model 输出 Schema
status: draft
card_type: data-model
tags: [knowledge-model, schema, parquet, entities, relationships, communities, text-units, covariates]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
evidence_basis: code_implementation
justification: ../justification/graphrag-knowledge-model-schema.md
canonical_concept: graphrag-knowledge-model-schema
aliases: [GraphRAG Knowledge Model, knowledge model schema, 知识模型, output tables, parquet outputs]
summary: >-
  GraphRAG Knowledge Model 定义了索引输出的数据抽象层，包含 7 种表：Document（输入文档）、TextUnit（分析切片，含 n_tokens/entity_ids/relationship_ids）、Entity（title/type/description/frequency/degree）、Relationship（source/target/description/weight/combined_degree）、Covariate（可选 claims，含 subject/object/status/时间范围）、Community（Leiden 层次结构含 parent/children/level）、Community Report（title/summary/full_content/rank/findings）。所有表含 UUID id 和 human_readable_id。默认输出为 Parquet 文件。knowledge model schema entities relationships communities text-units parquet。
related: [graphrag-six-phase-indexing-pipeline, graphrag-community-hierarchy-leiden]
---

GraphRAG Knowledge Model 是索引流水线输出的数据抽象层，定义了底层存储技术的统一接口。默认以 Parquet 文件格式输出。所有表共享两个标识字段：`id`（全局唯一 UUID）和 `human_readable_id`（每次运行递增的短 ID，用于引用）。[^src-1]

核心表结构：

- **Document**：输入文档，含 title、text、text_unit_ids、metadata。[^src-2]
- **TextUnit**：文本分析切片，含 text、n_tokens、document_id、entity_ids、relationship_ids、covariate_ids。
- **Entity**：提取的实体节点，含 title、type（默认 organization/person/geo/event）、description（多描述 LLM 摘要合一）、text_unit_ids、frequency（出现次数）、degree（图节点度）。
- **Relationship**：实体间关系（图边列表），含 source、target、description、weight（LLM 评估的 strength 总和）、combined_degree、text_unit_ids。
- **Covariate**（可选）：Claims 提取结果，含 subject_id、object_id、type、description、status（TRUE/FALSE/SUSPECTED）、start_date、end_date。
- **Community**：Leiden 层次社区，含 community ID、parent、children、level、entity_ids、relationship_ids、period、size。
- **Community Report**：社区摘要报告，含 title、summary、full_content、rank、rating_explanation、findings（5-10 个 insights）、full_content_json。[^src-3]

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/outputs.md" P840-848 -- "default pipeline produces a series of output tables... By default we write these tables out as parquet files"
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/outputs.md" P903-948 -- documents, entities, relationships, text_units table schemas
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/outputs.md" P869-885 -- community_reports schema with findings, rank, full_content_json
[^card-1]: [graphrag-six-phase-indexing-pipeline](graphrag-six-phase-indexing-pipeline.md) -- Knowledge Model 是流水线各阶段的输出规范
[^card-2]: [graphrag-community-hierarchy-leiden](graphrag-community-hierarchy-leiden.md) -- Community/Community Report 表由社区检测阶段产出
