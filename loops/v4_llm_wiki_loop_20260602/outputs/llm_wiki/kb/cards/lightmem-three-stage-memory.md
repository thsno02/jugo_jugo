---
id: lightmem-three-stage-memory
title: LightMem 三阶段记忆架构
status: accepted
card_type: mechanism
tags: [memory-system, llm-memory, atkinson-shiffrin, multi-stage-architecture, cognitive-inspired]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-lightmem]
justification: ../justification/lightmem-three-stage-memory.md
canonical_concept: lightmem-three-stage-memory
aliases: [LightMem, 三阶段记忆, Atkinson-Shiffrin LLM记忆]
summary: >-
  lightmem-three-stage-memory（LightMem, 三阶段记忆, Atkinson-Shiffrin LLM记忆）借鉴人类 Atkinson-Shiffrin 认知模型，将 LLM 记忆系统分为感觉记忆（轻量压缩+主题分组）、短期记忆（主题感知的整合摘要）、长期记忆（离线 sleep-time 更新）三个互补阶段，在性能与效率间取得平衡。
related: [locomo-reflect-respond-architecture, memgpt-memory-hierarchy, memory-augmentation-overhead, sleep-time-memory-consolidation]
---

LightMem 是一种面向大语言模型的记忆增强生成系统，其核心设计思想来自人类认知心理学中的 Atkinson-Shiffrin 记忆模型，将记忆组织为三个互补阶段 [^src-1]：

**第一阶段：感觉记忆（Sensory Memory）** —— 受认知科学启发，通过轻量级压缩快速过滤无关信息，并按主题对信息进行分组 [^src-2]。这一阶段的目标是在信息进入系统时进行第一道高效筛选。

**第二阶段：主题感知短期记忆（Topic-Aware Short-Term Memory）** —— 在感觉记忆的主题分组基础上进行整合（consolidation），对内容进行组织和摘要，以提供更结构化的访问方式 [^src-3]。

**第三阶段：长期记忆（Long-Term Memory with Sleep-Time Update）** —— 采用离线过程（offline procedure），将记忆巩固与在线推理解耦 [^src-4]。该阶段的 sleep-time update 机制及其效率收益在单独的卡片中详述[^card-2]。

该三阶段架构的设计目标是在记忆系统的性能（QA 准确率）与效率（token 消耗和 API 调用次数）之间取得平衡。在 LongMemEval 和 LoCoMo 基准上，使用 GPT 和 Qwen 作为骨干模型，LightMem 在 QA 准确率上最高提升 7.7%/29.3%，同时将总 token 使用量最多降低 38x/20.9x，API 调用次数最多降低 30x/55.5x [^src-5]。

MemGPT 从操作系统的主内存/磁盘类比出发也提出了分层记忆架构，侧重 LLM 的自主内存管理能力而非效率优化[^card-1]。LoCoMo 的反思-回应架构则从生成式代理的认知模型出发，以会话边界驱动的递增摘要+观察提取实现双层记忆，与本卡的 Atkinson-Shiffrin 三阶段模型形成不同的认知隐喻路径[^card-3]。

## Footnotes

[^card-1]: [MemGPT 两级内存层次结构](memgpt-memory-hierarchy.md) -- MemGPT 的 OS 类比（主上下文=RAM vs 外部上下文=磁盘）与 LightMem 的认知模型形成互补的分层记忆设计路径
[^card-2]: [睡眠期离线记忆巩固机制](sleep-time-memory-consolidation.md) -- 本卡描述 LightMem 的完整三阶段架构，该卡聚焦第三阶段 sleep-time update 机制的效率收益（在线 token 减少 106x/117x）
[^card-3]: [LoCoMo 反思-回应双层记忆代理架构](locomo-reflect-respond-architecture.md) -- 两种认知隐喻驱动的多层记忆架构：本卡采用 Atkinson-Shiffrin 模型（感觉→短期→长期三阶段），该卡采用生成式代理的反思-回应（递增摘要+观察提取双层）

[^src-1]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- Abstract -- "Inspired by the Atkinson-Shiffrin model of human memory, LightMem organizes memory into three complementary stages."
[^src-2]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- Abstract -- "cognition-inspired sensory memory rapidly filters irrelevant information through lightweight compression and groups information according to their topics"
[^src-3]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- Abstract -- "topic-aware short-term memory consolidates these topic-based groups, organizing and summarizing content for more structured access"
[^src-4]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- Abstract -- "long-term memory with sleep-time update employs an offline procedure that decouples consolidation from online inference"
[^src-5]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- Abstract -- "LightMem consistently surpasses strong baselines, improving QA accuracy by up to 7.7% / 29.3%, reducing total token usage by up to 38x / 20.9x and API calls by up to 30x / 55.5x"
