---
schema: justification_journal.v1
card: ../cards/scenario-based-tool-selection.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/robin-cartier-llm-knowledge-bases/text.txt`
源证据：
- L49-57 — "When to use it vs alternatives [src-002]: Personal second brain, research, learning → LLM wiki (this pattern); Operational automation, trend tracking, pipeline-fed knowledge → structured knowledge bases (relational); Enterprise scale, millions of documents → Retrieval-Augmented Generation (RAG) (or hybrid)"
- L45 — "Temporal signal is weak: a single 'last updated' field loses the trend-tracking capability a relational store would give you (first_seen / last_seen)."
范围论证：该三段式框架与现有 use-case-domains（wiki 内部应用领域）和 llm-wiki-scale-boundary（wiki 规模上限）互补。其独特贡献是引入关系型知识库作为中间选项，将讨论从 wiki-vs-RAG 二元对立扩展为三元选择。temporal signal weakness 作为关系型中间选项存在的理由被整合进该卡，无需独立成卡。
