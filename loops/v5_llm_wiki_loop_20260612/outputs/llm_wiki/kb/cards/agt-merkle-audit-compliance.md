---
id: agt-merkle-audit-compliance
title: AGT Merkle 链审计与合规映射
status: accepted
card_type: audit-compliance-mechanism
tags:
- merkle-chain
- audit-log
- tamper-evident
- compliance-mapping
- decision-bom
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-microsoft-agent-governance-toolkit
evidence_basis: code_implementation
justification: ../justification/agt-merkle-audit-compliance.md
canonical_concept: merkle-chain-agent-audit
aliases:
- Audit and Compliance
- Merkle-chained audit logs
- Decision BOM
- tamper-evident audit
- 防篡改审计日志
- Merkle 链审计
summary: AGT 使用 tamper-evident Merkle-chained audit logs 记录治理决策。可从 observability signals 重建 Decision BOM。支持 EU AI Act / SOC 2 / HIPAA / GDPR 自动化合规映射。CloudEvents 格式导出供 SIEM 集成。157 conformance tests。merkle-chain-agent-audit
  Decision BOM tamper-evident compliance mapping
related:
- agt-deterministic-policy-enforcement
- agt-zero-trust-agent-identity
---

AGT 的审计层使用 tamper-evident Merkle-chained audit logs，确保治理决策记录不可被事后篡改 [^src-1]。Merkle chain 结构意味着任何对历史记录的修改都会破坏链的完整性验证。

Decision BOM（Bill of Materials）可从 observability signals 重建 [^src-1]，这使得任何治理决策的完整上下文（who / what / when / why）可追溯。与 [^card-1] 的策略引擎和 [^card-2] 的身份层配合，审计链记录了哪个 agent（身份）的哪个动作被哪条策略 allow/deny。

合规映射覆盖 EU AI Act、SOC 2、HIPAA、GDPR [^src-1]，支持 CloudEvents 格式导出至 SIEM 系统。该模块有 157 conformance tests [^src-2]。

[^src-1]: `data/raw/github_repo/repo-microsoft-agent-governance-toolkit/repo/README.md` -- "Audit and Compliance" P1 -- "Tamper-evident Merkle-chained audit logs. Reconstructible Decision BOMs from observability signals. Automated compliance mapping for EU AI Act, SOC 2, HIPAA, and GDPR. CloudEvents export for SIEM integration."
[^src-2]: `data/raw/github_repo/repo-microsoft-agent-governance-toolkit/repo/README.md` -- "Specifications" P1 -- "Audit and Compliance ... Merkle audit, compliance mapping, Decision BOM | 157"
[^card-1]: agt-deterministic-policy-enforcement -- 策略引擎的 allow/deny 决策被审计链记录
[^card-2]: agt-zero-trust-agent-identity -- 身份层提供审计记录中的 "who" 信息
