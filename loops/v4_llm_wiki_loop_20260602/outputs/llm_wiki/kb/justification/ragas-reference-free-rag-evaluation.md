---
schema: justification_journal.v1
card: ../cards/ragas-reference-free-rag-evaluation.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragas/text.txt`
源证据：
- Abstract L37 — "We introduce Ragas (Retrieval Augmented Generation Assessment), a framework for reference-free evaluation of Retrieval Augmented Generation (RAG) pipelines."
- Abstract L37 — "a suite of metrics which can be used to evaluate these different dimensions without having to rely on ground truth human annotations"
- Comments L39 — "Reference-free (not tied to having ground truth available) evaluation framework for retrieval augmented generation"
- Abstract L37 — "such a framework can crucially contribute to faster evaluation cycles of RAG architectures, which is especially important given the fast adoption of LLMs"
范围论证：本卡聚焦于 RAGAS 框架的核心定义特征——无参考评估（reference-free evaluation）及其对评估迭代速度的实际影响。这是 RAGAS 的第一性概念，独立于具体的评估维度分解（后者由 rag-evaluation-tri-dimension 覆盖）。源材料为 arXiv 摘要页，信息密度有限但足以支撑框架级概念卡。
