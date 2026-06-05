---
schema: justification_journal.v1
card: ../cards/rag-retrieval-generation-dual-condition.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt`
源证据：
- method.tex — "we need to achieve two conditions, namely retrieval condition and generation condition, for the malicious text P"
- method.tex — "the embedding vectors produced by a retriever for the malicious text P and the target question Q should be similar"
- method.tex — "the LLM should generate the target answer R when P alone is used as the context for the target question Q"
- evaluation.tex — "Existing baselines are not designed to simultaneously achieve retrieval and generation conditions, resulting in sub-optimal performance."
范围论证：此机制是论文的核心理论贡献，提供了分析 RAG 攻击有效性的通用框架。双条件模型解释了为什么现有攻击方法（prompt injection, corpus poisoning, GCG）在 RAG 场景下效果不佳，也指导了 PoisonedRAG 的设计。概念独立于具体实现策略（S⊕I 分解），属于独立原子知识。
