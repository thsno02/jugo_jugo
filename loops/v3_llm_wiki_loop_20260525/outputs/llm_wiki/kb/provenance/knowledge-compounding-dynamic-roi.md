---
schema: accepted_card_provenance.v3
card: ../cards/knowledge-compounding-dynamic-roi.md
material_id: arxiv-knowledge-compounding
digest_id: digest_arxiv-knowledge-compounding
source_paths:
  - data/raw/arxiv/arxiv-knowledge-compounding/text.txt
draft_card: ../../drafts/cards/knowledge-compounding-dynamic-roi.md
draft_provenance: ../../drafts/provenance/knowledge-compounding-dynamic-roi.md
similarity_result: ../../drafts/similarity/knowledge-compounding-dynamic-roi.json
comparison_provenance: ../../drafts/comparison/knowledge-compounding-dynamic-roi.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:22:00+08:00
  gate_notes: 6/6 项通过：Cost(t)/H(t) 模型 + 47K vs 305K 实证 + 30 天校准节省 + 边界。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:22:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:22:00+08:00
- 检查要点：
  - 非标题复述：以核心主张 + 机制含义 + 实证锚点 + 边界四段实质展开。
  - 知识密度：Cost(t)/H(t) 模型 + 47K/305K/84.6% / 53.7% / 81.3% 全部具体数字。
  - 源支撑：arxiv-knowledge-compounding text:37 多锚点。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 5 个 v3 draft id。

## 备注

- 与 v2 卡片 `auto-index-replaces-rag-at-small-scale` 可能存在主题重叠：v2 卡讲的是"小规模下 auto-index 替代 RAG"，本卡讲的是"复利模型让 Cost 单调下降"，一定性一定量，可在 audit 阶段交叉链接。
- Adoption 阶段观察：comparison 三个 v2 候选仅靠「的」字撞分，无实质主题共享。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/knowledge-compounding-dynamic-roi.md`
- draft provenance: `../../drafts/provenance/knowledge-compounding-dynamic-roi.md`
- similarity: `../../drafts/similarity/knowledge-compounding-dynamic-roi.json`
- comparison provenance: `../../drafts/comparison/knowledge-compounding-dynamic-roi.md`
