---
schema: justification_journal.v1
card: ../cards/closed-book-citation-paradox.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`
源证据：
- sections/results.tex -- "ClosedBook+PostCite delivers strong correctness but poor citation quality."
- sections/results.tex -- "(1) open-book models are easily distracted by irrelevant passages...a phenomenon also observed by Shi et al.; (2) ClosedBook often generates texts that are correct but not similar to any retrieved passages"
- tables/eli5.tex, tables/asqa.tex -- specific numeric comparisons
范围论证：ClosedBook+PostCite 的悖论现象是 ALCE 论文中最有洞察力的发现之一，揭示了正确性和引用质量之间的非线性关系，对 RAG 系统设计有重要启示。独立于其他实验发现，值得单独成卡。
