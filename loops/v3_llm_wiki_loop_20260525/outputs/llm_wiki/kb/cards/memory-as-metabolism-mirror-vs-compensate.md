---
id: memory-as-metabolism-mirror-vs-compensate
title: 伴侣记忆的"镜像-补偿"设计原则
status: accepted
card_type: operational_rule
tags: [#memory, #companion-system, #design-principle, #governance]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T11:16:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
provenance_card: ../provenance/memory-as-metabolism-mirror-vs-compensate.md
aliases: [Mirror-vs-Compensate, 操作维度对齐与认知失效补偿, companion governance principle]
related: [memory-as-metabolism-five-operations, memory-gravity-load-bearing-protection, minority-pressure-promotion, memory-as-metabolism-conflict-routing-matrix, memory-as-metabolism-architectural-separability, audit-by-suspension-against-entrenchment]
---

## 核心主张

Miteski (2026) 提出，针对单用户的"伴侣型"个人 LLM 记忆系统，应当按维度差异化处理与用户对齐 vs 反对齐：

- **操作维度（Operational）做镜像（Mirror）**：用户当前的工作上下文、依赖结构、自我指称连续性、词汇与框架。这些维度上，"与用户一致"是设计目标，偏离是失败模式。一个拒绝继承用户词汇的伴侣是不可用的。
- **认知失效维度（Epistemic failure）做补偿（Compensate）**：高引力（gravity）条目的固化、对相反证据的压制、单一文化（monoculture）的收敛。这些维度上，"与用户一致"反而是失败模式，偏离才是设计目标。一个把用户每个确认偏误都继承下来的伴侣是有害的。

这不是哲学命题，而是**工具性选择规则**：mirror-vs-compensate is "instrumental, not philosophical"。

## 时间结构化的程序冲突规则

当 mirror 与 compensate 在同一事件上指向相反方向时，框架按时间窗口分发：

1. **流式路径（TRIAGE）默认镜像**：单条矛盾不实时覆盖高引力条目，避免在毫秒级破坏用户的操作连续性。
2. **调度的整合窗口（CONSOLIDATE）做补偿**：批量整合时对积累的矛盾施加更高摩擦，让"少数派 buffer 压力"有结构化机会改写主导解释。
3. **AUDIT 作为决胜者**：当受引力保护的条目在多轮 AUDIT 中持续与坏结果相关时，强制走 §5.8 的引力削减通路，剥离其保护。

这是 v3 论文宣称的核心新贡献——不是 mirror/compensate 词汇本身（Qian 等 arXiv:2510.01924 已用），不是 sleep-time consolidation 机制本身（LightMem、SleepGate 已实现），而是**"时间结构化的程序冲突规则作为单用户 companion 衬底的绑定"**。

## 五操作的角色分配

| 操作 | 镜像/补偿 | 角色 |
| --- | --- | --- |
| TRIAGE | 镜像（中立采集） | 浅层流式过滤 |
| DECAY | 镜像（运营连续性） | 活动 wiki 上的生存权重保留 |
| CONTEXTUALIZE | **补偿**（选择性吸收） | 把外部源压缩到用户当前 working depth |
| CONSOLIDATE | **补偿**（中心机制） | 批量深度整合、buffer-to-wiki |
| AUDIT | **补偿** | 高引力条目的结构性压力测试 |
| Memory gravity | 镜像 | 承重保护 |
| Minority-hypothesis retention | **补偿** | buffer/quarantine 中的方差保留 |

## 边界与诚实之处

- **不是真理追踪器**：框架不主张能取代外部真理判断，论文反复强调"truth re-enters through consequence, not through correspondence"。
- **承认部分性的安全故事**：mirror 一侧的对齐被作为"伴侣可用性"的代价显式接受；compensate 一侧仅在三个时间尺度（agent 内 consolidation、跨 agent federation、底模演化）上提供结构性防御，而非保证。
- **AUDIT 灵敏度是开放问题**：若 stress-test 查询集自我确认或过窄，固化仍可幸存（§9 limitation）。

## References

- 论文正文 §1.2 "Mirror where mirroring serves utility. Compensate where mirroring damages it." 第 283–344 行附近。
- §5.0 "Mapping operations to mirror and compensate" 表格，第 1037–1067 行。
- 来源：`data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt`。

## Footnotes

[^1]: 原文（agent_source_bundle.txt 第 309–311 行）："Qian et al. (arXiv:2510.01924) uses it explicitly in 'To Mask or to Mirror' — empirically observing that some models mirror human biases while others mask and compensate for them at inference time."

[^2]: 原文（第 322–327 行）："The contribution is the TRIAGE → CONSOLIDATE → AUDIT execution model as a binding: not the discovery of the tension, and not the individual operations, but the procedural rule that decides how and when each operation applies to the mirror-vs-compensate conflict in a companion wiki."

[^3]: 原文（第 346–360 行）："The framework defaults to preserving operational continuity in the streaming path and routing the conflict to scheduled compensate operations ... mirror by default under time pressure, compensate during scheduled integration windows, and treat AUDIT as the tiebreaker."
