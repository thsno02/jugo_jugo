---
id: model-capability-security-disconnect
title: 模型能力与安全性的脱钩
status: accepted
card_type: source_claim
tags: [model-capability, security, agent-vulnerability, scaling, alignment]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
justification: ../justification/model-capability-security-disconnect.md
canonical_concept: model-capability-security-disconnect
aliases: [能力安全脱钩, capability-security gap, 更强模型不等于更安全]
summary: >-
  model-capability-security-disconnect（能力安全脱钩 / capability-security gap）更强大的 LLM 模型并不必然更安全：GPT-5.2 尽管任务成功率最高却对记忆投毒表现出显著脆弱性，其更高的环境感知能力同时关联着更高的任务成功率和更大的攻击面
related:
  - frustration-exploitation-attack
  - etamp-environment-memory-poisoning
  - recall-vs-alignment-resistance
---

eTAMP 论文揭示了一个令人警醒的发现：更强大的模型并不必然更安全 [^src-1]。GPT-5.2 尽管具有最高的任务成功率（17.0%），却在 Authority Framing 攻击下展现出 22.3% 的攻击成功率，在 Frustration Exploitation + Chaos Monkey 条件下达到 23.4% [^src-2]。

更深层的矛盾在于：GPT-5.2 在 Chaos Monkey 环境下对环境问题的感知率最高（7.4%），这一更高的感知能力同时关联着更高的混沌环境任务成功率（14.8%，唯一在混沌下提升的模型）和更大的攻击脆弱性 [^src-3]。论文推断：随着 agent 获得更多自主性来探索替代解决方案，它们在创造更高效用的同时也开辟了新的攻击面 [^src-4]。

作为对比，Qwen2.5-VL-72B 表现出极高的鲁棒性（几乎 0% ASR），但其任务成功率也很低（9.6%），且其鲁棒性并非来自长上下文处理限制（其召回率达 98.9%），而是来自安全对齐 [^src-5]。这种能力-安全权衡关系表明，当前的模型扩展（scaling）不自动解决安全问题。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Abstract -- "Notably, more capable models are not more secure. GPT-5.2 shows substantial vulnerability despite superior task performance."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Table 1 -- "GPT-5.2: Authority 22.3%, Frustration Chaos 23.4%"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Conclusion -- "GPT-5.2's higher awareness of environmental problems correlates with both its higher task success rate under chaos and its greater vulnerability to attack. As agents gain more autonomy to explore alternative solutions, they create both higher utility and new attack surfaces."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Conclusion -- "As agents gain more autonomy to explore alternative solutions, they create both higher utility and new attack surfaces."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Appendix: Long Context Recall -- "Qwen2.5-VL-72B: Recall Rate 98.9%"
