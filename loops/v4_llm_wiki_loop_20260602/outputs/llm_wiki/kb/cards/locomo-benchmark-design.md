---
id: locomo-benchmark-design
title: LOCOMO 长期对话记忆基准测试设计
status: accepted
card_type: example_pattern
tags: [benchmark, LOCOMO, evaluation, long_term_memory, question_taxonomy]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
justification: ../justification/locomo-benchmark-design.md
canonical_concept: locomo-benchmark-design
aliases: [LOCOMO 基准, LOCOMO benchmark, 长期对话记忆评测]
summary: >-
  locomo-benchmark-design（LOCOMO 基准 / LOCOMO benchmark）LOCOMO 包含 10 段长对话（各约 600 轮、26K token），配有平均 200 个问题，分为四类：单跳（单轮事实检索）、多跳（跨会话信息整合）、时序（事件排序与时间推理）、开放域（需外部知识整合），用于全面评估长期对话记忆系统
related: [full-context-accuracy-ceiling, lexical-vs-semantic-eval-gap, locomo-benchmark, locomo-five-reasoning-types, memory-vs-rag-salience]
---

LOCOMO 是由 Maharana et al. 设计的长期对话记忆评测基准，被 Mem0 论文用作主要评估平台 [^src-1]。

**数据集结构**：包含 10 段扩展对话，每段约 600 轮对话、平均约 26000 token，分布在多个会话中。每段对话描述两个人讨论日常经历或过去事件。每段对话附带平均约 200 个问题及对应的标准答案 [^src-2]。

**问题四分类**：

1. **单跳（Single-hop）**：定位包含在单个对话轮次中的单一事实片段。考察基础记忆检索能力。

2. **多跳（Multi-hop）**：需要综合分散在多个对话会话中的信息。考察记忆整合和跨会话推理能力。

3. **时序（Temporal）**：依赖于对事件序列、相对时序和持续时间的精确建模。考察时间推理能力。

4. **开放域（Open-domain）**：需要将对话记忆与更广泛的知识整合。考察外部知识融合能力 [^src-3]。

原始数据集还包含对抗性问题类别（旨在测试系统识别不可回答问题的能力），但因缺少标准答案而在 Mem0 论文的评估中被排除 [^src-4]。

LoCoMo 原始论文提供了该基准的更完整描述：50 段对话（各约 300 轮、9K tokens），并包含第五类对抗性问题（1,871 题），人类 QA F1=87.9 远超最佳模型 41.4 [^card-1]。LoCoMo 的五类推理维度中，adversarial 类别因缺少标准答案而在 Mem0 评测中被排除，但该维度揭示了长上下文模型的最大脆弱性（仅 2.1%）[^card-2]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/experiment_setup.tex -- "The LOCOMO dataset is designed to evaluate long-term conversational memory in dialogue systems."
[^src-2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/experiment_setup.tex -- "It comprises 10 extended conversations, each containing approximately 600 dialogues and 26000 tokens on average, distributed across multiple sessions."
[^src-3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/experiment_setup.tex -- "These questions are categorized into multiple types: single-hop, multi-hop, temporal, and open-domain."
[^src-4]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/experiment_setup.tex -- "The dataset originally included an adversarial question category...However, this category was excluded from our evaluation because ground truth answers were unavailable"
[^card-1]: [LoCoMo 超长期对话记忆评测基准](locomo-benchmark.md) -- LoCoMo 原始论文描述了完整的 50 段对话数据集和三项评测任务，人类 QA F1=87.9 远超最佳模型
[^card-2]: [LoCoMo 对话记忆 QA 的五类推理维度](locomo-five-reasoning-types.md) -- 原始 LoCoMo 定义了五类推理维度（含 adversarial），揭示了时序推理差距最大（73%）和对抗性问题的模型脆弱性
