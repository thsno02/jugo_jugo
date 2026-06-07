---
id: comparison-full-context-task-divergence
title: 全上下文方法的任务依赖性分歧
status: accepted
card_type: distinction
tags: [full_context, task_divergence, QA, event_summarization, context_window]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0, arxiv-locomo]
justification: ../justification/comparison-full-context-task-divergence.md
canonical_concept: full-context-task-divergence
aliases: [全上下文任务分歧, full-context task divergence, 上下文扩展任务依赖性]
summary: >-
  comparison-full-context-task-divergence（全上下文任务分歧）全上下文方法在事实检索 QA 中达到最高准确率（LOCOMO Judge=72.90%），但在事件摘要中长上下文模型 F1 反而低于短上下文模型（39.9 vs 45.9）；区分点在于任务类型：检索类任务从更多上下文获益，因果时序理解类任务反而受损
related: [attention-dilution-at-scale, full-context-accuracy-ceiling, long-context-comprehension-illusion]
---

全上下文方法（将全部历史/文档直接传入 LLM）的效果并非单调——它在不同任务类型上表现出根本性的分歧。

**事实检索 QA：全上下文最优**。在 LOCOMO 基准的 QA 任务中，将约 26K token 的完整对话历史传入 LLM 达到了所有方法中最高的 Judge 分数（72.90%），超越了 Mem0（66.88%）和 Mem0^g（68.44%）[^card-full-context-accuracy-ceiling]。对于"用户的饮食偏好是什么"这类事实性问题，更多上下文意味着更高的命中概率。

**事件摘要：全上下文反而更差**。在同一基准的事件摘要任务中，拥有 16K 窗口的 GPT-3.5-turbo-16K 的 FactScore F1 仅为 39.9，低于 4K 窗口的 GPT-3.5-turbo 的 45.9。精度降 3.0%，召回降 8.7%[^card-long-context-comprehension-illusion]。对于"这段关系经历了怎样的发展"这类需要因果时序理解的问题，更多上下文反而干扰了模型对事件动态的把握。

**区分点：检索 vs 理解**。事实检索本质上是"大海捞针"——上下文越多，针越可能在其中；模型只需定位并提取。事件摘要则要求在大量对话中建立跨会话的时序和因果链接（long-range dependency），更多的无关对话增加了注意力稀释的负担，使模型更难准确追踪因果结构。

这一分歧意味着：不存在"全上下文总是最好"或"全上下文总是退化"的简单结论。系统设计者需根据目标任务类型选择策略——事实检索密集型场景可倾向全上下文，深层理解密集型场景则需要更结构化的记忆方案。

## Footnotes

[^card-full-context-accuracy-ceiling]: [全上下文方法的准确率天花板效应](full-context-accuracy-ceiling.md) -- 量化了全上下文在 QA 任务中的准确率优势（Judge=72.90%）及其延迟代价（p95=17.1s）
[^card-long-context-comprehension-illusion]: [长上下文模型的理解假象](long-context-comprehension-illusion.md) -- 展示了长上下文模型在事件摘要任务中反而低于短上下文模型的反直觉发现（F1: 39.9 vs 45.9）
[^src-1]: data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt -- "Empirical results demonstrate that our methods consistently outperform all existing memory systems across four question categories: single-hop, temporal, multi-hop, and open-domain."（Mem0 在 LOCOMO QA 上全上下文 Judge=72.90%，为所有方法最高）
[^src-2]: data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt -- "the long-context model does not surpass the base model ... gpt-3.5-turbo-16k exhibits a decline in both precision (by 3.0%) and recall (by 8.7%) compared to gpt-3.5-turbo which has a 4K context window. This suggests that long-context models may not be proficient at utilizing their context appropriately"
