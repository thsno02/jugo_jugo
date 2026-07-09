---
id: ai-agent-context-scarcity
title: AI Agent 的上下文稀缺性问题
status: draft
card_type: problem-statement
tags: [ai-agent, context, claude-mcp, knowledge-graph, stale-documentation]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
evidence_basis: practitioner_report
justification: ../justification/ai-agent-context-scarcity.md
canonical_concept: ai-agent-context-scarcity
aliases: [context as scarcest resource for AI agents, agent context problem, AI agent 上下文稀缺]
summary: >-
  Anthropic 工程团队将 context 描述为 AI agent 最稀缺资源 agents need just-in-time access to current accurate context；AI coding agent 读取过时内部文档则产出过时输出；企业 LLM wiki 通过 Claude MCP 协议为 agent 提供持续维护的知识图谱查询接口；agent 与人类查询同一图谱确保 grounded in same current context
related: [continuous-drift-detection, enterprise-llm-wiki-architecture]
---

材料引述 Anthropic 工程团队的观点：context（上下文）是 AI agent 最稀缺的资源——agent 需要即时访问当前、准确的上下文才能在真实工作中可靠执行。[^src-1]

**问题具象化**：coding agent 读取过时的内部文档（如六个月前编写、系统已重写两次的 runbook），会产出基于 2024 年假设的代码。一年未做健康检查的知识图谱是 agent 最糟糕的输入。[^src-2]

**解决路径**：企业 LLM wiki 为 AI agent 提供持续维护的知识图谱查询接口，通常通过 Claude MCP 等协议。Agent 与人类工程师查询同一图谱，确保 agent 输出 grounded 在团队运作的同一当前上下文中。[^src-3] [^card-1]

这一论述将企业知识维护的价值从"帮助人类找到信息"扩展到"确保 AI agent 不产出错误输出"——后者在 AI automation 普及的背景下可能是更大的商业动机。

[^card-1]: 参见 [[enterprise-llm-wiki-architecture]] Step 5 Query the wiki
[^src-1]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Stay current: health checks need to run automatically" P34 -- "Anthropic's engineering team frames context as the scarcest resource for AI agents: agents need just-in-time access to current, accurate context to perform reliably on real work."
[^src-2]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Stay current: health checks need to run automatically" P33 -- "an AI agent reads the stale runbook and produces code that worked in 2024"
[^src-3]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Step 5: Query the wiki" P59 -- "AI coding agents through protocols like Claude MCP. The agents query the same knowledge graph the humans do"
