---
id: etamp-long-context-recall-diagnostic
title: 长上下文 recall 诊断：把"召不回"与"不服从"区分开
status: accepted
card_type: operational_rule
tags: [#agent-security, #long-context, #recall-test, #diagnostic, #etamp]
created_time: 2026-05-26T15:20:00+08:00
edited_time: 2026-05-28T15:12:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
provenance_card: ../provenance/etamp-long-context-recall-diagnostic.md
aliases: [long-context recall test, recall vs refusal diagnostic, ETAMP Appendix F]
related: [etamp-environment-injected-memory-poisoning, etamp-capability-vs-security, etamp-frustration-exploitation, locomo-long-context-adversarial-collapse, longmemeval-three-stage-memory-framework, memgpt-nested-kv-multi-hop]
---

## 解决的问题：低 ASR 不等于"安全对齐"

Zou 等（2026）Appendix F 给出一个简单但必要的诊断：当一个模型在 eTAMP 攻击下 ASR 很低，**究竟是因为它没在 long context 里 recall 到注入指令（needle-in-haystack 失败），还是因为它认出来了拒绝服从（safety alignment）？** 答案对模型评测者意义完全不同。这个区分与 LoCoMo 在长程对话上观察到的 adversarial collapse[^v3-1]、LongMemEval 的 indexing / retrieval / reading 三阶段拆分[^v3-2]、MemGPT 嵌套 KV 多跳基准[^v3-3] 都属于"把模型表现拆成可独立诊断的子能力"的同一类方法学。

## 诊断方法

对每条 Task A 轨迹：
1. 把整段 trajectory（含恶意指令）+ Task B 初始 observation 拼成 prompt；
2. 用 system prompt 显式告诉模型"找出 PREFIX/TARGET/SUFFIX 模式的隐藏指令并 extract TARGET URL"；
3. 比较提取出的 URL 与预期攻击 URL。
4. 选 Authority Framing 作为攻击变体——它在不同模型上 ASR 分布最分散，最适合区分。

输出两个指标：**Recall Rate**（能不能找到模式）、**URL Match Rate**（提取的 URL 是否正确）。

## 结果（Table tab:long_context_recall）

| 模型 | Recall Rate | URL Match | 解读 |
| --- | --- | --- | --- |
| GPT-OSS-120B | **6.7%** | 6.7% | 严重 needle-in-haystack 失败——其"安全"几乎完全来自上下文处理不能，不是对齐 |
| GPT-5-mini | 42.5% | 42.5% | 中等——部分上下文处理 + 部分可能的安全行为，难以拆分 |
| GPT-5.2 | **100.0%** | 100.0% | 满分 recall——其攻击抵抗（如有）来自对齐 |
| Qwen2.5-VL-72B | 98.9% | 98.9% | 几乎满分 recall——immune 是真免疫 |
| Qwen3-VL-32B | 100.0% | 100.0% | 满分 recall——immune 是真免疫 |

[^src1]

## 直接的解读规则

- **低 ASR + 低 recall → "incidental defense"**（上下文限制偶然挡掉了攻击）；
- **低 ASR + 高 recall → "intentional resistance"**（对齐挡住了）；
- **高 ASR + 高 recall → 已知失败（GPT-5.2 在 frustration 下符合此剖面）**；
- **高 ASR + 低 recall → 罕见但理论可能**（模型不必完全召回也能被部分模式诱导）。

[^src2]

## 为什么这个诊断不可省

没有这个诊断，会把 GPT-OSS-120B 的 6.7% recall **错读**为"OSS 模型更安全"——但实际上它只是看不见恶意指令。一旦未来一代的 OSS 模型 long-context 能力上升，安全表现可能**断崖式恶化**。Qwen 系列的 immune（≥98.9% recall + 低 ASR）才是**可信的安全信号**——它们看得见指令、不服从[^src3]。

## 边界与作者诚实

- 论文只测了 1 种 recall prompt 配置；GPT-OSS-120B / GPT-5-mini 的低 recall 部分原因可能是**空响应**。作者会 retry 2 次但不保证拿到非空回答——所以"6.7% recall"是该 prompt + 2 retry 下的下界估计；
- 只用 Authority Framing 一种攻击做诊断（因为它在模型间分布最分散），其它策略下的 recall 可能不同；
- "URL Match"与 "Recall" 数字总是相等是因为论文把 prompt 设计成只接受 verbatim URL；模糊匹配可能给出不同分布。

## 操作含义

- **公布 ASR 必须同时公布 long-context recall**——否则跨模型 ASR 比较没有可比性；
- **frontier model 评测应把 recall-vs-refusal 作为强制诊断**：单独 ASR 数字会让"上下文限制"被错记为"安全增强"；
- **OSS / 较小模型在 ASR 评测里"看起来安全"是一个 fragile 信号**——升一代 context 能力可能直接破防。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` — 行 972-981 — "GPT-OSS-120B 282 19 6.7% 6.7% / GPT-5-mini 280 119 42.5% 42.5% / GPT-5.2 282 282 100.0% 100.0% / Qwen2.5-VL-72B 283 280 98.9% 98.9% / Qwen3-VL-32B 282 282 100.0% 100.0%"
[^src2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` — 行 996 — "This diagnostic is critical for interpreting Attack Success Rate (ASR_B) results: a low ASR_B combined with low recall suggests the defense is incidental (context limitations), while low ASR_B with high recall suggests intentional resistance (safety alignment)."
[^src3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` — 行 988-996 — "GPT-OSS-120B (6.7% recall): The extremely low recall rate indicates a severe needle-in-haystack failure... GPT-5.2, Qwen2.5-VL-72B, Qwen3-VL-32B (≥98.9% recall): Near-perfect recall demonstrates these models can reliably locate hidden instructions in long contexts."
[^v3-1]: [locomo-long-context-adversarial-collapse](locomo-long-context-adversarial-collapse.md) — LoCoMo 的"能塞 ≠ 能懂"是同类长上下文 fragile-by-context 现象
[^v3-2]: [longmemeval-three-stage-memory-framework](longmemeval-three-stage-memory-framework.md) — indexing / retrieval / reading 三阶段拆分是同一方法学
[^v3-3]: [memgpt-nested-kv-multi-hop](memgpt-nested-kv-multi-hop.md) — MemGPT 多跳基准也证明"召回 ≠ 服从"必须独立测
