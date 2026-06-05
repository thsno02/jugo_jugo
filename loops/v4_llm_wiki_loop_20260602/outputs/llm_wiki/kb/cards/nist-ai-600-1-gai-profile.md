---
id: nist-ai-600-1-gai-profile
title: NIST AI 600-1 生成式 AI 风险管理框架概况
status: accepted
card_type: source_claim
tags: [nist, ai-risk-management, generative-ai, governance, eo-14110, framework-profile]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [nist-gai-profile]
justification: ../justification/nist-ai-600-1-gai-profile.md
canonical_concept: nist-ai-600-1-gai-profile
aliases: [NIST AI 600-1, GAI Profile, 生成式AI风险管理概况, Generative AI Profile]
summary: >-
  nist-ai-600-1-gai-profile（NIST AI 600-1 / GAI Profile / 生成式AI风险管理概况）
  NIST 于 2024 年 7 月发布 AI 600-1，作为 AI RMF 1.0 的跨部门生成式 AI 概况文件，
  依据行政令 EO 14110 编制，旨在为组织将可信赖性纳入 AI 全生命周期提供自愿性指南
related: [agent-governance-standards-mapping, ai-rmf-voluntary-trustworthiness]
---

NIST AI 600-1 是美国国家标准与技术研究院（NIST）于 2024 年 7 月 26 日发布的一份跨部门（cross-sectoral）概况文件，定位为 AI 风险管理框架（AI RMF 1.0）针对生成式 AI 的配套资源 [^src-1]。该文件的编制依据是拜登总统签署的第 14110 号行政令（Executive Order 14110），主题为"安全、可靠和可信赖的人工智能" [^src-1]。

AI RMF 1.0 本身于 2023 年 1 月发布，设计为自愿性（voluntary）使用框架，核心目标是提升组织在 AI 产品、服务和系统的设计、开发、使用和评估中融入可信赖性考量的能力 [^src-2]。AI 600-1 作为 GAI Profile 的意义在于：将通用框架的原则具体化到生成式 AI 这一特定技术领域，同时保持跨行业适用性（"cross-sectoral"），而非仅针对某一垂直行业 [^src-3]。

文件的关键概念域包括：AI 生命周期（AI Lifecycle）、AI 行为者（AI Actor）以及 GAI 风险（GAI Risk）[^src-3]。

AI RMF 1.0 的自愿性设计和可信赖性核心定位为该概况文件提供了基本框架哲学 [^card-2]。在操作化层面，Microsoft Agent Governance Toolkit 将治理控制显式映射到 NIST AI RMF 1.0 的全部四个功能域，展示了该框架的一种工程实践路径 [^card-1]。

## Footnotes

[^src-1]: `data/raw/webpage/nist-gai-profile/text.txt` -- Abstract L219 -- "This document is a cross-sectoral profile of and companion resource for the AI Risk Management Framework (AI RMF 1.0) for Generative AI, pursuant to President Biden's Executive Order (EO) 14110 on Safe, Secure, and Trustworthy Artificial Intelligence."
[^src-2]: `data/raw/webpage/nist-gai-profile/text.txt` -- Abstract L219 -- "The AI RMF was released in January 2023, and is intended for voluntary use and to improve the ability of organizations to incorporate trustworthiness considerations into the design, development, use, and evaluation of AI products, services, and systems."
[^src-3]: `data/raw/webpage/nist-gai-profile/text.txt` -- Keywords L241 -- "Artificial Intelligence, AI, Risk Management Framework, Generative AI, Cross-sectoral profile, AI Lifecycle, AI Actor, GAI, GAI Risk"
[^card-1]: [Agent 治理标准合规映射](agent-governance-standards-mapping.md) -- Microsoft Agent Governance Toolkit 将治理控制映射到 NIST AI RMF 的全部四个功能域，展示了该框架的一种操作化实现
[^card-2]: [AI RMF 的自愿性与可信赖性导向](ai-rmf-voluntary-trustworthiness.md) -- 本卡聚焦 AI 600-1 概况文件的编制背景和跨行业定位，该卡聚焦其母体框架 AI RMF 1.0 的自愿性设计和可信赖性核心
