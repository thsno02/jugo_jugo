---
id: memgpt-dmr-vs-baseline-information-access
title: DMR 中 MemGPT 与基线的信息访问差异
status: draft
card_type: comparison
tags: [memgpt, dmr, baseline, lossy-summarization, paginated-search, information-access]
created_time: 2026-06-12T10:15:00+08:00
edited_time: 2026-06-12T10:15:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-dmr-vs-baseline-information-access.md
canonical_concept: dmr-information-access-comparison
aliases: [DMR信息访问对比, lossy summarization vs paginated search]
summary: >-
  DMR dmr-information-access-comparison 中 baseline 看过去五次对话的有损摘要（信息少但直接可用），MemGPT 有完整历史但需分页检索调入上下文；MemGPT 大幅胜出说明主动检索收益远超摘要信息损失。
related: [memgpt-dmr-task-results, memgpt-recursive-summary-limitations]
---

DMR 任务中 MemGPT 与 fixed-context baseline 的核心区别在于信息访问方式：

**Baseline（有损摘要）**：看到过去五次对话的 lossy summarization，模拟 extended recursive summarization 流程。信息量少但全部直接在上下文中可见，LLM 无需额外操作即可参考。[^src-1]

**MemGPT（分页检索）**：有权访问完整对话历史（存储于 recall storage），但必须通过 paginated search queries 主动将相关信息调入 main context。信息量完整但需要 LLM 正确识别需要哪些信息并执行检索。[^src-1]

**结果解读**：MemGPT 大幅胜出（93.4% vs 35.3%）说明两点：(a) 有损摘要丢失的信息对窄范围问答至关重要——summary 可能保留了话题概况但丢失了具体细节（如"上次在夏威夷买了什么"这类细节在摘要中很可能被省略）；(b) MemGPT 的检索机制在 GPT-4 级别 LLM 的驱动下足够可靠，能找到正确的历史片段。

然而，这一比较的公平性有前提限制：baseline 的 summarization 策略论文未详细说明是最优的，可能存在更好的摘要方法缩小差距。此外 MemGPT 访问完整历史的优势在 sessions 增多到极大规模时可能因检索噪声而衰减。[^src-1]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: DMR -- "The baselines are able to see a lossy summarization of the past five conversations to mimic an extended recursive summarization procedure, while MemGPT instead has access to the full conversation history but must access it via paginated search queries to recall memory"
[^card-1]: -> memgpt-dmr-task-results -- 本卡分析 MemGPT 与 baseline 的信息访问差异，该卡报告 DMR 数值结果
[^card-2]: -> memgpt-recursive-summary-limitations -- 本卡从比较角度讨论 lossy summarization 的代价，该卡从 MemGPT 自身角度分析 recursive summary 的局限
