---
id: memgpt-dmr-task-results
title: MemGPT 深度记忆检索任务大幅超越基线
status: draft
card_type: empirical-result
tags: [memgpt, dmr, deep-memory-retrieval, consistency, msc-dataset, rouge-l]
created_time: 2026-06-12T10:23:00+08:00
edited_time: 2026-06-12T10:23:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-dmr-task-results.md
canonical_concept: dmr-task-performance
aliases: [深度记忆检索, deep memory retrieval, DMR task, consistency evaluation]
summary: >-
  MemGPT dmr-task-performance 在 DMR 任务中 MemGPT+GPT-4T 达 93.4% 准确率/ROUGE-L(R)=0.827，vs baseline GPT-4T 仅 35.3%/0.359；评估用 ROUGE-L recall + LLM Judge 双重验证。
related: [memgpt-dmr-vs-baseline-information-access, memgpt-conversation-opener-results, memgpt-llm-capability-dependency]
---

Deep Memory Retrieval（DMR）任务评估对话 agent 的一致性——测试 agent 能否准确回答明确指向先前对话的窄范围问题：

**任务设计**：基于 Multi-Session Chat（MSC）数据集，创建 session 6 包含单个 QA pair。问题由独立 LLM 生成，要求只能用对话历史（非 persona 信息）回答。[^src-1]

**评估方法**：ROUGE-L recall（R）处理生成答案更冗长的情况 + LLM Judge（GPT-4 判断生成回复与 gold response 的一致性，已证明与人类评判高度一致）。[^src-1]

**核心结果**：
| Model | Accuracy | ROUGE-L (R) |
|-------|----------|-------------|
| GPT-3.5 Turbo | 38.7% | 0.394 |
| + MemGPT | 66.9% | 0.629 |
| GPT-4 | 32.1% | 0.296 |
| + MemGPT | 92.5% | 0.814 |
| GPT-4 Turbo | 35.3% | 0.359 |
| + **MemGPT** | **93.4%** | **0.827** | [^src-2]

值得注意的是 GPT-4 baseline（32.1%）甚至低于 GPT-3.5 baseline（38.7%），但加 MemGPT 后 GPT-4 远超 GPT-3.5——说明 GPT-4 作为 summarization 目标反而更保守（少猜测），但作为 agent 底座更善于主动检索。

然而，DMR 任务的外部效度有限——MSC 数据集仅有 5 个 session（~60 条消息），远少于真实长期对话可能累积的数千条消息。MemGPT 在更大规模对话历史下的检索准确率论文未验证。[^src-1]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Deep memory retrieval task -- "We introduce a new 'deep memory retrieval' (DMR) task based on the MSC dataset designed to test the consistency of a conversational agent."
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Table: deep-memory-task -- "GPT-4 Turbo + MemGPT 93.4% 0.827"
[^card-1]: -> memgpt-dmr-vs-baseline-information-access -- 本卡报告 DMR 数值结果，该卡深入分析 MemGPT 与 baseline 的信息访问方式差异
[^card-2]: -> memgpt-llm-capability-dependency -- 本卡从 DMR 角度展示模型间性能差异，该卡综合分析 MemGPT 对模型能力的依赖
