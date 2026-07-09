---
id: agt-four-privilege-ring-execution-sandbox
title: AGT 四特权环执行沙箱模型
status: draft
card_type: architecture-concept
tags: [agent-runtime, privilege-rings, sandboxing, execution-isolation, security, saga-orchestration, kill-switch]
created_time: 2026-06-12T20:00:00+08:00
edited_time: 2026-06-12T20:00:00+08:00
edited_entity: llm
source_ids: [microsoft-agent-governance-toolkit-docs, repo-microsoft-agent-governance-toolkit]
evidence_basis: documentation+code_implementation
justification: ../justification/agt-four-privilege-ring-execution-sandbox.md
canonical_concept: agt-four-privilege-ring-execution-sandbox
aliases: [Agent Runtime, four privilege rings, 四环特权模型, execution sandboxing, 执行沙箱, saga orchestration, kill switch, 特权环隔离]
summary: >-
  AGT Agent Runtime 的执行沙箱采用四特权环模型（kernel / supervisor / user / untrusted），
  借鉴硬件风格隔离语义实现分级执行控制。配套 Saga orchestration 处理多步工作流
  自动补偿失败步骤，Kill switch 实现 agent 立即终止。Agent Hypervisor 模块提供
  执行审计(execution audit)、增量引擎(delta engine)和承诺锚定(commitment anchoring)，
  拥有独立规范配备 80 项合规测试。重要限制：治理在 Python middleware 层而非 OS kernel，
  生产建议每 agent 独立容器。
related: [agt-deterministic-policy-enforcement, agt-zero-trust-agent-identity, microsoft-agent-governance-toolkit-overview]
---

AGT Agent Runtime 是 Microsoft Agent Governance Toolkit 中负责执行沙箱的核心组件，采用四特权环模型实现分级执行控制。[^src-1] [^src-4]

**四环层级**（kernel / supervisor / user / untrusted）借鉴传统操作系统 ring 0-3 架构理念，将代理操作按权限层级隔离。[^src-4]

**配套机制**：
- **Saga orchestration**：管理多步工作流，当流程中某步失败时自动执行补偿操作 [^src-4]
- **Kill switch**：允许立即终止异常 agent [^src-4]
- **Agent Hypervisor**：提供执行审计（execution audit）、增量引擎（delta engine）和承诺锚定（commitment anchoring）三项能力，形成"沙箱执行 + 审计追踪"的双层安全保障 [^src-2]

Agent Runtime 拥有独立的正式规范——Agent Hypervisor Execution Control specification，配备 80 项合规测试，表明该组件的执行控制行为是形式化定义的。[^src-3]

**重要限制**：治理执行在 Python middleware 层，policy engine 与 agents 共享进程边界，并非 OS kernel 级隔离。生产环境建议每个 agent 运行在独立容器中以获取 OS 级隔离。[^src-5]

[^src-1]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- "Packages" P1 -- "Agent Runtime Execution sandboxing with four privilege rings"
[^src-2]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- "Packages" P1 -- "Agent Hypervisor Execution audit, delta engine, commitment anchoring"
[^src-3]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- "Specifications" P1 -- "Agent Hypervisor Execution Control | 80"
[^src-4]: `data/raw/github_repo/repo-microsoft-agent-governance-toolkit/repo/README.md` -- "Execution Sandboxing" P1 -- "Four privilege rings (kernel, supervisor, user, untrusted) with hardware-style isolation semantics. Saga orchestration for multi-step workflows with automatic compensation on failure. Kill switch for immediate agent termination."
[^src-5]: `data/raw/github_repo/repo-microsoft-agent-governance-toolkit/repo/README.md` -- "Security" P1 -- "AGT enforces governance at the Python middleware layer, not at the OS kernel level. The policy engine and agents share the same process boundary."
