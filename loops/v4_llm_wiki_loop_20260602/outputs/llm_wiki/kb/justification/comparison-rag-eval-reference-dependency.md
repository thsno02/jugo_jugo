# Justification: comparison-rag-eval-reference-dependency

## Why this card exists

三大 RAG 评估框架（RAGAS、ARES、RAGChecker）在对 ground truth 的依赖程度上形成了一条清晰的设计光谱。这一取舍不是表面的工程选择，而是反映了一个底层逻辑约束：completeness（完整性/recall）度量在语义上预设了参照物的存在。将这一区分提炼为独立卡片，有助于开发者在选择评估框架时理解不同方法论的能力边界。

## Source evidence

- RAGAS 论文明确声明"reference-free (not tied to having ground truth available)"（arxiv-ragas, Abstract & Comments）
- ARES 论文："ARES utilizes a small set of human-annotated datapoints for prediction-powered inference (PPI)"（arxiv-ares, Abstract）
- RAGChecker 论文的 claim recall 定义依赖 ground truth answer claims（arxiv-ragchecker, Retriever Metrics）
- RAGChecker 元评估结果：completeness Pearson 60.67 vs RAGAS 53.16（arxiv-ragchecker, human_eval_selected.tex）

## Relationship to existing cards

本卡是 ragas-reference-free-rag-evaluation、ares-rag-evaluation-framework、ragchecker-three-tier-metrics 三卡之间张力的显式化。三卡各自描述了一个框架的设计，本卡提炼了贯穿三者的核心设计取舍维度。
