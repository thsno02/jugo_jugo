---
id: lightmem-stm-buffer-threshold
title: LightMem STM 缓冲区阈值权衡机制
status: accepted
card_type: mechanism
tags:
- short-term-memory
- buffer-threshold
- efficiency-accuracy-tradeoff
- api-call-reduction
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-lightmem
evidence_basis: experimental_paper
justification: ../justification/lightmem-stm-buffer-threshold.md
canonical_concept: lightmem-stm-buffer-threshold
aliases:
- STM buffer threshold
- STM 阈值
- topic-aware short-term memory
- Light2
- th parameter
summary: LightMem Light2 维护 STM buffer，当累积 token 数达到阈值 th 时触发 LLM summarization 生成记忆条目。存储结构为 {topic, {sum_i, user_i, model_i}}。th 增大一致性地提升效率（减少 API 调用），但对准确率影响非单调——最优 th 取决于模型和压缩率 r。较小 th（0, 256）时 r=0.6
  最优；较大 th（512, 1024）时 r=0.7 最优，据论文推测这是因为更大 buffer 容量使 LLM 能利用更丰富的较少压缩信息，借助长上下文处理能力缓解 lost-in-the-middle 问题。
related:
- lightmem-three-stage-architecture
- lightmem-pre-compression-sensory-memory
- lightmem-complexity-reduction-analysis
- lightmem-compression-ratio-accuracy-interaction
- lightmem-incremental-turn-feeding
- lightmem-sleep-time-offline-update
---
LightMem 的 Light2 模块实现主题感知短期记忆，核心参数为 STM buffer 容量阈值 th（以 token 数计量）。

**工作流程**：主题分割后的各 segment 进入 STM buffer。当 buffer 中 token 总量达到 th 时，调用 LLM f_sum 对 buffer 内所有 {topic, message turns} 结构生成摘要。最终存入 LTM 的记忆条目为 {topic, embedding(sum_i), user_i, model_i}。

**效率-准确率权衡**：
- th 增大 → API 调用频率降低 → 效率一致提升
- 但准确率呈非单调变化：过大的 buffer 可能导致主题混杂影响摘要质量，过小的 buffer 无法充分利用 LLM 长上下文能力

**与单 turn / 多 session 直接输入的对比**：相比逐 turn 调用（高延迟）或直接多 session 拼接（主题混杂导致记忆条目不准确），基于 topic 约束的输入粒度在最小化 API 调用和维持摘要准确性之间达到最佳平衡。[^src-1] [^src-2]

[^src-1]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- "Light2: Topic-aware short-term memory" P830-849 -- "When the token count in the buffer reaches a preset threshold, we invoke LLM f_sum to generate concise summaries"
[^src-2]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- "Analysis of the STM Threshold's Impact" P643-650 -- "as th increases, there is a marked improvement in efficiency... the effect on QA accuracy is non-monotonic"
