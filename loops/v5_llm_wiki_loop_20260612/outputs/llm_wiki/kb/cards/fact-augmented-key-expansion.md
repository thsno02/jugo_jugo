---
id: fact-augmented-key-expansion
title: 事实增强的 Key Expansion 提升检索与 QA
status: accepted
card_type: empirical-finding
tags:
- long-term-memory
- RAG
- document-expansion
- key-design
- indexing
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-longmemeval
evidence_basis: experimental_paper
justification: ../justification/fact-augmented-key-expansion.md
canonical_concept: fact-augmented-key-expansion
aliases:
- key expansion
- fact-augmented indexing
- document expansion
- 事实增强索引
- K=V+fact
summary: fact-augmented-key-expansion 在 LongMemEval_M 上，将提取的用户事实（user facts）拼接到原始 value 形成扩展 key（K=V+fact），采用 document expansion 技术，平均提升 recall@k 9.4% 和最终 QA 准确率 5.4%。单独使用压缩形式（摘要/事实/关键短语）作为 key 并不优于直接使用
  value 本身，据论文推测是因为 retriever 已能有效处理长文本语义。Key merging（索引阶段拼接）显著优于 rank merging（检索阶段合并排名），后者由于将索引大小扩大 m+1 倍而表现更差。
related:
- unified-memory-framework-three-stages
- value-decomposition-round-granularity
- longmemeval-error-distribution-analysis
- time-aware-query-expansion
---
在 LongMemEval_M 上探索 key 设计，论文发现：[^src-1]

1. 单独使用压缩形式（summary/fact/keyphrase）作为 key 并不优于直接使用 value 本身。据论文推测这是因为检索器已能有效处理长文本语义。

2. 采用 document expansion 技术——将压缩信息拼接到原始 value 形成 key（K = V + fact）——在所有模型上平均提升 recall@k 9.4% 和最终 QA 准确率 5.4%。[^src-2]

具体数值（Value=Round, K=V+fact, Stella V5 retriever）：
- Recall@5: 0.644 vs baseline 0.582
- Recall@10: 0.784 vs 0.692
- GPT-4o Top-10 QA: 0.720 vs 0.670

3. Key merging（索引阶段拼接）显著优于 rank merging（检索阶段合并不同路径的排名）。后者表现更差，据论文分析是因为 rank merging 将索引大小扩大 m+1 倍。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/5_experiment.tex" Section "Key: Multi-key indexing improves retrieval and RAG" -- "using these condensed forms alone does not enhance the memory recall performance"
[^src-2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/5_experiment.tex" -- "yielded an average improvement of 9.4% in recall@k and 5.4% in final accuracy across all models"
[^src-3]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/appendix.tex" Section "Post-retrieval rank merging" -- "rank merging has much lower performance than key merging"
