---
id: longmemeval-commercial-system-memory-gap
title: 商用记忆系统在 LongMemEval 上的性能差距
status: accepted
card_type: empirical-finding
tags:
- long-term-memory
- ChatGPT
- Coze
- performance-gap
- evaluation
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-longmemeval
evidence_basis: experimental_paper
justification: ../justification/longmemeval-commercial-system-memory-gap.md
canonical_concept: commercial-memory-system-gap
aliases:
- commercial memory system gap
- ChatGPT memory degradation
- Coze memory failure
summary: commercial-memory-system-gap 商用记忆对话系统在 LongMemEval 上表现显著低于离线阅读基线。ChatGPT 使用 GPT-4o 从离线阅读的 0.9184 降至 0.5773（降 37%），Coze GPT-4o 降至 0.3299（降 64%）。ChatGPT 倾向在压缩历史时覆写关键信息，Coze 经常无法记录间接提供的用户信息。揭示"通过召回孤立事实构建表面个性化"与"真正强大记忆能力"之间的差距。
related:
- longmemeval-benchmark-overview
- longmemeval-long-context-llm-degradation
---
在 LongMemEval 的先导研究中，两个商用记忆增强聊天系统表现出显著的性能下降：[^src-1]

- ChatGPT（GPT-4o）：从离线阅读的 0.9184 降至在线记忆的 0.5773，下降 37%
- ChatGPT（GPT-4o-mini）：在线记忆准确率 0.7113
- Coze（GPT-4o）：降至 0.3299，下降 64%
- Coze（GPT-3.5-turbo）：降至 0.2474

人工分析揭示了两种不同的失败模式：ChatGPT 倾向于在对话继续时压缩历史并覆写关键信息；Coze 经常无法记录用户间接提供的信息。[^src-2]

这一结果突出了"通过召回孤立事实构建看似个性化的聊天助手"与"展示真正强大的记忆能力"之间存在的差距。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "figures/proof_of_difficulty.tex" -- "ChatGPT and Coze instantiated with GPT-4o exhibits 37% and 64% performance drop, respectively"
[^src-2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/appendix.tex" Section "A Human Study on Commercial Memory Chatbots" -- "ChatGPT often modify this information when it compresses the history, resulting in information loss"
[^src-3]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/3_benchmark.tex" -- "gap between building a seemingly personalized chat assistant by recalling isolated facts and demonstrating a genuinely strong memory ability"
