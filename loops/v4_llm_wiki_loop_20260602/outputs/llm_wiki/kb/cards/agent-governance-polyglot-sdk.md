---
id: agent-governance-polyglot-sdk
title: Agent 治理多语言 SDK 策略
status: accepted
card_type: mechanism
tags: [governance, sdk, polyglot, multi-language, developer-experience, agent-governance]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [microsoft-agent-governance-toolkit-docs]
justification: ../justification/agent-governance-polyglot-sdk.md
canonical_concept: agent-governance-polyglot-sdk
aliases: [治理SDK多语言支持, governance polyglot SDK, agent governance language SDKs, 多语言治理SDK]
summary: >-
  agent-governance-polyglot-sdk（治理SDK多语言支持 / governance polyglot SDK / agent governance language SDKs）
  Microsoft Agent Governance Toolkit 提供 5 种语言的原生 SDK（Python/TypeScript/.NET/Rust/Go），
  确保治理集成不强制语言迁移，开发者可在已有技术栈中直接嵌入治理能力
related: [framework-agnostic-governance-layer, agent-governance-modular-packages]
---

Microsoft Agent Governance Toolkit 通过原生 SDK 覆盖五种主流编程语言，使治理集成不要求团队变更技术栈 [^src-1]：

| 语言 | 包名 | 安装命令 |
|------|------|----------|
| Python | agent-governance-toolkit | `pip install agent-governance-toolkit` |
| TypeScript | @microsoft/agent-governance-sdk | `npm install @microsoft/agent-governance-sdk` |
| .NET | Microsoft.AgentGovernance | `dotnet add package Microsoft.AgentGovernance` |
| Rust | agent-governance | `cargo add agent-governance` |
| Go | agent-governance-golang | `go get github.com/microsoft/agent-governance-toolkit/agent-governance-golang` |

这种多语言 SDK 策略的设计意义在于：agent 治理的采纳阻力被大幅降低。开发者无需学习新语言或引入 FFI 绑定即可将确定性策略引擎、沙箱、SRE 能力嵌入已有系统。五种语言的选择覆盖了当前 agent 生态的主要技术栈——Python（ML/AI 主力）、TypeScript（前端/全栈）、.NET（企业级）、Rust（安全关键）、Go（基础设施/云原生）[^src-1]。

这与框架无关治理层的设计互补 [^card-1]：框架无关性解决了"哪个 agent 框架都行"的问题，多语言 SDK 解决了"哪种编程语言都行"的问题。两者共同消除了治理集成的两大技术障碍——框架锁定和语言锁定。八个治理模块的能力通过这些 SDK 暴露，使模块化分包架构对各语言开发者均可达 [^card-2]。

## Footnotes

[^src-1]: `data/raw/webpage/microsoft-agent-governance-toolkit-docs/markdown.md` -- L10-16 -- "🐍 Python pip install agent-governance-toolkit ... 🐹 Go go get github.com/microsoft/agent-governance-toolkit/agent-governance-golang"
[^card-1]: [框架无关的治理层](framework-agnostic-governance-layer.md) -- 本卡解决语言锁定问题（5 种语言原生 SDK），该卡解决框架锁定问题（20+ agent 框架适配器）；两者从不同维度消除治理集成障碍
[^card-2]: [Agent 治理模块化分包架构](agent-governance-modular-packages.md) -- 八个独立治理模块通过多语言 SDK 向各语言开发者暴露能力
