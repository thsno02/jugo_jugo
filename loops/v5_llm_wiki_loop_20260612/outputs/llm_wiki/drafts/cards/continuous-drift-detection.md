---
id: continuous-drift-detection
title: 持续漂移检测机制
status: draft
card_type: mechanism
tags: [drift-detection, health-check, staleness, automation, enterprise-knowledge]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
evidence_basis: practitioner_report
justification: ../justification/continuous-drift-detection.md
canonical_concept: continuous-drift-detection
aliases: [drift detection, 漂移检测, continuous health check, 持续健康检查]
summary: >-
  企业 LLM wiki 将 Karpathy 的按需健康检查升级为持续自动漂移检测；当新 PR 与 runbook 矛盾时系统检测冲突并草拟更新路由给 document owner 审批；检测节奏为周检而非季度审计以匹配企业变更速率；LLM 执行与 Karpathy vault 相同的一致性检查但自动化运行
related: [enterprise-llm-wiki-architecture, personal-to-enterprise-scaling-barriers, context-rot-vs-compounding]
---

材料将 Karpathy 的按需健康检查（on-demand health check）升级为企业场景的**持续漂移检测**（continuous drift detection）。[^card-1]

**运行模式**：漂移检测作为后台循环运行，而非由人触发。LLM 执行与 Karpathy 在其 vault 上运行的相同类型的一致性检查，但节奏匹配企业变更速率——周检（weekly review）而非季度审计（quarterly audit）。[^src-1]

**冲突处理流程**：当新 PR 与 runbook 矛盾时，系统需要检测该矛盾、草拟更新、并路由给文档 owner 审批。这要求系统理解文档所有权（ownership）和路由逻辑——Karpathy 的 vault 只需将矛盾呈现给他本人。[^src-2]

**失败后果**：Anthropic 工程团队将 context 描述为 AI agent 最稀缺的资源——agent 需要即时访问当前、准确的上下文才能可靠执行真实工作。一年未做健康检查的知识图谱是 agent 最糟糕的输入。[^src-3]

[^card-1]: 参见 [[personal-to-enterprise-scaling-barriers]] Stay current 维度的障碍分析
[^src-1]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "What an enterprise LLM wiki has to do differently" P40 -- "It runs as a background loop, surfacing flagged content on a schedule the team can act on (weekly review rather than quarterly audit)"
[^src-2]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "What an enterprise LLM wiki has to do differently" P39 -- "the system needs to detect the contradiction, draft an update, and route it to the document owner for review"
[^src-3]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Stay current: health checks need to run automatically" P34 -- "Anthropic's engineering team frames context as the scarcest resource for AI agents"
