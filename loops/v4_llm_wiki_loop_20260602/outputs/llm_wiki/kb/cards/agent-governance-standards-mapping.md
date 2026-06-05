---
id: agent-governance-standards-mapping
title: Agent 治理标准合规映射
status: accepted
card_type: mechanism
tags: [governance, compliance, owasp, nist, eu-ai-act, soc2, standards]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [microsoft-agent-governance-toolkit-docs]
justification: ../justification/agent-governance-standards-mapping.md
canonical_concept: agent-governance-standards-mapping
aliases: [治理标准映射, compliance mapping, agent standards compliance, 合规映射]
summary: >-
  agent-governance-standards-mapping（治理标准映射 / compliance mapping / agent standards compliance）
  Microsoft Agent Governance Toolkit 将治理控制显式映射到 OWASP Agentic AI Top 10（全部覆盖）、NIST AI RMF 1.0
  （GOVERN/MAP/MEASURE/MANAGE 全对齐）、EU AI Act（自动化证据）、SOC 2（审计导出），实现合规自动化证明
related: []
---

Microsoft Agent Governance Toolkit 将其治理控制显式映射到四个主流合规标准框架 [^src-1]：

1. **OWASP Agentic AI Top 10** — 全部 10 项风险均由确定性控制覆盖（"All 10 risks covered with deterministic controls"）[^src-2]。
2. **NIST AI RMF 1.0** — 完整对齐 GOVERN、MAP、MEASURE、MANAGE 四个功能域 [^src-2]。
3. **EU AI Act** — 提供合规映射并支持自动化证据生成（"compliance mapping with automated evidence"）[^src-2]。
4. **SOC 2** — 提供控制映射并支持审计轨迹导出（"control mapping with audit trail export"）[^src-2]。

这一映射机制的意义在于：组织不必从零构建合规论证，而是通过工具包内置的映射关系，将技术治理控制自动关联到监管要求。ADR-0022 记录了"Compliance Auto-Mapping"的架构决策 [^src-3]，表明合规映射被视为一等架构关注点而非事后文档工作。配合 Agent Compliance 包的 OWASP 验证、策略 lint 和完整性检查能力 [^src-4]，形成从控制实施到合规证明的闭环。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L427-428 -- "Standards Compliance"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L429-438 -- "OWASP Agentic AI Top 10 All 10 risks covered with deterministic controls ... SOC 2 Control mapping with audit trail export"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L308 -- "ADR-0022: Compliance Auto-Mapping"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L365 -- "Agent Compliance OWASP verification, policy linting, integrity checks"
