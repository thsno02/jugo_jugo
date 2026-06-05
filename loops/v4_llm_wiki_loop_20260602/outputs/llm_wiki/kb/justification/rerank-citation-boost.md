---
schema: justification_journal.v1
card: ../cards/rerank-citation-boost.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`
源证据：
- sections/model.tex -- "We randomly sample n_sample=4 responses for each question, and select the best response using the automatic citation recall score."
- sections/results.tex -- "Rerank leads to consistent improvement in citation quality (on ASQA and ELI5)."
- tables/human_asqa_all.tex -- human evaluation confirmation
范围论证：Rerank 是 ALCE 中唯一能大幅提升引用质量的策略，且经人工验证有效。作为一种独立的后编辑机制，其原理（利用采样方差择优）可推广至其他生成场景。
