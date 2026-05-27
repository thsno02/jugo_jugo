---
id: cognition-skill-loop-evidence-to-teaching
title: Cognition 的"证据 → 巩固 → 衰减 → 教学"四步技能闭环
status: accepted
card_type: mechanism
tags: [#agent-memory, #team-knowledge, #skill-as-artifact, #cognition]
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-27T14:38:00+08:00
edited_entity: llm
source_ids: [cognitionus-llm-wiki-guide]
provenance_card: ../provenance/cognition-skill-loop-evidence-to-teaching.md
aliases: [Cognition skill loop, evidence to skill, agent team brain loop]
related: [cognition-human-approved-skill-md, file-outputs-back-as-compounding-loop, idea-file-as-agent-era-artifact, knowledge-compounding-three-mechanisms, llm-wiki-mcp-skills-vs-tools-workflow]
---

## "产品就是闭环，不是仪表盘"

Cognition 主张面向编码 agent 的团队记忆**不是上下文堆栈**，而是一个 4 步、连续运转的闭环：

| 步骤 | 行为 | 何时触发 |
| --- | --- | --- |
| **01 Ask first**（先问） | 任务开始时 agent 先查询团队**已经解决过**的相似问题 | 任务起点 |
| **02 Capture work**（捕获工作） | 命令、文件编辑、卡点、结果作为证据流被记录为可复用工作流的原材料 | 任务进行中 |
| **03 Save skills**（保存技能） | Cognition 起草 SKILL.md 并**等待人审 yes** 才向团队公开 | 工作结束、确认有价值后 |
| **04 Retrieve later**（后续取用） | 下一个 agent（如同事 Bob）遇到同类墙时，加载前一作者（Alice）的修复方案 | 下次相似任务 |

页面用了一个具体场景串起这个闭环：Alice 在 Claude Code 中解决了 Vercel 的 `.env` 生产配置错配问题（"vercel --prod failed → .env production mismatch → build passed after fix"），系统把这些证据 → 起草草稿 `vercel-env-scoping` → 等待 Alice 的人审 → Bob 后来在同样问题上撞墙，agent 立即拉出 "Using Alice's deploy fix"。

## 与"通用公司大脑"的差异

Cognition 把自己定位为**与"generic company brain"对立**：

- 通用公司大脑只是把上下文堆起来；
- Cognition 把**工作本身**当作**学习信号**，把会话/操作压缩为"被人类审核过的技能"，并对其建立**新鲜度与结果历史**。

页面给出的四个对位机制：

1. **Evidence**：prompts、files、tool calls、decisions、outcomes 成为**类型化的学习事件**；
2. **Consolidation**：raw traces 经 LLM 压缩为带步骤、检查项、失败模式的 SKILL，须经人审；
3. **Decay**：召回率和新鲜度按时间建模，**陈旧指引会自动让位或刷新**；
4. **Teaching**：下一个 agent 收到的不是"一堆 notes"，而是一条**路径**——哪个 skill、出自谁的判断、如何应用。

## 写卡的三个安全/治理承诺

- **Confirm-first capture**：草稿不直接进团队库，需明确人审通过才保存——避免 agent 自动把私人或未确认的内容暴露给团队。
- **Person-specific retrieval**：skill 携带"谁教的、为什么这位作者的判断有效"，让 agent 跟随**正确的品味**，而非平均化推荐。
- **Group-code setup**：一个队员创建 group，其他人用同样 code 加入，开始共享记忆——这是 onboarding 的最小协议。

## 适用边界

- 面向**编码 agent + 团队**场景；solo 个人也可用，但主张随着团队加入累积"复用收据与结果"。
- 仅文本/操作类型的技能（命令、文件编辑、决策、结果），未涉及视觉/二进制工件。
- 页面是产品宣传材料，**未公开**衰减算法、新鲜度具体度量与 person-specific 检索的实现细节。

## References

- 来源页面：`data/raw/webpage/cognitionus-llm-wiki-guide/text.txt`。
- 第 49–107 行：4 步闭环（SKILL LOOKUP / EVIDENCE LOG / DRAFT SKILL / AGENT CONTEXT）。
- 第 112–146 行："Memory that decays, consolidates, and teaches back" 与四对位机制。

## Footnotes

[^1]: 闭环 4 步小标题原文（第 60–107 行）："Ask first / Capture work / Save skills / Retrieve later"，对应正文 "At task start, the agent checks what your team has already figured out" 等四段描述。

[^2]: 与公司大脑对位原文（第 116 行）："Generic company brains store context. Cognition treats work as learning signal: sessions become approved skills, skills get freshness and outcome history, and agents retrieve executable guidance instead of a pile of notes."

[^3]: Confirm-first capture 原文（第 136 行）："Cognition drafts skills and waits for explicit approval before saving anything to the group."
