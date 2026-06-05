---
schema: justification_journal.v1
card: ../cards/context-utilization-noise-faithfulness-trilemma.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt`
源证据：
- sections/experiments.tex, Diagnosis -- "the trilemma of context utilization, noise sensitivity, and faithfulness"
- sections/appendix_diagnosis.tex -- 优化提示的具体效果数据和分析
- tables/ablation_prompt.tex -- 基础 vs 优化提示的完整指标对比
范围论证：三难困境是 RAGChecker 实验的独特发现，揭示了 prompt tuning 在 RAG 生成器调优中的根本局限性。该概念对 RAG 系统设计有直接指导意义，独立于 RAGChecker 框架本身。
