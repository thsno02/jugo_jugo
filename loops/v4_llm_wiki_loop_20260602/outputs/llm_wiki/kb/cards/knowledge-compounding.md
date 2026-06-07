---
id: knowledge-compounding
title: 知识复利效应
status: accepted
card_type: concept
tags: [knowledge-compounding, agentic-roi, economic-analysis, persistent-knowledge]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-knowledge-compounding]
justification: ../justification/knowledge-compounding.md
canonical_concept: knowledge-compounding
aliases: [知识复利, knowledge compounding, 复利效应, 知识积累经济学]
summary: >-
  knowledge-compounding（知识复利 / knowledge compounding / 复利效应）是 Wen & Ku (2026)
  对 Agentic ROI 框架的扩展：当持久化知识层存在时，每任务成本不再独立，而是关于知识库覆盖率
  H(t) 的递减时间函数，表现为凹饱和曲线
related: [capitalized-latency, compounding-cost-honesty, cost-independence-assumption, dynamic-agentic-roi, invest-harvest-cycle, output-compounding-loop, search-write-back, token-capital-goods, wiki-compounding-artifact]
---

知识复利（Knowledge Compounding）是 Wen & Ku (2026) 提出的经济学概念，用于描述以下现象：当 LLM 智能体系统引入持久化结构化知识层后，每任务的 token 成本不再是独立常量，而变为时间递减函数[^src-1]。

核心论断分三层：

1. **成本时变性**——传统 Agentic ROI 框架假设每任务成本 Ci 仅取决于当前任务复杂度，与历史任务集无关。一旦引入持久化知识层，这一假设失效：先前任务构建的知识库降低了后续任务的成本[^src-2]。

2. **凹饱和曲线**——知识库覆盖率 H(t) 遵循凹饱和曲线（数学上与生态学中的 logistic 增长曲线和经济学中的 Gompertz 扩散模型同构），表现为初期快速增长、后期缓慢增长、渐近趋近于主题分布的稳态覆盖[^src-3]。

3. **经济范式转换**——知识复利将 LLM 经济学的分析单元从「每查询边际成本最小化」转向「动态资本积累最大化」[^src-4]。正确的问题不再是「每次查询花费多少？」而是「系统在一年结束时拥有什么开始时没有的东西？」[^src-5]。

知识复利通过三个微观机制实现：(i) INGEST 一次性投入在 N 次检索中摊销；(ii) 高价值问答自动沉淀为综合页面；(iii) 外部搜索结果回写至实体页面[^src-6]。llm-wiki.net 的产出复利循环为这一理论框架提供了实践印证——产出（报告/幻灯片/计划）回写进 wiki，使每个新产出建立在所有先前研究之上，直接体现了 H(t) 的递增覆盖[^card-output-compounding-loop]。

Karpathy 的 LLM Wiki 设计从产品视角枚举了五类具体的复利型制品——交叉引用、矛盾标记、综合叙述、实体页面和归档查询——为理论框架中的"持久化知识层"提供了具象参照[^card-wiki-compounding-artifact]。第三微观机制（搜索回写）的完整运作细节——包括 CEO 编排器触发搜索、搜索结果合并回写到实体页面——在搜索回写卡中有详细阐述[^card-search-write-back]。四查询实验中观测到的投资-收获振荡成本曲线（Q1 12K→Q2 3K→Q3 28K→Q4 4K）则从成本侧验证了 H(t) 凹饱和曲线的预测[^card-invest-harvest-cycle]。

然而，这一乐观论述需要与核心诚实发现对照：在原始 token 计量下，Compounding 在任何时间跨度内从不胜过 Chunk-RAG，其经济论据不在于成本节省而在于额外 token 购买了持久化知识资产[^dist-1]。知识复利理论的立论前提——传统 Agentic ROI 框架中的成本独立性假设为何失效——在成本独立性假设批判卡中有系统阐述[^card-cost-independence]。资本品重分类向延迟维度的推广——揭示 81 秒中仅 15.3 秒为资本化投资——在资本化延迟卡中展开[^card-capitalized-latency]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Abstract P2 -- "We extend the Agentic ROI framework of Liu et al. (2026) by relaxing its implicit assumption that per-task LLM costs are independent. Once a persistent knowledge layer is introduced, this assumption fails: cost becomes a time-varying function Cost(t) governed by a coverage rate H(t) that follows a concave saturation curve."
[^src-2]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 1.3 P4 -- "we generalize the cost term from a static variable to a time-varying function Cost(t), introduce the knowledge-base coverage rate H(t) as the key mediating variable"
[^src-3]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.3 P9 -- "H(t) takes a concave saturation curve: rapid early growth, slow late growth, asymptotically approaching the steady-state coverage of the topic distribution. This shape is mathematically isomorphic to the logistic growth curve in ecology and the Gompertz diffusion model in economics"
[^src-4]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.4 P10 -- "The reclassification shifts the unit of economic analysis for AI systems from minimizing marginal cost to maximizing capital accumulation"
[^src-5]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.4 P10 -- "Under the capital-goods view, the right question is 'what does the system own at the end of a year that it did not own at the beginning?'"
[^src-6]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Abstract P2 -- "three microeconomic mechanisms underlying the compounding effect: (i) one-time INGEST amortized over N retrievals, (ii) auto-feedback of high-value answers into synthesis pages, and (iii) write-back of external search results into entity pages"
[^card-output-compounding-loop]: [产出复利循环](output-compounding-loop.md) -- llm-wiki.net 实现的产出回写机制（产出写回 wiki 索引使后续产出更强）是知识复利理论在实际 LLM Wiki 产品中的直接体现
[^card-wiki-compounding-artifact]: [Wiki 作为复利型知识制品](wiki-compounding-artifact.md) -- 本卡提出知识复利的经济学理论框架，该卡从 Karpathy 设计视角枚举了 wiki 中持续积累的五类具体制品
[^card-search-write-back]: [搜索回写机制](search-write-back.md) -- 本卡将搜索回写列为三微观机制之一，该卡详细阐述了 Qing Claw 中 CEO 编排器触发搜索回写的完整流程与实证案例
[^card-invest-harvest-cycle]: [投资-收获振荡成本曲线](invest-harvest-cycle.md) -- 本卡预测 H(t) 凹饱和曲线，该卡展示四查询实验中观测到的投资-收获振荡成本轨迹，从成本侧验证了理论预测
[^dist-1]: [复利方案在原始 token 成本上从不胜出](compounding-cost-honesty.md) -- 本卡主张知识复利使每任务成本递减，该卡主张原始 token 成本永远不低于 Chunk-RAG，区分点在于"递减"是相对于自身历史而非相对于无记忆基线
[^card-cost-independence]: [Agentic ROI 成本独立性假设批判](cost-independence-assumption.md) -- 本卡在假设失效后构建新理论，该卡系统阐述原框架中三个未经检验的假设为何失效
[^card-capitalized-latency]: [资本化延迟与瞬时延迟](capitalized-latency.md) -- 本卡聚焦 token 维度的复利效应，该卡将同一资本品重分类推广到延迟维度
