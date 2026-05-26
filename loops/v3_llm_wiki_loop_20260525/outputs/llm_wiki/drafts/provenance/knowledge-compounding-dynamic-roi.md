---
schema: draft_card_provenance.v3
draft_card: ../cards/knowledge-compounding-dynamic-roi.md
material_id: arxiv-knowledge-compounding
digest_id: digest_arxiv-knowledge-compounding
source_paths:
  - data/raw/arxiv/arxiv-knowledge-compounding/text.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/arxiv/arxiv-knowledge-compounding/text.txt:37` —— "Our central theoretical claim is that the cost term in the original Agentic ROI equation contains an unexamined assumption -- that the cost of each task is mutually independent. This assumption holds under the traditional retrieval-augmented generation (RAG) paradigm but breaks down once a persistent, structured knowledge layer is introduced."
2. `data/raw/arxiv/arxiv-knowledge-compounding/text.txt:37` —— "We propose a dynamic Agentic ROI model in which cost is treated as a time-varying function Cost(t) governed by a knowledge-base coverage rate H(t)."
3. `data/raw/arxiv/arxiv-knowledge-compounding/text.txt:37` —— "Empirical results from four sequential queries on the same domain yield a cumulative token consumption of 47K under the compounding regime versus 305K under a matched RAG baseline -- a savings of 84.6%."
4. `data/raw/arxiv/arxiv-knowledge-compounding/text.txt:37` —— "Calibrated 30-day projections indicate cumulative savings of 53.7% under medium topic concentration and 81.3% under high concentration, with the gap widening monotonically over time."

## 卡片范围是否成立

- 卡片范围聚焦在 "ROI 成本项从常量变为 Cost(t)" 这一单一主张，正是论文核心定理贡献，与源材料直接对应。
- 47K vs 305K、84.6%、53.7% / 81.3% 等数字直接来自摘要原文。
- "高分散长尾导致 H(t)≈0" 是基于覆盖率定义的合理引申，论文未直接给出但与定义自洽；本卡在"边界 / 误用条件"中已明确标注为外推。
- "只读不写的 wiki 不会复利" 是基于论文第 (ii)(iii) 机制的引申（auto-feedback、write-back），论文支持但未明确单独列出。

## 发表门控结果

本轮未运行。

## 备注

- 与 v2 卡片 `auto-index-replaces-rag-at-small-scale` 可能存在主题重叠：v2 卡讲的是"小规模下 auto-index 替代 RAG"，本卡讲的是"复利模型让 Cost 单调下降"，两者一个偏定性结论一个偏定量机制，可在 comparison_provenance 阶段决定是否合并或互链。
