---
schema: justification_journal.v1
card: ../cards/graphrag-self-reflection-gleaning.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt`
源证据：
- Appendix A.2 (appendix.tex) — "GPT-4 extracted almost twice as many entity references when the chunk size was 600 tokens than when it was 2400"
- Appendix A.2 — "using a logit bias of 100 to force a yes/no decision...MANY entities were missed"
- self_reflection_figure.tex — 数据坐标 (0, 9348)→(3, 27240) for 600 chunk size
范围论证：自我反思/拾遗是 GraphRAG 实体提取阶段的关键工程技术，具体操作步骤和量化效果构成独立原子知识。与 chunk-size-tradeoff 卡相关但不重叠——本卡聚焦解决方案而非问题本身。
