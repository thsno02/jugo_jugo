---
schema: justification_journal.v1
card: ../cards/gap-mapping-promotion.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`
源证据：
- "What 0.4.4 Implements" — "deterministic gap mapping and promotion through kb_map_gaps and kb_promote_gap"
- "Runtime Philosophy" — "kb_map_gaps and kb_promote_gap still cover durable knowledge growth on top of that ingest layer."
- "CLI Commands" — "llm-wiki-karpathy kb_map_gaps --vault-root /vault --limit 10"
- "CLI Commands" — "llm-wiki-karpathy kb_promote_gap --vault-root /vault --note-id synthesis-retrieval-vs-memory"
范围论证：本卡描述缺口映射与晋升这一对确定性操作作为 wiki 内部驱动的知识增长机制。它与 lint-operation（检测健康问题）和 ingest-operation（外部资料驱动的增长）互补但不重叠：lint 识别不一致性，ingest 处理新资料进入，gap mapping/promotion 专门处理已有知识图谱中系统性的覆盖空白并将其转化为一等笔记。
