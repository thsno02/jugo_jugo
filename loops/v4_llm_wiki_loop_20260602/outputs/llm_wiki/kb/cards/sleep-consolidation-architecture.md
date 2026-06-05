---
id: sleep-consolidation-architecture
title: 睡眠整合架构
status: accepted
card_type: mechanism
tags: [companion-memory, consolidation, buffer, sleep-function, anti-self-sealing, dream-cycle]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/sleep-consolidation-architecture.md
canonical_concept: sleep-consolidation-architecture
aliases: [睡眠整合架构, sleep consolidation architecture, 原始缓冲区+批量整合, raw buffer consolidation, dream cycle, 梦周期]
summary: >-
  sleep-consolidation-architecture（睡眠整合架构 / raw buffer consolidation / dream cycle）将摄取与整合分离：原始缓冲区接受浅层 TRIAGE 过滤的条目，活跃 wiki 仅在定期 CONSOLIDATE 周期中修改；核心理由是流式一致性判断是自密封的——单条矛盾条目会被立即隔离，使主导解释永远不更新
related: [companion-knowledge-system, contextualize-depth-fitted-compression, locomo-reflect-respond-architecture, minority-pressure-promotion, sleep-time-memory-consolidation, triage-shallow-filter]
---

睡眠整合架构是伴侣知识系统的核心结构设计，将摄取（ingestion）与整合（integration）分离为两个不同的时间路径[^src-1]。

**架构**：原始缓冲区通过浅层 TRIAGE 过滤器以流式方式接受条目。深度一致性工作——分类、矛盾解决、与活跃 wiki 的整合、少数派立场的提升——在定期 CONSOLIDATE 操作中批量运行（每晚、每周或事件驱动）[^src-2]。

**为什么要分离**：流式一致性判断是自密封的（self-sealing）。一个单独到达的条目如果与主导 wiki 矛盾，在评分时会被立即隔离，这意味着主导解释永远不会更新[^src-3]。批量整合打破了这个锁定：多个缓冲区条目不仅互相评分，也对 wiki 评分。三个互相支持的条目与一个高引力 wiki 条目对比，是与一条孤立矛盾完全不同的信号[^src-4]。

**认知科学基础**：该模式直接借鉴自 Tononi 的突触稳态假说和 McClelland 的互补学习系统——情节性经验在清醒时段积累在快速学习缓冲区中，深度整合工作（一致性检查、矛盾解决、向长期稳定结构的转移）在睡眠期间离线完成[^src-5]。

**CONSOLIDATE 的四个阶段**[^src-6]：
1. 缓冲区内部评分——发现积累的少数派压力
2. Wiki 评分——检测与高引力节点的矛盾成本
3. 分类和路由——使用梯形隶属函数的模糊一致性梯度
4. 少数派压力提升——互相支持的矛盾条目作为候选更新而非隔离

**实现约束**：两调度器架构是合规级别的承诺——热路径调度器处理 TRIAGE 和检索读取（在对话延迟预算内），睡眠周期调度器处理 DECAY、CONSOLIDATE、AUDIT 作为后台任务[^src-7]。LightMem 独立提出了类似的离线巩固机制（sleep-time update），但侧重工程效率（token 降低 106x）而非治理语义[^card-1]。CONTEXTUALIZE 作为同一框架中的第五个操作，在梦周期内执行外部来源的深度适配压缩[^card-2]。LoCoMo 的反思-回应架构则以会话边界为单位进行递增式记忆整合，与本卡的批量整合构成不同粒度的离线处理策略[^card-3]。

## Footnotes

[^card-1]: [睡眠期离线记忆巩固机制](sleep-time-memory-consolidation.md) -- 两个不同来源独立收敛于"离线批量整合"架构：伴侣记忆框架出于反自密封的治理理由，LightMem 出于推理效率的工程理由
[^card-2]: [CONTEXTUALIZE 深度适配压缩](contextualize-depth-fitted-compression.md) -- 本卡描述摄取-整合分离的整体架构，该卡描述梦周期内执行的第五个操作——将外部来源压缩到用户当前工作上下文深度
[^card-3]: [LoCoMo 反思-回应双层记忆代理架构](locomo-reflect-respond-architecture.md) -- 本卡的批量 CONSOLIDATE 在定期梦周期中整合缓冲区，该卡的反思-回应在每个会话边界递增式生成摘要和观察；两者都实现离线记忆处理但粒度和动机不同

[^src-1]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.1" -- "The framework splits ingestion from integration. A raw buffer accepts entries as they arrive; the active wiki is modified only during scheduled consolidation cycles."
[^src-2]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.1" -- "Deep coherence work --- classification, contradiction resolution, integration with the active wiki, promotion of minority positions, flagging of gravity conflicts --- runs during a batched CONSOLIDATE operation on a scheduled rhythm"
[^src-3]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.1" -- "streaming coherence is self-sealing. A single entry arriving alone and scored against the dominant wiki gets quarantined immediately if it contradicts the dominant interpretation, which means the dominant interpretation never updates."
[^src-4]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.1" -- "three mutually-supporting entries against a high-gravity wiki entry is a different signal from one isolated contradiction"
[^src-5]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 2.3" -- "episodic experience accumulates in a fast-learning buffer during waking hours, and the deep integration work... happens offline during sleep"
[^src-6]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.5" -- "The operation has four phases: 1. Buffer-internal scoring... 2. Wiki scoring... 3. Classification and routing... 4. Minority-pressure promotion."
[^src-7]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 6.1" -- "The hot-path scheduler gates TRIAGE and retrieval reads... The sleep-cycle scheduler queues DECAY, CONSOLIDATE, and AUDIT as background jobs."
