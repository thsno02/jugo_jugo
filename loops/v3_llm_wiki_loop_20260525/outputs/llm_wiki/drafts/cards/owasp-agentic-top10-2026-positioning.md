---
id: owasp-agentic-top10-2026-positioning
title: OWASP Agentic Top 10 (2026) 的定位与受众
status: draft
card_type: source_claim
tags: [#owasp, #agent-security, #governance, #risk-framework]
created_time: 2026-05-26T11:30:00+08:00
edited_time: 2026-05-26T11:30:00+08:00
edited_entity: llm
source_ids: [owasp-agentic-top10-2026]
provenance_card: ../provenance/owasp-agentic-top10-2026-positioning.md
aliases: ["OWASP Top 10 for Agentic Applications", "agentic risk top 10"]
related: [owasp-agentic-vs-llm-top10-2025, owasp-llm-top10-community-genealogy, owasp-genai-landscape-2026q2, microsoft-agent-governance-standards-alignment, nist-ai-rmf-gai-profile, etamp-environment-injected-memory-poisoning]
---

OWASP GenAI Security Project 在 2025 年 12 月 9 日发布的 **OWASP Top 10 for Agentic Applications 2026**，是 OWASP 在传统 LLM Top 10 之外、面向 agentic / 自治 AI 系统单列的一份风险清单。要点（按源页的官方描述还原，不外推内容）：

- **范围**：面向"能 plan、act、make decisions across complex workflows 的 agentic AI 系统"，与单轮 prompt-response 类 LLM 应用区分开。这是它和 OWASP 已有的 "LLM Top 10 for 2025"、"LLM Top 10 for 2023/24" 三者并列的根本原因——agentic 应用的失败模式不能用早期 LLM Top 10 覆盖。
- **过程**：源页明确写出"globally peer-reviewed framework"，依靠 100 名以上行业专家、研究者、从业者的协作产出。这一点意味着它的权威性靠社区评审而不是单一作者立场。
- **作用层**：源页把它定位成"distilling a broad ecosystem of OWASP GenAI Security guidance into an accessible, operational format"——一份把分散的指南压成可操作起点的清单。换言之，它是入门导航 + 决策起点，不是穷举手册。
- **受众**：源页同时点出三类——builders（构建者）、defenders（防御者）、decision-makers（决策者）。设计这三类同时阅读，意味着它在抽象层应当"可被工程师落到具体控制、可被管理层用来对齐采购/治理判断"。
- **配套位置**：在 OWASP GenAI Security Project 的 resources 体系里，它与 "AI Security Solutions Landscape for Agentic AI Q2 2026"、"AI Security Landscape"、"AI Red Teaming"、"Threat Intelligence" 等 initiative 互相补位；Top 10 是触达层，landscape / red teaming 等是支撑研究。

操作含义：

- 作为入门级 baseline 清单，应当与 OWASP "LLM Top 10 for 2025" 并行使用，**不互相替代**——传统 LLM Top 10 仍处理 prompt injection、output handling、supply chain 等共性风险；agentic Top 10 才补齐"自治决策与多步执行"维度的新风险。
- 引用者要注意：源页本身只给出元数据 + 项目定位 + 下载入口；具体 10 条目内容需要通过页面 "Download" 链接的 PDF 获取，不能仅凭这条 web 文案展开任何具体风险条目的论断。

## References

- OWASP 项目页对该清单的描述：`data/raw/webpage/owasp-agentic-top10-2026/text.txt` L90–98（"About" 段）。
- 发布日期与配套资源位置：同文件 L92, L100–118。
- 受众三类：同文件 L96（builders / defenders / decision-makers）。

## Footnotes

- `data/raw/webpage/owasp-agentic-top10-2026/text.txt` L96：`"The OWASP Top 10 for Agentic Applications 2026 is a globally peer-reviewed framework that identifies the most critical security risks facing autonomous and agentic AI systems."` 同段：`"Developed through extensive collaboration with more than 100 industry experts, researchers, and practitioners"`；`"By distilling a broad ecosystem of OWASP GenAI Security guidance into an accessible, operational format, the Top 10 equips builders, defenders, and decision-makers with a clear starting point"`。
- 同文件 L92：`"December 9, 2025"`（发布日期）。
- 同文件 L24-26：项目页同时列出"LLM TOP 10 FOR 2025"与"LLM TOP 10 FOR 2023/24"作为并列条目。
