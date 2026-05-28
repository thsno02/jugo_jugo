---
id: locomo-three-task-evaluation-framework
title: LoCoMo 用 QA + 事件摘要 + 多模态对话三任务测量"长期记忆"
status: accepted
card_type: concept
tags: [#evaluation, #long-term-memory, #benchmark]
created_time: 2026-05-26T14:10:00+08:00
edited_time: 2026-05-28T10:20:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
provenance_card: ../provenance/locomo-three-task-evaluation-framework.md
aliases: [LoCoMo 评测框架]
related: [locomo-long-context-adversarial-collapse, locomo-persona-event-graph-pipeline, longmemeval-five-core-memory-abilities]
---

## 三个任务对应的不同记忆面

LoCoMo 不把 "long-term memory" 当作单一指标，而是拆成三个相互独立的评测任务，对应不同的能力[^src1]：

1. **Question Answering (QA)**——直接检验"回忆"。每条问题分到 5 类 reasoning[^src2]：
   - single-hop（单 session 直接答）
   - multi-hop（跨多 session 综合）
   - temporal（时间推理）
   - open-domain knowledge（结合 commonsense / world knowledge）
   - adversarial（不可答，期望模型识别并拒答）—— 这一类是 long-context LLM 容易崩到 2.1% 的源头[^v3-1]
   评测用 F1 partial match；每条问题标注了出处 turn ID，可同时报告 RAG 检索 recall@k。
2. **Event Graph Summarization**——给定一段对话，要模型把其中发生的"个人事件"汇总成列表，与生成时的 ground-truth 事件图 $\mathcal{G}$[^v3-2] 对比。用 FactScore（atomic-fact precision/recall）替代 ROUGE/BLEU，因为关注事实是否对得上而不是字面相似[^src3]。
3. **Multi-Modal Dialog Generation**——给定 persona + 历史对话，让模型续写下一轮多模态对话，与 ground-truth 比 MMRelevance（image-text alignment）+ 常规 NLG 指标。

## 为什么三任务而不是一任务

- 直接 QA 只检验"记得起来"；事件摘要才检验"理解了长程因果"；对话生成才检验"能保持人物 + 叙事连贯"。
- 论文实验显示三者的赢家并不相同：QA 上 long-context 16K > 4K，但事件摘要上 long-context 反而比短 context 差（precision -3%、recall -8.7%）[^src4]，暗示**模型能"看到全文"不等于"理解了全文"**。
- 五种 reasoning 分类不是任意切法——它直接对应"哪一类长期记忆能力被破坏"：adversarial 测幻觉抑制，temporal 测时间推理，open-domain 测外部知识与对话的耦合。LongMemEval 把"五种能力"重新组织成 single-session preference / single-session assistant / temporal-reasoning / knowledge updates / multi-session 五大类，是同一思路的精细版本[^v3-3]。

## 边界与误用

- 三任务的标注全部基于 LLM 生成的对话 + 人工修订，标注本身就有 LLM bias；论文 limitations 自己点明长 form NLG 评估难度。
- adversarial 题在 long-context 模型上掉到 2.1% F1（GPT-3.5-turbo-16K），但在 base GPT-4-turbo 上反而 70.2%——说明 adversarial 表现强烈依赖模型本身的"会不会承认不知道"，不是单纯的长期记忆问题。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` — 第 296-333 行（benchmark 章节 4） — 三任务定义。
[^src2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` — 第 302-307 行 — "(1) \textbf{Single-hop} ... (2) \textbf{Multi-hop} ... (3) \textbf{Temporal reasoning} ... (4) \textbf{Open-domain knowledge} ... (5) \textbf{Adversarial} questions are designed to trick the agent into providing wrong answers, with the expectation that the agent will correctly identify them as unanswerable."
[^src3]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` — 第 320-323 行 — "we employ FactScore ... (1) precision of the summarized content by counting the number of atomic facts within the content that correspond with those in $\mathcal{G}$; (2) recall ..."
[^src4]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` — 第 491 行 — "$\texttt{gpt-3.5-turbo-16k}$ exhibits a decline in both precision (by 3.0\%) and recall (by 8.7\%) compared to $\texttt{gpt-3.5-turbo}$ which has a 4K context window."
[^v3-1]: [locomo-long-context-adversarial-collapse](locomo-long-context-adversarial-collapse.md) — adversarial 类对应的长上下文塌陷实验。
[^v3-2]: [locomo-persona-event-graph-pipeline](locomo-persona-event-graph-pipeline.md) — ground-truth 事件图 $\mathcal{G}$ 的来源。
[^v3-3]: [longmemeval-five-core-memory-abilities](longmemeval-five-core-memory-abilities.md) — LongMemEval 把 reasoning 类型组织成 5 种核心 memory 能力。
