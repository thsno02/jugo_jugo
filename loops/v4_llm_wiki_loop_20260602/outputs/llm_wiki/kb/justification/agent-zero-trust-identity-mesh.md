---
schema: justification_journal.v1
card: ../cards/agent-zero-trust-identity-mesh.md
created_time: 2026-06-11T10:00:00+08:00
---

## creation | 2026-06-11T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md`
源证据：
- L2 — "zero-trust identity" 列为四大支柱之一
- L8 — "Agent Mesh Agent discovery, routing, and trust mesh"
- L32-34 — "AgentMesh Identity and Trust 135" 和 "AgentMesh Trust and Coordination 62" 两份形式规范
- L22,26 — 示例项目展示信任层级和信任验证实现
范围论证：现有卡片 deterministic-policy-enforcement 覆盖了四大支柱中的确定性策略执行，agent-governance-modular-packages 简要提及 Agent Mesh 模块但未深入零信任身份概念。零信任身份作为独立的治理支柱，有独立的形式规范（197 项合规测试）和独立的设计理念（默认不信任、每次验证），构成一个原子概念。
