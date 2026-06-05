---
id: temporal-event-graph-grounding
title: 时序事件图作为对话锚定机制
status: accepted
card_type: mechanism
tags: [temporal-event-graph, dialogue-grounding, causal-connection, persona, agent-architecture]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
justification: ../justification/temporal-event-graph-grounding.md
canonical_concept: temporal-event-graph-grounding
aliases: [temporal event graph, 时序事件图, 因果事件图]
summary: >-
  temporal-event-graph-grounding（temporal event graph, 时序事件图, 因果事件图）为每个对话代理构建含日期和因果连接的生活事件图（最多 25 事件 / 6-12 个月），作为长期对话的叙事锚定，迫使对话反映真实时间推移和因果关系
related: [locomo-benchmark, observation-based-memory-representation]
---

LoCoMo 的对话生成管线为每个虚拟代理构建一个时序事件图（temporal event graph）$\mathcal{G}$，用于将对话锚定在真实的人生经历上[^src-1]。该图包含事件节点 $e_i$（各带日期 $t_i$）和因果连接 $l = (e_i, e_j)$，体现事件间的因果关系和自然继承关系[^src-2]。

图的生成采用迭代过程：先基于人设声明（persona）用 LLM（text-davinci-003）生成初始批次 $k=3$ 个独立事件，再以已有事件为输入迭代生成后续事件，每个图最多 25 个事件，时间跨度 6-12 个月[^src-3]。这种迭代设计在推理开销和时间-因果连贯性之间取得平衡。

在对话生成时，代理的回复会额外以两次会话之间发生的事件子集为条件：$\{e \in \mathcal{G} \mid t_k^s < t_i^e < t_{k+1}^s\}$，从而在对话中注入长期时序叙事[^src-4]。例如，某角色 Jack 热爱游戏 -> 被知名游戏公司邀请，或立志做酒店经理 -> 报名酒店管理课程 -> 三个月后在社交媒体分享心得[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.2" -- "we construct a temporal event graph, labeled as G, for each agent"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.2" -- "G includes causal connections l = (e_i, e_j) that illustrate the causal relationships among events"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.2" -- "we create up to 25 events, spread across a time frame of 6 to 12 months, in an iterative process... Initially, a small batch of k=3 events is generated"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.3" -- "Long-term temporal narratives are induced in the conversation by additionally conditioning the agent's response on the subset of events in G that occur between the last and current session"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Appendix Section A.2" -- "Jack aspires to be a hotel manager. Consequently, he enrolls in a hotel management course in July, and after three months, he expresses his excitement about the course on social media"
