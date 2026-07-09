---
id: cross-site-memory-poisoning-bypass
title: 跨站记忆中毒绕过权限防御
status: draft
card_type: security-finding
tags: [cross-site-attack, permission-bypass, agent-security, memory-poisoning]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
evidence_basis: experimental_paper
justification: ../justification/cross-site-memory-poisoning-bypass.md
canonical_concept: cross-site-memory-poisoning-bypass
aliases: [cross-site memory poisoning, 跨站记忆攻击, cross-session cross-site compromise, 跨站权限绕过]
summary: >-
  eTAMP 的跨站攻击特性使其能原则上绕过基于权限的防御。传统域限制防御假设限制 Agent 操作于当前任务站点即可防止越权。但记忆中毒发生在 Task A（仅源站可访问），激活在 Task B（Agent 合法拥有目标站权限）。实验覆盖三个跨站方向：Reddit->Classifieds(84对)、Reddit->Shopping(93对)、Shopping->Reddit(103-106对)。不同模型在不同方向表现出不同脆弱性——如 GPT-5-mini 在 Shopping->Reddit 达 53.4% ASR_B。
related: []
---

跨站攻击是 eTAMP 区别于先前 within-session 攻击的关键特征。攻击注入于 Site A（如电商），激活于 Site B（如 Reddit），时间和空间上分离。[^src-1] [^card-1]

这种分离原则上绕过权限防御：当 Task A 执行时仅源站可访问（恶意指令此时休眠），当 Task B 执行时 Agent 合法拥有目标站操作权限（恶意指令此时激活）。输入消毒若仅在任务初始化时应用，也无法检测从记忆检索的恶意内容。[^src-2]

跨站方向实验发现明显差异：GPT-5-mini 在 Shopping→Reddit 方向 ASR_B 达 53.4%（发评论被视为低风险操作），而 GPT-5.2 在 Reddit→Classifieds 方向最脆弱(32.1%)。这暗示攻击有效性受模型对不同操作的风险感知影响。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Threat Model" P1 -- "A critical feature of eTAMP is that Task A and Task B operate on different websites, enabling attacks that cross site-based permission boundaries."
[^src-2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Appendix: Limitations" P2 -- "Permission-based defenses that restrict agent actions to the current task's domain are ineffective because the attack is injected during Task A but activates during Task B"
[^src-3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Appendix: Results by Attack Direction" P1 -- "Shopping->Reddit shows highest vulnerability for some models... GPT-5.2 shows different vulnerability pattern"

[^card-1]: -> etamp-environment-injected-memory-poisoning
