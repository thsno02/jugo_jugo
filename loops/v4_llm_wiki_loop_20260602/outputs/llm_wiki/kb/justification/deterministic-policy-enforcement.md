---
schema: justification_journal.v1
card: ../cards/deterministic-policy-enforcement.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt`
源证据：
- L351 — "Runtime governance for AI agents: deterministic policy enforcement, zero-trust identity, execution sandboxing, and SRE for autonomous agents."
- L272 — "ADR-0004: Deterministic Policy"
- L134 — "OPA / Rego / Cedar"
- L290 — "ADR-0013: Fail Closed on Errors"
范围论证：确定性策略执行是该工具包的四大核心支柱之一，也是其区别于基于 LLM 判断的治理方案的关键设计选择。从源材料中可提取其定义（确定性 vs 概率性）、实现方式（Policy-as-Code + 可插拔后端）、配套决策（fail closed）三个维度的信息，足以构成一张独立的原子卡片。
