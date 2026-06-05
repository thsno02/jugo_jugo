---
schema: justification_journal.v1
card: ../cards/inventory-evidence-separation.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt`
源证据：
- L154-156 — "Parts, source queues, corpora, watch items, and next actions live under inventory/ so they can be listed and revisited without becoming evidence."
- L316-317 — "Inventory (inventory/) is for durable operational state... It is intentionally not evidence for factual claims."
- L158-160 — "datasets/ stores manifests, samples, profiles, and query recipes for large data. The wiki indexes data without copying it into the source corpus."
范围论证：操作状态与事实证据的分离是一个独立的设计区分（distinction），不同于三层架构中的 raw/wiki/schema 分层。它定义了 wiki 内部的一条语义边界——哪些内容可以作为论据引用、哪些不能。
