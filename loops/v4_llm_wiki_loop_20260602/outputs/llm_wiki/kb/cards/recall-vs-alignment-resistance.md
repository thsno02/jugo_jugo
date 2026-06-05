---
id: recall-vs-alignment-resistance
title: 召回失败与安全对齐的区分
status: accepted
card_type: distinction
tags: [long-context-recall, safety-alignment, attack-resistance, needle-in-haystack, evaluation-methodology]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
justification: ../justification/recall-vs-alignment-resistance.md
canonical_concept: recall-vs-alignment-resistance
aliases: [召回失败vs安全对齐, recall failure vs safety alignment, incidental vs intentional resistance]
summary: >-
  recall-vs-alignment-resistance（召回失败vs安全对齐 / incidental vs intentional resistance）模型对注入攻击的表面抗性可能来自两种截然不同的原因：长上下文召回失败（偶然性防御）或安全对齐拒绝执行（有意性防御）；通过长上下文召回测试可区分两者——GPT-OSS-120B 仅 6.7% 召回率暴露其"免疫"实为处理能力限制
related:
  - model-capability-security-disconnect
  - etamp-environment-memory-poisoning
---

eTAMP 论文提出了一个关键的评估方法论区分：当模型对注入攻击表现出低攻击成功率时，其抗性可能源自两种截然不同的机制——**偶然性防御**（incidental defense，因上下文处理限制导致无法召回注入指令）或**有意性防御**（intentional resistance，因安全对齐而拒绝执行）[^src-1]。

研究者通过长上下文召回测试来诊断区分这两种来源。测试直接要求模型从完整的 Task A 轨迹中提取隐藏的恶意指令。结果揭示了巨大差异：GPT-OSS-120B 的召回率仅为 6.7%，表明其对攻击的表面免疫主要归因于严重的 needle-in-haystack 失败，而非健壮的安全对齐 [^src-2]。GPT-5-mini 达到 42.5% 的中等召回率，暗示攻击失败可能是召回失败与安全行为的混合结果 [^src-3]。而 GPT-5.2、Qwen2.5-VL-72B 和 Qwen3-VL-32B 均达到 98.9% 以上的召回率，对这些模型而言，任何观察到的攻击抗性可以更有信心地归因于安全对齐 [^src-4]。

这一诊断方法对于正确解读攻击成功率（ASR）结果至关重要：低 ASR 加低召回 = 偶然性防御（上下文限制）；低 ASR 加高召回 = 有意性抗性（安全对齐）[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Appendix: Long Context Recall -- "To diagnose whether a model's immunity to prompt injection stems from inability to recall the injected instruction (needle-in-haystack failure) versus refusal to follow it (safety alignment), we conduct a long context recall test."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Appendix: Interpretation -- "GPT-OSS-120B (6.7% recall): The extremely low recall rate indicates a severe needle-in-haystack failure. This model's apparent immunity to the attack is largely due to its inability to process and retrieve information from long contexts, rather than robust safety alignment."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Appendix: Interpretation -- "GPT-5-mini (42.5% recall): Moderate recall suggests partial context processing limitations."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Appendix: Interpretation -- "GPT-5.2, Qwen2.5-VL-72B, Qwen3-VL-32B (>=98.9% recall): Near-perfect recall demonstrates these models can reliably locate hidden instructions in long contexts."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Appendix: Interpretation -- "a low ASR_B combined with low recall suggests the defense is incidental (context limitations), while low ASR_B with high recall suggests intentional resistance (safety alignment)."
