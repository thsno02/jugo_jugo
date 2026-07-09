---
id: agt-privilege-ring-sandboxing
title: AGT 四特权环执行沙箱
status: superseded
superseded_by: agt-four-privilege-ring-execution-sandbox
card_type: execution-isolation-model
tags: [privilege-rings, sandboxing, saga-orchestration, kill-switch, agent-runtime]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-agent-governance-toolkit]
evidence_basis: code_implementation
justification: ../justification/agt-privilege-ring-sandboxing.md
canonical_concept: agent-privilege-ring-sandboxing
aliases: [Execution Sandboxing, privilege rings, Agent Hypervisor, Agent Runtime, saga orchestration, kill switch, 特权环隔离, 执行沙箱]
summary: >-
  AGT 执行沙箱采用四特权环模型（kernel / supervisor / user / untrusted），硬件风格隔离语义。Saga orchestration 处理多步工作流并在失败时自动补偿。Kill switch 实现 agent 立即终止。治理在 Python middleware 层而非 OS kernel——生产建议每 agent 独立容器。agent-privilege-ring-sandboxing Execution Sandboxing Agent Hypervisor saga kill switch
related: [agt-deterministic-policy-enforcement, agt-zero-trust-agent-identity]
---

AGT 的执行隔离采用四特权环模型：kernel、supervisor、user、untrusted，借鉴硬件特权级的隔离语义 [^src-1]。该设计为 agent 动作提供分层权限边界。

多步工作流通过 Saga orchestration 管理，当流程中某步失败时自动执行补偿操作 [^src-1]。Kill switch 机制允许立即终止异常 agent [^src-1]，与 [^card-1] 中的信任衰减评分配合——当信任分跌破阈值时据材料推测可触发 kill switch。

重要限制：治理执行在 Python middleware 层，policy engine 与 agents 共享进程边界，并非 OS kernel 级隔离 [^src-2]。生产环境建议每个 agent 运行在独立容器中以获取 OS 级隔离 [^src-2]。

[^src-1]: `data/raw/github_repo/repo-microsoft-agent-governance-toolkit/repo/README.md` -- "Execution Sandboxing" P1 -- "Four privilege rings (kernel, supervisor, user, untrusted) with hardware-style isolation semantics. Saga orchestration for multi-step workflows with automatic compensation on failure. Kill switch for immediate agent termination."
[^src-2]: `data/raw/github_repo/repo-microsoft-agent-governance-toolkit/repo/README.md` -- "Security" P1 -- "AGT enforces governance at the Python middleware layer, not at the OS kernel level. The policy engine and agents share the same process boundary."
[^card-1]: agt-zero-trust-agent-identity -- trust scoring 衰减机制与 kill switch 的协同
