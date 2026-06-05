---
schema: justification_journal.v1
card: ../cards/search-write-back.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-knowledge-compounding/source.pdf`
源证据：
- Section 6.3 P25 — "This is the mechanism that distinguishes Qing Claw from all other LLM Wiki implementations"
- Section 6.3 P25-26 — "the search results do not evaporate... the wiki is bidirectional and respiring"
- Appendix B P32 — "Search must be written back to wiki after supplementing it"
- Table 3 P22 — "Search write-back to wiki... supported only by Qing Claw"
范围论证：搜索回写是论文识别的三个复利微观机制中最关键的一个（作者称之为"compounding loop 的灵魂"），也是 Qing Claw 的独有能力。虽然与 ingest-operation 和 query-and-answer-filing 相关，但搜索回写的信息来源（外部搜索结果）和触发条件（wiki 不足时）均不同，值得独立成卡。
