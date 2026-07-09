---
id: temporal-event-graph-dialogue
title: 时间事件图驱动对话生成
status: accepted
card_type: method
tags:
- temporal-event-graph
- dialogue-generation
- causal-chain
- persona-grounded
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-locomo
evidence_basis: experimental_paper
justification: ../justification/temporal-event-graph-dialogue.md
canonical_concept: temporal-event-graph-dialogue
aliases:
- temporal event graph
- 时间事件图
- event graph G
- causal event timeline
summary: temporal-event-graph-dialogue 时间事件图驱动对话生成方法。为每个 agent 构建包含最多25个因果链接事件的 temporal event graph G，事件跨度6-12个月。用 text-davinci-003 基于 persona 迭代生成（每批k=3），后续事件以先前事件为条件保持因果一致性。对话生成时 agent 条件于两次 session
  间新发生的事件子集 {e in G | t_k^s < t_i^e < t_{k+1}^s}，注入长程时间叙事。
related:
- locomo-dataset
- locomo-human-machine-pipeline
- locomo-event-summarization-degradation
- locomo-evaluation-framework
- reflect-and-respond-agent
---
Temporal event graph 是 LoCoMo 数据生成管线的核心组件，用于为每个 LLM agent 模拟真实生活事件序列。[^src-1]

构建过程：给定 persona statement p，用 text-davinci-003 迭代产生事件图 G。首先生成 k=3 个独立事件作为初始化，然后以已有事件为条件迭代生成后续因果关联事件，每个事件 e_i 关联发生日期 t_i，事件间建立因果连接 l=(e_i, e_j)。每个图最多 25 个事件，时间跨度 6-12 个月。[^src-2]

在对话生成中，agent 在 session k+1 响应时条件于两次 session 之间发生的事件子集，从而将长期时间叙事自然注入对话。[^src-3]

事件图同时作为 event summarization 任务的 ground truth：模型需从对话中还原出事件图，评估其对时间和因果动态的理解。[^src-4] [^card-1]

[^src-1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Temporal Event Graph" -- "we construct a temporal event graph, labeled as G, for each agent"
[^src-2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Temporal Event Graph" -- "we create up to 25 events, spread across a time frame of 6 to 12 months, in an iterative process... Initially, a small batch of k=3 events is generated"
[^src-3]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Reflect & Respond" -- "Long-term temporal narratives are induced in the conversation by additionally conditioning the agent's response on the subset of events in G that occur between the last and current session"
[^src-4]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Event Summarization Task" -- "the event graphs linked to each LLM speaker serve as the correct answers"

[^card-1]: 与 [locomo-dataset] 关联——事件图是该数据集的结构支柱
