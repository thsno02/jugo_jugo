---
id: locomo-very-long-term-dialogue-dataset
title: LoCoMo 把"超长期对话"定义为 9K token、19 个 session 的量级
status: accepted
card_type: source_claim
tags: [#long-term-memory, #dialogue-dataset, #benchmark]
created_time: 2026-05-26T14:00:00+08:00
edited_time: 2026-05-28T10:16:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
provenance_card: ../provenance/locomo-very-long-term-dialogue-dataset.md
aliases: [LoCoMo dataset, 超长对话 benchmark]
related: [longmemeval-five-core-memory-abilities, locomo-three-task-evaluation-framework, locomo-persona-event-graph-pipeline, mem0-locomo-benchmark-evaluation, longmemeval-benchmark-construction-pipeline]
---

## 这张卡片想锁定什么

之前 long-term dialogue 工作（MSC、Conversation Chronicles）所谓的"长对话"通常 ≤5 session、≤1.2K token，等于把"几天的聊天"当作长期。LoCoMo（Maharana et al., 2024，ACL）把这个量级提高了一个数量级，明确把"超长期"定义在：

- **平均 300 turn、9,209 token、19.3 session、跨数月**——是 MSC（53 turn / 1.2K token / 4 session / 几天）的约 9 倍 token、6 倍 turn、4 倍 session。
- 共 50 段对话，且是 multi-modal（含图片）的双角色对话。

## 为什么这个边界值得固定下来

- 这是后续 mem0 等系统反复引用的"事实上的长记忆评测上限"。讨论 long-context LLM 或 RAG 在长对话里的表现时，"是否能 cover 9K token / 19 session"成为基本门槛。
- 它也间接界定了**"超长期"不是 token 量级，而是 session 数 + 时间跨度**：跨月的多次 session 才会触发时间推理、persona 一致性等真正的长期记忆问题，单次塞进 context 的 9K token 并不等价。

## 边界与误用

- LoCoMo 的 9K token 在今天 long-context 模型眼里仍属"短"——单看 token 数不会触发 lost-in-the-middle；真正难的是 **多 session 的时间/因果连贯**。
- 数据是 LLM 生成 + 人工编辑（编辑了约 15% 的 dialog turn、19% 的图片），不是真实长期人际对话；不要把它当作真实用户行为分布。

## References

- 论文标题与统计来源：`data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` 第 72-77 行（title / authors）、第 113-114 行（abstract: 300 turns, 9K tokens, up to 35 sessions, 50 conversations）、第 149 行（与其他数据集对比）。

## Footnotes

- 原文："we collect \dataset{}, a dataset of \textit{very} long-term conversations, each encompassing 300 turns and 9K tokens on avg., over up to 35 sessions."（第 114 行）
- 对比表中 LoCoMo 行：`304.9 turns | 19.3 sessions | 9,209.2 tokens | few months | multimodal`（第 149 行）。
- 同样在 anthology 引用里写的是 600 turns / 16K tokens / 32 sessions（第 1844 行）——是 ACL 最终版的数字，与本文 arXiv 版略有出入；本卡以 arXiv 版 abstract 为准。
