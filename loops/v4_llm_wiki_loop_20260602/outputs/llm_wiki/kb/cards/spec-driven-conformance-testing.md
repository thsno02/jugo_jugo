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
related: []
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

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L401 -- "Every major component has a formal RFC 2119 specification with conformance tests."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L355-358 -- "13,000+ Tests, 10 Formal Specs, 5 Languages, 20+ Integrations"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L403-424 -- "Agent OS Policy Engine 68 ... Audit and Compliance 157"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L425 -- "25 Architecture Decision Records document the reasoning behind key design choices."
