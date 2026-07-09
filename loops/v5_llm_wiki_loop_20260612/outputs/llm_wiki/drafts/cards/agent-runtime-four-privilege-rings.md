---
id: agent-runtime-four-privilege-rings
title: 代理运行时四环特权模型
status: superseded
superseded_by: agt-four-privilege-ring-execution-sandbox
card_type: architecture-concept
tags: [agent-runtime, privilege-rings, sandboxing, execution-isolation, security]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [microsoft-agent-governance-toolkit-docs]
evidence_basis: documentation
justification: ../justification/agent-runtime-four-privilege-rings.md
canonical_concept: agent-runtime-four-privilege-rings
aliases: [Agent Runtime, four privilege rings, 四环特权模型, execution sandboxing, 执行沙箱]
summary: >-
  Agent Runtime 是 Microsoft Agent Governance Toolkit 的执行沙箱组件，采用四环特权模型(four privilege rings)对代理执行进行隔离。该设计借鉴操作系统特权环概念，将代理操作按权限层级分为四个环，实现分级执行控制。Agent Hypervisor 模块与之配合提供执行审计(execution audit)、增量引擎(delta engine)和承诺锚定(commitment anchoring)。
related: [microsoft-agent-governance-toolkit-overview, deterministic-policy-enforcement-for-agents]
---

Agent Runtime 是 Microsoft Agent Governance Toolkit 中负责执行沙箱的核心组件，其关键设计特征是采用四环特权模型（four privilege rings）。[^src-1] [^card-1]

该模型借鉴了传统操作系统的特权环（ring 0-3）架构理念，将代理的执行操作按权限层级分为四个环，实现分级执行控制和隔离。材料仅提及"four privilege rings"这一概念而未展开各环的具体定义，据此推测该模型可能将代理操作从最高特权（如系统级资源访问）到最低特权（如只读查询）分层管控。

与 Agent Runtime 紧密配合的是 Agent Hypervisor 模块，它提供执行审计（execution audit）、增量引擎（delta engine）和承诺锚定（commitment anchoring）三项能力，形成"沙箱执行 + 审计追踪"的双层安全保障。[^src-2]

Agent Runtime 拥有独立的正式规范——Agent Hypervisor Execution Control specification，配备 80 项合规测试，表明该组件的执行控制行为是形式化定义的。[^src-3]

[^src-1]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- "Packages" P1 -- "Agent Runtime Execution sandboxing with four privilege rings"
[^src-2]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- "Packages" P1 -- "Agent Hypervisor Execution audit, delta engine, commitment anchoring"
[^src-3]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- "Specifications" P1 -- "Agent Hypervisor Execution Control | 80"
[^card-1]: 见卡片 [[microsoft-agent-governance-toolkit-overview]] 了解工具包整体架构
