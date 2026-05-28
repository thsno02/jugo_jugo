---
id: longmemeval-five-core-memory-abilities
title: LongMemEval 把"长期记忆"切成五种能力，KU/ABS 是它独有的
status: accepted
card_type: concept
tags: [#long-term-memory, #benchmark, #evaluation]
created_time: 2026-05-26T14:20:00+08:00
edited_time: 2026-05-28T10:30:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
provenance_card: ../provenance/longmemeval-five-core-memory-abilities.md
aliases: [IE, MR, KU, TR, ABS, LongMemEval 五能力]
related: [locomo-three-task-evaluation-framework, longmemeval-three-stage-memory-framework, longmemeval-benchmark-construction-pipeline, longmemeval-commercial-system-failure-modes, zep-dmr-benchmark-critique]
---

## 五种能力

LongMemEval（Wu et al., ICLR 2025）认为以前的 long-term dialogue benchmark（MemoryBank、PerLTQA、LoCoMo[^v3-1]、DialSim）覆盖不全，把"chat assistant 的长期记忆"显式切成 5 类核心能力，再以 7 种问题类型对应[^src1]：

1. **Information Extraction (IE)**——能回忆 user 或 assistant 在历史 session 里讲过的具体细节。
2. **Multi-Session Reasoning (MR)**——能跨多个 session 综合信息（聚合、比较）。
3. **Knowledge Updates (KU)**——能识别 user 个人信息的变化，把"上次说的"覆盖成"这次说的"[^src2]。
4. **Temporal Reasoning (TR)**——既要利用 session 的 timestamp metadata，也要解析 user 句子里的时间引用（"上周末"）。
5. **Abstention (ABS)**——对 history 里根本没有的信息，拒答 "I don't know"，不要编[^src3]。

7 个具体 question type：`single-session-user`、`single-session-assistant`、`single-session-preference`、`multi-session`、`knowledge-update`、`temporal-reasoning`、`abstention`。

## 为什么这套划分有意义

- **KU 和 ABS 是 LoCoMo / MemoryBank / PerLTQA 都不测的能力**[^src4]。KU 直接对标"用户信息会改变"这件事——这是真实助手记忆最容易出 bug 的地方（ChatGPT 在论文 pilot study 里被发现"会随后续聊天篡改之前记下的事实"[^src5]，详见商用系统失败模式卡[^v3-2]）。ABS 测的是反幻觉——常被忽略，但用户对"不会瞎编"的容忍度比"答对"还低；这与 LoCoMo adversarial 题在长上下文 LLM 上掉到 2.1% 是同一类问题[^v3-3]。
- **single-session-assistant** 是另一个常被遗漏的维度——以前的 benchmark 一般只问"用户说过什么"，不问"模型自己说过什么"，但实际产品里"上次你给我推荐了哪家餐厅"是高频需求。

## 边界

- 这 5 类是"功能性"切分，不直接映射到任何特定记忆架构（key-value、graph、hierarchical），因此它评测的是黑盒结果，不是机制。
- ABS 只有 30 题（从其他类型修改成 false-premise），样本小；过度调优 abstention 容易拖低其它指标。
- Zep 后续论文也指出 DMR 等老 benchmark 区分度不足，与 LongMemEval 五能力的论证方向一致[^v3-4]。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 1363-1369 行 — IE/MR/KU/TR/ABS 五条要点；第 1371 行 — 七问题类型。
[^src2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 1366 行 — "Ability to recognize the changes in the user's personal information and update the knowledge of the user dynamically over time."
[^src3]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 1368 行 — "Ability to identify questions seeking unknown information, i.e., information not mentioned by the user in the interaction history, and answer ``I don't know''."
[^src4]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 977-984 行 — 与既有 benchmark 对比表（MSC / DuLeMon / MemoryBank / PerLTQA / LoCoMo / DialSim / LongMemEval 在 IE/MR/KU/TR/ABS 上的覆盖）。
[^src5]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 1629 行 — "ChatGPT generally records the evidence statements immediately after it has been presented ... However, as the interaction proceeds, ChatGPT often modify this information when it compresses the history, resulting in information loss."
[^v3-1]: [locomo-three-task-evaluation-framework](locomo-three-task-evaluation-framework.md) — LoCoMo 三任务作为对比的代表 benchmark。
[^v3-2]: [longmemeval-commercial-system-failure-modes](longmemeval-commercial-system-failure-modes.md) — ChatGPT KU 失败的具体观察。
[^v3-3]: [locomo-long-context-adversarial-collapse](locomo-long-context-adversarial-collapse.md) — adversarial / abstention 的同根问题在长上下文 LLM 上的表现。
[^v3-4]: [zep-dmr-benchmark-critique](zep-dmr-benchmark-critique.md) — Zep 对 DMR 区分度不足的批评，方向与 LongMemEval 一致。
