---
id: lightmem-compression-ratio-accuracy-interaction
title: LightMem 压缩率与 STM 阈值的交互效应
status: accepted
card_type: empirical-finding
tags:
- hyperparameter-interaction
- compression-ratio
- lost-in-the-middle
- parameter-tuning
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-lightmem
evidence_basis: experimental_paper
justification: ../justification/lightmem-compression-ratio-accuracy-interaction.md
canonical_concept: lightmem-compression-ratio-accuracy-interaction
aliases:
- r-th interaction
- 压缩率-阈值交互
- compression ratio impact
summary: LightMem 参数扫描表明压缩率 r 与 STM 阈值 th 对准确率存在交互效应：较小 th（0, 256 tokens）时最优 r 为 0.6；较大 th（512, 1024 tokens）时最优 r 提升至 0.7。论文推测更大 buffer 容量使 LLM 能有效利用更丰富的较少压缩信息，借助高级长上下文处理能力缓解 lost-in-the-middle 问题。效率方面，较低
  r 一致带来更高效率——因为相同 th 下触发 buffer 溢出的频率更低。GPT-4o-mini 最优配置为 r=0.7/th=512（ACC 68.64%）；Qwen3 最优配置为 r=0.6/th=768（ACC 73.20%）。
related:
- lightmem-stm-buffer-threshold
- lightmem-pre-compression-sensory-memory
---

论文对 LightMem 的两个核心超参数进行了系统性网格搜索，揭示了它们之间的非平凡交互：

**观察 1——th 与最优 r 的关系**：
- th in {0, 256}: 最优 r = 0.6（激进压缩 + 频繁摘要）
- th in {512, 1024}: 最优 r = 0.7（保守压缩 + 低频摘要）

**解释**：更大的 STM buffer 允许积累更多内容，LLM 在长上下文中能利用更丰富的信息；但前提是压缩不能过度削减有效信息。

**观察 2——效率单调性**：r 降低一致提升效率（更少 token → 更慢填满 buffer → 更少 API 调用），但准确率并非单调——存在信息保留与噪声过滤的平衡点。

**最佳配置**：
- GPT-4o-mini: r=0.7, th=512 → ACC 68.64%, Total 28.25k tokens, 18.43 calls
- Qwen3: r=0.6, th=768 → ACC 73.20%, Total 32.40k tokens, 9.97 calls [^src-1]

[^src-1]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- "Impact of r on Performance" P624-630 -- "For smaller thresholds (th in {0, 256}), an r of 0.6 achieves the highest ACC. In contrast, for larger thresholds (th in {512, 1024}), a higher retention rate of r=0.7 performs best. This suggests greater buffer capacity enables effective use of richer, less-compressed information"
