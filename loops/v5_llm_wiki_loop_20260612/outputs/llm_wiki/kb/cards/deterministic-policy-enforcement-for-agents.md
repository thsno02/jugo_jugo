---
id: deterministic-policy-enforcement-for-agents
title: 代理系统的确定性策略执行
status: accepted
card_type: design-principle
tags:
- deterministic-policy
- governance
- agent-os
- owasp
- compliance
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- microsoft-agent-governance-toolkit-docs
evidence_basis: documentation
justification: ../justification/deterministic-policy-enforcement-for-agents.md
canonical_concept: deterministic-policy-enforcement-for-agents
aliases:
- deterministic policy enforcement
- 确定性策略执行
- deterministic controls
summary: 确定性策略执行(deterministic policy enforcement)是 Microsoft Agent Governance Toolkit
  的核心设计原则：策略判定结果可预测、可审计，不依赖概率性 AI 审查。Agent OS 作为策略引擎(policy engine)实现治理门(governance
  gate)，对代理生命周期中的操作做确定性拦截/放行。OWASP Agentic AI Top 10 全部 10 项风险以 deterministic controls
  覆盖，强调治理结果的可重现性。
related:
- microsoft-agent-governance-toolkit-overview
- agt-four-privilege-ring-execution-sandbox
---

确定性策略执行（deterministic policy enforcement）是 Microsoft Agent Governance Toolkit 的首要设计原则，在工具包介绍的第一句即被强调。[^src-1] [^card-1]

该原则意味着：给定相同的策略配置和代理操作输入，治理判定的结果始终一致、可预测——与基于 LLM 的概率性审查形成对比。这为审计追踪和合规报告提供了确定性基础。

实现该原则的核心模块是 Agent OS，它作为策略引擎（policy engine）管理代理生命周期，并通过治理门（governance gate）对代理操作做确定性拦截或放行。Agent Compliance 模块进一步提供 OWASP 验证和策略 linting，确保策略本身的正确性。[^src-1]

在合规层面，工具包声称以"deterministic controls"覆盖 OWASP Agentic AI Top 10 全部 10 项风险，强调治理结果的可重现性而非概率性缓解。[^src-2]

[^src-1]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- "Agent Governance Toolkit" P1 -- "Runtime governance for AI agents: deterministic policy enforcement, zero-trust identity, execution sandboxing, and SRE for autonomous agents."
[^src-2]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- "Standards Compliance" P1 -- "OWASP Agentic AI Top 10 | All 10 risks covered with deterministic controls"
[^card-1]: 见卡片 [[microsoft-agent-governance-toolkit-overview]] 了解工具包整体架构
