---
id: graphrag-knowledge-poisoning-attack-surface
title: GraphRAG 知识投毒攻击面
status: draft
card_type: vulnerability-concept
tags: [graphrag, attack-surface, knowledge-poisoning, manipulation-only]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
evidence_basis: experimental_paper
justification: ../justification/graphrag-knowledge-poisoning-attack-surface.md
canonical_concept: graphrag-knowledge-poisoning-attack-surface
aliases: [Knowledge Poisoning Attack, KPA, GraphRAG attack surface, 知识投毒攻击, manipulation-only attack surface]
summary: >-
  GraphRAG knowledge poisoning attack surface 是一种 manipulation-only 攻击面：攻击者无需注入新文档，
  仅修改可信语料中极少量词（<0.05%-0.06%）即可扭曲 LLM 提取的实体和关系，使构建的知识图谱产生持久性
  结构失真并误导下游推理。该攻击面对应 Wikipedia 等可信源的细微编辑场景，与加性注入攻击（如 GRAGPOISON）
  形成互补。Knowledge Poisoning Attacks KPA manipulation-only。
related: [graphrag-pipeline-architecture]
---

GraphRAG 依赖 LLM 从原始文本提取知识构建图谱，这一过程可被恶意操纵以植入误导信息。本文揭示的 manipulation-only 攻击面表明：即使攻击者无法添加新文本，仅修改已有语料中的少数词即可扭曲图构建阶段提取的实体和关系，腐败的结构随后持续误导大量查询。[^src-1]

该威胁对应对可信来源的细微编辑（如 Wikipedia 的微小改动），而非注入明显恶意内容。与先前 GRAGPOISON 的加性攻击（注入新 chunk/重复关系）形成根本区别。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Introduction" P197-201 -- "An unexplored question is whether GraphRAG is also vulnerable when the adversary cannot add new text, but is only able to make small, subtle modifications to the existing corpus"
[^src-2]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Introduction" P193-199 -- "While GRAGPOISON demonstrates that GraphRAG can indeed be poisoned, its attack strategies all operate in an additive manner"

[^card-1]: [[graphrag-pipeline-architecture]] GraphRAG 流水线是该攻击面的前提架构
