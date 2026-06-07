---
id: invest-harvest-cycle
title: 投资-收获振荡成本曲线
status: accepted
card_type: example_pattern
tags: [cost-trajectory, compounding, capital-formation, empirical-pattern]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-knowledge-compounding]
justification: ../justification/invest-harvest-cycle.md
canonical_concept: invest-harvest-cycle
aliases: [投资收获循环, invest-harvest cycle, 振荡凹曲线, concave-with-spike pattern, 资本形成周期]
summary: >-
  invest-harvest-cycle（投资收获循环 / invest-harvest cycle / 振荡凹曲线）是 Compounding
  方案独有的成本轨迹模式：Q1 冷启动 12K→Q2 缓存命中 3K→Q3 搜索回写投资 28K→Q4 复用收获 4K，
  呈现尖峰=资本形成、波谷=资本收获的振荡凹曲线，是三种方案中唯一的历史依赖型轨迹
related: [compounding-cost-honesty, dynamic-agentic-roi, knowledge-compounding, search-write-back]
---

Wen & Ku (2026) 通过四查询实验发现，Compounding 方案的累积 token 消耗呈现一种**独特的振荡凹曲线（concave-with-spike pattern）**，与两种无状态基线的线性轨迹形成鲜明对比[^src-1]。

**三种轨迹对比**：

1. **Long-Context**：累积成本以陡峭斜率线性增长（每步 +70K 或 +95K），斜率仅取决于源文档大小，与查询内容无关——无状态成本的上界[^src-2]。

2. **Chunk-RAG**：累积成本以浅斜率线性增长（每步约 +3.4K），斜率仅取决于 top-k 和 chunk size，与历史查询无关。完全失忆——**第 1000 次查询的边际成本等于第 1 次**[^src-3]。

3. **Compounding**：Q1 中等偏高（12K，冷启动综合）→ Q2 极低（3K，命中 Q1 的综合页面）→ Q3 投资尖峰（28K，搜索 + 回写）→ Q4 再次下降（4K，复用 Q3 的实体页面）[^src-4]。

**尖峰与波谷的经济含义**：在静态成本框架下，尖峰只是昂贵的查询；在动态框架下，**尖峰对应资本形成事件（capital formation events），波谷对应资本收获事件（capital harvest events）**。这种"投资 → 收获 → 再投资 → 再收获"的振荡凹曲线是 Section 3.3 中 H(t) 演化轨迹在成本侧的直接体现[^src-5]。

**唯一的历史依赖型轨迹**：Compounding 是三种方案中唯一具有历史依赖性的方案——查询 N 的成本取决于查询 1 到 N-1 的结果；另外两种方案中每次查询的成本与历史查询完全独立[^src-6]。

振荡凹曲线是 Wen & Ku (2026) 知识复利理论在成本侧的直接印证——理论预测的 H(t) 凹饱和曲线在累积成本图中表现为投资-收获交替[^card-1]。其中 Q3 投资尖峰（28K）的主要成分是搜索回写操作——CEO 编排器触发外部搜索并将结果合并回写到实体页面，这一成本高但一次性的操作使 Q4 得以 4K 低成本复用[^card-2]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 5.2 P17 -- "Plotting the cumulative token consumption of the four queries as a time series (Figure 2b) reveals three qualitatively different growth patterns, one per regime"
[^src-2]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 5.2 P18 -- "Long-Context: cumulative cost grows linearly with a steep slope (each step +70K or +95K)"
[^src-3]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 5.2 P18 -- "Chunk-RAG: cumulative cost grows linearly with a shallow slope... It is also entirely amnesiac: the marginal cost of the 1000th query equals the marginal cost of the first"
[^src-4]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 5.2 P18 -- "Compounding: cumulative cost displays a concave-with-spike pattern—Q1 is moderately high (12K)... Q2 is extremely low (3K)... Q3 introduces an investment spike (28K)... Q4 falls again (4K)"
[^src-5]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 5.2 P18 -- "the spikes correspond to capital formation events and the troughs correspond to capital harvest events... This 'invest → harvest → reinvest → reharvest' oscillating concave curve is the direct cost-side manifestation of the H(t) evolution trajectory"
[^src-6]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 5.2 P18 -- "it is the only one of the three regimes whose trajectory is history-dependent: in the other two regimes, the cost of query N is independent of queries 1 through N−1"
[^card-1]: [知识复利效应](knowledge-compounding.md) -- 本卡展示成本侧的振荡凹曲线实证，该卡提供 H(t) 凹饱和曲线的理论框架，投资-收获模式是理论预测在经验数据中的直接体现
[^card-2]: [搜索回写机制](search-write-back.md) -- 本卡中 Q3 投资尖峰（28K）的核心成分是搜索回写操作，该卡详述搜索回写的完整机制流程（CEO 触发搜索→结果合并→实体页面覆盖写入）
