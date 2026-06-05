---
id: long-context-comprehension-illusion
title: 长上下文模型的理解假象
status: accepted
card_type: source_claim
tags: [long-context, comprehension, event-summarization, agent-memory, evaluation]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
justification: ../justification/long-context-comprehension-illusion.md
canonical_concept: long-context-comprehension-illusion
aliases: [长上下文理解假象, long-context comprehension illusion, 上下文扩展无助于深度理解]
summary: >-
  long-context-comprehension-illusion（长上下文理解假象, long-context comprehension illusion）LoCoMo 事件摘要任务中长上下文 GPT-3.5-turbo-16K（FactScore F1=39.9）反而低于基座 GPT-3.5-turbo（F1=45.9），精度降 3.0% 召回降 8.7%，表明长上下文模型可能抓住事实要素但无法准确理解因果时序动态
related: [locomo-benchmark, long-context-adversarial-vulnerability, context-window-degradation, event-summarization-error-taxonomy]
---

LoCoMo 的事件摘要（event summarization）任务提供了一个反直觉的发现：拥有更大上下文窗口的模型在需要深层理解的任务上反而表现更差[^src-1]。

GPT-3.5-turbo-16K（16K 窗口）在 FactScore 上的 F1=39.9，低于 GPT-3.5-turbo（4K 窗口）的 F1=45.9。具体而言，精度从 45.3 降至 42.3（降 3.0%），召回从 46.5 降至 37.8（降 8.7%）[^src-2]。这与 QA 任务中长上下文模型在事实性问题上的提升形成鲜明对比。

论文的解释是：事件摘要任务要求模型理解跨多个会话的时序和因果连接（long-range dependency），而非简单的事实检索。长上下文模型"may grasp the factual elements within the entire conversation but do not accurately comprehend the context"[^src-3]。这一发现与 Li et al. (2023) 在 LooGLE 基准上的类似结论一致[^src-4]。

该发现意味着上下文窗口的扩展并不等价于理解能力的提升，模型看到更多内容可能反而干扰其对因果结构的准确把握。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 6.2" -- "the long-context model does not surpass the base model, despite its capability for extended-range reasoning facilitated by a larger context window"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table 4" -- "GPT-3.5-turbo FactScore: P=45.3 R=46.5 F1=45.9; GPT-3.5-turbo-16K: P=42.3 R=37.8 F1=39.9"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 1" -- "they may grasp the factual elements within the entire conversation but do not accurately comprehend the context"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 6.2" -- "long-context models may not be proficient at utilizing their context appropriately, which also aligns with similar findings in Li et al. (2023, LooGLE)"
