---
schema: draft_card_provenance.v3
draft_card: ../cards/microsoft-agent-governance-standards-alignment.md
material_id: microsoft-agent-governance-toolkit-docs
digest_id: digest_microsoft-agent-governance-toolkit-docs
source_paths:
  - data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt
created_time: 2026-05-26T11:45:00+08:00
edited_time: 2026-05-26T11:45:00+08:00
edited_entity: llm
---

## 源证据

- 标准合规表（第 429–437 行）：
  > "OWASP Agentic AI Top 10 — All 10 risks covered with deterministic controls / NIST AI RMF 1.0 — Full GOVERN, MAP, MEASURE, MANAGE alignment / EU AI Act — Compliance mapping with automated evidence / SOC 2 — Control mapping with audit trail export"。
- 审计链 ADR（第 298–302 行）：
  > "ADR-0017: Merkle Audit Chain / ADR-0018: Reconstructible Decision BOM / ADR-0019: OTel Event Sink Pattern"。
- Agent Compliance 包职责（第 365 行）：
  > "✅ Agent Compliance OWASP verification, policy linting, integrity checks"。
- Agent Hypervisor 包职责（同上）：
  > "🔒 Agent Hypervisor Execution audit, delta engine, commitment anchoring"。
- Policy 引擎语言（第 134 行 + 第 244 行）：
  > "OPA / Rego / Cedar"、"Agent OS Policy Engine"。

## 卡片范围是否成立

这张卡只就"四份外部标准对齐方式 + 它们如何被 toolkit 落地"展开。原文 Standards Compliance 表是关键证据；卡内每条"设计选择"都能在文档其他位置找到对应（OWASP→deterministic policy 对应 OPA/Rego/Cedar；EU AI Act→automated evidence 对应 Agent Compliance + Hypervisor + Merkle 链）。没有引入文档外的标准细节。

## 发表门控结果

本轮未运行。

## 备注

与 `microsoft-agent-governance-eight-packages` 互补，前者按包看，本卡按外部标准看。预计 `new_card`。
