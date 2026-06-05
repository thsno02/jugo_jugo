---
schema: justification_journal.v1
card: ../cards/rag-evaluation-tri-dimension.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-ragas/text.txt`
源证据：
- Abstract L37 — "Evaluating RAG architectures is, however, challenging because there are several dimensions to consider"
- Abstract L37 — "the ability of the retrieval system to identify relevant and focused context passages"
- Abstract L37 — "the ability of the LLM to exploit such passages in a faithful way"
- Abstract L37 — "the quality of the generation itself"
范围论证：本卡聚焦于 RAGAS 论文提出的 RAG 评估三维度分解：检索质量、忠实性、生成质量。这是一个独立的概念区分（distinction），与 RAGAS 框架本身的无参考评估特征（ragas-reference-free-rag-evaluation）正交。三维分解与 ALCE 的 citation-quality-tri-dimension 形成互补视角：ALCE 从输出侧评估（流畅度/正确性/引用质量），RAGAS 从管道组件侧评估（检索/忠实性/生成）。源材料虽仅为摘要，但三维度的定义表述明确，足以支撑本卡。
