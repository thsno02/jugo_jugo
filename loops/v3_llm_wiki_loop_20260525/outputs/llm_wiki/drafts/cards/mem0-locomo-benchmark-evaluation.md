---
id: mem0-locomo-benchmark-evaluation
title: Mem0 在 LOCOMO 上的评估：质量、token、延迟三轴的"性价比"故事
status: draft
card_type: source_claim
tags: [#memory, #mem0, #benchmark, #LOCOMO, #evaluation]
created_time: 2026-05-26T11:45:00+08:00
edited_time: 2026-05-26T11:45:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
provenance_card: ../provenance/mem0-locomo-benchmark-evaluation.md
aliases: [Mem0 LOCOMO results, LLM-as-Judge mem0, 91% p95 latency reduction]
related: [mem0-extract-update-pipeline, mem0-graph-memory-variant]
---

## 评估对象与指标

LOCOMO（Maharana 2024）：10 段长对话，平均 ~600 turns、~26k tokens，每段约 200 个问题，分四类：**single-hop / multi-hop / temporal / open-domain**（原 adversarial 类被排除，因 ground truth 缺失）。

Mem0 评估同时报告：

- **质量**：F1 (F1)、BLEU-1 (B1)、**LLM-as-a-Judge (J)**（每方法 10 次独立运行，报 mean ± 1σ）；
- **token**：用 `cl100k_base` 编码，统计检索阶段返回的 token 数；
- **延迟**：search latency（取 memories/chunks 的时间）+ total latency（含 LLM 生成）的 p50 与 p95。

## 主表数据（LLM-as-Judge）

| 方法 | Single-Hop J | Multi-Hop J | Open-Domain J | Temporal J |
| --- | --- | --- | --- | --- |
| LangMem | 62.23 | 47.92 | 71.12 | 23.43 |
| Zep | 61.70 | 41.35 | **76.60** | 49.31 |
| OpenAI (ChatGPT memory) | 63.79 | 42.92 | 62.29 | 21.71 |
| A-Mem* | 39.79 | 18.85 | 54.05 | 49.91 |
| **Mem0** | **67.13** | **51.15** | 72.93 | 55.51 |
| **Mem0g** | 65.71 | 47.19 | 75.71 | **58.13** |

要点：

- **Mem0** 在 single-hop、multi-hop 上是表中最高 J；
- **Mem0g** 在 temporal 上最高，open-domain 仅次于 Zep；
- OpenAI 在 temporal 上跌至 21.71，论文归因于"即便显式 prompt 要求带时间戳，多数生成记忆仍丢失时间戳"。

## 总分（Overall J）与 RAG / Full-context 对比

- **Full-context**（26k tokens 全塞进窗口）J ≈ 72.90 —— 最高，但 p50/p95 total latency = 9.870s / 17.117s；
- **最强 RAG 配置**（k=2, chunk=256）J ≈ 60.97；
- **Mem0** J ≈ 66.88，**Mem0g** J ≈ 68.44；
- 与 full-context 相比，**Mem0 的 p95 total latency 降低约 92%（17.117s → 1.440s），Mem0g 降低约 85%（→ 2.590s）**；
- 与最强 RAG 相比，Mem0/g 提升约 10–12% 的 J 分。

论文给出的 "26% relative improvement in LLM-as-Judge over OpenAI" 是 abstract 中的总结性数字，源自上述四类问题加权后与 OpenAI ChatGPT memory 的对比。

## token / 构建效率（vs Zep）

- **Mem0**：~7k tokens/对话；
- **Mem0g**：~14k tokens/对话；
- **Zep**：> 600k tokens/对话（每个图节点缓存全摘要 + 边上存事实导致大量冗余）；
- 原始 full-context：~26k tokens/对话；
- **Mem0g vs Zep**：约 43× 更少 token，存储与查询成本差距明显。

另：论文报告 Zep 添加记忆后**短时间**内即时检索经常答错，须等"几个小时"再 query 才好——猜测 Zep 内部有异步 LLM 图构建。Mem0 图构建在最坏情况下也小于 1 分钟，新记忆可立即用于查询。

## 论文未声称的事

- **不是 SOTA 全胜**：Zep 在 open-domain F1/J 仍有 ~1pp 优势；
- 不评估 adversarial / unanswerable 类问题；
- 不做长序列以外的多模态评估；
- 不报告 NOOP 比率，因此"语义抖动率"在论文中不可直接量化。

## References

- §4 主表（`sections/result.tex` 第 1047–1085 行）：四类题目质量对比。
- §4.3 / Table（第 1218–1264 行）：延迟与 token 总体比较，含 RAG/full-context/Zep/LangMem/OpenAI/Mem0/Mem0g 全部条目。
- §3.4 / §5（第 1313–1318 行）：token 总览，含 Zep 600k 与 Mem0 7k 的对比。
- abstract（`sections/abs.tex` 第 681–698 行）：26% over OpenAI、91% p95 lower latency、>90% token cost 节省的总体声明。
- 数据集说明 §3.1（`sections/experiment_setup.tex` 第 1010–1011 行）。
- 来源：`data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt`。

## Footnotes

[^1]: abstract 总体声明 verbatim（第 689–691 行）："Mem0 achieves 26% relative improvements in the LLM-as-a-Judge metric over OpenAI, while Mem0 with graph memory achieves around 2% higher overall score than the base Mem0 configuration. ... Mem0 attains a 91% lower p95 latency and saves more than 90% token cost."

[^2]: OpenAI temporal 跌幅原因原文（§4 `result.tex` 第 1212 行）："OpenAI notably underperforms, with scores below 15%, primarily due to missing timestamps in most generated memories despite explicit prompting in the OpenAI ChatGPT to extract memories with timestamps."

[^3]: Zep 异步图构建的运营观察原文（第 1316 行）："After adding memories to Zep's system, we observed that immediate memory retrieval attempts often failed to answer our queries correctly. Interestingly, re-running identical searches after a delay of several hours yielded considerably better results."
