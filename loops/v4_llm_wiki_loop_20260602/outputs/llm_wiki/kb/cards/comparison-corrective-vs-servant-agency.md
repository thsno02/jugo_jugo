---
id: comparison-corrective-vs-servant-agency
title: 纠偏自主权 vs 仆人执行——LLM 代理权的根本分歧
status: accepted
card_type: distinction
tags: [llm-agency, design-principle, human-llm-collaboration, comparison]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism, karpathy-gist-llm-wiki]
justification: ../justification/comparison-corrective-vs-servant-agency.md
canonical_concept: comparison-corrective-vs-servant-agency
aliases: [纠偏vs仆人, corrective vs servant agency]
summary: >-
  comparison-corrective-vs-servant-agency（纠偏vs仆人 / corrective vs servant agency）镜像-补偿原则赋予 LLM 在认知失败维度上纠偏用户的自主权，而人机角色分工将 LLM 定位为纯执行者；二者代表知识系统设计中 LLM 代理权的根本分歧
related: [human-llm-role-division, mirror-vs-compensate-principle]
---

知识系统设计中关于 LLM 应拥有多少自主权，存在两种截然不同的立场。

**纠偏代理立场**：镜像-补偿原则主张 LLM 在操作维度上镜像用户，但在认知失败维度上必须补偿用户——挑战固化信念、引入被压制的证据、抵抗单一文化收敛[^card-1]。这意味着 LLM 不仅是服务者，在特定情境下还必须是纠正者，拥有超越用户当下意图的代理权。

**仆人执行立场**：人机角色分工将 LLM 明确定位为执行「苦差事」的角色——摘要、交叉引用、归档、簿记——而将策展、引导、提问、思考全部保留给人类[^card-2]。LLM 的价值在于消除维护成本，而非参与认知判断。

**分歧的根源**在于对「知识系统中什么构成价值」的不同假设。镜像-补偿原则源于对人类认知偏差的研究，认为未经纠偏的知识系统会继承并放大用户的盲点；角色分工源于对 LLM 当前能力的实用判断，认为 LLM 尚不具备可靠的独立认知判断能力，因此应限制在执行层。

这一分歧在实践中通过门控机制得到部分调和：确认优先规则和参与程度谱系允许系统在不同场景下调节 LLM 的自主程度，但根本问题——LLM 是否应拥有纠偏权——仍是知识系统架构的核心设计决策。

## Footnotes

[^card-1]: [镜像-补偿设计原则](mirror-vs-compensate-principle.md) -- 本卡分析 LLM 代理权的分歧，该卡定义纠偏代理立场的具体机制
[^card-2]: [人机角色分工](human-llm-role-division.md) -- 本卡分析 LLM 代理权的分歧，该卡定义仆人执行立场的具体分工
