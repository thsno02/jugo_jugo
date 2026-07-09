---
id: more-context-enhances-faithfulness
title: 更多上下文增强生成器忠实度
status: draft
card_type: experimental-finding
tags: [top-k, chunk-size, faithfulness, claim-recall, rag-tuning, context-amount]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
evidence_basis: experimental_paper
justification: ../justification/more-context-enhances-faithfulness.md
canonical_concept: more-context-enhances-faithfulness
aliases: [More Context Enhances Faithfulness, 更多上下文增强忠实度]
summary: >-
  RAGChecker 诊断实验表明增加上下文量（通过增大 top-k 或 chunk size）可提升生成器 faithfulness。增大 k 从 5 到 20：claim recall 61.5→77.6，faithfulness 88.1→92.2，F1 51.7→53.4。增大 chunk size 从 150 到 300：claim recall 70.3→77.6，faithfulness 91.2→92.2。副作用是 noise sensitivity 略升（34.0→35.4）。但效果在高值时饱和（有用信息总量有限）。给定有限 context window，较大 chunk size 配合较小 k 优于反向组合。
related: [ragchecker-generator-metrics, retrieval-noise-sensitivity-tradeoff, chunk-overlap-minimal-effect]
---

RAGChecker 的诊断实验通过调整 top-k 选择数和 chunk size 两个维度验证了上下文量对生成器行为的影响。[^src-1]

**Top-k 实验**（k: 5 → 10 → 20）：[^src-2]
- Claim Recall: 61.5 → 70.3 → 77.6（更多 chunks 覆盖更多 ground truth claims）
- Context Precision: 下降（更多 chunks 引入更多不相关内容）
- Faithfulness: 88.1 → 90.8 → 92.2（更多上下文促使 generator 更忠实）
- Noise Sensitivity: 34.0 → 34.5 → 35.4（略升）
- F1: 51.7 → 52.6 → 53.4

**Chunk Size 实验**（150 → 300）：[^src-2]
- Context Precision 随 chunk size 增大而上升（与 k 相反）
- Claim Recall/Faithfulness/F1 的趋势与增大 k 类似

**设计建议**：[^src-3]
- 适度增加上下文量有利于 faithfulness 和 overall recall
- 高值时效果饱和（有用信息总量固定）
- 给定有限 context window，较大 chunk size + 较小 k 优于反向组合（尤其在较简单数据集如 Finance/Writing 上）
- 这在比较 chunk size 150 + k=20 vs chunk size 300 + k=10 时可明确看出

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/appendix_diagnosis.tex" -- "More Context Enhances Faithfulness. Top-k selection and chunk size both balance the amount of noise and useful information"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex Diagnosis" -- "faithfulness 88.1→92.2 with k 5→20, 91.2→92.2 with size 150→300...F1 51.7→53.4 with k 5→20"
[^src-3]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/appendix_diagnosis.tex" -- "Given a limited context length, a larger chunk size with a smaller k is preferred, especially for easier datasets"

[^card-10]: 参见 [retrieval-noise-sensitivity-tradeoff] 了解为何更多 context 同时带来噪声增加
