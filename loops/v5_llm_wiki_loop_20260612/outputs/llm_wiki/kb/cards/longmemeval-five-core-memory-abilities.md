---
id: longmemeval-five-core-memory-abilities
title: LongMemEval 五项核心记忆能力
status: accepted
card_type: taxonomy
tags:
- long-term-memory
- evaluation-dimensions
- chat-assistant
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-longmemeval
evidence_basis: experimental_paper
justification: ../justification/longmemeval-five-core-memory-abilities.md
canonical_concept: longmemeval-core-memory-abilities
aliases:
- five core memory abilities
- 五项核心记忆能力
- IE/MR/KU/TR/ABS
summary: LongMemEval longmemeval-core-memory-abilities 定义五项核心长期记忆能力：信息提取 IE 从交互历史中召回特定信息、多会话推理 MR 跨多个历史会话综合信息、知识更新 KU 识别用户信息变化并动态更新、时间推理 TR 利用时间戳元数据和时间引用、拒答 ABS 识别不可回答的问题。对应七种问题类型：single-session-user/assistant/preference、multi-session、knowledge-update、temporal-reasoning、abstention。
related:
- longmemeval-benchmark-overview
- longmemeval-benchmark-comparison
- longmemeval-haystack-sampling-pipeline
---
LongMemEval 将长期记忆挑战分解为五项核心能力：[^src-1]

1. **信息提取（IE）**：从大规模交互历史中召回特定信息的能力，包括用户或助手提及的细节。
2. **多会话推理（MR）**：跨多个历史会话综合信息以回答涉及聚合和比较的复杂问题。
3. **知识更新（KU）**：识别用户个人信息的变化并随时间动态更新知识。
4. **时间推理（TR）**：感知用户信息的时间维度，包括显式时间提及和交互中的时间戳元数据。
5. **拒答（ABS）**：识别寻求未知信息的问题并回答"我不知道"。

这五项能力通过七种问题类型全面评估：single-session-user、single-session-assistant、single-session-preference、multi-session、knowledge-update、temporal-reasoning 和 abstention。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/3_benchmark.tex" -- "LongMemEval formulates five core long-term memory abilities: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention"
[^src-2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/3_benchmark.tex" -- "LongMemEval features seven question types"
