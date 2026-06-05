---
schema: justification_journal.v1
card: ../cards/ares-rag-evaluation-framework.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-ares/text.txt`
源证据：
- Title & Abstract -- "We introduce ARES, an Automated RAG Evaluation System, for evaluating RAG systems along the dimensions of context relevance, answer faithfulness, and answer relevance."
- Abstract -- "ARES accurately evaluates RAG systems while using only a few hundred human annotations during evaluation."
- Abstract -- "ARES judges remain effective across domain shifts"
范围论证：ARES 作为一个完整的 RAG 自动评估框架，包含合成数据生成、LM 评审微调、PPI 校准三个子机制，是一个独立的系统概念，值得单独建卡。与其子机制（tri-dimension、synthetic-judge-PPI）形成整体-部分关系。
