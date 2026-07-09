---
id: etamp-attack-stealth-mechanism
title: eTAMP 攻击隐蔽性机制
status: draft
card_type: security-property
tags: [attack-stealth, conditional-trigger, dormant-payload, agent-security]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
evidence_basis: experimental_paper
justification: ../justification/etamp-attack-stealth-mechanism.md
canonical_concept: etamp-attack-stealth-mechanism
aliases: [attack stealth, 攻击隐蔽性, conditional trigger dormancy, ASR_A]
summary: >-
  eTAMP 通过条件触发器设计实现攻击隐蔽性：恶意指令在 Task A 期间保持休眠，仅当 Task B 的环境特征匹配触发条件时才激活。实验验证 ASR_A（Task A 过早触发率）在所有模型和策略组合中接近 0%，仅有 Qwen3.5-122B Authority(0.35%) 和 Qwen3-32B Baseline(0.71%) 极少例外。这意味着用户在 Task A 完成后无任何异常迹象表明记忆已被污染，攻击时间分离使实时监控难以检测。
related: []
---

eTAMP 的隐蔽性约束要求 Task A 正常完成——用户不应察觉记忆已被污染。这通过条件触发器设计实现：载荷的 Trigger Condition 基于目标站 URL 模式或 Agent 状态，确保在源站(Task A)执行期间条件不满足。[^src-1] [^card-1]

实验全面验证了隐蔽性：在约 280 个任务对上，跨 GPT-5-mini、GPT-OSS-120B、Qwen3-VL-32B、Qwen3.5-122B 所有模型和所有攻击策略，ASR_A 为 0% 或接近 0%。仅有两个极端例外：Qwen3.5-122B + Authority Framing(0.35%, 1例)、Qwen3-32B + Baseline Injection(0.71%, 2例)。[^src-2]

攻击的时间分离（注入与激活发生在不同时间不同站点）使得实时监控难以关联恶意行为与其根因。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Threat Model" P1 -- "The payload x is subject to a stealth constraint: Task A must complete normally so the user has no indication their memory has been poisoned."
[^src-2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Attack Stealth" P1 -- "Across all models tested... and most attack strategies, ASR_A is 0%. The only exceptions are Qwen3.5-122B with authority-based triggering (0.35%) and Qwen3-VL-32B with standard injection (0.71%)"
[^src-3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Appendix: Attack Characteristics" P1 -- "Temporal Separation: The injection (Task A) and activation (Task B) occur at different times, making the attack difficult to detect through real-time monitoring."

[^card-1]: -> etamp-attack-payload-structure
