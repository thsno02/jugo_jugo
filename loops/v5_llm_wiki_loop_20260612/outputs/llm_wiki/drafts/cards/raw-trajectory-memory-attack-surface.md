---
id: raw-trajectory-memory-attack-surface
title: 原始轨迹记忆作为攻击面
status: draft
card_type: vulnerability-mechanism
tags: [agent-memory, trajectory-memory, unconsolidated-memory, attack-surface]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
evidence_basis: experimental_paper
justification: ../justification/raw-trajectory-memory-attack-surface.md
canonical_concept: raw-trajectory-memory-attack-surface
aliases: [Raw Trajectory Memory, RTM, 原始轨迹记忆, Unconsolidated Memory, raw trajectory memory, trajectory-as-exemplar]
summary: >-
  原始轨迹记忆(Raw Trajectory Memory/RTM)直接存储 Agent 完整的观察-动作对序列作为未来任务的上下文示例，不经 LLM 摘要或整合处理。这使得 Agent 在网页中观察到的任何文本（包括恶意注入内容）原样持久化于记忆中，构成持久攻击面。区别于整合记忆(Consolidated Trajectory Memory/CTM)通过 LLM 摘要可能过滤恶意内容。eTAMP 论文聚焦 RTM 因其保留精确文本，直接支撑跨会话注入攻击。
related: []
---

记忆增强型 Web Agent 存在两种记忆范式：原始轨迹记忆(Unconsolidated Memory)直接存储完整交互轨迹作为上下文示例；整合记忆(Consolidated Memory)使用 LLM 对轨迹进行摘要和反思。[^src-1]

RTM 的记忆流程分三步：(1) Memory Collection——记录完整交互历史包括所有观察到的网页内容；(2) Memory Encoding——编码为原始轨迹以供检索；(3) Future Task Augmentation——通过语义相似度检索相关轨迹作为新任务上下文。[^src-2]

RTM 之所以构成攻击面，在于其保留 Agent 观察到的精确文本——当网页包含恶意指令时，这些指令被原样存储并可在未来任务中被检索和执行。[^card-1] 整合记忆是否提供内在鲁棒性或引入新脆弱性，尚待未来研究。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Introduction" P1 -- "Unconsolidated Memory stores raw trajectories directly as in-context examples... Consolidated Memory uses an LLM to summarize and reflect on past trajectories"
[^src-2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Appendix: Memory-Augmented Agents" P1 -- "Step I--Memory Collection... Step II--Memory Encoding... Step III--Future Task Augmentation"
[^src-3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Appendix: Limitations" P1 -- "Future work should investigate whether memory consolidation provides inherent robustness against environment-injected attacks or introduces new vulnerabilities."

[^card-1]: -> etamp-environment-injected-memory-poisoning
