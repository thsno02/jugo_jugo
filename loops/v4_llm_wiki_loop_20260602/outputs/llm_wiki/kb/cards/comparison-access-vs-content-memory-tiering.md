---
id: comparison-access-vs-content-memory-tiering
title: 访问距离分层 vs 认知内容分层：记忆层次化的两个正交维度
status: accepted
card_type: distinction
tags: [memory_hierarchy, tiering, access_proximity, cognitive_type, MemGPT, Zep]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt, arxiv-zep]
justification: ../justification/comparison-access-vs-content-memory-tiering.md
canonical_concept: comparison-access-vs-content-memory-tiering
aliases: [访问分层vs内容分层, access-based vs content-based tiering]
summary: >-
  comparison-access-vs-content-memory-tiering（访问分层vs内容分层）LLM agent 记忆层次化存在两种正交的划分标准：
  MemGPT 按访问距离（in-context vs out-of-context）划分，Zep 按认知内容类型（episodic vs semantic）划分，
  两者可组合使用
related: [episodic-semantic-memory-duality, memgpt-memory-hierarchy, temporal-knowledge-graph-three-tier]
---

LLM agent 记忆系统中「分层」看似是共识，但不同系统的分层标准存在根本差异，构成两个正交维度：

**访问距离维度（access proximity）**：MemGPT 的分层标准是数据离 LLM 推理的「距离」。主上下文（main context）中的数据在推理时直接可用，外部上下文（external context）中的数据必须通过函数调用显式移入[^card-1]。这一维度关心的问题是「这条数据此刻能否被 LLM 看到」，类比操作系统中 RAM vs 磁盘的层次。

**认知内容维度（cognitive content type）**：Zep 的分层标准是数据的认知功能类别。情景记忆（episodic）保存原始事件，语义记忆（semantic）保存提取后的概念关系[^card-2]。这一维度关心的问题是「这条数据代表什么类型的知识」，借鉴人类记忆心理学中的 episodic-semantic 区分。

两种维度正交而非互斥：一条数据可以同时拥有「是否 in-context」和「是 episodic 还是 semantic」两个属性。[编者注：以下为 KB 编辑合成的分析框架]理论上可以构建四象限：in-context episodic、in-context semantic、out-of-context episodic、out-of-context semantic。这意味着完整的记忆架构可能需要同时在两个维度上做层次化设计，而非仅选择其中一个。

## Footnotes

[^card-1]: [MemGPT 两级内存层次结构](memgpt-memory-hierarchy.md) -- 访问距离维度的代表：按 in-context vs out-of-context 划分，类比 OS 的 RAM vs 磁盘
[^card-2]: [情景记忆与语义记忆的双存储设计](episodic-semantic-memory-duality.md) -- 认知内容维度的代表：按 episodic vs semantic 划分，借鉴人类记忆心理学模型
[^src-1]: data/raw/arxiv/arxiv-memgpt/text.txt -- "virtual context management, a technique drawing inspiration from hierarchical memory systems in traditional operating systems that provide the appearance of large memory resources through data movement between fast and slow memory"
[^src-2]: data/raw/arxiv/arxiv-zep/agent_source_bundle.txt -- "The dual storage of both raw episodic data and derived semantic entity information mirrors psychological models of human memory. These models distinguish between episodic memory, which represents distinct events, and semantic memory, which captures associations between concepts and their meanings"
