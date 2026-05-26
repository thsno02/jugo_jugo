---
id: microsoft-agent-governance-eight-packages
title: 微软 Agent Governance Toolkit 用八个包切分智能体治理面
status: draft
card_type: concept
tags: [#agent-governance, #microsoft, #policy-engine, #runtime]
created_time: 2026-05-26T11:40:00+08:00
edited_time: 2026-05-26T11:40:00+08:00
edited_entity: llm
source_ids: [microsoft-agent-governance-toolkit-docs]
provenance_card: ../provenance/microsoft-agent-governance-eight-packages.md
aliases: [Agent Governance Toolkit, Microsoft Agent OS, agent runtime sandboxing rings]
related: [microsoft-agent-governance-standards-alignment, owasp-agentic-top10-2026-positioning, owasp-agentic-vs-llm-top10-2025, nist-ai-rmf-gai-profile, etamp-environment-injected-memory-poisoning, poisonedrag-knowledge-database-attack-surface]
---

微软 `agent-governance-toolkit` 把"如何在生产环境里治理一群自主智能体"拆成 8 个独立但同名前缀的包，每个包负责一个明确职责。这种"按运行时关心点切分"的做法本身就是值得收藏的设计选择——它让安全/合规、调度、可靠性、生态等问题不必塞在同一个"agent framework"里。

八包速览（按文档原文）：

| 包 | 关心的问题 |
| --- | --- |
| Agent OS | 策略引擎（policy engine）、agent 生命周期、治理网关 |
| Agent Mesh | agent 发现、路由、信任网络 |
| Agent Runtime | 执行沙箱，含**四个权限环（four privilege rings）** |
| Agent SRE | kill switch、SLO 监控、chaos testing |
| Agent Compliance | OWASP 验证、policy linting、完整性检查 |
| Agent Marketplace | 插件治理 + trust scoring |
| Agent Lightning | RL 训练治理，含违规惩罚 |
| Agent Hypervisor | 执行审计、delta engine、commitment anchoring |

要点：

- **policy 是 first-class 概念，不是 framework 的附属**：Agent OS 把"策略引擎 + 治理网关"作为最底层包，其他包都向它申报；策略以 OPA / Rego / Cedar 表达（见侧边栏 "Policy & Authorization" 章）。
- **运行时安全用"环"而不是单一沙箱**：Agent Runtime 用 "four privilege rings" 把工具调用按权限分级（对应 ADR-0002）——这是把 OS 的 ring 模型搬到 agent 层的具体例子。
- **可观测性与责任审计被单独抽出**：Agent Hypervisor 负责"事后能复现决策"——文档里 ADR-0017 用 Merkle audit chain、ADR-0018 用 reconstructible Decision BOM、ADR-0019 用 OTel event sink；这意味着 audit trail 不是日志拼出来的，而是结构化的可重放证据。
- **生态侧用 trust scoring 而不是审核制**：Agent Marketplace 引入 plugin trust score，这是 plugin marketplace 不直接审查每个插件、而是用可量化的信任分数加门控的工程取舍。

整体观察：这是把"agent 框架"层（LangChain / CrewAI / AutoGen / Microsoft Agent Framework / OpenAI Agents / LlamaIndex / Haystack / Mastra / MCP / A2A 等）和"治理面"层强行分开的 toolkit——它声明对任何框架都能挂上（"Works with any agent framework"[^1]），并通过 "Framework Adapter Contract" 这个规范保证适配的一致性。

边界 / 限制：

- 文档本身是导航页，每个包的具体合同（spec）需要进到对应的 RFC 2119 specification 才能拿到准确的接口语义；
- "Agent Hypervisor"、"Agent Lightning"、"Agent Mesh" 命名易与传统虚拟化/RL/服务网格混淆，但语义全部偏向 agent 治理。

## References

- 微软文档站首页（material `microsoft-agent-governance-toolkit-docs`）的 "Packages" 章节与左侧导航树，列出八个包及其一句话职责；同页 "Specifications" 给出对应规范的 RFC 2119 测试数；ADR 列表给出运行时环、Merkle 链等具体设计决定。

## Footnotes

[^1]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` 第 383 行：
    > "Works with any agent framework: LangChain, CrewAI, AutoGen, Google ADK, OpenAI Agents, LlamaIndex, Haystack, Mastra, MCP, A2A, and more."
[^2]: 同文件第 365 行（八个包的并列描述）：
    > "⚙️ Agent OS Policy engine, agent lifecycle, governance gate 🔗 Agent Mesh Agent discovery, routing, and trust mesh 🛡️ Agent Runtime Execution sandboxing with four privilege rings 📊 Agent SRE Kill switch, SLO monitoring, chaos testing ✅ Agent Compliance OWASP verification, policy linting, integrity checks 🏪 Agent Marketplace Plugin governance and trust scoring ⚡ Agent Lightning RL training governance with violation penalties 🔒 Agent Hypervisor Execution audit, delta engine, commitment anchoring"
