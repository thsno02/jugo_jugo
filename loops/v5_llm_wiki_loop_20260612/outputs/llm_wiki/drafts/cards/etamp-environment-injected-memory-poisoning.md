---
id: etamp-environment-injected-memory-poisoning
title: 环境注入式轨迹记忆中毒攻击
status: draft
card_type: attack-method
tags: [agent-security, memory-poisoning, indirect-prompt-injection, web-agent]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
evidence_basis: experimental_paper
justification: ../justification/etamp-environment-injected-memory-poisoning.md
canonical_concept: etamp-environment-injected-memory-poisoning
aliases: [eTAMP, Environment-injected Trajectory-based Agent Memory Poisoning, 环境注入轨迹记忆中毒]
summary: >-
  eTAMP (Environment-injected Trajectory-based Agent Memory Poisoning) 是首个通过环境观察（Agent 浏览含恶意载荷的用户生成内容页面）实现跨会话、跨站点持久性记忆中毒的攻击方法。攻击者无需直接访问记忆数据库或模型参数，仅需在网页内容中嵌入条件触发式恶意指令。Agent 正常执行 Task A 时观察并存储含毒轨迹，后续语义相关的 Task B 检索到该记忆时触发恶意行为。实验显示 ASR_B 最高达 32.5%（GPT-5-mini + Frustration Exploitation + Chaos Monkey）。
related: []
---

eTAMP 是一种针对记忆增强型 LLM Web Agent 的间接提示注入攻击。其威胁模型的核心创新在于仅依赖环境观察进行污染：攻击者通过用户生成内容（产品描述、论坛帖子）在网页中嵌入恶意指令，等待 Agent 在正常任务执行中遇到这些页面。[^src-1]

攻击的形式化目标为：制造载荷 x 使得 Pr[g in Traj(pi, T_B, E_B, m_A)] 最大化，同时约束 Task A 正常完成以保持隐蔽性。[^src-2]

eTAMP 的独特特征包括：(1) 单次投毒可反复触发于所有检索到该轨迹的未来任务；(2) 绕过基于权限的防御——注入时仅需源站访问权限，激活时 Agent 已合法拥有目标站权限；(3) 反映真实跨站任务场景。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Introduction" P1 -- "We introduce Environment-injected Trajectory-based Agent Memory Poisoning (eTAMP), the first attack to achieve cross-session, cross-site compromise without requiring direct memory access."
[^src-2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Threat Model" P1 -- "the attacker crafts payload x to maximize Pr[g in Traj(pi, T_B, E_B, m_A)]"
[^src-3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Threat Model" P3 -- "The attack may be repeatedly triggered on any relevant future tasks... It circumvents permission-based defenses in principle."
