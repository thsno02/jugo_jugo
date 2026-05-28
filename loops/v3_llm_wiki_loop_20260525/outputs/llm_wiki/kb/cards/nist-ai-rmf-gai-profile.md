---
id: nist-ai-rmf-gai-profile
title: NIST AI 600-1 是 AI RMF 1.0 针对生成式 AI 的跨行业 profile
status: accepted
card_type: source_claim
tags: [#nist, #ai-rmf, #generative-ai, #risk-management]
created_time: 2026-05-26T14:55:00+08:00
edited_time: 2026-05-28T15:48:00+08:00
edited_entity: llm
source_ids: [nist-gai-profile]
provenance_card: ../provenance/nist-ai-rmf-gai-profile.md
aliases: [NIST AI 600-1, GAI Profile, AI RMF Generative AI Profile]
related: [owasp-llm-top10-community-genealogy, microsoft-agent-governance-standards-alignment, owasp-agentic-top10-2026-positioning]
---

## 这份文档是什么

NIST 在 2024-07-26 发布 `Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile`（报告编号 `NIST AI 600-1`）[^src2]，作为 2023-01 发布的 **AI RMF 1.0** 的"配套资源 / 跨行业 profile"，专门对应生成式 AI 的风险面[^src1]。它与 OWASP LLM Top 10[^v3-1] 在 voluntary / 政府框架与 community / 项目清单两侧扮演同等的"共享坐标"角色，并一同被微软 Agent Governance Toolkit[^v3-2] 列为对齐对象。

关键定位：

- **它是 cross-sectoral profile**（跨行业 profile），不是 AI RMF 的替代——AI RMF 1.0 仍然是基础，本文档是按"生成式 AI 这一类技术"为视角的剪裁与扩展。
- **它响应 EO 14110**——美国总统 Biden 2023 年的 *Safe, Secure, and Trustworthy AI* 行政令。也就是说它是行政令落地的具体技术产物之一[^src1]。
- **属性是"voluntary use"**——AI RMF 系列在美国是自愿采纳的框架，不是强制法规，目的是"帮组织把可信性考虑纳入 AI 产品/服务/系统的设计、开发、使用与评估"[^src1]。这与 OWASP Agentic Top 10[^v3-3] 同属"自愿采用、社区/政府层共享坐标"路线；与 EU AI Act / SOC 2 等强制法规体系在微软 Toolkit 的合规对齐表[^v3-2] 里并列。

## 用这张卡时要注意

- 本卡只从 NIST publications 索引页文本提取——具体的"风险类目、控制项、操作建议"在 PDF 全文里，索引页只有 abstract。要引用具体控制项必须读 600-1 PDF 本身。
- "AI Actor / GAI Risk"等术语都是 NIST 自家词汇表，与欧盟 AI Act 不直接对应；做合规对照需另查。

## Footnotes

[^src1]: `data/raw/webpage/nist-gai-profile/text.txt` — 行 219 — "This document is a cross-sectoral profile of and companion resource for the AI Risk Management Framework (AI RMF 1.0) for Generative AI, pursuant to President Biden's Executive Order (EO) 14110 on Safe, Secure, and Trustworthy Artificial Intelligence. The AI RMF was released in January 2023, and is intended for voluntary use and to improve the ability of organizations to incorporate trustworthiness considerations into the design, development, use, and evaluation of AI products, services, and systems."
[^src2]: `data/raw/webpage/nist-gai-profile/text.txt` — 行 208-235 — 标题、报告号 `NIST AI 600-1`、DOI `10.6028/NIST.AI.600-1`、发布日期 2024-07-26、第一作者 Chloe Autio 等元数据
[^v3-1]: [owasp-llm-top10-community-genealogy](owasp-llm-top10-community-genealogy.md) — community 一侧的"共享坐标"对偶
[^v3-2]: [microsoft-agent-governance-standards-alignment](microsoft-agent-governance-standards-alignment.md) — 把 NIST AI RMF 与 OWASP / EU AI Act / SOC 2 同列为可机器核验对齐对象
[^v3-3]: [owasp-agentic-top10-2026-positioning](owasp-agentic-top10-2026-positioning.md) — 同属自愿采用类社区/政府共享坐标
