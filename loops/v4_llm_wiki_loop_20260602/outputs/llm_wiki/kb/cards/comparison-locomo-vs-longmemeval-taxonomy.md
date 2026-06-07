---
id: comparison-locomo-vs-longmemeval-taxonomy
title: LoCoMo 五类推理 vs LongMemEval 五项能力——两套记忆评测分类体系的对比
status: accepted
card_type: distinction
tags: [benchmark, evaluation-taxonomy, LoCoMo, LongMemEval, memory-ability, reasoning-types]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo, arxiv-longmemeval]
justification: ../justification/comparison-locomo-vs-longmemeval-taxonomy.md
canonical_concept: locomo-vs-longmemeval-taxonomy
aliases: [记忆评测分类对比, LoCoMo vs LongMemEval taxonomy comparison]
summary: >-
  comparison-locomo-vs-longmemeval-taxonomy（记忆评测分类对比）LoCoMo 的五类推理维度（single-hop/multi-hop/temporal/open-domain/adversarial）面向问题复杂度，LongMemEval 的五项记忆能力（IE/MR/KU/TR/ABS）面向系统能力；两者在 MR/TR/ABS 三个维度高度对应，但 LoCoMo 独有 open-domain 维度而缺少知识更新（KU）和助手侧信息回忆
related: [locomo-five-reasoning-types, longmemeval-five-memory-abilities]
---

LoCoMo（2024）和 LongMemEval（ICLR 2025）各自提出了包含五个维度的长期记忆评测分类体系，但设计视角不同 [^card-1] [^card-2]。

**分类视角差异**：LoCoMo 的五类维度以"问题需要何种推理"为轴，关注的是回答问题的认知复杂度（从单跳检索到跨会话综合再到时序推理）。LongMemEval 的五项维度以"系统需要何种能力"为轴，关注的是记忆系统必须具备的功能属性（从信息提取到知识更新到拒答）。

**高度对应的三个维度**：

| LoCoMo 推理类型 | LongMemEval 记忆能力 | 对应关系 |
|---|---|---|
| Multi-hop | Multi-Session Reasoning (MR) | 均需跨会话信息综合 |
| Temporal reasoning | Temporal Reasoning (TR) | 均需时间维度建模 |
| Adversarial | Abstention (ABS) | 均需识别不可回答的问题 |

**LoCoMo 独有维度**：
- **Single-hop**：LongMemEval 将其归入更宽泛的 Information Extraction (IE)，不作为独立维度。
- **Open-domain knowledge**：需整合外部世界知识与对话记忆。LongMemEval 未单独评估此能力。

**LongMemEval 独有维度**：
- **Knowledge Updates (KU)**：识别用户信息的变化并动态更新。LoCoMo 的对话设计未包含信息覆盖/更新场景。
- **IE 中的助手侧信息**：LongMemEval 的 IE 维度显式包含回忆助手自身说过的话，而 LoCoMo 仅评估用户侧信息。

LongMemEval 论文明确指出"所有此前的长期记忆基准（包括 LoCoMo）均未评估助手侧信息的回忆能力，也未评估对用户信息更新的推理能力"，这一批评精准定位了两套分类体系的覆盖差距。

## Footnotes

[^card-1]: [LoCoMo 对话记忆 QA 的五类推理维度](locomo-five-reasoning-types.md) -- LoCoMo 的五类推理维度以问题复杂度为分类轴，含独有的 open-domain 维度
[^card-2]: [LongMemEval 五项核心长期记忆能力](longmemeval-five-memory-abilities.md) -- LongMemEval 的五项能力以系统功能为分类轴，含独有的知识更新（KU）和助手侧信息回忆
[^src-1]: data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt -- "we introduce a question-answering task divided into five distinct reasoning categories: (1) Single-hop questions require answers based on a single session; (2) Multi-hop questions require synthesizing information from multiple different sessions; (3) Temporal reasoning questions can be answered through temporal reasoning and capturing time-related data cues within the conversation; (4) Open-domain knowledge questions can be answered by integrating a speaker's provided information with external knowledge such as commonsense or world facts; (5) Adversarial questions are designed to trick the agent into providing wrong answers"
[^src-2]: data/raw/arxiv/arxiv-longmemeval/text.txt -- "five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention"
