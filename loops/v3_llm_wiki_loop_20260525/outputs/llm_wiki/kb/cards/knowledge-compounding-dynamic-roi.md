---
id: knowledge-compounding-dynamic-roi
title: 知识复利让 Agentic ROI 的成本项从常量变为时间函数 Cost(t)
status: accepted
card_type: mechanism
tags: [#agentic-roi, #knowledge-compounding, #llm-wiki, #economics]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-knowledge-compounding]
provenance_card: ../provenance/knowledge-compounding-dynamic-roi.md
aliases: [动态 Agentic ROI, Cost(t) 模型, H(t) 覆盖率]
related: [knowledge-compounding-three-mechanisms]
---

## 核心主张

Wen 与 Ku（2026）指出，Liu 等人提出的 Agentic ROI 原始方程在成本项上隐含了一个未被检验的假设——**每个任务的成本相互独立**。这个独立性假设在传统 RAG 范式下成立，但一旦引入"持久的、结构化的知识层"，假设就会失效。论文据此提出 **动态 Agentic ROI 模型**：把成本视为时间函数 `Cost(t)`，由 **知识库覆盖率 H(t)** 控制[^src1]。

## 机制含义

- **静态视角（RAG）**：每条 query 都要重新检索原始文档、重新拼装上下文、重新生成答案，token 成本与历史任务无关。
- **动态视角（Wiki）**：一旦某个领域的核心实体页、综合页已经被写入并维护，后续同主题 query 的检索范围会逐步收敛到 wiki 内已编译的摘要，原始文档不再被重复读入。`H(t)` 越高，`Cost(t)` 越低，且单调下降。

## 实证锚点

四条相同领域的连续 query 在工业级 C# 多智能体框架 Qing Claw 上跑出来：复利体制下累计 47K token，匹配的 RAG 基线 305K token，**节省 84.6%**[^src2]。30 天校准外推（确定性种子 = 42）：中等主题集中度 53.7% 节省、高集中度 81.3% 节省，且节省比例随时间单调扩大[^src3]。

## 边界 / 误用条件

- `H(t)` 的提升不是免费的——需要把每次 query 的高价值答案 / 检索结果反写回 wiki；只读不写的 wiki 不会复利。这正是三机制卡所拆解的 auto-feedback 与 write-back[^v3-1]。
- 当 query 流是高度分散的"长尾未知主题"时，`H(t)` 始终接近 0，动态模型退化为静态 RAG。
- 当前论文只在工业级单主题流上做了 4-query 控制实验，对跨主题、多团队场景的外推需要更多证据。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-knowledge-compounding/text.txt` — 第 37 行 — "the cost term in the original Agentic ROI equation contains an unexamined assumption -- that the cost of each task is mutually independent. This assumption holds under the traditional retrieval-augmented generation (RAG) paradigm but breaks down once a persistent, structured knowledge layer is introduced." 配合 "cost is treated as a time-varying function Cost(t) governed by a knowledge-base coverage rate H(t)"。
[^src2]: `data/raw/arxiv/arxiv-knowledge-compounding/text.txt` — 第 37 行 — "a cumulative token consumption of 47K under the compounding regime versus 305K under a matched RAG baseline -- a savings of 84.6%"。
[^src3]: `data/raw/arxiv/arxiv-knowledge-compounding/text.txt` — 第 37 行 — "53.7% under medium topic concentration and 81.3% under high concentration, with the gap widening monotonically over time"。
[^v3-1]: [knowledge-compounding-three-mechanisms](knowledge-compounding-three-mechanisms.md) — H(t) 单调上升的前提是同一论文拆出的"写回"机制起效。
