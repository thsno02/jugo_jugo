---
id: confidence-level-annotation
title: 置信度标注体系
status: draft
card_type: governance-mechanism
tags: [confidence, annotation, knowledge-quality, verification]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-sdyckjq-llm-wiki-skill]
evidence_basis: code_implementation
justification: ../justification/confidence-level-annotation.md
canonical_concept: confidence-level-annotation
aliases: [置信度标注, confidence level annotation, 置信度, EXTRACTED, INFERRED, AMBIGUOUS, UNVERIFIED]
summary: >-
  llm-wiki 的知识治理机制：对知识库中每条信息标注置信度层级。四级枚举：EXTRACTED（直接提取）/ INFERRED（推断得出）/ AMBIGUOUS（语义模糊）/ UNVERIFIED（未经核实）。用于标识信息可信程度，一眼看出哪些需要核实。是知识编译产物的质量治理层。
related: [knowledge-compilation-paradigm, digital-landscape-knowledge-graph]
---

llm-wiki 对知识库中的信息实施四级置信度标注，作为知识质量治理机制。四个层级为：[^src-1]

- **EXTRACTED**：直接从源材料提取的事实
- **INFERRED**：基于源材料推断得出的结论
- **AMBIGUOUS**：语义模糊、存在多种解读的信息
- **UNVERIFIED**：尚未经过核实的信息

该体系使用户能"一眼看出哪些需要核实"，将知识库从单纯的信息聚合提升为具备可信度感知的结构化产物。[^src-1] [^card-1]

[^src-1]: `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md` -- "核心亮点" -- "EXTRACTED / INFERRED / AMBIGUOUS / UNVERIFIED，一眼看出哪些需要核实"
[^card-1]: knowledge-compilation-paradigm -- 置信度标注是编译产物的质量元数据层
