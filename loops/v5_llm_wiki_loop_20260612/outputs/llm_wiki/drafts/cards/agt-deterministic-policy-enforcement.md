---
id: agt-deterministic-policy-enforcement
title: AGT 确定性策略执行引擎
status: draft
card_type: governance-mechanism
tags: [policy-engine, deterministic-enforcement, fail-closed, sub-millisecond, agent-governance]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-agent-governance-toolkit]
evidence_basis: code_implementation
justification: ../justification/agt-deterministic-policy-enforcement.md
canonical_concept: deterministic-agent-policy-enforcement
aliases: [Agent Governance Toolkit, AGT, Policy Engine, PolicyEvaluator, Agent OS, 确定性策略引擎, application-layer enforcement]
summary: >-
  Microsoft Agent Governance Toolkit (AGT) 的核心是确定性策略执行引擎：每个 agent action（tool call / resource access / inter-agent message）执行前经 policy check，结果为 allow 或 deny。Sub-millisecond 延迟（0.012ms p50，35K ops/sec）。支持 YAML / OPA Rego / Cedar 策略语言。Fail-closed 设计——引擎出错默认 deny。Prompt-based safety 红队测试 26.67% violation rate，AGT 为 0.00%。deterministic-agent-policy-enforcement PolicyEvaluator fail-closed
related: [agt-zero-trust-agent-identity, agt-privilege-ring-sandboxing]
---

Microsoft Agent Governance Toolkit (AGT) 的核心机制是 application-layer 的确定性策略执行引擎 [^src-1]。每个 agent 动作——tool call、resource access、inter-agent message——在执行前必须通过 policy check，结果只有 allow 或 deny 两种确定性输出 [^src-1]。

性能表现为 sub-millisecond 级：单规则评估 0.012ms p50，并发 35K ops/sec [^src-2]。支持三种策略语言：YAML、OPA/Rego、Cedar [^src-2]。

关键设计决策为 fail-closed：当引擎自身出错时，动作默认被 deny [^src-2]。这与 prompt-based safety 形成对比——红队测试中 prompt-based 方式有 26.67% 的 policy violation rate，而 AGT 的 application-layer enforcement 为 0.00% [^src-1]。

当前状态为 Public Preview，Microsoft 签名发布，GA 前可能有 breaking changes [^src-3]。

[^src-1]: `data/raw/github_repo/repo-microsoft-agent-governance-toolkit/repo/README.md` -- "Header" P1 -- "Runtime governance for AI agents. Every tool call, resource access, and inter-agent message is evaluated against policy *before* execution -- deterministic, sub-millisecond, and auditable."
[^src-2]: `data/raw/github_repo/repo-microsoft-agent-governance-toolkit/repo/README.md` -- "Policy Engine" P1 -- "Deterministic allow/deny evaluation for every agent action. Sub-millisecond latency (0.012ms p50 for single rule, 35K ops/sec concurrent). Supports YAML, OPA/Rego, and Cedar policy languages. Fail-closed by default -- if the engine errors, the action is denied."
[^src-3]: `data/raw/github_repo/repo-microsoft-agent-governance-toolkit/repo/README.md` -- "Important banner" P1 -- "Public Preview -- production-quality, Microsoft-signed releases. May have breaking changes before GA."
