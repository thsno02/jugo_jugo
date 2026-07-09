---
id: memgpt-msc-dataset-extension
title: MemGPT 扩展 MSC 数据集用于评估
status: draft
card_type: methodology
tags: [memgpt, msc-dataset, multi-session-chat, dataset-augmentation, self-instruct]
created_time: 2026-06-12T10:32:00+08:00
edited_time: 2026-06-12T10:32:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-msc-dataset-extension.md
canonical_concept: msc-dataset-extension
aliases: [MSC数据集扩展, Multi-Session Chat, dataset augmentation, DMR dataset generation]
summary: >-
  MemGPT msc-dataset-extension 基于 Xu et al. 的 Multi-Session Chat 数据集（5 session 人类对话）创建 session 6 用于 DMR 评估，QA pairs 由独立 LLM 用 self-instruct 方式生成，要求答案不可从 persona 推断。
related: [memgpt-dmr-task-results, memgpt-llm-judge-evaluation]
---

MemGPT 的 conversational agent 评估基于对 Multi-Session Chat (MSC) 数据集的扩展：

**原始 MSC**：由 Xu et al. (2021) 引入，包含人类标注者生成的多 session 对话日志。每个对话有 5 个 session，每个 session 约十余条消息。每个标注者在所有 session 中扮演一致的 persona。[^src-1]

**扩展方法**：论文创建了 session 6，包含单个 QA response pair（用于 DMR 任务）。QA pairs 使用独立 LLM 通过 self-instruct 方式生成，prompt 要求：(a) 问题必须只能通过阅读对话历史回答；(b) 绝不能创建可从 persona 信息直接推断的问题。[^src-2]

**质量控制示例**：Good question——"Remember that one time we went surfing? What was that one place we went to for lunch called?"（需要具体对话记忆）；Bad question——"Do you like surfing?"（可从 persona 推断）。[^src-2]

然而，使用 LLM 生成评估数据存在 tradeoff：(a) 生成的问题可能偏向 LLM 容易表述的模式，不完全代表真实用户的记忆测试问题；(b) 论文未报告生成问题的人工审核通过率或质量分布；(c) session 6 仅有单个 QA pair 意味着每个对话样本只测试一个知识点，覆盖面有限。[^src-1]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Conversational agents dataset -- "We evaluate MemGPT and our fixed-context baselines on the Multi-Session Chat (MSC) dataset... each multi-session chat in MSC has five total sessions... we created a new session (session 6)"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Appendix: Self-instruct DMR dataset generation -- "Never, ever, ever create questions that can be answered from the persona information"
[^card-1]: -> memgpt-dmr-task-results -- 本卡描述 DMR 的数据集构建方法，该卡报告 DMR 的性能结果
