---
id: comparison-detection-blind-spot-under-entrenchment
title: 一致性检测在范式固化下的结构性盲区
status: accepted
card_type: distinction
tags: [drift, detection, entrenchment, blind-spot, paradigm-consistency]
created_time: 2026-06-05T18:00:00+08:00
edited_time: 2026-06-05T18:00:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide, arxiv-memory-as-metabolism]
justification: ../justification/comparison-detection-blind-spot-under-entrenchment.md
canonical_concept: detection-blind-spot-under-entrenchment
aliases: [检测盲区, detection blind spot, 范式一致性伪装, paradigm consistency masking]
summary: >-
  detection-blind-spot-under-entrenchment（检测盲区 / 范式一致性伪装）描述持续偏移检测与
  用户耦合固化之间的结构性张力：不一致检测对事实层偏移有效，但当知识库在错误范式内达成
  虚假内部一致性时，检测机制恰恰因"一切一致"而失灵——最危险的漂移形式对最常用的检测手段不可见
related: [continuous-drift-detection, entrenchment-under-user-coupled-drift]
---

持续偏移检测[^card-1]与用户耦合漂移下的固化[^card-2]之间存在一个重要的结构性张力，值得作为独立概念捕捉。

**检测的假设**：持续偏移检测机制——无论是个人 LLM Wiki 的按需巡检还是企业级的后台循环——都建立在一个隐含假设之上：偏移表现为可检测的**事实不一致**。系统通过比对来源之间、文档之间、或文档与代码之间的矛盾来发现问题。

**固化的特征**：然而，用户耦合漂移下的固化恰恰打破了这一假设。固化的知识库不是充满矛盾的——相反，它在错误范式内达成了**虚假的内部一致性**。主导解释获得保护，矛盾证据被边缘化或重新解释以适配现有框架，系统从表面上看"一切一致"。

**盲区的结构**：这意味着最危险的漂移形式——范式层面的结构性偏差——恰恰对最常用的检测手段不可见。一致性检查在此场景下不仅无效，甚至可能产生**虚假安全感**：检测报告"无不一致发现"，运维团队据此认为知识库健康，而实际上系统已深度偏离真实。

**设计含义**：弥合这一盲区可能需要超越一致性检查的机制——例如伴侣记忆框架提出的少数压力提升（minority pressure promotion）、审计压力测试（audit stress test）等主动对抗固化的治理机制，或定期的外部锚点回溯验证。

## Footnotes

[^card-1]: [持续偏移检测](continuous-drift-detection.md) -- 该卡描述企业级自动化不一致检测机制，本卡分析其在范式固化场景下的结构性盲区
[^card-2]: [用户耦合漂移下的固化](entrenchment-under-user-coupled-drift.md) -- 该卡描述固化如何产生虚假内部一致性，本卡将此与检测机制的假设对照揭示盲区
