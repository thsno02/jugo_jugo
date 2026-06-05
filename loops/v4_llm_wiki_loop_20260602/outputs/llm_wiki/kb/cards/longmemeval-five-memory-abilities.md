---
id: longmemeval-five-memory-abilities
title: LongMemEval 五项核心长期记忆能力
status: accepted
card_type: distinction
tags: [benchmark, long-term-memory, memory-ability, evaluation-taxonomy, LongMemEval]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
justification: ../justification/longmemeval-five-memory-abilities.md
canonical_concept: longmemeval-five-memory-abilities
aliases: [五项记忆能力, five core memory abilities, IE/MR/KU/TR/ABS]
summary: >-
  longmemeval-five-memory-abilities（五项记忆能力 / five core memory abilities / IE/MR/KU/TR/ABS）将聊天助手的长期记忆评估分解为五项核心能力：信息提取(IE)、跨会话推理(MR)、知识更新(KU)、时间推理(TR)、拒答(ABS)，覆盖了先前基准遗漏的关键维度如知识更新与助手侧信息回忆
related: [lightmem-three-stage-memory, memory-crud-operation-taxonomy]
---

LongMemEval（ICLR 2025）将聊天助手的长期记忆评估定义为五项核心能力 [^src-1]：

1. **信息提取（Information Extraction, IE）**——从广泛的交互历史中回忆特定信息的能力，包括用户或助手提到的细节。
2. **跨会话推理（Multi-Session Reasoning, MR）**——综合跨多个历史会话的信息以回答涉及聚合和比较的复杂问题。
3. **知识更新（Knowledge Updates, KU）**——识别用户个人信息的变化并随时间动态更新用户知识。
4. **时间推理（Temporal Reasoning, TR）**——对用户信息的时间维度保持感知，包括显式时间提及和交互中的时间戳元数据。
5. **拒答（Abstention, ABS）**——识别寻求未知信息（即用户在交互历史中未提及的信息）的问题，并回答"我不知道"。

这一分类体系相比先前基准（如 MemoryBank 仅覆盖 IE+TR，PerLTQA 仅覆盖 IE+ABS）代表了更全面的能力覆盖 [^src-2]。特别是，所有此前的长期记忆基准均未评估助手侧信息的回忆能力，也未评估对用户信息更新的推理能力 [^src-3]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/3_benchmark.tex` -- Section 3.2 -- "LongMemEval formulates five core long-term memory abilities: Information Extraction (IE), Multi-Session Reasoning (MR), Knowledge Updates (KU), Temporal Reasoning (TR), Abstention (ABS)"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/3_benchmark.tex` -- Section 3.2 -- "this formulation represents a more comprehensive ability coverage compared to prior long-term memory benchmarks like MemoryBank and PerLTQA"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/1_introduction.tex` -- Section 1 -- "All long-term memory benchmarks including recent ones such as LoCoMo also fail to evaluate recall of information provided by the assistant or reasoning with updated user information"
