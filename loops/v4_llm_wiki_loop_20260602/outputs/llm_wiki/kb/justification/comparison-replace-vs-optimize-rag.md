---
schema: justification_journal.v1
card: ../cards/comparison-replace-vs-optimize-rag.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：governance cross-link 判断（full-context-vs-chunked-retrieval 聚类）
来源：综合四张独立来源卡片的论点
源证据：
- full-context-anti-rag -- Karpathy 哲学立场：拒绝 RAG 分块检索
- kv-cache-vs-rag-tradeoff -- WiCER 实证：全上下文 KV cache 在策展知识上优于 RAG（4.38 vs 4.08）
- memory-vs-rag-salience -- Mem0 实验：结构化记忆（Judge 67-68%）一致优于 RAG（最高 61%）
- chunk-size-tradeoff -- RAG 内部优化路径：分块粒度权衡与语义分块/混合搜索改进方向
范围论证：该区分卡捕获了面对 RAG 局限性时的根本架构分歧——替代 vs 优化。现有卡片各自阐述了其中一个立场或实证，但无卡片将这两条路径对立比较并揭示分歧根源（对分块缺陷的归因差异）和选择条件（知识规模与动态性假设）。该区分在实践中具有直接决策价值
