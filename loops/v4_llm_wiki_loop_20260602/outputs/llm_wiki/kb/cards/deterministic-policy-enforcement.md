---
id: deterministic-policy-enforcement
title: 确定性策略执行
status: accepted
card_type: mechanism
tags: [governance, policy-engine, deterministic, agent-governance, policy-as-code]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [microsoft-agent-governance-toolkit-docs]
justification: ../justification/deterministic-policy-enforcement.md
canonical_concept: deterministic-policy-enforcement
aliases: [确定性策略, deterministic policy, 规则式治理, 确定性治理控制]
summary: >-
  deterministic-policy-enforcement（确定性策略 / deterministic policy / 规则式治理）
  Microsoft Agent Governance Toolkit 的核心设计原则：agent 治理使用确定性策略执行而非概率性 LLM 判断，
  通过 OPA/Rego/Cedar 等引擎实现 Policy-as-Code，保证策略评估结果可重现、可审计
related: []
---

Microsoft Agent Governance Toolkit 将"确定性策略执行"（deterministic policy enforcement）列为 agent 运行时治理的四大支柱之一 [^src-1]。这意味着治理决策（如是否允许某次工具调用、是否放行某 agent 请求）由确定性规则引擎做出，而非依赖 LLM 的概率性输出。

该工具包通过 Policy-as-Code 方法落地这一原则，支持 OPA / Rego / Cedar 等可插拔策略后端 [^src-2]，并在架构决策记录 ADR-0004 中明确记录了"Deterministic Policy"这一设计选择 [^src-3]。配套的 Policy-as-Code 系列教程涵盖了策略编写、能力范围界定、速率限制、条件策略、审批工作流、策略测试和策略版本管理等完整生命周期 [^src-4]。

确定性策略的核心优势在于：每次评估结果一致、可重现、可审计，不受模型输出随机性的影响。这与 ADR-0013"Fail Closed on Errors"配合——当策略引擎出错时默认拒绝，而非交由 LLM 做兜底判断 [^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L351 -- "Runtime governance for AI agents: deterministic policy enforcement, zero-trust identity, execution sandboxing, and SRE for autonomous agents."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L134 -- "OPA / Rego / Cedar"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L272 -- "ADR-0004: Deterministic Policy"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L148-163 -- "Policy-as-Code Series: Your First Policy, Capability Scoping, Rate Limiting, Conditional Policies, Approval Workflows, Policy Testing, Policy Versioning, MCP Governance"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L290 -- "ADR-0013: Fail Closed on Errors"
