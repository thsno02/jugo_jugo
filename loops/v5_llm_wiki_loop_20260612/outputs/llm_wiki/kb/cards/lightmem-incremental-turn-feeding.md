---
id: lightmem-incremental-turn-feeding
title: LightMem 增量逐轮输入实验设定
status: accepted
card_type: experimental-design
tags:
- incremental-feeding
- turn-level
- realistic-evaluation
- streaming-dialogue
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-lightmem
evidence_basis: experimental_paper
justification: ../justification/lightmem-incremental-turn-feeding.md
canonical_concept: lightmem-incremental-turn-feeding
aliases:
- Incremental Dialogue Turn Feeding
- 增量逐轮输入
- turn-level processing
summary: LightMem 实验采用"增量逐轮输入"设定：完整对话历史按 turn 级别逐条输入并处理，模拟真实场景中用户-模型交互逐轮形成的过程。这区别于一次性提供全部对话历史的静态评估设定，更贴近实际部署中记忆系统需增量处理流式输入的需求。该设定下 LightMem 的感知记忆 buffer 和 STM buffer 的阈值机制自然运作。
related:
- lightmem-three-stage-architecture
- lightmem-stm-buffer-threshold
---

论文在实验设定中明确采用"Incremental Dialogue Turn Feeding"——对话历史在 turn 级别逐条输入并实时处理，而非一次性提供完整历史。

**设计动机**：反映实际场景中用户-模型交互逐轮增量形成的特征。记忆系统需要在每个新 turn 到达时决定如何处理（压缩、缓存、触发摘要等），而非拥有全局视角后再处理。

**对 LightMem 的意义**：该设定下 LightMem 的各级 buffer 机制（sensory buffer 512 tokens → topic segmentation trigger; STM buffer → summarization trigger）自然运作，体现了设计与评估的一致性。

**与基线的公平性**：所有对比方法均在同一设定下评估，确保效率指标（runtime, API calls）的可比性。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- "experimental setup" P557-558 -- "Our experiments adopt a realistic Incremental Dialogue Turn Feeding setting, where the entire dialogue history is fed and processed at the turn level, one turn at a time"
