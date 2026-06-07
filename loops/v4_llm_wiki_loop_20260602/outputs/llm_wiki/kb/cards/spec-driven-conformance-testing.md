---
id: spec-driven-conformance-testing
title: 规范驱动的合规测试
status: accepted
card_type: mechanism
tags: [governance, specification, conformance-testing, rfc-2119, quality-assurance]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [microsoft-agent-governance-toolkit-docs]
justification: ../justification/spec-driven-conformance-testing.md
canonical_concept: spec-driven-conformance-testing
aliases: [规范驱动合规, spec-driven governance, RFC 2119 合规测试, 规范先行]
summary: >-
  spec-driven-conformance-testing（规范驱动合规 / spec-driven governance / RFC 2119 合规测试）
  Microsoft Agent Governance Toolkit 为每个主要组件编写 RFC 2119 形式规范，并配以合规测试（共 13,000+ 测试、
  10 份形式规范），用可执行测试取代自然语言约束来定义治理行为的正确性
related: [audit-stress-test, companion-conformance-invariants]
---

Microsoft Agent Governance Toolkit 的一个显著特征是"规范先行"（spec-first）：每个主要组件都有一份 RFC 2119 形式规范（formal specification），并配以可执行的合规测试（conformance tests）[^src-1]。

整个工具包共有 13,000+ 测试和 10 份形式规范 [^src-2]。各组件的合规测试规模如下 [^src-3]：
- Agent OS Policy Engine：68 项测试
- AgentMesh Identity and Trust：135 项测试
- Agent Hypervisor Execution Control：80 项测试
- AgentMesh Trust and Coordination：62 项测试
- Agent SRE Governance：111 项测试
- MCP Security Gateway：127 项测试
- Agent Lightning Fast-Path：100 项测试
- Framework Adapter Contract：152 项测试
- Audit and Compliance：157 项测试

此外，25 份架构决策记录（Architecture Decision Records, ADR）文档化了关键设计选择的推理过程 [^src-4]。这种规范驱动的方法意味着治理行为的正确性由可执行测试而非自然语言文档定义，任何实现都可以通过跑通合规测试来验证其符合规范。

值得注意的是，「规范先行、可执行验证」并非 Microsoft 独有的方法论。学术界的伴侣记忆框架也独立采用了类似思路——为每个操作定义合规不变量，将说服性框架转化为构建者可测试的规范[^card-1]。同一框架中的 AUDIT 压力测试则从不同角度验证质量：合规测试验证实现是否符合规范（正确性），AUDIT 通过经验性悬挂验证知识条目是否仍然承重（效用性），两者共同覆盖质量保障的正确性与效用性维度[^card-2]。

## Footnotes

[^src-1]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L401 -- "Every major component has a formal RFC 2119 specification with conformance tests."
[^src-2]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L355-358 -- "13,000+ Tests, 10 Formal Specs, 5 Languages, 20+ Integrations"
[^src-3]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L403-424 -- "Agent OS Policy Engine 68 ... Audit and Compliance 157"
[^src-4]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L425 -- "25 Architecture Decision Records document the reasoning behind key design choices."
[^card-1]: [伴侣系统合规不变量](companion-conformance-invariants.md) -- 本卡聚焦工业级治理工具包的 RFC 2119 规范与 13,000+ 合规测试，该卡聚焦学术伴侣记忆框架中的操作级合规不变量；两者共享「规范先行、可执行验证」方法论但应用于截然不同的领域
[^card-2]: [AUDIT 结构性压力测试](audit-stress-test.md) -- 本卡通过 RFC 2119 合规测试验证实现的规范正确性，该卡通过经验性悬挂验证知识条目的功能效用性；两者从正确性和效用性两个维度互补覆盖质量保障
