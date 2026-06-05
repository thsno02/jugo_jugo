---
id: agent-governance-modular-packages
title: Agent 治理模块化分包架构
status: accepted
card_type: concept
tags: [governance, modular-architecture, agent-governance, separation-of-concerns]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [microsoft-agent-governance-toolkit-docs]
justification: ../justification/agent-governance-modular-packages.md
canonical_concept: agent-governance-modular-packages
aliases: [治理分包架构, agent governance packages, 治理模块化]
summary: >-
  agent-governance-modular-packages（治理分包架构 / agent governance packages / 治理模块化）
  Microsoft Agent Governance Toolkit 将 agent 治理分解为八个独立包——Agent OS（策略引擎）、Mesh（发现与信任）、
  Runtime（沙箱）、SRE（可靠性）、Compliance（合规）、Marketplace（插件治理）、Lightning（训练治理）、
  Hypervisor（执行审计），各包职责正交、独立可选
related: [agent-governance-standards-mapping]
---

Microsoft Agent Governance Toolkit 将 agent 治理关注点分解为八个独立的包（package），各有明确职责边界 [^src-1]：

1. **Agent OS** — 策略引擎（policy engine）、agent 生命周期管理、治理门禁（governance gate），是整个治理体系的核心运行时 [^src-2]。
2. **Agent Mesh** — agent 发现、路由和信任网格（trust mesh），处理多 agent 之间的身份与通信 [^src-2]。
3. **Agent Runtime** — 基于四层特权环（four privilege rings，ADR-0002）的执行沙箱 [^src-2][^src-3]。
4. **Agent SRE** — Kill switch、SLO 监控、混沌测试，将 SRE 实践引入 agent 运维 [^src-2]。
5. **Agent Compliance** — OWASP 验证、策略 lint、完整性检查 [^src-2]。
6. **Agent Marketplace** — 插件治理和信任评分 [^src-2]。
7. **Agent Lightning** — RL 训练治理，包含违规惩罚机制 [^src-2]。
8. **Agent Hypervisor** — 执行审计、delta 引擎、承诺锚定（commitment anchoring）[^src-2]。

这种分包模式使各治理能力可独立采纳、独立演进，组织可根据自身成熟度逐步引入（参见 Progressive Governance 教程 [^src-4]）。各模块产出的治理控制已被显式映射到 OWASP、NIST AI RMF、EU AI Act、SOC 2 等主流合规标准，实现从控制实施到合规证明的自动化闭环 [^card-1]。

## Footnotes

[^src-1]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L363 -- "Packages"
[^src-2]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L365-366 -- "Agent OS Policy engine, agent lifecycle, governance gate ... Agent Hypervisor Execution audit, delta engine, commitment anchoring"
[^src-3]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L268 -- "ADR-0002: Four Execution Rings"
[^src-4]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L92 -- "Progressive Governance"
[^card-1]: [Agent 治理标准合规映射](agent-governance-standards-mapping.md) -- 本卡聚焦治理架构的八个独立模块分包及其职责边界，该卡聚焦各模块控制如何映射到 OWASP/NIST/EU AI Act/SOC 2 合规标准
