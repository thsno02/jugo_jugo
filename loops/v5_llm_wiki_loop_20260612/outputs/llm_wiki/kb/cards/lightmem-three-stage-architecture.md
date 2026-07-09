---
id: lightmem-three-stage-architecture
title: LightMem 三阶段记忆架构
status: accepted
card_type: system-architecture
tags:
- memory-system
- llm-agent
- atkinson-shiffrin
- lightweight
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-lightmem
evidence_basis: experimental_paper
justification: ../justification/lightmem-three-stage-architecture.md
canonical_concept: lightmem-three-stage-architecture
aliases:
- LightMem
- LightMem architecture
- 三阶段记忆框架
- memory-augmented generation
summary: LightMem 受 Atkinson-Shiffrin 人类记忆模型启发，将 LLM agent 外部记忆组织为三阶段：Light1 认知感知记忆（pre-compression + topic segmentation）、Light2 主题感知短期记忆（STM buffer + LLM summarization）、Light3 睡眠时更新的长期记忆（soft update +
  offline parallel update）。该架构在 LongMemEval 和 LoCoMo 上以 GPT-4o-mini / Qwen3 为骨干模型，相比 A-MEM 等基线提升 QA 准确率最高 7.67%，同时减少 token 消耗最高 117 倍、API 调用最高 310 倍。
related:
- unified-memory-framework-three-stages
- lightmem-attention-topic-segmentation
- lightmem-complexity-reduction-analysis
- lightmem-incremental-turn-feeding
- lightmem-online-offline-cost-decoupling
- lightmem-pre-compression-sensory-memory
- lightmem-sleep-time-offline-update
- lightmem-stm-buffer-threshold
- memory-bank-construction-pipeline
- memory-system-three-limitations
---
LightMem 是一种轻量高效的记忆增强生成框架，其核心设计受 Atkinson-Shiffrin 人类记忆多阶段模型启发。架构包含三个互补阶段：

1. **Light1（感知记忆）**：通过预压缩子模块过滤冗余 token，再通过基于注意力的主题分割子模块将压缩后的信息按语义主题分组。
2. **Light2（短期记忆）**：维护一个 STM buffer，当累积 token 达到阈值时触发 LLM summarization，生成结构化记忆条目。
3. **Light3（长期记忆）**：测试时仅执行软更新（直接插入），将昂贵的记忆整合解耦到离线阶段并行执行。

该框架在性能与效率之间取得平衡，是首个系统性将人类记忆层级映射到 LLM agent 外部记忆并同时优化效率的工作。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- "Introduction" P735-745 -- "Inspired by the efficiency and structure of human memory, we introduce LightMem... (1) A pre-compression sensory memory module... (2) A topic-aware short-term memory... (3) A sleep-time update mechanism"
