---
schema: justification_journal.v1
card: ../cards/chunk-size-tradeoff.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/kunal-local-knowledge-base/text.txt`
源证据：
- L72 — "Chunk size matters more than most tutorials admit — too small and you lose context, too large and your retrieval gets noisy."
- L125-126 — "Naive fixed-size chunking throws away document structure. Semantic chunking, hierarchical indexing, and hybrid search (combining vector similarity with BM25 keyword matching) need to become standard."
范围论证：分块大小权衡是 RAG 管线的核心机制性问题，虽然是已知概念，但此博文以实践者视角给出了具体参数范围（256-512 token）和"比教程承认的更重要"的判断，且将三种改进方向明确列举。既有 KB 中无分块/chunking 相关卡片。
