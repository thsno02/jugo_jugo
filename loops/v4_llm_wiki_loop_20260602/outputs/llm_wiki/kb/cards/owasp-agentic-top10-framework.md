---
id: owasp-agentic-top10-framework
title: OWASP Agentic Top 10 框架
status: accepted
card_type: concept
tags: [security, governance, agentic, owasp, risk-framework, peer-review]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [owasp-agentic-top10-2026]
justification: ../justification/owasp-agentic-top10-framework.md
canonical_concept: owasp-agentic-top10-framework
aliases: [OWASP Top 10 for Agentic Applications, OWASP Agentic Top 10, Agentic App Security Top 10]
summary: >-
  owasp-agentic-top10-framework（OWASP Top 10 for Agentic Applications, Agentic App Security Top 10）OWASP 发布的针对自主式 agentic AI 系统的十大安全风险框架，由 100+ 专家同行评审，面向构建者/防御者/决策者，将 GenAI 安全生态浓缩为可操作的风险清单
related: []
---

OWASP Top 10 for Agentic Applications 2026 是一个全球同行评审的安全风险框架，专门识别自主式和 agentic AI 系统面临的最关键安全风险 [^src-1]。该框架由超过 100 名行业专家、研究者和从业者协作开发 [^src-2]，为组织保护那些能够"规划、行动并在复杂工作流中做出决策"的 AI agent 提供实用且可操作的指导 [^src-3]。

该框架的定位是将更广泛的 OWASP GenAI Security 指导生态系统提炼为一种"可访问的、可操作的格式"，为构建者（builders）、防御者（defenders）和决策者（decision-makers）提供一个减少 agentic AI 风险的清晰起点 [^src-4]。框架于 2025 年 12 月 9 日发布 [^src-5]。

需要注意的是，本来源仅为该框架的概览页面，实际的十大风险条目内容未包含在此抓取中。Microsoft Agent Governance Toolkit 声称通过确定性控制覆盖了全部 10 项风险 [^card-1]。该框架的 agentic 聚焦与 OWASP LLM Top 10 的通用 LLM 安全关注互为补充 [^card-2]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/owasp-agentic-top10-2026/text.txt` -- About 段落 L96 -- "a globally peer-reviewed framework that identifies the most critical security risks facing autonomous and agentic AI systems"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/owasp-agentic-top10-2026/text.txt` -- About 段落 L96 -- "Developed through extensive collaboration with more than 100 industry experts, researchers, and practitioners"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/owasp-agentic-top10-2026/text.txt` -- About 段落 L96 -- "secure AI agents that plan, act, and make decisions across complex workflows"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/owasp-agentic-top10-2026/text.txt` -- About 段落 L96 -- "By distilling a broad ecosystem of OWASP GenAI Security guidance into an accessible, operational format, the Top 10 equips builders, defenders, and decision-makers with a clear starting point for reducing agentic AI risks"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/owasp-agentic-top10-2026/text.txt` -- 发布日期 L92 -- "December 9, 2025"
[^card-1]: [Agent 治理标准合规映射](agent-governance-standards-mapping.md) -- Microsoft Agent Governance Toolkit 将治理控制映射到全部 10 项 OWASP Agentic 风险，声称实现确定性全覆盖
[^card-2]: [OWASP LLM Top 10 安全倡议](owasp-llm-top10-initiative.md) -- 2023 年启动的通用 LLM 安全风险倡议，Agentic Top 10 将其延伸到自主式系统
