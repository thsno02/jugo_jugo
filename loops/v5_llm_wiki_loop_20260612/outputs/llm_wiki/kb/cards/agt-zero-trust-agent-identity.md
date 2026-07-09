---
id: agt-zero-trust-agent-identity
title: AGT 零信任 Agent 身份与信任评分
status: accepted
card_type: identity-trust-mechanism
tags:
- zero-trust
- agent-identity
- trust-scoring
- post-quantum-crypto
- delegation-chain
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-microsoft-agent-governance-toolkit
evidence_basis: code_implementation
justification: ../justification/agt-zero-trust-agent-identity.md
canonical_concept: zero-trust-agent-identity
aliases:
- Zero-Trust Identity
- AgentMesh Identity
- agent trust scoring
- Ed25519 + ML-DSA-65
- trust ceiling
- 零信任 agent 身份
summary: AGT 的 Zero-Trust Identity 使用 Ed25519 + 量子安全 ML-DSA-65 作为 agent credentials。行为信任评分
  0-1000，agent 偏离预期模式时分数衰减。SPIFFE/SVID 兼容。Trust ceiling 在 delegation chain 中传播——delegated
  agent 永远不能超过 parent trust level。zero-trust-agent-identity AgentMesh trust scoring
  delegation chain
related:
- agt-deterministic-policy-enforcement
- agt-four-privilege-ring-execution-sandbox
- agt-merkle-audit-compliance
---
AGT 的身份层采用零信任架构，每个 agent 持有 Ed25519 + 量子安全 ML-DSA-65 双重 credentials [^src-1]。ML-DSA-65 的引入似乎是为应对后量子计算威胁 [^card-1]。

行为信任评分范围 0-1000，当 agent 行为偏离预期模式时分数自动衰减 [^src-1]。该机制兼容 SPIFFE/SVID 标准 [^src-1]。

关键设计约束：trust ceiling 在委托链中传播——被委托的 agent 永远不能超过其 parent 的 trust level [^src-1]。这确保信任不会在多跳委托中被放大，与 [^card-1] 中的 fail-closed 策略引擎形成互补的安全保障。

[^src-1]: `data/raw/github_repo/repo-microsoft-agent-governance-toolkit/repo/README.md` -- "Zero-Trust Identity" P1 -- "Ed25519 + quantum-safe ML-DSA-65 agent credentials. Behavioral trust scoring (0--1000) that decays when agents act outside expected patterns. SPIFFE/SVID compatible. Trust ceilings propagate through delegation chains -- a delegated agent can never exceed its parent's trust level."
[^card-1]: agt-deterministic-policy-enforcement -- fail-closed 策略引擎作为信任体系的执行层
