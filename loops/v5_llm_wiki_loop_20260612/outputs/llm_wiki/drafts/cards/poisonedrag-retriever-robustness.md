---
id: poisonedrag-retriever-robustness
title: PoisonedRAG 跨检索器鲁棒性
status: draft
card_type: experimental-finding
tags: [poisonedrag, retriever, contriever, ance, robustness]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-retriever-robustness.md
canonical_concept: poisonedrag-retriever-robustness
aliases: [retriever robustness, cross-retriever attack, 跨检索器攻击鲁棒性]
summary: >-
  PoisonedRAG 对不同检索器(Contriever, Contriever-ms, ANCE)和不同相似度度量(dot product, cosine)均保持高 ASR。黑盒设定下 ASR 在 0.83-1.0 之间, 因为恶意文本(P=Q⊕I)在语义上与目标问题相似, 该语义相似性对检索器类型和相似度函数选择不敏感。白盒设定下 ASR 达 0.87-1.0。
related: [poisonedrag-black-box-attack, poisonedrag-white-box-attack]
---

论文在三种检索器和两种相似度度量上评估了 PoisonedRAG 的鲁棒性:

**检索器消融** (NQ 数据集):
| Retriever | BB ASR | WB ASR | BB F1 | WB F1 |
|-----------|--------|--------|-------|-------|
| Contriever | 0.97 | 0.97 | 0.96 | 1.0 |
| Contriever-ms | 0.96 | 0.97 | 0.98 | 1.0 |
| ANCE | 0.95 | 0.98 | 0.96 | 0.97 |
[^src-1]

**相似度度量消融**:
- Dot product (默认) vs Cosine: ASR 差异极小
- NQ BB: 0.97 vs 0.99; WB: 0.97 vs 0.97 [^src-2]

**黑盒有效性原因**: P=Q⊕I 在语义上与 Q 高度相关，无论使用何种 encoder/metric，Q 与自身的语义相似性都能保证高检索概率。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / Impact of retriever" -- Table tab:impact-of-retrievers
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / Impact of similarity metric" -- Table tab:impact-of-similarity
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / Impact of retriever" -- "NameTag is effective in the black-box setting because the crafted malicious texts are semantically similar to the target questions"
[^card-1]: [poisonedrag-black-box-attack]
