---
id: locomo-benchmark
title: LoCoMo 超长期对话记忆评测基准
status: accepted
card_type: source_claim
tags: [benchmark, long-term-conversation, agent-memory, evaluation, dataset]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
justification: ../justification/locomo-benchmark.md
canonical_concept: locomo-benchmark
aliases: [LoCoMo, very long-term conversational memory benchmark]
summary: >-
  locomo-benchmark（LoCoMo, very long-term conversational memory benchmark）首个超长期多模态对话记忆评测基准，50 段对话各含约 300 轮 / 9K tokens / 最多 35 个会话，覆盖 QA（五类推理）、事件图摘要、多模态对话生成三项任务，人类 QA F1=87.9 远超最佳模型 41.4
related: [context-window-degradation, temporal-event-graph-grounding, observation-based-memory-representation]
---

LoCoMo（Long-term Conversational Memory）是首个针对"超长期"（very long-term）多模态对话的评测基准[^src-1]。该数据集包含 50 段高质量对话，每段平均 304.9 轮、19.3 个会话、9,209.2 tokens，时间跨度可达数月、最多 35 个会话[^src-2]。相比此前最长的 MSC 数据集（53.3 轮、4 个会话、1,225.9 tokens），LoCoMo 在 token 量上达到其 9 倍、轮次 6 倍、会话数 4 倍[^src-3]。

评测框架由三项任务组成：(1) 问答任务（QA），细分为 single-hop、multi-hop、temporal reasoning、open-domain knowledge、adversarial 五类推理类型，共 7,512 道题；(2) 事件图摘要任务，要求模型从对话中提取说话者的因果-时序事件图并与 ground truth 对比；(3) 多模态对话生成任务，衡量模型在长期叙事中保持人设一致性和叙事连贯性的能力[^src-4]。

实验核心发现：人类在 QA 任务上达到 F1=87.9，最佳基座模型（GPT-4-turbo）仅 32.1，最佳 RAG（observation top-5）为 41.4，差距仍达 56%[^src-5]。

Mem0 论文将 LoCoMo（以 LOCOMO 命名）用作主要评估平台，但使用了 10 段更长对话（各约 600 轮、26K token），并将问题分为四类（排除了对抗性类别），展示了该基准在不同系统评测中的复用方式 [^card-1]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 0_abstract" -- "we collect LoCoMo, a dataset of very long-term conversations, each encompassing 300 turns and 9K tokens on avg., over up to 35 sessions"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table 1 / Section 3" -- "304.9 avg turns, 19.3 avg sessions, 9,209.2 avg tokens"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table 1 caption" -- "The average length of a conversation in LoCoMo is 9x that of MSC, distributed over 6x more turns and 4x more sessions"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 4" -- "we introduce an evaluation benchmark composed of three tasks to assess the accuracy of long-term memory"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 1_introduction" -- "still significantly lag behind human levels (by 56%), especially in temporal reasoning, (by 73%)"
[^card-1]: [LOCOMO 长期对话记忆基准测试设计](locomo-benchmark-design.md) -- Mem0 论文使用 LoCoMo 的变体版本（10 段 x ~600 轮 x 26K token）作为评估平台，排除了对抗性问题类别
