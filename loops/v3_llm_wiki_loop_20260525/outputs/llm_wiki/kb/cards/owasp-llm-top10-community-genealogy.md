---
id: owasp-llm-top10-community-genealogy
title: OWASP Top 10 for LLM Applications：从社区议题列表到 LLM 安全治理坐标
status: accepted
card_type: concept
tags: [#llm, #security, #owasp, #governance]
created_time: 2026-05-26T11:35:00+08:00
edited_time: 2026-05-27T15:24:00+08:00
edited_entity: llm
source_ids: [owasp-llm-top10-2025]
provenance_card: ../provenance/owasp-llm-top10-community-genealogy.md
aliases: ["OWASP LLM Top 10", "OWASP GenAI Top 10"]
related: [owasp-genai-landscape-2026q2, owasp-agentic-top10-2026-positioning, owasp-agentic-vs-llm-top10-2025, nist-ai-rmf-gai-profile, microsoft-agent-governance-standards-alignment, microsoft-agent-governance-eight-packages]
---

OWASP 的 *Top 10 for LLM Applications* 不是某个机构发布的安全标准，而是一份**社区驱动**的"当下最值得防的 LLM 相关风险清单"。它在 2023 年首版，2024 年 11 月 17 日推出 2025 版，由 OWASP GenAI 项目维护。它的存在意义在于：在缺乏成熟法规与认证框架的阶段，给 LLM 应用开发者与安全工程师一个**共享的优先级坐标**——讨论 prompt injection、训练数据泄漏、不安全输出处理时，可以直接引用一个被业界广泛认可的编号体系，而不必每次重新定义术语。

从 2023 到 2025 这两年里，OWASP 的工作向外辐射出多个相关项目：AI Security Landscape、AIBOM Generator、Governance Checklist、Threat Intelligence、Agentic App Security、Secure AI Adoption、AI Red Teaming、Data Security。这些不是 Top 10 本身的内容，而是围绕 Top 10 形成的**治理周边**——表明 OWASP 在 2026 年的工作重心已经从"列举漏洞"扩展到"列举防御与采购参考"，例如 Q2 2026 发布的 AI Security Solutions Landscape 系列（For LLM and Gen AI Apps、For Agentic AI、For LLM and Gen AI Apps + Agentic Red Teaming）。

作为一份清单它的局限同样明显：

- Top 10 列表会随版本变化，**不能把"某项不在当年 Top 10"当成"该风险已解决"**。
- 它的更新节奏跟不上 LLM 攻击面的演化（如 Agentic AI、知识图谱投毒等新方向），需要配套使用 Landscape 系列与 Threat Intelligence 报告。
- OWASP 的所有内容默认 CC BY-SA 4.0，可自由引用与改写，但 Top 10 不构成审计合规标准——把它当审计依据需另行映射到企业自己的控制框架。

## References

- 项目页：OWASP Top 10 for LLM Applications 2025，发布日期 November 17, 2024（`data/raw/webpage/owasp-llm-top10-2025/text.txt`，第 90–96 行）。
- 周边项目列表见同页 "Project Initiatives" 区块（同文件 L42–58）。
- Landscape 系列发布信息（Q2 2026）见同页 L100–118。
- 许可与免责声明见 L156–158。

## Footnotes

- L96：*"The OWASP Top 10 for Large Language Model Applications started in 2023 as a community-driven effort to highlight and address security issues specific to AI applications."*
- L100–118：列出 2026 年 3–4 月发布的三份 AI Security Solutions Landscape 资源。
- L156–158：CC BY-SA 4.0 许可条款。
