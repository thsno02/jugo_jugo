---
id: owasp-genai-landscape-2026q2
title: OWASP 2026 Q2 三件套：把"Top 10"扩成"防御方案地图"
status: accepted
card_type: example_pattern
tags: [#llm, #security, #owasp, #genai, #marketplace]
created_time: 2026-05-26T11:40:00+08:00
edited_time: 2026-05-27T15:22:00+08:00
edited_entity: llm
source_ids: [owasp-llm-top10-2025]
provenance_card: ../provenance/owasp-genai-landscape-2026q2.md
aliases: ["AI Security Solutions Landscape Q2 2026", "OWASP GenAI Landscape"]
related: [owasp-llm-top10-community-genealogy, owasp-agentic-top10-2026-positioning, owasp-agentic-vs-llm-top10-2025, microsoft-agent-governance-standards-alignment, nist-ai-rmf-gai-profile]
---

OWASP 在 2026 年 3 月 17 日 与 4 月 9 日 集中发布三份 *AI Security Solutions Landscape Q2 2026*：

- **For LLM and Gen AI Apps**（2026-03-17）
- **For Agentic AI**（2026-03-17）
- **For AI and Agentic Red Teaming**（2026-04-09）

这是一个值得记住的"项目演化模式"：当一份社区漏洞清单（Top 10）开始被业内引用，下一步通常不是写更多的 Top 10，而是出**与该清单互补的"防御 / 工具 / 服务地图"**。理由是：

1. 用户拿到 Top 10 后，下一个问题就是"那有什么工具能防"。如果项目方不答，市场会出现一群营销驱动的"AI 安全方案对比表"。
2. OWASP 用 Landscape 名义自己出，等于给社区一个可被引用、可被 PR 修正的中立地图，避免被供应商话术殖民。
3. 把"LLM/GenAI"、"Agentic AI"、"Red Teaming"分成三份意味着 OWASP 已经把 Agentic AI 视为独立的安全形态——和传统 GenAI App 在威胁模型上不可混为一谈。

边界与误读：

- Landscape 是清单 + 简介，不是工具排名或测评；不要把"被列入"等同于"被推荐"。
- 三份资源虽然在同一季度发布，但维护节奏不同，不能假定它们的 Top 10 引用同步。
- 这是一个**项目运营 / 治理**层面的模式，不是 LLM 安全技术本身——把它作为参考案例引用时，要明确这一点。

## References

- 三份 Landscape 发布日期与标题见 `data/raw/webpage/owasp-llm-top10-2025/text.txt`，第 100–118 行。

## Footnotes

- L106：*"April 9, 2026 — Resources — AI Security Solutions Landscape For AI and Agentic Red Teaming Q2 2026"*。
- L110：*"March 17, 2026 — AI Security Solutions Landscape for Agentic AI Q2 2026"*。
- L114：*"March 17, 2026 — Al Security Solutions Landscape For LLM and Gen Al Apps Q2 2026"*。
