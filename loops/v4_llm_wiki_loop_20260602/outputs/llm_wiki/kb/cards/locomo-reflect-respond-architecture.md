---
id: locomo-reflect-respond-architecture
title: LoCoMo 反思-回应双层记忆代理架构
status: accepted
card_type: mechanism
tags: [agent-architecture, short-term-memory, long-term-memory, reflect-respond, generative-agents]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
justification: ../justification/locomo-reflect-respond-architecture.md
canonical_concept: locomo-reflect-respond-architecture
aliases: [reflect and respond, 反思-回应架构, LoCoMo agent architecture]
summary: >-
  locomo-reflect-respond-architecture（reflect and respond, 反思-回应架构）LoCoMo 代理采用双层记忆：短期记忆为逐会话递增摘要（avg 127.4 tokens），长期记忆为对话轮次的 observation 断言（avg 18.2 tokens），回复时综合最新摘要+检索的相关 observation+当前会话+人设+会话间事件
related: [observation-based-memory-representation, temporal-event-graph-grounding, episodic-semantic-memory-duality, sleep-consolidation-architecture]
---

LoCoMo 论文中的虚拟代理采用源自 Park et al. (2023) 生成式代理架构的"反思与回应"（reflect & respond）机制，实现了短期-长期双层记忆系统[^src-1]。

**短期记忆** $\mathcal{H}_s$：每个会话 $k$ 结束后，代理生成一个会话摘要 $w_k$（平均 127.4 tokens），该摘要以当前会话对话历史 $h_k$ 和前一个摘要 $w_{k-1}$ 为条件生成，形成递增式摘要链[^src-2]。

**长期记忆** $\mathcal{H}_l$：每个对话轮次 $h_{k_j}$ 被转化为一个观察 $o_{k_j}$（平均 18.2 tokens），即关于说话者的断言式陈述，存入长期记忆[^src-3]。观察带有来源轮次 ID 标注，便于追踪证据链。

**回复生成**：代理在会话 $k+1$ 中生成回复时，综合以下信息：最新摘要 $w_k$、从长期记忆中检索的相关 observation、当前会话历史 $h_{k+1}$、人设声明 $p$、以及两次会话间发生的事件子集[^src-4]。这种架构模拟了人类在对话中同时依赖近期对话的短期记忆和蒸馏过的长期经验记忆的方式。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.3" -- "Every agent L_i incorporates modules from generative agent architecture (Park et al. 2023)... reflect and respond"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.3" -- "each agent is asked to produce a summary w_k... conditioned on both the most recent session conversation history h_k and the preceding summary w_{k-1}"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.3 + Table dataset_statistics" -- "a single turn of the conversation h_{k_j} is transformed into an observation o_{k_j}... Avg tokens observation: 18.2"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.3" -- "agent generates a response by basing it on the latest summary w_k, reflections based on the retrieved relevant observations, the ongoing conversation history, persona statement p"
