---
id: locomo-event-summarization-degradation
title: 长上下文模型事件摘要反而退化
status: accepted
card_type: finding
tags:
- event-summarization
- long-context-llm
- context-utilization
- FactScore
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-locomo
evidence_basis: experimental_paper
justification: ../justification/locomo-event-summarization-degradation.md
canonical_concept: long-context-event-summarization-degradation
aliases:
- long-context summarization degradation
- 长上下文事件摘要退化
- context utilization failure in summarization
summary: long-context-event-summarization-degradation 长上下文模型在事件摘要任务中反而不如 base model。 GPT-3.5-turbo-16K (16K context) FactScore precision 下降3.0%、recall 下降8.7%（相对 GPT-3.5-turbo 4K）。 GPT-3.5-turbo 使用 incremental
  summarization 取得最高 recall (46.5%) 和 F1 (45.9%)。 论文据此推测长上下文模型似乎不擅长正确利用其上下文，与 Lost in the Middle 发现一致。
related:
- locomo-evaluation-framework
- long-context-adversarial-hallucination
- locomo-summarization-error-taxonomy
- temporal-event-graph-dialogue
---
在 LoCoMo 的事件摘要任务中，长上下文模型 GPT-3.5-turbo-16K 的表现反而低于使用 4K 上下文窗口的 base model GPT-3.5-turbo。[^src-1]

具体数据（FactScore）：
- GPT-3.5-turbo (4K, incremental summarization): precision=45.3%, recall=46.5%, F1=45.9%
- GPT-3.5-turbo-16K (16K): precision=42.3%, recall=37.8%, F1=39.9%
- GPT-4-turbo (4K): precision=51.6%, recall=41.8%, F1=45.1% [^src-2]

论文解释为"长上下文模型似乎不擅长正确利用其上下文"（long-context models may not be proficient at utilizing their context appropriately）。尽管更大的上下文窗口提供了更多信息，模型无法从中准确提取和组织因果/时序连接。[^src-3]

该结论与 Liu et al. (2024) "Lost in the Middle" 以及 QA 任务中 adversarial 性能暴跌的发现一致，共同表明长上下文并不自动等于更好的理解。[^src-4] [^card-1] [^card-2]

[^src-1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Event Summarization Results" -- "the long-context model does not surpass the base model, despite its capability for extended-range reasoning facilitated by a larger context window"
[^src-2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table summ_results" -- "GPT-3.5-turbo: Precision 45.3 Recall 46.5 F1 45.9; GPT-3.5-turbo-16K: Precision 42.3 Recall 37.8 F1 39.9"
[^src-3]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Event Summarization Results" -- "long-context models may not be proficient at utilizing their context appropriately"
[^src-4]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Event Summarization Results" -- "which also aligns with similar findings in Li et al. (2023) as well as the QA task in LoCoMo"

[^card-1]: 与 [long-context-adversarial-hallucination] 关联——同一论文中 QA 任务的平行发现
[^card-2]: 与 [locomo-evaluation-framework] 关联——此发现来自事件摘要任务
