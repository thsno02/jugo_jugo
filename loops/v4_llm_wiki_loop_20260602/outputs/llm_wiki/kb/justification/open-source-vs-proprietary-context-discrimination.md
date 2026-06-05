---
schema: justification_journal.v1
card: ../cards/open-source-vs-proprietary-context-discrimination.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt`
源证据：
- sections/experiments.tex -- "Open-Source Models are Worse at Distinguishing Accurate Information from Noise"
- sections/experiments.tex -- "superior faithfulness scores of Llama3-70b are primarily due to its higher noise sensitivity"
- tables/ragchecker_results_avg.tex -- GPT-4 vs Llama3 vs Mixtral 的 CU/NS 数值对比
范围论证：该发现揭示了 faithfulness 指标的反直觉特性（高 faithfulness 可能来自盲目信任而非有效利用），对 RAG 系统选型和开源模型改进方向有指导意义。
