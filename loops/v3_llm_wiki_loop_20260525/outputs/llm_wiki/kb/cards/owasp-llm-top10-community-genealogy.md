---
id: owasp-llm-top10-community-genealogy
title: OWASP Top 10 for LLM Applications：从社区议题列表到 LLM 安全治理坐标
status: accepted
card_type: concept
tags: [#llm, #security, #owasp, #governance]
created_time: 2026-05-26T11:35:00+08:00
edited_time: 2026-05-28T15:42:00+08:00
edited_entity: llm
source_ids: [owasp-llm-top10-2025]
provenance_card: ../provenance/owasp-llm-top10-community-genealogy.md
aliases: ["OWASP LLM Top 10", "OWASP GenAI Top 10"]
related: [owasp-genai-landscape-2026q2, owasp-agentic-top10-2026-positioning, owasp-agentic-vs-llm-top10-2025, nist-ai-rmf-gai-profile, microsoft-agent-governance-standards-alignment, microsoft-agent-governance-eight-packages]
---

OWASP 的 *Top 10 for LLM Applications* 不是某个机构发布的安全标准，而是一份**社区驱动**的"当下最值得防的 LLM 相关风险清单"[^src1]。它在 2023 年首版，2024 年 11 月 17 日推出 2025 版，由 OWASP GenAI 项目维护。它的存在意义在于：在缺乏成熟法规与认证框架的阶段，给 LLM 应用开发者与安全工程师一个**共享的优先级坐标**——讨论 prompt injection、训练数据泄漏、不安全输出处理时，可以直接引用一个被业界广泛认可的编号体系，而不必每次重新定义术语。NIST AI 600-1 GAI Profile[^v3-1] 在 voluntary 政府框架一侧扮演同等坐标的角色；二者一同被微软 Agent Governance Toolkit[^v3-2] 列为对齐对象，可见这套"坐标→工具"链路的工程闭环。

从 2023 到 2025 这两年里，OWASP 的工作向外辐射出多个相关项目：AI Security Landscape、AIBOM Generator、Governance Checklist、Threat Intelligence、Agentic App Security、Secure AI Adoption、AI Red Teaming、Data Security[^src2]。这些不是 Top 10 本身的内容，而是围绕 Top 10 形成的**治理周边**——表明 OWASP 在 2026 年的工作重心已经从"列举漏洞"扩展到"列举防御与采购参考"，例如 Q2 2026 发布的 AI Security Solutions Landscape 系列[^v3-3]（For LLM and Gen AI Apps、For Agentic AI、For LLM and Gen AI Apps + Agentic Red Teaming）。微软 Toolkit 的八包结构[^v3-4] 是把这一治理体系工程化的具体案例。

作为一份清单它的局限同样明显：

- Top 10 列表会随版本变化，**不能把"某项不在当年 Top 10"当成"该风险已解决"**。
- 它的更新节奏跟不上 LLM 攻击面的演化（如 Agentic AI、知识图谱投毒等新方向），需要配套使用 Landscape 系列与 Threat Intelligence 报告；agentic 维度由独立的 Agentic Top 10[^v3-5] 补齐。
- OWASP 的所有内容默认 CC BY-SA 4.0[^src3]，可自由引用与改写，但 Top 10 不构成审计合规标准——把它当审计依据需另行映射到企业自己的控制框架。

## Footnotes

[^src1]: `data/raw/webpage/owasp-llm-top10-2025/text.txt` — 行 96 — "The OWASP Top 10 for Large Language Model Applications started in 2023 as a community-driven effort to highlight and address security issues specific to AI applications."
[^src2]: `data/raw/webpage/owasp-llm-top10-2025/text.txt` — 行 42-58 — "Project Initiatives" 区块：列出 AI Security Landscape / AIBOM Generator / Governance Checklist / Threat Intelligence / Agentic App Security / Secure AI Adoption / AI Red Teaming / Data Security 八项 initiative
[^src3]: `data/raw/webpage/owasp-llm-top10-2025/text.txt` — 行 156-158 — CC BY-SA 4.0 许可与免责声明
[^v3-1]: [nist-ai-rmf-gai-profile](nist-ai-rmf-gai-profile.md) — voluntary 政府框架一侧的同等"共享坐标"
[^v3-2]: [microsoft-agent-governance-standards-alignment](microsoft-agent-governance-standards-alignment.md) — 把 OWASP / NIST / EU AI Act / SOC 2 同列为对齐对象
[^v3-3]: [owasp-genai-landscape-2026q2](owasp-genai-landscape-2026q2.md) — 围绕 Top 10 形成的"防御方案地图"
[^v3-4]: [microsoft-agent-governance-eight-packages](microsoft-agent-governance-eight-packages.md) — 把治理周边工程化为 8 包的具体案例
[^v3-5]: [owasp-agentic-top10-2026-positioning](owasp-agentic-top10-2026-positioning.md) — agentic 维度由独立清单补齐
