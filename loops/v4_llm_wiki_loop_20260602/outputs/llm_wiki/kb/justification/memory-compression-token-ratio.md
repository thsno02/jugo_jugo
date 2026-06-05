---
schema: justification_journal.v1
card: ../cards/memory-compression-token-ratio.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt`
源证据：
- sections/result.tex — "Mem0 encodes complete dialogue turns in a natural language representation and therefore occupies only 7k tokens...Zep's memory graph consumes in excess of 600k tokens"
- sections/result.tex — "The inflation arises from Zep's design choice to cache a full abstractive summary at every node"
范围论证：token 效率差异（7K vs 600K）揭示了记忆架构设计的根本性影响。该卡片聚焦于量化对比和冗余膨胀的因果解释，是理解记忆系统实际部署成本的关键参考点。
