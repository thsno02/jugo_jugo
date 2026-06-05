---
schema: justification_journal.v1
card: ../cards/wicer-iterative-refinement.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-wicer/text.txt`
源证据：
- Abstract — "we propose WiCER (Wiki-memory Compile, Evaluate, Refine), an iterative algorithm inspired by counterexample-guided abstraction refinement (CEGAR) that closes this gap"
- Abstract — "WiCER evaluates compiled wikis against diagnostic probes, identifies dropped facts, and forces their preservation in subsequent compilations"
- Abstract — "One to two iterations recover 80% of lost quality (mean 3.24 vs. 3.47 for raw full-context across the 15 topics with baselines), reducing catastrophic failures by 55% relative"
范围论证：WiCER 是论文的核心贡献——一种具有明确三阶段结构的迭代算法，具备独立的机制描述和量化效果指标，适合作为独立的 mechanism 卡。与 compilation-gap（问题定义）和 targeted-diagnosis-vs-generic-pinning（消融发现）形成互补。
