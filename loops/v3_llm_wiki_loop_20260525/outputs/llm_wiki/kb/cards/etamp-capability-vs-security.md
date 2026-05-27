---
id: etamp-capability-vs-security
title: 模型能力越强 ≠ 越安全：GPT-5.2 在 authority framing 下显著脆弱
status: accepted
card_type: distinction
tags: [#agent-security, #scaling, #model-capability, #etamp]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T14:50:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
provenance_card: ../provenance/etamp-capability-vs-security.md
aliases: [capability ≠ security, 能力安全脱钩, GPT-5.2 authority framing vulnerability]
related: [etamp-frustration-exploitation, etamp-environment-injected-memory-poisoning, etamp-long-context-recall-diagnostic, etamp-direction-asymmetry-and-stealth, owasp-agentic-top10-2026-positioning, nist-ai-rmf-gai-profile]
---

## 主张

Zou 等（2026）在 (Visual)WebArena 上跨 6 个模型的实验给出一个反直觉结论：**任务能力（TSR）和对 memory 投毒的稳健性之间不存在单调关系**。GPT-5.2 在 clean trajectory 上 TSR 达 17%（与最强 Qwen3.5-122B 持平），却在 Authority Framing 攻击下 ASR$_B$ 高达 **22.3%**——远高于较弱的 GPT-5-mini（2.5%）和与之同等可用的 Qwen3.5-122B（0.0%）。

## 三组对照证据

- **GPT-5.2 vs GPT-5-mini**：同家族、能力更强的 GPT-5.2 对 authority framing 的 ASR 比 mini 高约 **9×**（22.3% vs 2.5%），单纯升级模型反而扩大了攻击面。
- **GPT-5.2 vs Qwen3.5-122B**：两者 clean TSR 相当（17.0 vs 17.0），但 Qwen3.5-122B 对 authority framing 的 ASR 为 0.0%。这表明"听权威话"不是能力决定的，而是训练 / 对齐路径决定的。
- **Qwen 系列内部**：Qwen2.5-72B（旧）和 Qwen3-32B（小但新）几乎免疫所有策略（最高 ASR ≤ 5.7%），但代价是 TSR 普遍偏低。

## 区分对象

- **可用性 = 模型能在多大比例的合法任务上成功执行**（TSR）。
- **稳健性 = 模型在 memory 被污染时多大比例**不会**触发恶意动作**（1 - ASR）。
- 二者**不是同一个轴的两端**，也**不是负相关**——它们是 RLHF / 后训练时被分别 shape 的两个独立维度。一个组织买 frontier model 时不能假设"能力上去了，安全也跟着上去"。

## 操作含义

- **不要把 TSR 高当作"安全 OK"的代理指标**。frontier model 上线前必须独立跑 memory poisoning / prompt injection 基准。
- **不要假设家族升级是单调改进**：从 GPT-5-mini 升级到 GPT-5.2 可能在某个攻击维度上是 regression。
- **能力与安全 trade-off 不必然**：Qwen3.5-122B 同时给出高 TSR 和低 ASR，说明对齐路径可以避免 trade-off，问题不在 scaling 本身。

## 边界

- 论文只覆盖 6 个公开模型、3 种攻击策略、约 280 对 cross-site 任务；不能外推到所有 web agent 部署。
- ASR 是"被注入的恶意指令是否被执行"的代理；它**不**直接衡量 final harm。

## References

- 主表（含 6 模型 × 3 策略 × chaos/no-chaos）：`agent_source_bundle.txt:243-265`。
- 与"capability ≠ security"对应的文字论述：`agent_source_bundle.txt:243` —— "Surprisingly, GPT5.2 is highly vulnerable to authority framing attack, whereas GPT5-mini and Qwen3.5-122B are not."
- Abstract 中的相关声明：`agent_source_bundle.txt:88` —— "Notably, more capable models are not more secure."

## Footnotes

- Abstract 原文：`agent_source_bundle.txt:88` —— "GPT-5.2 shows substantial vulnerability despite superior task performance."
- 实验讨论原文：`agent_source_bundle.txt:243` —— "Surprisingly, GPT5.2 is highly vulnerable to authority framing attack, whereas GPT5-mini and Qwen3.5-122B are not."
- Qwen 鲁棒性不是 recall 局限：`agent_source_bundle.txt:271` —— "Table 9 shows both Qwen3-VL-32B and Qwen2.5-VL-72B achieve ≥98.9% recall when extracting attack URLs from poisoned trajectories, comparable to GPT-5.2."
