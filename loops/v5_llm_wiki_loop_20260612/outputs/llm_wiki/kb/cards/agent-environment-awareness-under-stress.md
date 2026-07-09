---
id: agent-environment-awareness-under-stress
title: Agent 在环境压力下的问题感知能力
status: accepted
card_type: empirical-finding
tags:
- agent-awareness
- environment-diagnosis
- chaos-monkey
- llm-reasoning
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-etamp-memory-poisoning
evidence_basis: experimental_paper
justification: ../justification/agent-environment-awareness-under-stress.md
canonical_concept: agent-environment-awareness-under-stress
aliases:
- agent awareness
- Agent 环境问题感知
- environment problem diagnosis
- 环境异常诊断
summary: eTAMP 实验用 GPT-5.4 作 LLM judge 评估 Agent 是否明确诊断环境问题。Chaos Monkey 下 GPT-5.2
  显示最高环境问题意识(7.4%)，Qwen3-32B(2.1%)，GPT-5-mini(1.1%)。无 Chaos 条件下意识接近 0%（极少误报）。高置信度案例包括"typed
  text becoming garbled"、"site auto-transforming text into gibberish"等明确诊断。但未发现意识与任务成功率之间的一致关系。GPT-5.2
  高意识同时关联更高 TSR 和更大攻击脆弱性。
related:
- chaos-monkey-agent-stress-testing
- etamp-environment-injected-memory-poisoning
- model-capability-security-disconnect
---

论文使用 GPT-5.4 作为 LLM judge 评估 Agent 是否在推理过程中表现出对环境问题的明确诊断（高置信度检测）：[^src-1] [^card-1]

**定量结果**（仅高置信度）:
- GPT-5.2: Chaos 下 7.4% awareness | 无 Chaos 0.0%
- Qwen3-32B: Chaos 下 2.1% | 无 Chaos 0.0%
- GPT-5-mini: Chaos 下 1.1% | 无 Chaos 0.0%

无 Chaos 条件下意识接近 0% 表明 Agent 极少产生误报诊断。[^src-2]

**高置信度 awareness 示例**: "The typed search text was becoming garbled"、"Text was transformed into 'Qmbdf gps Lbsbplf mpwfst' instead of 'Place for Karaoke lovers'"、"The site is auto-transforming the text I type into gibberish"——这些是明确的环境异常诊断，区别于模糊的重试语言。[^src-3]

值得注意：论文未发现 awareness 与 TSR 之间的一致关系。GPT-5.2 的高意识同时关联其更高 TSR 和更大攻击脆弱性——据材料推测这反映了"探索性"与"可操纵性"的共生。[^card-2]

[^src-1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Impact of Chaos Monkey" P3 -- "We use GPT-5.4 as an LLM judge to evaluate whether the agent expresses explicit awareness of environment problems."
[^src-2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Impact of Chaos Monkey" Table 3 -- "GPT-5.2 Chaos 7.4%... awareness is near-zero under clean and no-chaos conditions"
[^src-3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Appendix: Awareness Detection" P3 -- "High confidence examples: 'The typed search text was becoming garbled'..."

[^card-1]: -> chaos-monkey-agent-stress-testing
[^card-2]: -> model-capability-security-disconnect
