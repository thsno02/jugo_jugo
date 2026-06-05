---
id: capitalized-latency
title: 资本化延迟与瞬时延迟
status: accepted
card_type: distinction
tags: [latency, capital-goods, cost-decomposition, user-experience]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-knowledge-compounding]
justification: ../justification/capitalized-latency.md
canonical_concept: capitalized-latency
aliases: [资本化延迟, capitalized latency, 瞬时延迟, transient latency, 延迟分解]
summary: >-
  capitalized-latency（资本化延迟 / capitalized latency / 延迟分解）是 token 资本品重分类向延迟维度的推广：
  Compounding 的 81 秒中 65.7 秒是用户等待的瞬时延迟，15.3 秒是用户已获答案后构建持久制品的
  资本化延迟，后者应在未来查询中摊销而非计入当次 ROI 损失
related: [compounding-cost-honesty, knowledge-compounding, token-capital-goods]
  - token-capital-goods
  - knowledge-compounding
---

Wen & Ku (2026) 将 token 资本品重分类推广到第二个成本维度——**延迟**[^src-1]。

**核心区分**：

- **瞬时延迟（transient latency）**：用户等待答案的时间，答案一旦交付不留下任何持久物。在 Liu et al. 的 Agentic ROI 公式中，这是直接降低 ROI 的时间成本。
- **资本化延迟（capitalized latency）**：系统在答案已可供用户使用之后花费在构建持久制品上的时间，该制品的价值跨越所有未来查询持续存在[^src-2]。

**实证数据**：Compounding 单次查询周期 81 秒，其中[^src-3]：
- memory_recall: 9 ms
- ceo_reasoning: 65,647 ms（用户等待阶段）
- memory_distill: 15,322 ms（用户已获答案，系统将答案回写为持久综合页面）

Compounding 因此比 Chunk-RAG（约 3.4 秒）慢约 24 倍——比 3.4 倍的 token 成本差距**更大**[^src-4]。但在消耗品视角下的严重劣势，在资本品视角下被分解：81 秒中仅前 65.7 秒是用户等待时间，后 15.3 秒不是等待时间，而是系统的资产投资[^src-5]。

**推广原则**：资本品重分类不仅适用于 token，而是适用于**任何花费在持久化可查询可继承制品构建上的成本分量**——token、延迟、算力、内存、美元成本均可做同样的分区[^src-6]。

本卡将资本品重分类从 token 推广到延迟，而 token 维度的完整理论框架——知识复利效应——在知识复利卡中建构[^card-knowledge-compounding]。token 维度的诚实成本数据（3.4 倍差距）与本卡的延迟数据（24 倍差距）共同构成 Compounding 成本诚实的完整画面[^card-compounding-cost-honesty]。本卡所推广的原始资本品框架——token 从消耗品到资本品的四属性重分类——在 Token 资本品重分类卡中建立[^card-1]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.4.5 P10 -- "Nothing in the argument above is specific to tokens. The same reframing applies to any cost component spent on the construction of a persistent knowledge artifact. The clearest second case is latency."
[^src-2]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.4.5 P10 -- "latency divides into transient latency (time the user waits for an answer that, once delivered, leaves nothing behind) and capitalized latency (time the system spends constructing a persistent artifact whose value persists across all future queries)"
[^src-3]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.4.5 P11 -- "memory_recall 9 ms + ceo_reasoning 65,647 ms + memory_distill 15,322 ms"
[^src-4]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.4.5 P11 -- "Compounding is therefore approximately 24x slower than Chunk-RAG—a per-query deficit much more severe than the 3.4x token-cost deficit"
[^src-5]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.4.5 P11 -- "Of the 81 seconds, only the first 65.7 seconds... are spent producing the answer the user is waiting for. The remaining 15.3 seconds... are spent after the answer is already available to the user"
[^src-6]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.4.5 P11 -- "We expect the same partition to apply cleanly to compute, memory, and dollar cost in future work"
[^card-knowledge-compounding]: [知识复利效应](knowledge-compounding.md) -- 本卡将资本品重分类推广到延迟维度，该卡在 token 维度建立了知识复利的完整理论框架
[^card-compounding-cost-honesty]: [复利方案在原始 token 成本上从不胜出](compounding-cost-honesty.md) -- 本卡揭示延迟维度的 24 倍差距，该卡揭示 token 维度的 3.4 倍差距，两者共同构成 Compounding 成本诚实的完整画面
[^card-1]: [Token 资本品重分类](token-capital-goods.md) -- 本卡将资本品重分类推广到延迟维度，该卡建立了 token 维度的资本品四属性重分类理论基础
