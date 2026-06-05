---
id: memory-compression-token-ratio
title: 记忆压缩的 token 效率差异
status: accepted
card_type: source_claim
tags: [token_efficiency, memory_compression, storage_overhead, Mem0, Zep, benchmark]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
justification: ../justification/memory-compression-token-ratio.md
canonical_concept: memory-compression-token-ratio
aliases: [记忆 token 压缩比, memory token efficiency, 记忆存储效率]
summary: >-
  memory-compression-token-ratio（记忆 token 压缩比 / memory token efficiency）Mem0 实验显示不同记忆架构的 token 效率差异悬殊：Mem0 平均 7K token/对话，Mem0^g 14K，原始对话 26K，而 Zep 图谱膨胀至 600K+，原因是 Zep 在每个节点缓存完整摘要且边上存储事实导致大量冗余
related: [memory-extraction-update-pipeline, graph-memory-temporal-advantage]
---

Mem0 论文测量了各系统物化长期记忆存储所需的平均 token 预算，揭示了记忆架构设计对存储效率的巨大影响 [^src-1]：

| 系统 | 平均 token/对话 |
|------|----------------|
| Mem0 | ~7K |
| Mem0^g | ~14K |
| 原始对话（全上下文） | ~26K |
| Zep | >600K |

Mem0 以自然语言表示编码完整对话轮次，仅占约 7K token。Mem0^g 引入图记忆（节点和关系）后大约翻倍至 14K token [^src-2]。

Zep 的记忆图谱消耗超过 600K token，膨胀的原因是其设计选择：在每个节点缓存完整的抽象摘要，同时在连接边上存储事实，导致"图中大量冗余"。相比之下，将整个原始对话提供给语言模型——不做任何记忆抽象——平均仅约 26K token，比 Zep 的图谱少 20 倍 [^src-3]。

除 token 低效外，Zep 还存在显著的操作瓶颈：添加记忆后立即检索往往无法正确回答查询，在等待数小时后重新运行相同搜索才能获得明显更好的结果。这种延迟表明 Zep 的图构建涉及多个异步 LLM 调用和大量后台处理。相比之下，Mem0 的图构建即使在最坏情况下也能在一分钟内完成 [^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/result.tex -- "We measure the average token budget required to materialise each system's long-term memory store."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/result.tex -- "Mem0 encodes complete dialogue turns in a natural language representation and therefore occupies only 7k tokens per conversation on an average. Where as Mem0^g roughly doubles the footprint to 14k tokens"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/result.tex -- "Zep's memory graph consumes in excess of 600k tokens. The inflation arises from Zep's design choice to cache a full abstractive summary at every node while also storing facts on the connecting edges, leading to extensive redundancy across the graph."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/result.tex -- "re-running identical searches after a delay of several hours yielded considerably better results...In contrast, Mem0 graph construction completes in under a minute even in worst-case scenarios"
