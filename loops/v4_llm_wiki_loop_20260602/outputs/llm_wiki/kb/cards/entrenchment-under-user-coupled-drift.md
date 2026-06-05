---
id: entrenchment-under-user-coupled-drift
title: 用户耦合漂移下的固化
status: accepted
card_type: concept
tags: [companion-memory, failure-mode, drift, entrenchment, kuhnian, ossification]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/entrenchment-under-user-coupled-drift.md
canonical_concept: entrenchment-under-user-coupled-drift
aliases: [用户耦合漂移固化, entrenchment under drift, 用户耦合保留漂移, user-coupled retention drift, 库恩式僵化, Kuhnian ossification, 范式维护系统]
summary: >-
  entrenchment-under-user-coupled-drift（用户耦合漂移固化 / user-coupled retention drift / Kuhnian ossification）是伴侣记忆框架针对的核心失败模式：个人 LLM wiki 随时间使主导解释越来越受保护、新矛盾证据越来越容易被驳回，知识库从活的知识基础变成范式维护系统；这是库恩正常科学的记忆层类比
related: [audit-stress-test, circularity-as-thesis, companion-knowledge-system, continuous-drift-detection, minority-pressure-promotion, source-faithfulness-risk]
---

用户耦合漂移下的固化是伴侣记忆框架识别和针对的特定失败模式[^src-1]。

**漂移的描述性事实**：基于增量 wiki 编译的个人 LLM 记忆系统已经展现出用户耦合的保留动态——Karpathy 的 LLM Wiki 通过整合用户认为值得整合的内容来增长，MemPalace 保留用户使用模式强化的内容，LLM Wiki v2 衰减用户不再回访的内容。这些系统都不是中性的知识基础设施，每个都是有立场的和个性化的[^src-2]。

**固化的结构**：随时间推移，主导解释获得更多保护，较新的矛盾证据更容易被驳回，原本是活的知识基础变成了**范式维护系统**——在现有结构内保持一致性，直到异常积累到足以迫使转变[^src-3]。这是正常科学，而非革命。

**库恩式类比**：范式自我强化恰恰是因为它组织了新证据的解释方式，异常被路由到外围作为例外、测量误差或"未来工作的开放问题"[^src-4]。

**与一般认知偏差的区别**：这不是一般的确认偏差问题，而是一个特定于**中心性保护的在位条目**的结构性失败模式——高引力条目因太多东西建立在其上而受保护，即使它是错的[^src-5]。

**框架的设计提问**：问题不是"如何防止漂移"，而是"如何在漂移发生时产出性地镜像、智能地补偿"[^src-6]。

循环性论题在哲学层面回应了固化批评：一致性的自密封性在伴侣框架下是拥有稳定自我的样子，而非缺陷——但本卡描述的正是该立场的失败边界[^dist-2]。框架的两个核心补偿机制分别从不同方向抵抗固化：AUDIT 通过经验性悬挂检测死权重和主动干扰条目（减法策略）[^card-2]，少数派压力提升通过跨周期积累异质证据挑战引力保护的在位条目（加法策略）[^card-3]。

源忠实性风险卡描述了一个互补的技术层面问题：多轮有损变换导致 wiki 内容偏离原始来源[^card-1]。值得注意的是，持续偏移检测机制假定偏移表现为可检测的事实不一致——但固化的核心特征恰恰是系统在错误范式内保持了内部一致性，使不一致检查失效[^dist-1]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Abstract" -- "testable conformance invariants for the specific failure mode of entrenchment under user-coupled drift in single-user knowledge wikis"
[^src-2]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 1.1" -- "None of these systems is a neutral knowledge infrastructure. Each is position-ful and personalized, even when its documentation does not say so."
[^src-3]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Abstract" -- "Over time the dominant interpretation gets more protected, newer contradicting evidence gets more easily dismissed, and what started as a living knowledge base turns into a paradigm maintenance system"
[^src-4]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.8" -- "a paradigm becomes self-reinforcing precisely because it organizes how new evidence is interpreted, and anomalies... are routed to the periphery as exceptions, measurement errors, or open problems"
[^src-5]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.6" -- "A false entry that became load-bearing before it was recognized as false is more protected, not less."
[^src-6]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 3" -- "the design question is not 'how do we prevent drift' but 'how do we mirror productively and compensate intelligently while the drift happens.'"
[^card-1]: [源忠实性风险与不可变锚点](source-faithfulness-risk.md) -- 本卡聚焦用户耦合的结构性范式固化，该卡聚焦多轮技术变换导致的内容偏离
[^dist-1]: [持续偏移检测](continuous-drift-detection.md) -- 本卡主张固化使知识库在错误范式内保持虚假的内部一致性，该卡主张自动化不一致检测可发现偏移，区分点在于：当偏移表现为事实层不一致时检测有效，但当固化产生范式层虚假一致性时检测机制失灵
[^dist-2]: [循环性作为论题](circularity-as-thesis.md) -- 本卡主张自密封一致性导致病理性范式僵化，该卡主张同一动态是稳定自我的特征，区分点在于：框架对循环性取「镜像侧接受 + 补偿侧抵抗」的立场，而本卡描述的是补偿侧失败时的退化结果
[^card-2]: [AUDIT 结构性压力测试](audit-stress-test.md) -- 本卡描述固化的失败模式，该卡提供减法补偿机制：通过悬挂高引力条目检测死权重和主动干扰
[^card-3]: [少数派压力提升机制](minority-pressure-promotion.md) -- 本卡描述固化的失败模式，该卡提供加法补偿机制：通过跨周期缓冲区压力积累挑战引力保护的在位者
