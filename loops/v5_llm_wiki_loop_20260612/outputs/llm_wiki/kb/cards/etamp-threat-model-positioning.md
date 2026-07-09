---
id: etamp-threat-model-positioning
title: eTAMP 威胁模型与先前工作的定位区分
status: accepted
card_type: comparative-analysis
tags:
- threat-model
- agent-security
- memory-attack
- related-work
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-etamp-memory-poisoning
evidence_basis: experimental_paper
justification: ../justification/etamp-threat-model-positioning.md
canonical_concept: etamp-threat-model-positioning
aliases:
- eTAMP vs prior work
- 威胁模型对比
- memory attack taxonomy
summary: eTAMP 在 agent/memory 安全研究中独特定位：(1) 无需直接记忆访问（vs AgentPoison 需直接操纵知识库）；(2)
  单用户记忆模型（vs MINJA/CrAIBench 假设用户间共享记忆）；(3) 交互式沙箱环境（vs InjecAgent/AgentPoison 离线数据集）；(4)
  跨会话持久攻击（vs WASP/RedTeamCUA/WIPI 仅单会话）。eTAMP 是唯一同时满足交互式环境+跨会话的工作。先前最接近的 WASP 虽用交互环境但仅测
  within-session 攻击。
related:
- cross-site-memory-poisoning-bypass
- etamp-environment-injected-memory-poisoning
- poisonedrag-threat-model
- graphrag-defense-evasion
---

eTAMP 在 agent 安全领域的定位通过与先前工作的系统对比体现：[^src-1] [^card-1]

**需直接记忆/知识库访问的工作**:
- AgentPoison: 假设攻击者可直接操纵知识库/长期记忆，嵌入后门记录
- PoisonedRAG: 向 RAG 管道注入损坏文本
- BadChain: 假设攻击者可访问和操纵用户提示的 chain-of-thought 示例

**假设跨用户共享记忆的工作**:
- MINJA: 不需直接记忆访问但假设攻击者和用户共享记忆——现实中用户通常有独立记忆库
- CrAIBench: 同样假设共享记忆，且仅限加密货币场景

**仅单会话/无记忆持久性的工作**:
- InjecAgent/AgentDojo: 单次注入即执行，无跨会话
- WASP: 最接近本文（交互式沙箱），但仅测 within-session 攻击，未验证原始轨迹记忆可作跨站攻击载体
- WIPI: 高 ASR(>90%) 但聚焦单会话
- RedTeamCUA: 混合沙箱但仅单任务

eTAMP 独特组合：真实环境注入 + 单用户记忆 + 交互式环境 + 跨会话持久性。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Related Work" Table 2 -- "Comparison of agent & memory security benchmarks"
[^src-2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Related Work" P_last -- "Our work differs from prior studies in three key ways: (1) Realistic threat model... (2) Single-user memory model... (3) Persistent vs. immediate impact"

[^card-1]: -> etamp-environment-injected-memory-poisoning
