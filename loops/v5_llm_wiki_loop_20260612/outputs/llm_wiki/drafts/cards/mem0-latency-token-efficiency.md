---
id: mem0-latency-token-efficiency
title: Mem0 延迟与 Token 效率分析
status: draft
card_type: empirical-finding
tags: [latency, token-efficiency, p95, deployment, cost-reduction]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
evidence_basis: experimental_paper
justification: ../justification/mem0-latency-token-efficiency.md
canonical_concept: mem0-latency-efficiency
aliases: [Mem0 latency, Mem0 token efficiency, 延迟分析, p95 latency reduction]
summary: >-
  Mem0 搜索延迟最低 p50=0.148s p95=0.200s，总延迟 p50=0.708s p95=1.440s，相比 full-context p95=17.117s 降低 91%。Mem0 每对话平均仅 7k tokens 记忆占用，Mem0^g 约 14k tokens，而 Zep 超 600k tokens（是原始对话 26k 的 20 倍以上）。Mem0^g 总延迟 p50=1.091s p95=2.590s 同时达到最高 overall Judge=68.44%。LangMem 搜索延迟极高 p95=59.82s 不适合交互应用。
related: []
---

Mem0 在延迟和 token 效率方面的实验数据：[^src-1]

**搜索延迟**：Mem0 达到所有方法中最低——p50=0.148s, p95=0.200s。归因于选择性记忆检索机制动态识别并检索最显著信息。Mem0^g 搜索延迟 p50=0.476s, p95=0.657s 仍优于所有现有记忆方案。

**总延迟**：Mem0 p50=0.708s, p95=1.440s；Mem0^g p50=1.091s, p95=2.590s。对比 full-context 的 p50=9.870s, p95=17.117s，Mem0 实现 92% 降低，Mem0^g 实现 85% 降低。[^src-2]

**Token 占用**：Mem0 每对话平均仅 7k tokens，Mem0^g 约 14k tokens（因引入图记忆的节点和关系）。相比之下，Zep 消耗超 600k tokens——其设计在每个节点缓存完整抽象摘要同时在边上存储事实，导致大量冗余。原始对话全文约 26k tokens，是 Zep 图的 20 倍以下。[^src-3]

**实用启示**：尽管 full-context 方法达到最高 Judge=72.90%，但延迟和 token 成本使其在生产规模部署中不可行。Mem0^g 在达到 Judge=68.44%（仅次于 full-context）的同时，延迟成本仅为其零头。随对话长度增长，full-context 计算开销指数增长，而记忆方法保持稳定性能。[^src-4]

[^card-1]: [[mem0-performance-results]] 提供了对应的质量指标
[^card-2]: [[mem0-memory-architecture-overview]] 描述了实现低延迟的架构设计

[^src-1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1259-1260 -- Table: Mem0 search p50=0.148 p95=0.200, total p50=0.708 p95=1.440
[^src-2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1299 -- "Mem0 and Mem0^g significantly reduce token usage and thus achieve lower p95 latencies of around 1.44 seconds (a 92% reduction) and 2.6 seconds (a 85% reduction)"
[^src-3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1315 -- "Mem0 encodes complete dialogue turns in a natural language representation and therefore occupies only 7k tokens... Mem0^g roughly doubles the footprint to 14k tokens... Zep's memory graph consumes in excess of 600k tokens"
[^src-4]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1297 -- "a full-context method that ingests a chunk of roughly 26,000 tokens still achieves the highest Judge score (approximately 73%). However... it also incurs a very high total p95 latency"
