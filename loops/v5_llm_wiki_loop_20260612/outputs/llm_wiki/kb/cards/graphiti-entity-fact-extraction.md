---
id: graphiti-entity-fact-extraction
title: Graphiti 实体与事实提取流程
status: accepted
card_type: mechanism
tags:
- knowledge-graph
- entity-extraction
- entity-resolution
- NER
- reflexion
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-zep
evidence_basis: experimental_paper
justification: ../justification/graphiti-entity-fact-extraction.md
canonical_concept: graphiti-entity-fact-extraction
aliases:
- entity extraction
- entity resolution
- fact extraction
- 实体提取
- 实体消解
summary: Graphiti 实体提取处理当前消息+前 n=4 条消息作为上下文，自动提取 speaker 为实体， 使用 reflexion 技术减少幻觉。实体名嵌入 1024 维向量空间，经 cosine similarity + full-text search 检索候选已有节点后由 LLM 执行 entity resolution。事实（facts） 提取为 edges，同一事实可在不同实体间多次提取以建模
  hyper-edges。去重搜索约束于 同一实体对以降低计算复杂度。使用预定义 Cypher 查询写入 Neo4j。
related:
- zep-temporal-knowledge-graph-architecture
- graphiti-edge-invalidation
- cross-tool-entity-resolution
- mem0-extraction-phase
---

**实体提取**：系统处理当前消息内容和前 n=4 条消息（两个完整对话轮次）作为命名实体识别的上下文。Speaker 被自动提取为实体。系统采用受 Reflexion 启发的反思技术来最小化幻觉并提高提取覆盖率。[^src-1]

**实体消解**：提取后，每个实体名被嵌入到 1024 维向量空间。系统通过 cosine similarity search 和 full-text search 在已有图实体节点中检索相似候选。候选节点连同 episode 上下文一起送入 LLM entity resolution prompt 进行判断。若判定为重复实体，系统生成更新后的名称和摘要。[^src-2]

**事实提取**：Facts 被提取为实体对之间的 edges，每条 fact 包含关键谓词。同一事实可在不同实体间被多次提取，从而通过 hyper-edges 实现复杂多实体事实建模。[^src-3]

**Fact 去重**：去重的混合搜索被约束在相同实体对的已有边上，既防止不同实体间相似边被错误合并，又通过限制搜索空间来降低计算复杂度。[^src-4]

系统选择预定义 Cypher 查询（而非 LLM 生成查询）写入图数据库，以确保一致的 schema 格式并减少幻觉可能。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Entities" P1 -- "the system processes both the current message content and the last n messages...we employ a reflection technique inspired by reflexion"
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Entities" P2 -- "the system embeds each entity name into a 1024-dimensional vector space...We chose this approach over LLM-generated database queries"
[^src-3]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Facts" P1 -- "the same fact can be extracted multiple times between different entities, enabling Graphiti to model complex multi-entity facts through an implementation of hyper-edges"
[^src-4]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Facts" P2 -- "The hybrid search for relevant edges is constrained to edges existing between the same entity pairs"
[^card-1]: [zep-temporal-knowledge-graph-architecture] -- 实体/事实提取是三层子图中语义层的构建机制
