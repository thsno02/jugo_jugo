---
id: microsoft-agent-governance-toolkit-overview
title: Microsoft 代理治理工具包概览
status: draft
card_type: system-overview
tags: [microsoft, agent-governance, runtime-governance, toolkit, multi-agent]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [microsoft-agent-governance-toolkit-docs]
evidence_basis: documentation
justification: ../justification/microsoft-agent-governance-toolkit-overview.md
canonical_concept: microsoft-agent-governance-toolkit
aliases: [Agent Governance Toolkit, agent-governance-toolkit, Microsoft Agent Governance]
summary: >-
  Microsoft Agent Governance Toolkit 是一个运行时治理框架(runtime governance)，为 AI 代理提供确定性策略执行(deterministic policy enforcement)、零信任身份(zero-trust identity)、执行沙箱(execution sandboxing)和自主代理 SRE 能力。包含 8 个核心包(Agent OS/Mesh/Runtime/SRE/Compliance/Marketplace/Lightning/Hypervisor)、5 种语言 SDK(Python/TypeScript/.NET/Rust/Go)、20+ 框架集成(LangChain/CrewAI/AutoGen/Google ADK/OpenAI Agents 等)。拥有 13000+ 测试、10 份 RFC 2119 正式规范、25 份 ADR。对齐 OWASP Agentic AI Top 10、NIST AI RMF 1.0、EU AI Act、SOC 2。
related: [deterministic-policy-enforcement-for-agents, agent-runtime-four-privilege-rings]
---

Microsoft Agent Governance Toolkit 是一个面向 AI 代理的运行时治理框架，其核心定位为：确定性策略执行、零信任身份、执行沙箱和自主代理的 SRE。[^src-1]

该工具包采用模块化架构，包含 8 个核心包：Agent OS（策略引擎、代理生命周期、治理门）、Agent Mesh（代理发现、路由、信任网格）、Agent Runtime（执行沙箱，四环特权模型）、Agent SRE（Kill switch、SLO 监控、混沌测试）、Agent Compliance（OWASP 验证、策略 linting、完整性检查）、Agent Marketplace（插件治理、信任评分）、Agent Lightning（RL 训练治理，违规惩罚）、Agent Hypervisor（执行审计、增量引擎、承诺锚定）。[^src-2]

语言覆盖方面提供 Python、TypeScript、.NET、Rust、Go 五种 SDK。框架集成覆盖 LangChain、CrewAI、AutoGen、Google ADK、OpenAI Agents、LlamaIndex、Haystack、Mastra、MCP、A2A 等 20+ 框架。[^src-3]

工程成熟度指标：13000+ 测试，10 份正式 RFC 2119 规范（含合规测试），25 份架构决策记录（ADR）。合规方面对齐 OWASP Agentic AI Top 10（全部 10 项风险以确定性控制覆盖）、NIST AI RMF 1.0（完整 GOVERN/MAP/MEASURE/MANAGE 对齐）、EU AI Act（自动化证据映射）、SOC 2（审计追踪导出）。[^src-4]

[^src-1]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- "Agent Governance Toolkit" P1 -- "Runtime governance for AI agents: deterministic policy enforcement, zero-trust identity, execution sandboxing, and SRE for autonomous agents."
[^src-2]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- "Packages" P1 -- "Agent OS Policy engine, agent lifecycle, governance gate ... Agent Hypervisor Execution audit, delta engine, commitment anchoring"
[^src-3]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- "Language SDKs / Framework Integrations" P1 -- "Works with any agent framework: LangChain, CrewAI, AutoGen, Google ADK, OpenAI Agents, LlamaIndex, Haystack, Mastra, MCP, A2A, and more."
[^src-4]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- "Standards Compliance" P1 -- "OWASP Agentic AI Top 10 | All 10 risks covered with deterministic controls"
