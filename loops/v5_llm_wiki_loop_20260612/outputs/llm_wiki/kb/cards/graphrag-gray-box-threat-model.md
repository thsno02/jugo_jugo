---
id: graphrag-gray-box-threat-model
title: GraphRAG 灰盒威胁模型
status: accepted
card_type: threat-model
tags:
- graphrag
- threat-model
- gray-box
- adversary
- corpus-modification
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-graph-poisoning
evidence_basis: experimental_paper
justification: ../justification/graphrag-gray-box-threat-model.md
canonical_concept: graphrag-gray-box-threat-model
aliases:
- GraphRAG threat model
- gray-box adversary
- 灰盒攻击者模型
- Attack Model
summary: GraphRAG gray-box threat model 定义灰盒攻击者：知道 GraphRAG 整体流程（分块-提取-建图-社区-摘要-检索） 但无法访问已构建图或模型参数。攻击者仅能修改可信源语料的小部分（如 Wikipedia 编辑），不能注入新文档。 TKPA 攻击者知道社区结构驱动答案；UKPA 攻击者仅知道系统从文本构建知识图谱。gray-box corpus modification。
related:
- graphrag-knowledge-poisoning-attack-surface
- targeted-knowledge-poisoning-attack
- universal-knowledge-poisoning-attack
---

本文考虑的灰盒攻击者通过编辑源语料而非注入全新文档或访问模型参数来投毒 GraphRAG。攻击者知道整体流水线（文本分块、实体关系提取、知识图谱构建、社区摘要生成），但无法接触已构建的图或模型参数。[^src-1]

两种攻击的知识/能力假设差异化：
- TKPA：知道 GraphRAG 将知识组织为驱动下游答案的社区；可修改语料小部分以影响特定查询答案
- UKPA：仅知道系统从文本构建知识图谱，不了解图结构细节；可做小编辑以广泛降低推理能力而非针对单一查询[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Attack Model" P284-295 -- "We consider a gray-box adversary that poisons GraphRAG by editing the source corpus rather than injecting entirely new documents or accessing model parameters"

[^card-7]: [[graphrag-knowledge-poisoning-attack-surface]] 该威胁模型定义了攻击面的约束条件
