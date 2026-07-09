---
id: minority-hypothesis-retention
title: 少数假说保留机制
status: draft
card_type: mechanism-specification
tags: [minority-hypothesis, variance-preservation, buffer-pressure, belief-revision, companion-memory]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
evidence_basis: theoretical_paper
justification: ../justification/minority-hypothesis-retention.md
canonical_concept: minority-hypothesis-retention
aliases: [minority-hypothesis retention, minority-pressure promotion, variance preservation, 少数假说保留, 少数压力晋升, 方差保持]
summary: >-
  minority-hypothesis retention 少数假说保留是伴侣记忆框架的补偿机制，
  休眠替代方案以低存储成本保存在缓冲区和隔离区中，使下一个巩固周期有历史方差可评分。
  无此机制则少数立场必须在单一周期窗口内从零积累全部支持。有此机制则三个周期前开始
  积累缓冲区压力的少数立场可在当前周期完成积累。
  少数分支的生命周期：open -> promoted（集群越过晋升阈值）或 closed（AUDIT 确认incumbent 仍为负载承载
  且分支跨定义周期数未增长）。分支永远不被静默关闭。
  受控方差注入借鉴推荐系统和强化学习的标准模式，目标不同（认知方差 vs 参与方差）但机械操作相同。
related: [consolidate-operation, sleep-consolidation-architecture, memory-gravity-mechanism]
---

少数假说保留将休眠替代方案以低存储成本保存在缓冲区和隔离区中。它们被保存的目的不是为了自身，而是为了使下一个巩固周期有历史方差可对传入条目评分。[^src-1]

无此机制：少数立场必须在单一巩固周期窗口内从零积累全部支持。有此机制：三个周期前开始积累缓冲区压力的少数立场可在当前周期完成积累。[^src-2]

少数分支（minority branch）的生命周期状态：open -> promoted（集群在 CONSOLIDATE 周期中越过晋升阈值）或 closed（AUDIT 确认 incumbent 仍为负载承载且分支跨定义周期数未增长）。分支永远不被静默关闭——如果两个条件均未被明确评估和解决，分支保持开放。[^src-3]

关键区分：保留本身不是方差。浮现本身不是方差。只有对下游输出的可测量影响才是有效方差。这是框架预测4愿意被度量的内容。[^src-4]

受控方差注入是推荐系统和强化学习中的标准模式，论文将其应用于伴侣记忆但不声称记忆情况可还原为推荐情况——目标不同（认知方差 vs 参与方差），机械操作相同。[^src-5]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.7 Minority-hypothesis retention" P1 -- "Dormant alternatives are kept in the buffer and in quarantine at low storage cost. They are not stored for their own sake; they are stored so that the next consolidation cycle has something to score against incoming entries."
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.7" P1 -- "a minority position that started building buffer pressure three cycles ago can complete the accumulation in the current cycle"
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "4. System Model" -- "Minority branches...Branches close only via two explicit paths: promotion...or AUDIT-triggered archival...Branches are never closed silently"
[^src-4]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "7. Predictions" P4-end -- "Retention alone is not variance. Surfacing alone is not variance. Only influence on a downstream output is effective variance"
[^src-5]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.7" P2 -- "Controlled variance injection is a standard pattern in recommender systems and reinforcement learning."

[^card-1]: consolidate-operation — 少数压力晋升是 CONSOLIDATE 第四阶段的功能
[^card-2]: audit-operation — 少数分支关闭需 AUDIT 确认
