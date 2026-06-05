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
related: [context-window-degradation, event-summarization-error-taxonomy, full-context-accuracy-ceiling, graphrag-small-context-window-advantage, locomo-benchmark, long-context-adversarial-vulnerability]
---

LoCoMo 的事件摘要（event summarization）任务提供了一个反直觉的发现：拥有更大上下文窗口的模型在需要深层理解的任务上反而表现更差[^src-1]。

GPT-3.5-turbo-16K（16K 窗口）在 FactScore 上的 F1=39.9，低于 GPT-3.5-turbo（4K 窗口）的 F1=45.9。具体而言，精度从 45.3 降至 42.3（降 3.0%），召回从 46.5 降至 37.8（降 8.7%）[^src-2]。这与 QA 任务中长上下文模型在事实性问题上的提升形成鲜明对比。

论文的解释是：事件摘要任务要求模型理解跨多个会话的时序和因果连接（long-range dependency），而非简单的事实检索。长上下文模型"may grasp the factual elements within the entire conversation but do not accurately comprehend the context"[^src-3]。这一发现与 Li et al. (2023) 在 LooGLE 基准上的类似结论一致[^src-4]。

该发现意味着上下文窗口的扩展并不等价于理解能力的提升，模型看到更多内容可能反而干扰其对因果结构的准确把握。GraphRAG 评估从不同系统独立验证了这一现象——8k 上下文窗口在全面性上反而优于 16k/32k/64k[^card-graphrag-small-context-window-advantage]。值得注意的是，全上下文方法在 QA 式事实检索任务中却达到最高准确率，表明退化效应具有任务依赖性[^dist-full-context-accuracy-ceiling]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 6.2" -- "the long-context model does not surpass the base model, despite its capability for extended-range reasoning facilitated by a larger context window"
[^src-2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table 4" -- "GPT-3.5-turbo FactScore: P=45.3 R=46.5 F1=45.9; GPT-3.5-turbo-16K: P=42.3 R=37.8 F1=39.9"
[^src-3]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 1" -- "they may grasp the factual elements within the entire conversation but do not accurately comprehend the context"
[^src-4]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 6.2" -- "long-context models may not be proficient at utilizing their context appropriately, which also aligns with similar findings in Li et al. (2023, LooGLE)"
[^card-graphrag-small-context-window-advantage]: [GraphRAG 中小上下文窗口反而更优的发现](graphrag-small-context-window-advantage.md) -- 本卡从 LoCoMo 事件摘要任务展示长上下文理解假象，该卡从 GraphRAG 评估独立验证了小上下文窗口反而更优的实证现象
[^dist-full-context-accuracy-ceiling]: [全上下文方法的准确率天花板效应](full-context-accuracy-ceiling.md) -- 本卡显示长上下文在事件摘要中降低理解质量（F1 从 45.9 降至 39.9），该卡显示全上下文在 QA 中达到最高准确率（72.90%），区分点在于任务类型：事实检索从扩展上下文获益，但因果时序理解从中受损
