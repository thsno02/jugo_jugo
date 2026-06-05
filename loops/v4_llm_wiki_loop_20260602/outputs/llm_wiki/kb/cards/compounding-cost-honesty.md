---
id: compounding-cost-honesty
title: 复利方案在原始 token 成本上从不胜出
status: accepted
card_type: source_claim
tags: [empirical-finding, cost-comparison, chunk-rag, compounding, honest-accounting]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-knowledge-compounding]
justification: ../justification/compounding-cost-honesty.md
canonical_concept: compounding-cost-honesty
aliases: [复利成本诚实, compounding cost honesty, 复利从不赢token, compounding never beats RAG]
summary: >-
  compounding-cost-honesty（复利成本诚实 / compounding never beats RAG）是 Wen & Ku (2026)
  的核心诚实发现：Compounding 在任何场景、任何时间跨度下的原始 token 消耗均高于 Chunk-RAG
  （4查询 47K vs 13.6K, 30天高集中度 3.92M vs 1.02M），其经济论据不在于成本节省而在于
  额外 token 购买了持久化知识资产
related: [capitalized-latency, cost-independence-assumption, knowledge-compounding]
  - knowledge-compounding
  - token-capital-goods
---

Wen & Ku (2026) 将以下发现称为论文的**核心诚实发现（central honest finding）**：在原始 token 计量下，Compounding 方案**在任何场景、任何时间跨度下都不胜过 Chunk-RAG**[^src-1]。

**四查询实证数据**[^src-2]：
- Chunk-RAG: 13.6K (4 x 3.4K)
- Compounding: 47K (Q1: 12K, Q2: 3K, Q3: 28K, Q4: 4K)
- Long-Context: 305K (4 x ~70K-95K)

排名为 Chunk-RAG < Compounding < Long-Context。

**30天仿真数据**（即使在高主题集中度 p=0.90 下）[^src-3]：
- Chunk-RAG: 1.02M
- Compounding: 3.92M（仍为 Chunk-RAG 的 3.8 倍）
- Long-Context: 21.0M

**比率随时间收窄但永不交叉**：第1天 Compounding 成本是 Chunk-RAG 的 6.3 倍，第30天降至 3.8 倍。外推至30天以后比率继续渐近收窄，但在任何合理参数范围内**token 成本交叉点可能不存在**[^src-4]。

这一发现迫使产生一个问题：**如果 Compounding 永远不能在 token 成本上胜出，它在哪个维度上胜出？那个维度值得衡量吗？**[^src-5] 答案在于 Compounding 的 47K token 同时购买了四个答案**和**一个知识资产（1个综合页面 + 5条新实体事实），而 Chunk-RAG 的 13.6K 只购买了四个答案[^src-6]。

本卡的成本诚实发现与知识复利效应卡构成核心张力：后者主张每任务成本呈递减时间函数，但本卡揭示该递减永远无法使绝对 token 消耗低于无记忆基线[^dist-1]。延迟维度的诚实数据更为严峻——24 倍差距远超 token 的 3.4 倍——但同样可做资本品分解[^card-capitalized-latency]。理解这一张力需要回溯到传统 Agentic ROI 框架的成本独立性假设为何失效[^card-cost-independence]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 5.3 P20 -- "This is the central honest finding of the paper, and it forces a question that the rest of the paper exists to answer: if Compounding never wins on token count, on what dimension does it win, and is that dimension worth measuring?"
[^src-2]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Table 2 P16 -- "Q1 Cold start 12... Q2 Synthesis hit 3... Q3 After restart 28... Q4 New angle 4... Total 47 / 13.6 / 305"
[^src-3]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Table 4 P19 -- "30-day... Chunk-RAG 1.02... Compounding p=0.90 3.92... Long-Context 21.00"
[^src-4]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 5.3 P20 -- "a token-count crossover—where Compounding actually undercuts Chunk-RAG on cumulative tokens—is not visible on any horizon we modeled, and likely does not exist for plausible parameter ranges"
[^src-5]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 5.3 P20 -- "if Compounding never wins on token count, on what dimension does it win, and is that dimension worth measuring?"
[^src-6]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 5.1 P16 -- "The 47K tokens of Compounding bought both the four answers and the persistent artifacts. The 13.6K tokens of Chunk-RAG bought only the four answers"
[^dist-1]: [知识复利效应](knowledge-compounding.md) -- 本卡主张原始 token 成本永远不低于 Chunk-RAG，该卡主张每任务成本呈递减时间函数，区分点在于前者衡量绝对 token 消耗、后者衡量单位 token 购买力
[^card-capitalized-latency]: [资本化延迟与瞬时延迟](capitalized-latency.md) -- 本卡揭示 token 维度的成本诚实数据（3.4倍），该卡揭示延迟维度的更大差距（24倍）并做同样的资本品分解
[^card-cost-independence]: [Agentic ROI 成本独立性假设批判](cost-independence-assumption.md) -- 本卡提供 Compounding 从不胜出的实证数据，该卡提供理论基础解释为何成本比较需要不同的分析透镜
