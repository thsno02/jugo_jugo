---
id: episodic-semantic-memory-duality
title: 情景记忆与语义记忆的双存储设计
status: accepted
card_type: concept
tags: [cognitive_model, agent_memory, episodic_memory, semantic_memory, knowledge_graph]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
justification: ../justification/episodic-semantic-memory-duality.md
canonical_concept: episodic-semantic-memory-duality
aliases: [情景-语义双存储, episodic-semantic duality, 人类记忆心理学模型映射]
summary: >-
  episodic-semantic-memory-duality（情景-语义双存储, episodic-semantic duality）Zep 同时存储原始事件数据（episodic）和提取的概念关联（semantic），镜像人类记忆心理学中情景记忆与语义记忆的区分，使 agent 形成更精细的记忆结构
related: [memgpt-memory-hierarchy, observation-based-memory-representation, temporal-knowledge-graph-three-tier]
  - temporal-knowledge-graph-three-tier
  - lightmem-three-stage-memory
---

Zep 的知识图谱同时维护原始事件数据（episode 子图）和从中提取的语义实体与关系（semantic entity 子图），这种双存储设计有意识地借鉴了人类记忆的心理学模型 [^src-1]。

心理学研究区分两种记忆类型：**情景记忆（episodic memory）**——代表具体事件的记忆；**语义记忆（semantic memory）**——捕获概念之间的关联及其含义。Zep 的 episode 子图对应情景记忆，保存原始消息等事件数据；semantic entity 子图对应语义记忆，保存提取后的实体与关系 [^src-2]。

这种设计的工程价值在于：episode 子图提供无损的原始数据存储和溯源能力（可追溯到每条事实的源消息），而 semantic entity 子图提供结构化的检索和推理能力。两个层次协同工作，使基于 Zep 的 LLM agent 能够发展出"更精细、更有层次的记忆结构，更好地与我们对人类记忆系统的理解对齐"[^src-3]。

Zep 的实现参考了 AriGraph 中对 episodic 与 semantic 子图的区分 [^src-4]。LoCoMo 的观察式记忆表示在工程层面验证了类似的直觉——将原始对话转化为断言式陈述（类似语义记忆提取）显著提升检索效果[^card-1]。Graphiti 在情景-语义双存储基础上增加了 community 聚类层，形成完整的三层子图架构[^card-2]。与 Zep 按认知功能划分记忆不同，MemGPT 按访问距离（in-context vs out-of-context）划分层次，两种分层标准构成正交维度[^dist-1]。

## Footnotes

[^card-1]: [观察断言式记忆表示](observation-based-memory-representation.md) -- Zep 的情景-语义双存储是理论框架，LoCoMo 的 observation 表示是工程验证——将对话转化为关于说话者的断言式陈述（类似语义记忆提取）使 QA F1 从 31.7 提升至 41.4
[^card-2]: [时序知识图谱的三层子图架构](temporal-knowledge-graph-three-tier.md) -- 本卡聚焦情景-语义双存储的认知心理学基础，该卡展开完整的三层工程架构（episode + semantic entity + community）
[^dist-1]: [MemGPT 两级内存层次结构](memgpt-memory-hierarchy.md) -- 本卡按认知功能（情景 vs 语义）划分记忆层次，该卡按访问距离（in-context vs out-of-context）划分，两种分层标准正交互补

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2 -- "The dual storage of both raw episodic data and derived semantic entity information mirrors psychological models of human memory."
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2 -- "These models distinguish between episodic memory, which represents distinct events, and semantic memory, which captures associations between concepts and their meanings"
[^src-3]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2 -- "This approach enables LLM agents using Zep to develop more sophisticated and nuanced memory structures that better align with our understanding of human memory systems."
[^src-4]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2 -- "our implementation of distinct episodic and semantic subgraphs draws from similar approaches in AriGraph"
