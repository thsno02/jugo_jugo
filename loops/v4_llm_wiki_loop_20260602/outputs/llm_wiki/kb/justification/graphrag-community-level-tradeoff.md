---
schema: justification_journal.v1
card: ../cards/graphrag-community-level-tradeoff.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt`
源证据：
- community_table.tex — C0 vs C3 的 units/tokens/% max 对比数据
- Results Section (graph_rag.tex) — "root-level GraphRAG offers a highly efficient method...retaining advantages in comprehensiveness (72% win rate) and diversity (62% win rate)"
- Conclusion — "summaries of root-level communities...provide a data index that is both superior to vector RAG and achieves competitive performance to other global methods at a fraction of the token cost"
范围论证：C0-C3 层级间的 token 效率与质量权衡是 GraphRAG 实际部署时的关键决策点，论文提供了详细的量化数据支持，构成独立的原子知识。
