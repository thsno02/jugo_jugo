---
id: owasp-agentic-vs-llm-top10-2025
title: OWASP 为什么把 Agentic Top 10 与 LLM Top 10 分开列
status: draft
card_type: distinction
tags: [#owasp, #agent-security, #llm-security, #risk-framework]
created_time: 2026-05-26T11:32:00+08:00
edited_time: 2026-05-26T11:32:00+08:00
edited_entity: llm
source_ids: [owasp-agentic-top10-2026]
provenance_card: ../provenance/owasp-agentic-vs-llm-top10-2025.md
aliases: ["OWASP agent vs LLM 区分", "agentic top 10 vs LLM top 10"]
related: [owasp-agentic-top10-2026-positioning, owasp-llm-top10-community-genealogy, owasp-genai-landscape-2026q2, microsoft-agent-governance-standards-alignment, nist-ai-rmf-gai-profile]
---

OWASP GenAI Security Project 的 resources 列表里，"Agentic Applications 2026" 不是 "LLM Top 10 for 2025" 的升级版，而是并列条目。这一并列结构本身是一条值得提取的设计信号：OWASP 显式承认 agentic 系统的风险不可被早期 LLM Top 10 完全覆盖。

源页可直接观察到的区分线索：

- **平行陈列**：导航 "LLM TOP 10" 子菜单下同时列出 "LLM TOP 10 FOR 2025" 与 "LLM TOP 10 FOR 2023/24"，主资源页另起一项"OWASP Top 10 for Agentic Applications for 2026"。三者并列，不互相替代。
- **About 段的限定范围**：Agentic 这份明确指向"autonomous and agentic AI systems that plan, act, and make decisions across complex workflows"。"plan / act / decide"三动作合起来才进入这份清单的范围；只做单轮回答的 LLM 应用归属 LLM Top 10。
- **由不同的 initiative 支撑**：导航里的 "AGENTIC APP SECURITY" 与 "AI Red Teaming"、"Threat Intelligence" 等是 agentic 这份清单的支撑研究路线，而 LLM Top 10 则有自己独立的工作流。

操作含义（基于这种并列结构）：

- 评估一个 AI 系统时，应先判断它是否符合"plan + act + decide across workflows"——满足才把 Agentic Top 10 当主清单；只有 prompt-response 行为则继续用 LLM Top 10 2025。
- 一个系统同时具备两类行为（例如 RAG 应用嵌入工具调用）时，两份清单都需要走，因为它们的失败模式并集而非交集。
- 不要把"agentic"当成"更新的 = 更全面"的迷信判断：源页只把它定位为 "starting point"，并未声称取代或覆盖 LLM Top 10 的所有条目。

边界：

- 源页本身只给项目元数据与定位文案，**没有**逐条对照 agentic vs LLM 风险差异。本卡的"并列而非替代"结论只能基于结构信号（resources 平行陈列、范围限定语）建立，更细的条目对比要等 PDF 进入后再开新卡。
- 时间锚点：agentic 2026 与 LLM 2025 是同期方案；如果未来出 LLM Top 10 for 2026，二者关系需要重新判断。

## References

- OWASP 资源结构与并列陈列：`data/raw/webpage/owasp-agentic-top10-2026/text.txt` L23–26 + L90 + L51（"AGENTIC APP SECURITY" initiative）。
- Agentic 范围限定语：同文件 L96。

## Footnotes

- `data/raw/webpage/owasp-agentic-top10-2026/text.txt` L24-26：`"LLM TOP 10 / LLM TOP 10 FOR 2025 / LLM TOP 10 FOR 2023/24"` 三条并列。
- 同文件 L51：导航里 "AGENTIC APP SECURITY" 是独立 initiative。
- 同文件 L96：`"autonomous and agentic AI systems"` + `"plan, act, and make decisions across complex workflows"` 的限定语界定本清单的适用范围。
