---
schema: justification_journal.v1
card: ../cards/synthetic-judge-ppi-pipeline.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ares/text.txt`
源证据：
- Abstract -- "By creating its own synthetic training data, ARES finetunes lightweight LM judges to assess the quality of individual RAG components."
- Abstract -- "To mitigate potential prediction errors, ARES utilizes a small set of human-annotated datapoints for prediction-powered inference (PPI)."
- Abstract -- "using only a few hundred human annotations during evaluation"
范围论证：合成数据生成与 PPI 校准是同一流水线的两个阶段，分开建卡会导致两张卡都不完整（合成数据卡缺少校准，PPI 卡缺少训练前提）。合并为一张机制卡保持原子性：描述的是一条完整的"低成本评审训练"流水线。
