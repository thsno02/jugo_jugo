---
schema: justification_journal.v1
card: ../cards/agent-sre-kill-switch-slo.md
created_time: 2026-06-11T10:00:00+08:00
---

## creation | 2026-06-11T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md`
源证据：
- L2 — "SRE for autonomous agents" 列为四大支柱之一
- L8 — "Agent SRE Kill switch, SLO monitoring, chaos testing"
- L35 — "Agent SRE Governance 111" 形式规范
范围论证：现有卡片 agent-governance-modular-packages 在八包列表中简要提及 Agent SRE 模块（一句话），但未展开 SRE 应用于自治 agent 的核心洞察——agent 不可靠时会"错误行动"而非仅"不响应"，因此需要 kill switch 这种硬件级中断能力。另外，现有 chaos-monkey-agent-stress-testing 卡来自学术安全研究（eTAMP 论文），聚焦攻击面评估，与本卡的生产运维 SRE 视角正交互补。Agent SRE 作为独立治理支柱、有独立规范和独立能力集，构成原子概念。
