---
id: comparison-storage-vs-retrieval-compression
title: 存储压缩与检索压缩的独立性
status: accepted
card_type: distinction
tags: [token-economics, memory-compression, storage-efficiency, retrieval-efficiency, Zep, Mem0]
created_time: 2026-06-05T18:00:00+08:00
edited_time: 2026-06-05T18:00:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0, arxiv-zep]
justification: ../justification/comparison-storage-vs-retrieval-compression.md
canonical_concept: storage-vs-retrieval-compression
aliases: [存储压缩vs检索压缩, storage vs retrieval token efficiency, 内部表征膨胀与检索精度]
summary: >-
  comparison-storage-vs-retrieval-compression（存储压缩vs检索压缩）揭示记忆系统的 token 效率
  存在两个独立维度：存储效率（内部表征占用多少 token）与检索效率（查询时注入 prompt 多少 token），
  两者可反向相关。Zep 是典型案例——存储侧 600K+ token（Mem0 论文），检索侧仅 1.6K token（Zep 论文）
related: [longmemeval-context-compression, memory-compression-token-ratio]
  - memory-compression-token-ratio
  - longmemeval-context-compression
---

记忆系统的 token 效率不是一个单一维度，而是至少包含两个可独立变化的维度：**存储效率**（内部表征占用多少 token）与**检索效率**（查询时注入 prompt 多少 token）。

**Zep 案例揭示了这一区分的实践意义**：

- **存储侧（Mem0 论文视角）**：Zep 的记忆图谱消耗超过 600K token 来存储对话记忆，而原始对话仅 26K token——图谱膨胀了约 23 倍。原因是 Zep 在每个节点缓存完整摘要且在边上存储事实，导致大量冗余[^card-1]。
- **检索侧（Zep 论文视角）**：Zep 在 LongMemEval 基准上将 115K token 的对话上下文压缩至仅 1.6K token 注入 prompt，同时提升准确率最高 18.5%、降低延迟 90%[^card-2]。

**这意味着同一系统在两个维度上可以呈现相反的表现**：存储侧极度膨胀（600K vs 原始 26K），检索侧高效压缩（115K -> 1.6K）。直觉上这并不矛盾——冗余的内部表征正是支持精确检索的基础设施，类似于数据库索引占用额外存储以加速查询。

**设计启示**：评估记忆系统的 token 效率时，必须分别衡量两个维度。仅看存储成本（如 Mem0 论文的批评）会低估系统的检索价值；仅看检索压缩比（如 Zep 论文的宣称）会隐藏系统的运营成本。完整的经济分析需要将存储 token 视为基础设施投资，将检索 token 视为每次查询的边际成本。

## Footnotes

[^card-1]: [记忆压缩的 token 效率差异](memory-compression-token-ratio.md) -- 本卡的存储侧数据来源，该卡详述 Mem0 论文对 Zep 存储膨胀（600K+ token）的批评
[^card-2]: [LongMemEval 上下文压缩与准确率提升](longmemeval-context-compression.md) -- 本卡的检索侧数据来源，该卡详述 Zep 论文在 LongMemEval 基准上的 115K->1.6K 压缩结果
