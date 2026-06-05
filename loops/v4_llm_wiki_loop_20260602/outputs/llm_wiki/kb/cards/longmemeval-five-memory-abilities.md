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
related: [dmr-benchmark-inadequacy, lightmem-three-stage-memory, locomo-five-reasoning-types, long-term-memory-accuracy-gap, memory-crud-operation-taxonomy]
---

LongMemEval（ICLR 2025）将聊天助手的长期记忆评估定义为五项核心能力 [^src-1]：

1. **信息提取（Information Extraction, IE）**——从广泛的交互历史中回忆特定信息的能力，包括用户或助手提到的细节。
2. **跨会话推理（Multi-Session Reasoning, MR）**——综合跨多个历史会话的信息以回答涉及聚合和比较的复杂问题。
3. **知识更新（Knowledge Updates, KU）**——识别用户个人信息的变化并随时间动态更新用户知识。
4. **时间推理（Temporal Reasoning, TR）**——对用户信息的时间维度保持感知，包括显式时间提及和交互中的时间戳元数据。
5. **拒答（Abstention, ABS）**——识别寻求未知信息（即用户在交互历史中未提及的信息）的问题，并回答"我不知道"。

这一分类体系相比先前基准（如 MemoryBank 仅覆盖 IE+TR，PerLTQA 仅覆盖 IE+ABS）代表了更全面的能力覆盖 [^src-2]。特别是，所有此前的长期记忆基准均未评估助手侧信息的回忆能力，也未评估对用户信息更新的推理能力 [^src-3]。

LoCoMo 的五类 QA 推理维度（single-hop/multi-hop/temporal/open-domain/adversarial）与本卡的能力分类存在交叉对应：single-hop↔IE、multi-hop↔MR、temporal↔TR、adversarial↔ABS，但 LoCoMo 另有 open-domain 维度而未覆盖知识更新 [^card-1]。基于这五项能力的实证评测揭示了当前系统的巨大差距——商业系统和长上下文 LLM 在持续交互中均出现 30%-64% 的准确率下降 [^card-2]。Zep 论文对 DMR 基准的批评（仅含单轮事实检索）进一步佐证了本卡关于先前基准覆盖不足的论断——DMR 实质上仅评估了信息提取（IE）一个维度 [^card-3]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-longmemeval/source/text/3_benchmark.tex` -- Section 3.2 -- "LongMemEval formulates five core long-term memory abilities: Information Extraction (IE), Multi-Session Reasoning (MR), Knowledge Updates (KU), Temporal Reasoning (TR), Abstention (ABS)"
[^src-2]: `data/raw/arxiv/arxiv-longmemeval/source/text/3_benchmark.tex` -- Section 3.2 -- "this formulation represents a more comprehensive ability coverage compared to prior long-term memory benchmarks like MemoryBank and PerLTQA"
[^src-3]: `data/raw/arxiv/arxiv-longmemeval/source/text/1_introduction.tex` -- Section 1 -- "All long-term memory benchmarks including recent ones such as LoCoMo also fail to evaluate recall of information provided by the assistant or reasoning with updated user information"
[^card-1]: [LoCoMo 对话记忆 QA 的五类推理维度](locomo-five-reasoning-types.md) -- 本卡聚焦 LongMemEval 的系统能力分类（含知识更新 KU），该卡聚焦 LoCoMo 的问题推理分类（含开放域知识），两套分类体系在 MR/TR/ABS 维度高度对应
[^card-2]: [长期记忆准确率差距（30-60% 下降）](long-term-memory-accuracy-gap.md) -- 本卡定义了五项评测维度，该卡报告了基于这些维度的实证发现：当前系统存在 30-64% 的准确率差距
[^card-3]: [DMR 基准测试的局限性](dmr-benchmark-inadequacy.md) -- 本卡定义了五项完整的记忆能力维度，该卡所批评的 DMR 基准仅评估了信息提取（IE）一个维度
