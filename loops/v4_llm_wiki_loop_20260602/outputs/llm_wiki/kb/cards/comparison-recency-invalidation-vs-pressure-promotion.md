---
id: comparison-recency-invalidation-vs-pressure-promotion
title: 即时新优先失效 vs 多周期压力积累提升
status: accepted
card_type: distinction
tags: [contradiction_handling, temporal_resolution, belief_revision, knowledge_graph, companion_memory, design_tradeoff]
created_time: 2026-06-05T22:00:00+08:00
edited_time: 2026-06-05T22:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep, arxiv-memory-as-metabolism]
justification: ../justification/comparison-recency-invalidation-vs-pressure-promotion.md
canonical_concept: comparison-recency-invalidation-vs-pressure-promotion
aliases: [即时失效 vs 压力积累, recency invalidation vs pressure promotion, 新信息优先 vs 少数派提升]
summary: >-
  comparison-recency-invalidation-vs-pressure-promotion（即时新优先失效 vs 多周期压力积累提升）
  同为"检测到矛盾后如何解决"的机制方案。Graphiti 的边失效机制采用即时新优先策略（单条新边即可失效旧边，沿事务时间线始终优先新信息），
  伴侣记忆框架的少数派压力提升机制采用多周期证据积累策略（单条矛盾视为噪声，需跨周期积累互相支持的证据才能挑战主导解释）。
  核心区分点在于矛盾解决的时间模型与证据门槛
related: [contradiction-as-asset, contradiction-state-machine, edge-invalidation-mechanism, minority-pressure-promotion]
---

「检测到知识矛盾后应如何解决」是持久化知识系统的核心设计问题。Graphiti 和伴侣记忆框架给出了两种时间模型截然不同的机制方案，反映了对「什么构成充分证据」的根本性分歧。

**Graphiti：即时新优先失效**[^card-1]——当新边（fact）与已有边产生矛盾时，系统沿事务时间线 T' 始终优先采纳新信息，将旧边的 t_invalid 设为新边的 t_valid。单条新信息即可触发失效。旧边不被删除但被标记为失效，实质上退出活跃知识集。隐含假设：**最新信息最可能正确**。

**伴侣记忆框架：多周期压力积累提升**[^card-2]——单条与主导解释矛盾的条目被视为噪声而非信号，仅存储在缓冲区和隔离区。只有当多条互相支持的矛盾条目跨多个整合周期积累了足够的缓冲区压力后，才会被标记为主导解释的候选更新。隐含假设：**多来源汇聚的证据才构成信号**。

| 维度 | Graphiti 边失效 | 伴侣记忆压力提升 |
|------|----------------|-----------------|
| 触发门槛 | 单条新边即可 | 多条互相支持的条目跨周期积累 |
| 时间模型 | 即时解决 | 多周期渐进 |
| 对噪声的鲁棒性 | 低（单条错误信息可失效正确知识） | 高（单条噪声被隔离，不影响主导解释） |
| 对时效性的响应 | 高（新信息立即生效） | 低（需等待积累周期） |
| 失败模式 | 错误的新信息覆盖正确的旧知识 | 相关噪声批量积累放大错误修正 |

这一区分揭示了知识系统设计中的一个基本张力：**时效性与鲁棒性的权衡**。即时失效在信息流可靠时表现最优（如事实性数据的时序更新），而压力积累在信息流含噪时更安全（如观点性知识的信念修订）。两种策略适用于不同的知识类型和噪声特征。

## Footnotes

[^card-1]: [边失效与动态知识更新机制](edge-invalidation-mechanism.md) -- Graphiti 的即时新优先策略：通过 LLM 比较新边与已有边，发现矛盾时将旧边 t_invalid 设为新边 t_valid
[^card-2]: [少数派压力提升机制](minority-pressure-promotion.md) -- 伴侣记忆框架的多周期积累策略：少数派假设在缓冲区跨周期积累互相支持的证据，达到阈值后挑战主导解释
