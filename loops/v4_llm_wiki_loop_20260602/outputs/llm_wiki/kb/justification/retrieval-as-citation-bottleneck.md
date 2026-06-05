---
schema: justification_journal.v1
card: ../cards/retrieval-as-citation-bottleneck.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`
源证据：
- sections/results.tex -- "The retrieval results play a crucial role to the correctness and the citation quality."
- sections/results.tex -- "both models' correctness lags behind the corresponding retrieval recall"
- sections/results.tex -- "more passages in context do not yield substantial improvement for ChatGPT"
- tables/asqa_different_llms.tex -- ChatGPT-16K 5/10/20-psg comparison showing no improvement
范围论证：检索瓶颈是 ALCE 识别出的三大挑战方向之首，涉及检索上界、oracle 差距、检索器选择和上下文段落数效果等多层次分析。作为独立的系统设计洞察适合单独成卡。
