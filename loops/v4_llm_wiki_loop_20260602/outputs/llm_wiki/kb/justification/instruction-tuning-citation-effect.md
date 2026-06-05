---
schema: justification_journal.v1
card: ../cards/instruction-tuning-citation-effect.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`
源证据：
- sections/results.tex -- "instruction-tuned models outperform the original LLaMA models...considerably enhance the citation quality"
- sections/results.tex -- "the original LLaMA models are able to copy facts from the context, they struggle with accurately citing the sources"
- tables/inst.tex -- instruction detail comparison
范围论证：指令微调对引用能力的影响是 ALCE 论文中关于模型能力的关键发现之一。从 LLaMA 10.6% 到 Vicuna 51.1% 的跃升具有很强的实践指导意义。这一效应独立于检索和提示策略的发现，值得单独成卡。
