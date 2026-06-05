---
id: minority-pressure-promotion
title: 少数派压力提升机制
status: accepted
card_type: mechanism
tags: [companion-memory, minority-hypothesis, buffer-pressure, belief-revision, consolidation, anti-entrenchment]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/minority-pressure-promotion.md
canonical_concept: minority-pressure-promotion
aliases: [少数派压力提升, minority pressure promotion, 少数假设保留, minority-hypothesis retention, 缓冲区压力积累, buffer pressure accumulation, 多周期压力]
summary: >-
  minority-pressure-promotion（少数派压力提升 / minority-hypothesis retention / buffer pressure accumulation）是伴侣记忆框架中防止单一文化坍缩的补偿机制：少数派假设跨多个整合周期在缓冲区和隔离区保留，当积累的互相支持证据跨过提升阈值时可挑战引力保护的在位条目；这是论文最尖锐的可证伪预测（Prediction 4）
related: [sleep-consolidation-architecture, contradiction-as-asset, memory-gravity, entrenchment-under-user-coupled-drift]
---

少数派压力提升是伴侣记忆框架中的核心补偿机制，解决的问题是：在流式一致性过滤下，少数派假设被存储但永远不被整合[^src-1]。

**保留机制**：休眠替代方案以低存储成本保留在缓冲区和隔离区中，目的不是为了保留本身，而是让下一个整合周期有历史方差可以与新到条目对比评分[^src-2]。没有少数派假设保留，少数派立场必须在单个周期窗口内从零积累全部支持。有了它，三个周期前开始积累缓冲区压力的少数派立场可以在当前周期完成积累[^src-3]。

**提升过程**（CONSOLIDATE 第四阶段）：单独矛盾主导 wiki 但在缓冲区内互相支持的条目被标记为主导解释的候选更新，而非被隔离[^src-4]。单条矛盾被视为噪声，积累的矛盾被视为信号。

**Prediction 4——最尖锐的可证伪预测**：论文不仅声称少数派假设被存储或被呈现，而是声称它们可衡量地改变下游输出[^src-5]。代理指标是"重新浮现到影响率"——对于每个在整合周期中被提升的少数派条目，衡量系统对后续相关查询的响应是否与没有提升时不同。

**与现有基准的区别**[^src-6]：
- LongMemEval 的"知识更新"测试显式档案变更（用户声明城市已更改）
- TeaFarm 测试记忆是否改变输出（反事实存在/缺失）
- Prediction 4 针对结构性不同的失败模式：通过多周期缓冲区压力积累在中心性保护的在位者下实现信念修订

**已知风险**：批量整合也可能放大相关噪声而非真正的纠正——多个互相支持但错误的条目可能积累足够缓冲区压力来挑战正确的主导解释[^src-7]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.5" -- "Under streaming coherence filtering, a minority hypothesis is stored but never integrated."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.7" -- "Dormant alternatives are kept in the buffer and in quarantine at low storage cost. They are not stored for their own sake; they are stored so that the next consolidation cycle has something to score against incoming entries."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.7" -- "a minority position that started building buffer pressure three cycles ago can complete the accumulation in the current cycle"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.5" -- "Entries that contradict the active wiki individually but mutually support each other in the buffer are flagged as candidate updates to the dominant interpretation rather than quarantined."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 7" -- "The claim is not that minority hypotheses are stored, nor that they are surfaced, but that they measurably change downstream outputs at a non-trivial rate."
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 7" -- "Prediction 4 targets something structurally different: belief revision through multi-cycle buffer pressure accumulation under a centrality-protected incumbent"
[^src-7]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.5" -- "Batched consolidation can also amplify correlated noise rather than genuine correction."
