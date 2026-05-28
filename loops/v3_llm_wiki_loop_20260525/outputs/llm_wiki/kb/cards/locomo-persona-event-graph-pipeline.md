---
id: locomo-persona-event-graph-pipeline
title: LoCoMo 的对话生成靠 persona + 时间事件图 + reflect/respond 三件套
status: accepted
card_type: mechanism
tags: [#dialogue-generation, #generative-agent, #event-graph]
created_time: 2026-05-26T14:05:00+08:00
edited_time: 2026-05-28T10:18:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
provenance_card: ../provenance/locomo-persona-event-graph-pipeline.md
aliases: [LoCoMo 生成管线]
related: [locomo-very-long-term-dialogue-dataset, locomo-three-task-evaluation-framework, locomo-event-summarization-five-error-types, longmemeval-benchmark-construction-pipeline]
---

## 机制概览

LoCoMo 不是真实采集的对话，而是用 LLM 双 agent 自对话 + 人工编辑生成。要让"长达数月、上百轮"的对话保持人物一致与事件因果，它把生成分成三个独立模块：

1. **Persona $p$**：从 MSC 的 4-5 句 persona seed 用 `gpt-3.5-turbo` 扩写成完整 persona statement（目标、过往经历、日常习惯、人际关系、姓名/年龄/性别）。
2. **时间事件图 $\mathcal{G}$**：用 `text-davinci-003` 基于 persona 生成 6-12 个月跨度内最多 25 个事件，每个事件带日期 $t_i$，事件之间标注因果连接 $l=(e_i, e_j)$。事件迭代生成，每批 $k=3$ 个，下一批以已有事件为 prompt——平衡推理成本和因果连贯。
3. **Reflect & respond + image sharing/reaction**：复用 Park et al. (2023) 的 generative agent 架构。每个 session $k$ 结束后生成摘要 $w_k$ 入短期记忆 $\mathcal{H}_s$；每个 turn $j$ 抽取为 *observation* $o_{k_j}$ 入长期记忆 $\mathcal{H}_l$。下一 session 的 response 同时基于：上次摘要 $w_k$ + 检索到的相关 observation + 当前 session 历史 $h_{k+1}$ + persona + 落在两次 session 时间窗内的事件集合 $\{e \mid t_k^s < t_i^e < t_{k+1}^s\}$。

最后人工编辑约 15% 的 turn、19% 的 image，主要修长程一致性、对齐事件图。

## 为什么值得抓住

- 这是后续 mem0、LongMemEval 等系统直接复用的"persona + observation"分层骨架，区分了"会话摘要 / 个人陈述 / 事件"三种粒度。
- "事件图驱动 → 对话基于事件窗口"暗示**长期一致性的根因不是模型记忆，而是有一个外部因果时间线 anchor**；这条 anchor 在数据生成时被显式构造，评测时再让模型反向恢复。

## 边界与误用

- Persona 与事件都靠 LLM 生成，分布与真实长期人际关系并不等同；论文自己在 limitations 里承认。
- Image 是 web search 抓取后用 BLIP-2 captioning 进入长期记忆，长时一致性（外观、家、宠物）几乎丧失，论文也明说"用 caption 替换 image 几乎不损失信息"。

## References

- 三模块与 reflect/respond 的完整描述：`data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` 第 238-285 行（pipeline、persona、event graph、agent architecture 章节）。
- 人工编辑比例：第 290 行。

## Footnotes

- Reflect/respond 公式："agent $\mathcal{L}_i$ generates a response in session $k+1$ on the date $t_{k+1}^s$ by basing it on the latest summary $w_k$, reflections based on the retrieved relevant observations $o \in \mathcal{H}_s$, the ongoing conversation history in the current session $h_{k+1}$ and persona statement $p$. Long-term temporal narratives are induced ... by additionally conditioning the agent's response on the subset of events in $\mathcal{G}$ that occur between the last and current session"（第 272 行）。
- 事件图迭代生成：第 258 行 "Initially, a small batch of $k=3$ events is generated, which is then used iteratively as input prompt"。
