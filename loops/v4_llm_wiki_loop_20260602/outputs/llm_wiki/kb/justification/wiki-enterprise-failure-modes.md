---
schema: justification_journal.v1
card: ../cards/wiki-enterprise-failure-modes.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt`
源证据：
- L436-437 — "Three core limitations constrain the approach at enterprise scale... the limitations are not bugs, they are consequences of the design assumptions."
- L281 — "The 50,000-100,000 token threshold is where the wiki approach stops working reliably"
- L357 — "multiple simultaneous agents updating a markdown wiki create race conditions, write conflicts, and potential for data corruption"
- L359 — "the LLM wiki breaks down immediately: index overflow, no access control layer, and write conflicts"
范围论证：现有 KB 的 index-based-navigation 卡提到 ~100 资料可运作、超出后可用 qmd，但未讨论企业级的失效分析。本卡提取 Atlan 文章中明确的三大企业失效模式（索引溢出、无 RBAC、并发冲突），以及 50K-100K token 的定量阈值和"规模是整个框架"的论断。三个失效模式作为一个包提取，因为原文将其作为统一分析对待。
