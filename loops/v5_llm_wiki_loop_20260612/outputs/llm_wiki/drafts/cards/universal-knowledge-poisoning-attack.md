---
id: universal-knowledge-poisoning-attack
title: 通用知识投毒攻击 UKPA
status: draft
card_type: attack-method
tags: [graphrag, ukpa, universal-attack, coreference, entity-linking, knowledge-poisoning]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
evidence_basis: experimental_paper
justification: ../justification/universal-knowledge-poisoning-attack.md
canonical_concept: universal-knowledge-poisoning-attack
aliases: [UKPA, Universal Knowledge Poisoning Attack, Universal KPA, 通用知识投毒]
summary: >-
  Universal Knowledge Poisoning Attack UKPA 利用语言学共指链（代词、定指描述、指代表达）作为攻击目标，
  破坏 GraphRAG 跨 chunk 的实体合并机制。通过微妙改写使共指消解失败，原本合并为单一节点的 mention 分裂
  为多个不连通节点，全局图碎片化。四步流程：语言学分析 -> 扰动候选生成 -> 结构影响评分 -> 选择与更新。
  修改仅 60/134072 词（<0.05%），QA 准确率从 95% 降至 50%。通用知识投毒 coreference chain disruption。
related: [graphrag-knowledge-poisoning-attack-surface, ukpa-structural-impact-score]
---

UKPA 的核心洞察：GraphRAG 严重依赖语言学一致性线索（coreference chains、指代表达）来决定跨 chunk 的多个 mention 是否合并为同一实体节点。这些信号是维持图连通性的"胶水"。[^src-1]

攻击策略完全在语言域操作：(1) 对每个 chunk 用 LLM 进行语言学分析提取共指链；(2) 生成满足流畅性/局部语义保持/小编辑距离的扰动候选；(3) 用代理评分函数估计结构影响；(4) 选最高分候选替换原文。[^src-2]

累积效果：mention 无法正确合并，节点增殖，关系分散到不连通组件，长距离推理路径断裂。仅修改 0.045% 语料（60 词/134072 词）即导致 MS-GraphRAG QA 从 95% 降至 50%。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Universal Knowledge Poisoning Attack" P478-485 -- "GraphRAG relies heavily on linguistic coherence cues, particularly coreference chains and referring expressions"
[^src-2]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Universal Knowledge Poisoning Attack" P503-548 -- "UKPA operates entirely in the language domain... four modules"
[^src-3]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "UKPA Performance" P665 -- "the QA accuracy on Microsoft GraphRAG dropped from 95% to 50% under our attack"

[^card-5]: [[graphrag-knowledge-poisoning-attack-surface]] UKPA 是该攻击面的通用实例化
