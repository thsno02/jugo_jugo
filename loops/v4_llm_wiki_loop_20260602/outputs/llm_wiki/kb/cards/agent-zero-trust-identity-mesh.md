---
id: agent-zero-trust-identity-mesh
title: Agent 零信任身份与信任网格
status: accepted
card_type: concept
tags: [zero-trust, identity, agent-mesh, trust, agent-governance, multi-agent]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [microsoft-agent-governance-toolkit-docs]
justification: ../justification/agent-zero-trust-identity-mesh.md
canonical_concept: agent-zero-trust-identity-mesh
aliases: [agent零信任身份, zero-trust agent identity, agent信任网格, AgentMesh trust mesh]
summary: >-
  agent-zero-trust-identity-mesh（agent零信任身份 / zero-trust agent identity / agent信任网格）
  Microsoft Agent Governance Toolkit 将零信任身份列为 agent 运行时治理四大支柱之一，通过 AgentMesh 实现
  agent 发现、路由和信任网格，配以 135 项合规测试的形式规范，确保多 agent 系统中每个 agent 的身份可验证、信任可计算
related: [deterministic-policy-enforcement, agent-governance-modular-packages, spec-driven-conformance-testing]
---

Microsoft Agent Governance Toolkit 将"零信任身份"（zero-trust identity）列为 agent 运行时治理的四大支柱之一，与确定性策略执行、执行沙箱、SRE 并列 [^src-1]。

零信任身份在工具包中通过 **AgentMesh** 模块落地，提供三项核心能力：agent 发现（discovery）、路由（routing）和信任网格（trust mesh）[^src-2]。其设计理念是：在多 agent 系统中，任何 agent 默认不被信任——每次交互都需要验证身份、评估信任等级，而非依赖网络边界或预设白名单。

该模块的正确性由"AgentMesh Identity and Trust"形式规范保障，配有 135 项合规测试 [^src-3]。此外还有"AgentMesh Trust and Coordination"规范（62 项测试）覆盖协调层面的信任 [^src-3]。两份规范合计 197 项测试，在所有组件中测试密度最高，反映了信任基础设施在治理体系中的关键地位。

零信任的具体应用可在示例项目中看到：`mcp-trust-verified-server` 展示了如何为 MCP 服务器实现信任验证 [^src-4]，`openai-agents-governed` 则展示了基于信任层级（trust tiers）的策略门禁工具调用 [^src-4]。

零信任身份与确定性策略执行形成互补 [^card-1]：身份层回答"这个 agent 是谁、可信度如何"，策略层回答"这个操作是否被允许"。两者共同构成 agent 治理的认证-授权闭环。

## Footnotes

[^src-1]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- L2 -- "Runtime governance for AI agents: deterministic policy enforcement, zero-trust identity, execution sandboxing, and SRE for autonomous agents."
[^src-2]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- L8 -- "🔗 Agent Mesh Agent discovery, routing, and trust mesh"
[^src-3]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- L32-34 -- "AgentMesh Identity and Trust 135 ... AgentMesh Trust and Coordination 62"
[^src-4]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- L22-26 -- "openai-agents-governed OpenAI Agents SDK Policy-gated tool calls with trust tiers ... mcp-trust-verified-server MCP Trust-verified MCP server implementation"
[^card-1]: [确定性策略执行](deterministic-policy-enforcement.md) -- 本卡聚焦身份验证与信任计算（"是谁、可信度如何"），该卡聚焦策略评估与执行（"是否被允许"）；两者构成 agent 治理的认证-授权闭环
