---
schema: justification_journal.v1
card: ../cards/rag-poisoning-defense-insufficiency.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt`
源证据：
- defense.tex — "PoisonedRAG could still achieve high ASRs and F1-Score, which means paraphrasing defense cannot effectively defend"
- defense.tex — "the perplexity values of malicious texts are not statistically higher than those of clean texts"
- defense.tex — "the ASR is the same, which means duplicate text filtering cannot successfully filter malicious texts"
- defense.tex — "this defense still cannot completely defend against our PoisonedRAG even if k=50"
- conclusion.tex — "we evaluate several defenses and find that they are insufficient to mitigate the proposed attacks"
范围论证：防御不充分性是论文的重要实验结论，汇集了四种防御策略的评估结果。作为 source_claim 类型卡片，忠实记录论文的实验发现。与攻击机制卡片独立，聚焦于"如何防御"维度。
