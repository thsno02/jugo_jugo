---
id: zep-dmr-benchmark-critique
title: DMR 已被 60 条消息的 full-context 打到 98%，不再适合评估长程记忆
status: accepted
card_type: source_claim
tags: [#benchmark, #dmr, #longmemeval, #memory-evaluation]
created_time: 2026-05-26T11:15:00+08:00
edited_time: 2026-05-28T11:36:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
provenance_card: ../provenance/zep-dmr-benchmark-critique.md
aliases: [DMR 基准批判, Deep Memory Retrieval 局限]
related: [zep-graphiti-three-tier-graph, zep-bi-temporal-edges, zep-hybrid-search-rerank, memgpt-dmr-task-evaluation, longmemeval-five-core-memory-abilities]
---

Zep 论文用一整节论证 MemGPT 团队提出的 **Deep Memory Retrieval (DMR) 基准已不适合衡量"agent 长程记忆"**，给出的依据可以独立成立，不依赖于"Zep 比 MemGPT 强"这一点：

1. **规模太小，已被 baseline 打满**：DMR 一共 500 段对话，每段 5 个 session、单 session ≤12 条 message，平均一段才 60 条消息——直接塞进现代 LLM 的上下文窗口完全没问题。论文复现的"full-conversation baseline"在 gpt-4-turbo 上拿到 94.4%，gpt-4o-mini 上拿到 98.0%，已经超过原 MemGPT 报告的 93.4%。换句话说，**任何检索/记忆策略带来的提升都被"全部塞进上下文"这种朴素做法挤压到零点几个百分点的边际**。
2. **问题形态过窄**：DMR 全是"单轮、事实型"问题，根本不考查多 session 综合、时间推理、知识更新这种真实长程记忆能力。
3. **题面措辞含糊**：很多问题用了"favorite drink to relax with"、"weird hobby"这类原对话里并没有显式标注的概念，使得正确答案在某种程度上靠 LLM 自己脑补一致性。
4. **不代表企业场景**：DMR 对话很短、风格单一，不能反映客服、跨会话综合等实际部署。
5. **复现性差**：Zep 团队"由于 MemGPT 论文方法学不足，无法用 gpt-4o-mini 复现 MemGPT 的 DMR 结果"。

操作含义：
- 用 DMR 作为新记忆系统主基准已经不能区分方法优劣；
- 论文给出的替代是 LongMemEval（平均 115k tokens、六类问题），后者中 Zep 相对 full-context 有 18.5% 的精度提升 + ~90% 延迟降低，**真正能拉开差距**；
- 对工程团队的含义：**评估记忆系统时要看上下文长度增长曲线下方法的相对优势，而不是单一短上下文的点估计**。

边界：批判针对的是 DMR 作为基准的"区分能力"，不是 MemGPT 算法本身。Zep 自己也没在 LongMemEval 上拿到 MemGPT 的对比数（论文明说 MemGPT 框架不支持注入既有历史，他们 workaround 用 archival history 也跑不出回答），这一处比较未实现。

## References

Zep 论文 §4.2 "Deep Memory Retrieval (DMR)" 与 §4.3.1 "LongMemEval and MemGPT"。

- 源路径：`data/raw/arxiv/arxiv-zep/agent_source_bundle.txt`（main.tex 行 218–226 DMR 批判与基线复现数据；表 1 行 236–252；行 257–266 转用 LongMemEval 与 MemGPT 比较的工程困难）。

## Footnotes

- "已被打满"原文（行 222–224）："Zep achieved 94.8% accuracy with gpt-4-turbo and 98.2% with gpt-4o-mini ... each conversation contains only 60 messages, easily fitting within current LLM context windows."
- 五点局限原文（行 224）："The evaluation relies exclusively on single-turn, fact-retrieval questions ... Many questions contain ambiguous phrasing ... Most critically, the dataset poorly represents real-world enterprise use cases for LLM agents."
- 无法对比 MemGPT 原文（行 266）："we attempted to evaluate MemGPT using the LongMemEval dataset ... we were unable to achieve successful question responses using this approach."
