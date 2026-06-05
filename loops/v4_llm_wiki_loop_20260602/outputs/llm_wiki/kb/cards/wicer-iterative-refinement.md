---
id: wicer-iterative-refinement
title: WiCER 迭代精炼算法
status: accepted
card_type: mechanism
tags: [llm-wiki, wicer, cegar, iterative-refinement, compilation, fact-recovery]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
justification: ../justification/wicer-iterative-refinement.md
canonical_concept: wicer-iterative-refinement
aliases: [WiCER, Wiki-memory Compile Evaluate Refine, WiCER算法, 迭代编译精炼]
summary: >-
  wicer-iterative-refinement（WiCER / Wiki-memory Compile Evaluate Refine / 迭代编译精炼）是一种受
  CEGAR 启发的迭代算法，通过诊断探针评估编译后 wiki、识别丢失事实并在后续编译中强制保留，1-2 次迭代可
  恢复 80% 的丢失质量，灾难性失败减少 55%
related: [compilation-gap, targeted-diagnosis-vs-generic-pinning, compile-time-vs-query-time]
---

**WiCER（Wiki-memory Compile, Evaluate, Refine）** 是一种迭代式知识编译算法，用于弥合 LLM Wiki 系统中的编译缺口[^src-1]。其设计灵感来自形式验证领域的 **CEGAR（counterexample-guided abstraction refinement，反例引导抽象精炼）** 方法[^src-2]。

WiCER 的工作机制分为三个阶段的迭代循环：

1. **Compile（编译）**：LLM 将原始文档蒸馏为 wiki 格式
2. **Evaluate（评估）**：用诊断探针（diagnostic probes）评估编译后的 wiki，识别被丢弃的事实
3. **Refine（精炼）**：将识别出的丢失事实强制注入后续编译轮次，确保其被保留[^src-3]

实验结果表明，仅需 **1 到 2 次迭代**即可恢复 80% 的丢失质量：在 15 个有基线对照的主题上，WiCER 编译后的平均质量为 3.24，而原始全上下文推理为 3.47（满分 5）[^src-4]。灾难性失败率相对减少了 55%[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-wicer/text.txt` -- Abstract -- "we propose WiCER (Wiki-memory Compile, Evaluate, Refine), an iterative algorithm inspired by counterexample-guided abstraction refinement (CEGAR) that closes this gap"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-wicer/text.txt` -- Abstract -- "inspired by counterexample-guided abstraction refinement (CEGAR)"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-wicer/text.txt` -- Abstract -- "WiCER evaluates compiled wikis against diagnostic probes, identifies dropped facts, and forces their preservation in subsequent compilations"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-wicer/text.txt` -- Abstract -- "One to two iterations recover 80% of lost quality (mean 3.24 vs. 3.47 for raw full-context across the 15 topics with baselines)"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-wicer/text.txt` -- Abstract -- "reducing catastrophic failures by 55% relative"
