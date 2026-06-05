---
id: longmemeval-context-compression
title: LongMemEval 上下文压缩与准确率提升
status: accepted
card_type: source_claim
tags: [benchmark, LongMemEval, context_compression, agent_memory, Zep, latency]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
justification: ../justification/longmemeval-context-compression.md
canonical_concept: longmemeval-context-compression
aliases: [LongMemEval上下文压缩, LongMemEval accuracy improvement, 115k-to-1.6k token compression]
summary: >-
  longmemeval-context-compression（LongMemEval上下文压缩, 115k-to-1.6k compression）Zep 在 LongMemEval 基准上将平均上下文从 115k 压缩至 1.6k tokens，同时提升准确率最高 18.5%、降低延迟 90%，但在 single-session-assistant 类问题上表现下降
related:
  - dmr-benchmark-inadequacy
  - search-rerank-construct-pipeline
---

在 LongMemEval_s 基准测试（平均约 115,000 tokens 的对话上下文）上，Zep 展示了显著的上下文压缩效果和性能提升 [^src-1]：

**整体结果**：使用 gpt-4o-mini 时准确率提升 15.2%（55.4% -> 63.8%），使用 gpt-4o 时提升 18.5%（60.2% -> 71.2%）。平均上下文 token 数从 115k 压缩至仅 1.6k，延迟从约 30 秒降至约 3 秒（降低约 90%）[^src-2]。

**按问题类型分析**：Zep 在复杂问题类型上提升最为显著 [^src-3]：
- single-session-preference：gpt-4o 提升 184%（20.0% -> 56.7%）
- temporal-reasoning：gpt-4o 提升 38.4%（45.1% -> 62.4%）
- multi-session：gpt-4o 提升 30.7%（44.3% -> 57.9%）

**弱点**：single-session-assistant 类问题上 Zep 表现下降（gpt-4o 下降 17.7%，gpt-4o-mini 下降 9.06%），论文承认需要进一步的研究和工程工作 [^src-4]。

论文指出更强的模型与 Zep 配合效果更好，gpt-4o 在 knowledge-update 类别上也获得提升，而 gpt-4o-mini 在该类别上未能改善，"可能需要额外开发以改进较弱模型对 Zep 时间数据的理解"[^src-5]。LightMem 论文从另一个角度量化了记忆系统开销问题的严重程度——此前的基线系统在 token 消耗上存在一到两个数量级的冗余[^card-1]。

## Footnotes

[^card-1]: [LLM 记忆系统的开销问题](memory-augmentation-overhead.md) -- Zep 展示了压缩后的性能提升（115k 至 1.6k token），LightMem 从反面量化了开销问题的严重程度（基线系统 token 冗余高达 38x），两者共同论证了记忆效率优化的必要性

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 4.3 (LongMemEval) -- "The LongMemEval_s dataset presents significant challenges... with conversations averaging approximately 115,000 tokens in length."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Table 2 (LongMemEval_s) -- "Full-context gpt-4o-mini 55.4% 31.3s 115k; Zep gpt-4o-mini 63.8% 3.20s 1.6k; Full-context gpt-4o 60.2% 28.9s 115k; Zep gpt-4o 71.2% 2.58s 1.6k"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Table 3 (LongMemEval_s Question Type Breakdown) -- "single-session-preference gpt-4o 20.0% -> 56.7% 184% up; temporal-reasoning gpt-4o 45.1% -> 62.4% 38.4% up"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 4.3.2 -- "The decrease in performance for single-session-assistant questions—17.7% for gpt-4o and 9.06% for gpt-4o-mini—represents a notable exception... and suggest further research and engineering work is needed."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 4.3.2 -- "additional development may be needed to improve less capable models' understanding of Zep's temporal data."
