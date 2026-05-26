---
id: knowledge-compounding-tokens-as-capital
title: 把 LLM token 从"消耗品"重新归类为"资本品"
status: draft
card_type: distinction
tags: [#economics, #knowledge-compounding, #capital-goods, #token-economics]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
source_ids: [arxiv-knowledge-compounding]
provenance_card: ../provenance/knowledge-compounding-tokens-as-capital.md
aliases: [token 资本品论, capital goods view of tokens, 从边际成本到资本积累]
related: [knowledge-compounding-dynamic-roi, knowledge-compounding-three-mechanisms, karpathy-llm-wiki-vs-rag, file-outputs-back-as-compounding-loop]
---

## 区分对象

Wen 与 Ku（2026）提出的**理论贡献**不是新指标也不是新算法，而是一次**会计归类的重构**：

- **传统视角（消耗品 / consumables）**：每次 query 消耗的 token 像电、像 API call、像短期可变成本，用完即清零；经济讨论停留在"边际成本分析"。
- **复利视角（资本品 / capital goods）**：花在 INGEST 和 synthesis 上的 token 会沉淀为持久的 wiki 页，继续在未来 N 次 query 中产生使用价值；经济讨论需要切换到"资本积累 / 折旧 / ROI"框架。

## 为什么这个区分重要

- 在消耗品框架下，"今天多花 10K token 把一篇论文写进 wiki"是**纯支出**，只能从 latency / quality 角度辩护。
- 在资本品框架下，同样这 10K token 是**投资**——它会被未来 query 反复折现，估值依赖剩余使用期与命中率 H(t)。
- 这把 LLM agent 工程的"做不做 wiki / 多深做 wiki"决策，从体验问题变成了财务问题，可以用 NPV、回本期、折旧曲线等正规工具分析。

## 边界与误用

- 不是所有 token 都是资本品：临时上下文、用过即丢的中间推理仍是消耗品。资本化的前提是该 token 写入了**持久、可寻址、可检索**的位置。
- 资本品也会折旧：信息过期、被新事实覆盖时，wiki 页价值下降；论文给出的 30 天外推是**校准模拟**而非长期生命周期分析，跨越数月、季度的折旧曲线尚未实证。
- 这个区分仅在主题集中度足够高时财务上才显著（论文给出 medium / high concentration 两档对比）。

## References

- 概念归类原文：`data/raw/arxiv/arxiv-knowledge-compounding/text.txt:37`，提出 "a recategorization of LLM tokens from consumables to capital goods, shifting the economic discussion from static marginal cost analysis to dynamic capital accumulation"。

## Footnotes

- 原文引语：`data/raw/arxiv/arxiv-knowledge-compounding/text.txt:37` —— "The theoretical contribution of this paper is a recategorization of LLM tokens from consumables to capital goods, shifting the economic discussion from static marginal cost analysis to dynamic capital accumulation."
- 论文 JEL 分类：`data/raw/arxiv/arxiv-knowledge-compounding/text.txt:39` —— "JEL: C63, D24, O33, L86"，包含 D24（生产 / 成本 / 资本与全要素生产率）和 O33（技术变迁），印证作者把这件事定位为"产业经济学"问题。
