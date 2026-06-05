---
schema: justification_journal.v1
card: ../cards/retrieval-improvement-faithfulness-noise-tradeoff.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt`
源证据：
- sections/experiments.tex, Main Results -- "As E5-Mistral achieves better claim recall, we observe generators paired to it achieves better faithfulness"
- sections/experiments.tex, Diagnosis -- "faithfulness 88.1->92.2 with k 5->20... noise sensitivity 34.0->35.4"
- tables/ragchecker_results_avg.tex -- BM25 vs E5-Mistral 的 faithfulness 和 NS 对比数据
范围论证：该权衡区别于 LoCoMo 的 retrieval-snr-tradeoff（top-k 直接降低 F1）。RAGChecker 的发现更细粒度：更好的检索同时改善 faithfulness 和增加 noise sensitivity，整体 F1 仍正向，但揭示了生成器在利用上下文时的能力边界。
