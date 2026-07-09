---
id: graphiti-episode-subgraph
title: Graphiti Episode 子图与非损失性数据存储
status: draft
card_type: mechanism
tags: [knowledge-graph, episodic-memory, data-ingestion]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
evidence_basis: experimental_paper
justification: ../justification/graphiti-episode-subgraph.md
canonical_concept: graphiti-episode-subgraph
aliases: [episode subgraph, episodic nodes, episodes in Graphiti]
summary: >-
  Graphiti episode subgraph 存储原始输入数据（message/text/JSON），作为非损失性数据源
  供语义实体提取。每条消息携带 reference timestamp t_ref 用于解析相对时间引用。
  Episodic edges 连接 episodes 到其引用的 semantic entity 节点，支持双向索引以实现
  溯源（citation）和前向遍历。
related: [zep-temporal-knowledge-graph-architecture]
---

Episode 子图是 Graphiti 知识图谱的最底层。Episodic 节点（episodes）包含原始输入数据，可以是 message、text 或 JSON 三种类型。Episodes 作为非损失性数据存储，是语义实体和关系提取的源头。[^src-1]

每条消息携带 reference timestamp t_ref，标识消息发送时间。这使系统能够准确提取消息中的相对或部分日期表述（如"next Thursday"、"in two weeks"、"last summer"）并转换为精确时间戳。[^src-2]

Episodic edges 连接 episodes 到其提取的实体节点。Episodes 与其派生的 semantic edges 之间维护双向索引：语义制品可追溯到源 episode 以实现引用/引述，episodes 也可快速检索其相关实体和事实。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Episodes" P1 -- "Episodes can be one of three core types: message, text, or JSON...Episodes serve as a non-lossy data store"
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Episodes" P2 -- "Each message includes a reference timestamp t_ref indicating when the message was sent"
[^src-3]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Episodes" P3 -- "Episodes and their derived semantic edges maintain bidirectional indices"
[^card-1]: [zep-temporal-knowledge-graph-architecture] -- 本卡为三层子图中 episode 层的展开
