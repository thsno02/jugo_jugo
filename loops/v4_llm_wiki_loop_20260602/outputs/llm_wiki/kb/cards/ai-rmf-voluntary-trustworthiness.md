---
id: ai-rmf-voluntary-trustworthiness
title: AI RMF 的自愿性与可信赖性导向
status: accepted
card_type: concept
tags: [ai-rmf, trustworthiness, voluntary-framework, governance, nist]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [nist-gai-profile]
justification: ../justification/ai-rmf-voluntary-trustworthiness.md
canonical_concept: ai-rmf-voluntary-trustworthiness
aliases: [AI RMF 自愿性框架, voluntary AI governance, AI 可信赖性框架]
summary: >-
  ai-rmf-voluntary-trustworthiness（AI RMF 自愿性框架 / voluntary AI governance / AI 可信赖性框架）
  NIST AI RMF 1.0 定位为自愿性使用框架，不具备法律强制力，其核心目标是帮助组织在 AI 全生命周期
  （设计、开发、使用、评估）中系统性融入可信赖性考量
related: [agent-governance-standards-mapping, deterministic-policy-enforcement, nist-ai-600-1-gai-profile]
---

NIST AI 风险管理框架（AI RMF 1.0）于 2023 年 1 月发布，其设计定位明确为"自愿性使用"（intended for voluntary use），不具备法律强制力 [^src-1]。这一设计选择意味着框架的采纳取决于组织自身意愿，而非监管合规义务。

框架的核心目标是"提升组织将可信赖性考量纳入 AI 产品、服务和系统的设计、开发、使用和评估的能力" [^src-1]。可信赖性（trustworthiness）被置于框架的中心位置，覆盖 AI 生命周期的四个阶段：设计（design）、开发（development）、使用（use）和评估（evaluation）[^src-1]。

值得注意的是，虽然框架本身是自愿性的，但行政令 EO 14110 将其作为生成式 AI 概况文件的基础框架予以引用 [^src-2]，这在事实上提升了框架的权威性和实践影响力。自愿性框架通过行政指令间接获得准规范地位，是治理工具演进中的常见模式。AI 600-1 正是在此基础上将通用框架原则具体化为生成式 AI 领域的跨行业风险管理指南 [^card-2]。

在操作化层面，确定性策略执行机制为框架中的可信赖性目标提供了可审计、可重现的技术保证 [^card-1]。Microsoft Agent Governance Toolkit 进一步将该框架四个功能域（GOVERN/MAP/MEASURE/MANAGE）的全部要求映射到自动合规证明机制 [^card-3]。

## Footnotes

[^src-1]: `data/raw/webpage/nist-gai-profile/text.txt` -- Abstract L219 -- "The AI RMF was released in January 2023, and is intended for voluntary use and to improve the ability of organizations to incorporate trustworthiness considerations into the design, development, use, and evaluation of AI products, services, and systems."
[^src-2]: `data/raw/webpage/nist-gai-profile/text.txt` -- Abstract L219 -- "pursuant to President Biden's Executive Order (EO) 14110 on Safe, Secure, and Trustworthy Artificial Intelligence"
[^card-1]: [确定性策略执行](deterministic-policy-enforcement.md) -- Microsoft 工具包通过确定性规则引擎而非概率性 LLM 判断来执行治理策略，为自愿性框架的落地提供可重现的技术基础
[^card-2]: [NIST AI 600-1 生成式 AI 风险管理框架概况](nist-ai-600-1-gai-profile.md) -- 本卡聚焦 AI RMF 1.0 的自愿性定位和可信赖性导向，该卡聚焦该框架在生成式 AI 领域的具体化概况文件 AI 600-1
[^card-3]: [Agent 治理标准合规映射](agent-governance-standards-mapping.md) -- 本卡描述 AI RMF 的自愿性设计哲学，该卡展示 Microsoft 如何将该框架四个功能域操作化为自动合规映射
