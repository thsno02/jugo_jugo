---
id: microsoft-agent-governance-standards-alignment
title: Agent Governance Toolkit 把四份外部合规标准做成可自动核验项
status: draft
card_type: source_claim
tags: [#compliance, #agent-governance, #owasp, #nist, #eu-ai-act, #soc2]
created_time: 2026-05-26T11:45:00+08:00
edited_time: 2026-05-26T11:45:00+08:00
edited_entity: llm
source_ids: [microsoft-agent-governance-toolkit-docs]
provenance_card: ../provenance/microsoft-agent-governance-standards-alignment.md
aliases: [OWASP Agentic AI Top 10, NIST AI RMF, EU AI Act, SOC 2 agent governance]
related: [microsoft-agent-governance-eight-packages, owasp-agentic-top10-2026-positioning, nist-ai-rmf-gai-profile, owasp-agentic-vs-llm-top10-2025, owasp-llm-top10-community-genealogy]
---

微软 `agent-governance-toolkit` 在首页声明对齐了四份独立的外部标准，并把它们做成 toolkit 内可以**自动**核验或导出证据的项。这一节通常会被读者一扫而过，但实际值得记住——它把"agent 合规"从一个开放问题降级为一组可机器检查的约束。

四个对齐（原文）：

| 标准 | toolkit 声称的覆盖方式 |
| --- | --- |
| **OWASP Agentic AI Top 10** | "All 10 risks covered with deterministic controls"——10 个风险条目全部对应**确定性**控制（不是建议，而是策略） |
| **NIST AI RMF 1.0** | "Full GOVERN, MAP, MEASURE, MANAGE alignment"——四个一级功能全部覆盖 |
| **EU AI Act** | "Compliance mapping with automated evidence"——映射 + 自动化证据导出 |
| **SOC 2** | "Control mapping with audit trail export"——控制点映射 + 审计轨迹导出 |

值得标注的设计选择：

- **OWASP Top 10 用确定性控制**：传统应用安全 Top 10 经常以"指南/建议"形式落地；这里用 deterministic policy（OPA / Rego / Cedar，参见侧边栏 Policy & Authorization 章）意味着 risk → policy → enforcement 是闭环且可机器验证。
- **NIST AI RMF 四功能全覆盖**：GOVERN（治理）/ MAP（识别上下文）/ MEASURE（度量）/ MANAGE（管理）是 NIST 风险管理框架的一级功能，"Full alignment" 暗示 toolkit 在每个功能下都有对应的包/规范，而不是只对 GOVERN 做一层壳。
- **EU AI Act 与 SOC 2 都强调"自动证据 / 审计轨迹导出"**：这跟 Agent Compliance 包的 "OWASP verification, policy linting, integrity checks" 以及 Agent Hypervisor 的 "execution audit" 是同一条线——证据不是事后人工补写的报告，而是运行时结构化产物（ADR-0017 Merkle audit chain、ADR-0018 reconstructible Decision BOM）。

含义：

- 如果你在做 agent 系统的合规架构，可以直接把 Agent Compliance 包 + Agent Hypervisor 当作"标准→证据"映射层，不必从零设计自己的审计链。
- 反之，如果你的 agent 框架没把"audit trail 导出"做成 first-class 产物（而是依赖应用层日志），上述四个标准里至少 EU AI Act 和 SOC 2 会很难合规。

## References

- 微软文档站首页 "Standards Compliance" 章（material `microsoft-agent-governance-toolkit-docs`，第 427–437 行），列出四份外部标准对齐方式；与左侧导航 "Agent Compliance" / "Audit & Compliance" / ADR-0017 / ADR-0018 / ADR-0019 一同构成证据闭环。

## Footnotes

[^1]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` 第 429–437 行：
    > "Standard Coverage / OWASP Agentic AI Top 10 All 10 risks covered with deterministic controls / NIST AI RMF 1.0 Full GOVERN, MAP, MEASURE, MANAGE alignment / EU AI Act Compliance mapping with automated evidence / SOC 2 Control mapping with audit trail export"
[^2]: 审计链相关 ADR（第 298–300 行）：
    > "ADR-0017: Merkle Audit Chain / ADR-0018: Reconstructible Decision BOM / ADR-0019: OTel Event Sink Pattern"
