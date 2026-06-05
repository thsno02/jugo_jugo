---
id: framework-agnostic-governance-layer
title: 框架无关的治理层
status: accepted
card_type: concept
tags: [governance, framework-agnostic, adapter-pattern, agent-governance, integration]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [microsoft-agent-governance-toolkit-docs]
justification: ../justification/framework-agnostic-governance-layer.md
canonical_concept: framework-agnostic-governance-layer
aliases: [框架无关治理, framework-agnostic governance, 治理与框架解耦]
summary: >-
  framework-agnostic-governance-layer（框架无关治理 / framework-agnostic governance / 治理与框架解耦）
  Microsoft Agent Governance Toolkit 将治理设计为与 agent 框架解耦的独立层，通过 Framework Adapter Contract
  规范适配器接口，支持 LangChain/CrewAI/AutoGen/OpenAI Agents/MCP/A2A 等 20+ 框架，治理规则一次定义多处执行
related: []
---

Microsoft Agent Governance Toolkit 将治理设计为一个与具体 agent 框架无关的独立层：同一套治理规则可跨框架执行，不需要为每个框架单独实现治理逻辑 [^src-1]。

当前支持的框架包括 LangChain、CrewAI、AutoGen、Google ADK、OpenAI Agents、LlamaIndex、Haystack、Mastra、MCP、A2A 等 20 种以上 [^src-1]。实现这一解耦的关键机制是"Framework Adapter Contract"——一份形式规范（配有 152 项合规测试），定义了治理层与框架之间的适配器接口 [^src-2][^src-3]。

具体集成示例展示了这种模式的实际运作 [^src-4]：对 OpenAI Agents SDK 实施策略门禁式工具调用（policy-gated tool calls with trust tiers）、对 CrewAI 实施基于角色的多 agent 治理策略、对 HuggingFace smolagents 实施轻量治理、对 MCP 实施信任验证服务器。这意味着组织可以更换底层 agent 框架而无需重写治理规则。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L383 -- "Works with any agent framework: LangChain, CrewAI, AutoGen, Google ADK, OpenAI Agents, LlamaIndex, Haystack, Mastra, MCP, A2A, and more."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L259 -- "Framework Adapter Contract"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L419 -- "Framework Adapter Contract 152"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` -- L387-398 -- "openai-agents-governed ... mcp-trust-verified-server MCP Trust-verified MCP server implementation"
