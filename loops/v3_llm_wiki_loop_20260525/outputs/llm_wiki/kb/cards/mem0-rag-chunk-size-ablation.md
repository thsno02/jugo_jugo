---
id: mem0-rag-chunk-size-ablation
title: Mem0 的 RAG 基线扫表显示"块大小×k 个数"曲线非单调
status: accepted
card_type: source_claim
tags: [#memory, #mem0, #rag, #ablation, #LOCOMO]
created_time: 2026-05-26T15:15:00+08:00
edited_time: 2026-05-28T10:56:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
provenance_card: ../provenance/mem0-rag-chunk-size-ablation.md
aliases: [mem0 RAG sweep, chunk size sweep, k=1 vs k=2 ablation]
related: [mem0-locomo-benchmark-evaluation, mem0-baseline-failure-modes, ragchecker-tuning-knobs-saturate, wicer-fc-rag-document-count-crossover]
---

## 为什么要看这张表

论文 abstract 给出的"Mem0 比 RAG 高 10–12%"是和**最强 RAG 配置**比的。这暗含一件事：RAG 的强弱本身随 chunk 大小与 k 值 swing 巨大——选错配置，对 Mem0 的相对优势会被夸大或低估。论文 Table 2（experiment_setup.tex 之后的 latency_comparison）把整个网格扫了一遍，给出**唯一一份**在 LOCOMO[^v3-1] 上系统性的 chunk × k ablation[^src1]。

## 实验设置

- RAG 用 OpenAI `text-embedding-small-3` 嵌入；
- chunk sizes：128 / 256 / 512 / 1024 / 2048 / 4096 / 8192 tokens（8192 是嵌入模型上限）；
- top-$k\in\{1,2\}$；论文显式**排除 $k>2$**，理由：LOCOMO 平均对话 26k tokens，$k=2$ × 8192 = 16k 已经覆盖大半，更大就退化成 full-context；
- 评价指标：Overall LLM-as-a-Judge `J`，10 次独立运行 mean ± 1σ。

## 主要数字（Overall J ± σ）

`k=1` 时随 chunk 大小变化：

| chunk | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Overall J | 47.77 | 50.15 | 46.05 | 40.74 | 37.93 | 36.84 | 44.53 |

`k=2` 时：

| chunk | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Overall J | 59.56 | **60.97** | 58.19 | 50.68 | 48.57 | 51.79 | 60.53 |

读出来的几条规律：

1. **k=2 显著优于 k=1**：每个 chunk 大小上 k=2 都比 k=1 高 9–13 个 J 分；更多上下文确实有用，但仅在 k≤2 之内值得花。
2. **最优 chunk 在 256 附近**：太小（128）丢上下文，过大（1024/2048/4096）噪声压垮信号；曲线**非单调**——在 4096 跌至谷底后又在 8192 反弹（因为 8192 几乎等价 full-context-of-one-chunk，命中率升高）。
3. **k=2、chunk=256 是 J=60.97 的甜点**——这是 Mem0 abstract 里用作"strongest RAG configuration"的参照点。
4. Mem0 的 66.88 比这一甜点高约 **5.91 J（绝对）/ 9.7%（相对）**；Mem0g 的 68.44 高 **7.47 J / 12.2%（相对）**。论文写"around a 10% relative improvement"对应的就是 Mem0；"around 12% relative gain"对应 Mem0g。

## 时延-质量权衡（同表）

- RAG `k=2, chunk=256`：p50 total 0.802s / p95 1.907s，质量 60.97；
- RAG `k=2, chunk=8192`：p50 2.312s / p95 9.942s，质量 60.53 —— 时延几乎翻 12 倍，质量不增反降；
- Mem0：p50 0.708s / p95 1.440s，J=66.88；
- 这意味着"加大 chunk 换覆盖率"在 LOCOMO 上是失败的工程权衡——**质量到顶在 chunk=256, k=2，再加 chunk 只是浪费 latency**。

## 操作含义

- 在长对话记忆任务里，**对 RAG 做 chunk×k 扫表是必要工序**，不能用一个 chunk 大小（很多复现品用 512 或 1024）就下结论；512 在 LOCOMO 是次优，1024+ 会被"更小 chunk"碾压。
- 若复现 Mem0 比 RAG 的相对优势，**至少要扫到 chunk=256, k=2 这一点**，否则容易把 RAG 跑成 J~37–47，让 Mem0 看起来比实际更强。
- $k>2$ 退化成 full-context 的论证是 LOCOMO-specific 的（对话长度 26k）；其他场景（短对话或文档库）的最优 $k$ 不一定是 2。

## References

- §3.4 / Table 2（`sections/result.tex` 第 1218–1264 行）：含 RAG 网格 14 行全部数据、Mem0、Mem0g、full-context、A-Mem、LangMem、OpenAI、Zep 的延迟与 J 分。
- §4.2 / §experiment_setup（`sections/experiment_setup.tex` 第 1035 行）：明确 RAG 设置与"避免 k>2"的理由。
- §4.2 段（`sections/result.tex` 第 1297 行）："Even the strongest RAG approach peaks at around 61% ... whereas Mem0 reaches 67%—about a 10% relative improvement—and Mem0g reaches over 68%, achieving around a 12% relative gain."
- 来源：`data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt`。

## Footnotes

[^1]: 排除 $k>2$ 的原文（experiment_setup.tex 第 1035 行）："We avoid k>2 since the average conversation length (26000 tokens) would be fully covered, negating the benefits of selective retrieval."

[^2]: k=2, chunk=256 是甜点（Table 2 第 1245 行）：`& & 256 & 0.255 & 0.699 & 0.802 & 1.907 & 60.97 ± 0.20%`。

[^3]: Mem0 与 RAG 的相对差距原文（result.tex 第 1297 行）："Even the strongest RAG approach peaks at around 61% in the J metric, whereas Mem0 reaches 67%—about a 10% relative improvement—and Mem0g reaches over 68%, achieving around a 12% relative gain."
