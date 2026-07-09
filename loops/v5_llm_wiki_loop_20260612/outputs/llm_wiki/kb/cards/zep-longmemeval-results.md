---
id: zep-longmemeval-results
title: Zep 在 LongMemEval 基准上的实验结果
status: accepted
card_type: empirical-finding
tags:
- benchmark
- LongMemEval
- temporal-reasoning
- multi-session
- evaluation
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-zep
evidence_basis: experimental_paper
justification: ../justification/zep-longmemeval-results.md
canonical_concept: zep-longmemeval-results
aliases:
- LongMemEval
- LME
- LongMemEval_s results
summary: Zep 在 LongMemEval_s（平均 115k tokens 对话）上表现：gpt-4o-mini 63.8% vs baseline 55.4%（+15.2%），gpt-4o
  71.2% vs 60.2%（+18.5%）。延迟从约 30s 降至约 3s（-90%）， 上下文 token 从 115k 降至 1.6k。改善最大的类型：single-session-preference（+184%）、
  temporal-reasoning（+38.4%）、multi-session（+30.7%）。下降类型：single-session-assistant （-17.7%），论文承认需进一步研究。
related:
- zep-temporal-knowledge-graph-architecture
- zep-dmr-benchmark-results
- longmemeval-benchmark-overview
- mem0-zep-comparison
---

LongMemEval_s 数据集提供平均约 115,000 tokens 的对话上下文，包含六种问题类型，比 DMR 更能反映企业场景。[^src-1]

**总体结果**：[^src-2]
- gpt-4o-mini: Zep 63.8% vs full-context 55.4%（+15.2%），延迟 3.20s vs 31.3s
- gpt-4o: Zep 71.2% vs full-context 60.2%（+18.5%），延迟 2.58s vs 28.9s
- 上下文 token 从 115k 降至 1.6k

**按问题类型（gpt-4o）**：[^src-3]
- single-session-preference: +184%（最大改善）
- temporal-reasoning: +38.4%
- multi-session: +30.7%
- single-session-user: +14.1%
- knowledge-update: +6.52%
- single-session-assistant: -17.7%（唯一显著下降）

论文指出更强模型（gpt-4o）在所有改善类型上表现更佳，但 single-session-assistant 类型的下降表明 Zep 的时序数据表示可能需要进一步优化，据材料推测这与 assistant 生成内容的提取/检索方式有关。[^src-4]

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "LongMemEval (LME)" P1 -- "LongMemEval_s dataset...conversations averaging approximately 115,000 tokens in length"
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "LongMemEval results" P1 -- "Zep demonstrates substantial improvements in both accuracy and latency"
[^src-3]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "LongMemEval results" Table 3 -- question type breakdown
[^src-4]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "LongMemEval results" P4 -- "The decrease in performance for single-session-assistant questions...represents a notable exception"
[^card-1]: [zep-dmr-benchmark-results] -- LongMemEval 是论文推荐的更有价值的评估基准
