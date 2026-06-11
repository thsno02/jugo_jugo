---
id: agent-sre-kill-switch-slo
title: Agent SRE：Kill Switch 与 SLO 监控
status: accepted
card_type: mechanism
tags: [sre, kill-switch, slo, chaos-testing, agent-governance, reliability, autonomous-agents]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [microsoft-agent-governance-toolkit-docs]
justification: ../justification/agent-sre-kill-switch-slo.md
canonical_concept: agent-sre-kill-switch-slo
aliases: [agent SRE, agent kill switch, agent SLO监控, SRE for agents, agent可靠性工程]
summary: >-
  agent-sre-kill-switch-slo（agent SRE / agent kill switch / agent SLO监控）
  Microsoft Agent Governance Toolkit 将 SRE 列为 agent 运行时治理四大支柱之一，通过 Agent SRE 模块提供
  Kill Switch（紧急停止）、SLO 监控和混沌测试三项能力，配以 111 项合规测试的形式规范，
  将传统站点可靠性工程实践系统性地迁移到自治 agent 的运维领域
related: [agent-governance-modular-packages, chaos-monkey-agent-stress-testing, deterministic-policy-enforcement]
---

Microsoft Agent Governance Toolkit 将"SRE for autonomous agents"列为 agent 运行时治理的四大支柱之一 [^src-1]，通过专用的 **Agent SRE** 模块提供三项核心能力 [^src-2]：

1. **Kill Switch**（紧急停止）——当 agent 行为偏离预期时，可立即终止其执行。这是最极端但最可靠的治理手段：当所有策略和监控都无法阻止有害行为时，物理切断是最后防线。
2. **SLO 监控**——为 agent 定义服务等级目标（Service Level Objectives），量化其可靠性和性能。传统 SLO 面向服务延迟/可用性，agent SLO 需额外覆盖任务成功率、策略合规率、资源消耗等 agent 特有指标。
3. **混沌测试**（Chaos Testing）——主动向 agent 注入故障以验证其容错能力。

该模块的正确性由"Agent SRE Governance"形式规范保障，配有 111 项合规测试 [^src-3]。

将 SRE 应用于自治 agent 的核心洞察在于：传统软件服务的可靠性问题（宕机、延迟、级联故障）在 agent 系统中被放大——因为 agent 具有自主决策能力，一个不可靠的 agent 不仅会"不响应"，还可能"错误地行动"。Kill Switch 的存在隐含了一个设计假设：agent 系统需要硬件级别的紧急中断能力，而非仅依赖软件层面的策略拒绝。

学术界的 Chaos Monkey 式 agent 压力测试从安全研究角度探索了类似思路——通过环境扰动注入来测试 agent 鲁棒性 [^card-1]。不同之处在于：Microsoft 的 Agent SRE 模块面向生产运维（确保服务连续性），而学术 Chaos Monkey 面向安全评估（揭示攻击面）。两者共同验证了将混沌工程方法迁移到 agent 领域的可行性。

## Footnotes

[^src-1]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- L2 -- "Runtime governance for AI agents: deterministic policy enforcement, zero-trust identity, execution sandboxing, and SRE for autonomous agents."
[^src-2]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- L8 -- "📊 Agent SRE Kill switch, SLO monitoring, chaos testing"
[^src-3]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- L35 -- "Agent SRE Governance 111"
[^card-1]: [Chaos Monkey 式 Agent 压力测试](chaos-monkey-agent-stress-testing.md) -- 本卡聚焦生产环境 SRE 运维（kill switch/SLO/混沌测试确保服务连续性），该卡聚焦安全研究中的环境扰动注入（揭示 agent 在噪声下的攻击面）；两者共同验证混沌工程方法在 agent 领域的价值
