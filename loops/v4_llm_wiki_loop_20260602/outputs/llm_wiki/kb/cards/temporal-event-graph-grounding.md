---
id: temporal-event-graph-grounding
title: 时序事件图作为对话锚定机制
status: accepted
card_type: mechanism
tags: [temporal-event-graph, dialogue-grounding, causal-connection, persona, agent-architecture]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
justification: ../justification/temporal-event-graph-grounding.md
canonical_concept: temporal-event-graph-grounding
aliases: [temporal event graph, 时序事件图, 因果事件图]
summary: >-
  temporal-event-graph-grounding（temporal event graph, 时序事件图, 因果事件图）为每个对话代理构建含日期和因果连接的生活事件图（最多 25 事件 / 6-12 个月），作为长期对话的叙事锚定，迫使对话反映真实时间推移和因果关系
related: [edge-invalidation-mechanism, locomo-benchmark, observation-based-memory-representation, temporal-knowledge-graph-three-tier, temporal-reasoning-difficulty]
---

LoCoMo 的对话生成管线为每个虚拟代理构建一个时序事件图（temporal event graph）$\mathcal{G}$，用于将对话锚定在真实的人生经历上[^src-1]。该图包含事件节点 $e_i$（各带日期 $t_i$）和因果连接 $l = (e_i, e_j)$，体现事件间的因果关系和自然继承关系[^src-2]。

图的生成采用迭代过程：先基于人设声明（persona）用 LLM（text-davinci-003）生成初始批次 $k=3$ 个独立事件，再以已有事件为输入迭代生成后续事件，每个图最多 25 个事件，时间跨度 6-12 个月[^src-3]。这种迭代设计在推理开销和时间-因果连贯性之间取得平衡。

在对话生成时，代理的回复会额外以两次会话之间发生的事件子集为条件：$\{e \in \mathcal{G} \mid t_k^s < t_i^e < t_{k+1}^s\}$，从而在对话中注入长期时序叙事[^src-4]。例如，某角色 Jack 热爱游戏 -> 被知名游戏公司邀请，或立志做酒店经理 -> 报名酒店管理课程 -> 三个月后在社交媒体分享心得[^src-5]。

Zep/Graphiti 的三层子图架构（episode/semantic entity/community）提供了一种更正式化的时序知识组织方案，其 semantic entity 子图的实体-关系结构与 LoCoMo 的事件-因果连接图在功能上高度对应，但 Graphiti 额外引入了社区聚类层和双时间线建模[^card-1]。Graphiti 的边失效机制则解决了时序事件图未覆盖的问题：当新事件与旧事件矛盾时，如何以非破坏性方式更新知识[^card-2]。LoCoMo 基准的评估结果表明，这类时序事件图所支撑的时序推理恰恰是 LLM 对话记忆中与人类差距最大的能力维度（73%），凸显了事件图锚定机制的重要性[^card-3]。

## Footnotes

[^card-1]: [时序知识图谱的三层子图架构](temporal-knowledge-graph-three-tier.md) -- Graphiti 的三层架构（episode/semantic/community）是对 LoCoMo 时序事件图的正式化扩展，增加了社区聚类层和双时间线维度
[^card-2]: [边失效与动态知识更新机制](edge-invalidation-mechanism.md) -- Graphiti 的边失效机制解决了时序事件图未覆盖的矛盾解决问题：当新信息与旧事实冲突时如何非破坏性更新
[^card-3]: [时序推理是 LLM 对话记忆中最困难的能力维度](temporal-reasoning-difficulty.md) -- 本卡提供事件图锚定机制支撑时序叙事，该卡量化了时序推理在 LLM 对话记忆中与人类 73% 的差距，凸显了结构化时序支撑的重要性

[^src-1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.2" -- "we construct a temporal event graph, labeled as G, for each agent"
[^src-2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.2" -- "G includes causal connections l = (e_i, e_j) that illustrate the causal relationships among events"
[^src-3]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.2" -- "we create up to 25 events, spread across a time frame of 6 to 12 months, in an iterative process... Initially, a small batch of k=3 events is generated"
[^src-4]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.3" -- "Long-term temporal narratives are induced in the conversation by additionally conditioning the agent's response on the subset of events in G that occur between the last and current session"
[^src-5]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Appendix Section A.2" -- "Jack aspires to be a hotel manager. Consequently, he enrolls in a hotel management course in July, and after three months, he expresses his excitement about the course on social media"
