---
id: knowledge-compounding-three-mechanisms
title: 知识复利的三个微观机制：INGEST 摊销 / answer 回灌 / 外部检索写回
status: accepted
card_type: mechanism
tags: [#agentic-roi, #knowledge-compounding, #llm-wiki, #ingest, #feedback-loop]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T10:02:00+08:00
edited_entity: llm
source_ids: [arxiv-knowledge-compounding]
provenance_card: ../provenance/knowledge-compounding-three-mechanisms.md
aliases: [三机制, ingest 摊销, auto-feedback, write-back, 外部检索写回]
related: [knowledge-compounding-dynamic-roi, knowledge-compounding-tokens-as-capital, file-outputs-back-as-compounding-loop, karpathy-llm-wiki-vs-rag, llm-knowledge-base-five-stage-workflow, mem0-extract-update-pipeline]
---

## 三个机制（不要混淆其分工）

Wen 与 Ku（2026）将"复利效应"分解为三条互相独立、可单独验证的微观机制[^src1]：

1. **INGEST 一次摊销到 N 次检索**：一份原始文档被读入并写成 wiki 页只发生一次，后续 N 次同领域 query 不必再触碰原文；INGEST 的 token 成本被摊到 N 上。
2. **高价值答案的自反馈（auto-feedback）**：query 阶段产生的高质量回答会被反写到对应主题的"综合页"（synthesis page），形成新的可复用片段。
3. **外部检索结果回写实体页（write-back）**：当 wiki 内没有答案、agent 触发外部搜索时，外部命中的关键事实写回对应"实体页"，下次同实体被问到时不再需要再做一次外部检索。

## 为什么这是"三个"机制而不是一个

- (i) 是输入端摊销：写入是被动的、一次性的，对应"看了一篇新论文"。
- (ii) 是输出端反哺：写入是主动的、增量的，对应"自己花算力推导出来的中间结论不要扔"。
- (iii) 是外部边界：写入是机会性的、跨源的，对应"上次查到的事实别再查第二次"。
- 三者写入的对象不同（raw → page、answer → synthesis page、external search → entity page），可独立打开 / 关闭来做消融实验。

## 操作含义

- 一个只实现 (i) 的系统等价于"缓存了 chunk"，复利效应非常有限。它驱动的成本曲线 Cost(t) 与覆盖率 H(t) 之间的耦合是动态 ROI 模型的核心[^v3-1]。
- 实现 (i)+(ii) 是 Karpathy LLM Wiki gist 的原始形态，也是把 file 输出反送回循环的最小闭环[^v3-2]。
- (iii) 是工程性扩展，需要 agent 有"主动写回外部命中"的策略；如果只把外部命中放进上下文用一次就丢，第 (iii) 项不生效。论文同时给出 ~200 行 C# 的"工业级 reference 实现"作为可复现的最小骨架[^src2]。

## 边界

- 三机制都依赖 wiki 的"可寻址性"：如果 synthesis page / entity page 没有稳定 slug 或没有进入索引，回写无法被下次检索召回，复利失效。
- 在主题极度分散的工作流中（每个 query 都跳新主题），(ii) 和 (iii) 的命中率接近零，节省主要来自 (i) 的有限部分。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-knowledge-compounding/text.txt` — 第 37 行 — "We further identify three microeconomic mechanisms underlying the compounding effect: (i) one-time INGEST amortized over N retrievals, (ii) auto-feedback of high-value answers into synthesis pages, and (iii) write-back of external search results into entity pages."
[^src2]: `data/raw/arxiv/arxiv-knowledge-compounding/text.txt` — 第 37 行 — "a minimal reproducible implementation in approximately 200 lines of C#, which we believe is the first complete industrial-grade reference implementation of Karpathy's (2026) LLM Wiki paradigm"。
[^v3-1]: [knowledge-compounding-dynamic-roi](knowledge-compounding-dynamic-roi.md) — 三机制是动态 ROI 的"为什么 Cost(t) 会下降"的微观解释。
[^v3-2]: [file-outputs-back-as-compounding-loop](file-outputs-back-as-compounding-loop.md) — (i)+(ii) 在 Karpathy 原始 gist 中已具备的最小复利闭环。
