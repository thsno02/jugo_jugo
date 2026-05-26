---
id: longmemeval-five-core-memory-abilities
title: LongMemEval 把"长期记忆"切成五种能力，KU/ABS 是它独有的
status: draft
card_type: concept
tags: [#long-term-memory, #benchmark, #evaluation]
created_time: 2026-05-26T14:20:00+08:00
edited_time: 2026-05-26T14:20:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
provenance_card: ../provenance/longmemeval-five-core-memory-abilities.md
aliases: [IE, MR, KU, TR, ABS, LongMemEval 五能力]
related: [locomo-three-task-evaluation-framework, longmemeval-three-stage-memory-framework, longmemeval-benchmark-construction-pipeline, longmemeval-commercial-system-failure-modes, zep-dmr-benchmark-critique]
---

## 五种能力

LongMemEval（Wu et al., ICLR 2025）认为以前的 long-term dialogue benchmark（MemoryBank、PerLTQA、LoCoMo、DialSim）覆盖不全，把"chat assistant 的长期记忆"显式切成 5 类核心能力，再以 7 种问题类型对应：

1. **Information Extraction (IE)**——能回忆 user 或 assistant 在历史 session 里讲过的具体细节。
2. **Multi-Session Reasoning (MR)**——能跨多个 session 综合信息（聚合、比较）。
3. **Knowledge Updates (KU)**——能识别 user 个人信息的变化，把"上次说的"覆盖成"这次说的"。
4. **Temporal Reasoning (TR)**——既要利用 session 的 timestamp metadata，也要解析 user 句子里的时间引用（"上周末"）。
5. **Abstention (ABS)**——对 history 里根本没有的信息，拒答 "I don't know"，不要编。

7 个具体 question type：`single-session-user`、`single-session-assistant`、`single-session-preference`、`multi-session`、`knowledge-update`、`temporal-reasoning`、`abstention`。

## 为什么这套划分有意义

- **KU 和 ABS 是 LoCoMo / MemoryBank / PerLTQA 都不测的能力**。KU 直接对标"用户信息会改变"这件事——这是真实助手记忆最容易出 bug 的地方（ChatGPT 在论文 pilot study 里被发现"会随后续聊天篡改之前记下的事实"，反映的就是 KU 失败）。ABS 测的是反幻觉——常被忽略，但用户对"不会瞎编"的容忍度比"答对"还低。
- **single-session-assistant** 是另一个常被遗漏的维度——以前的 benchmark 一般只问"用户说过什么"，不问"模型自己说过什么"，但实际产品里"上次你给我推荐了哪家餐厅"是高频需求。

## 边界

- 这 5 类是"功能性"切分，不直接映射到任何特定记忆架构（key-value、graph、hierarchical），因此它评测的是黑盒结果，不是机制。
- ABS 只有 30 题（从其他类型修改成 false-premise），样本小；过度调优 abstention 容易拖低其它指标。

## References

- 五能力定义：`data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` 第 1363-1369 行（IE/MR/KU/TR/ABS 五条要点）。
- 七问题类型：第 1371 行。
- 与既有 benchmark 对比表：第 977-984 行（MSC / DuLeMon / MemoryBank / PerLTQA / LoCoMo / DialSim / LongMemEval 在 IE/MR/KU/TR/ABS 上的覆盖）。

## Footnotes

- 原文五条要点之 KU："Ability to recognize the changes in the user's personal information and update the knowledge of the user dynamically over time."（第 1366 行）
- ABS："Ability to identify questions seeking unknown information, i.e., information not mentioned by the user in the interaction history, and answer ``I don't know''."（第 1368 行）
- ChatGPT 在 KU 上失败的 pilot 观察："ChatGPT generally records the evidence statements immediately after it has been presented ... However, as the interaction proceeds, ChatGPT often modify this information when it compresses the history, resulting in information loss."（第 1629 行）
