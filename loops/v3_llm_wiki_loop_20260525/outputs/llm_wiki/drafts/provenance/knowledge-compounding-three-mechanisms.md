---
schema: draft_card_provenance.v3
draft_card: ../cards/knowledge-compounding-three-mechanisms.md
material_id: arxiv-knowledge-compounding
digest_id: digest_arxiv-knowledge-compounding
source_paths:
  - data/raw/arxiv/arxiv-knowledge-compounding/text.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/arxiv/arxiv-knowledge-compounding/text.txt:37` —— "We further identify three microeconomic mechanisms underlying the compounding effect: (i) one-time INGEST amortized over N retrievals, (ii) auto-feedback of high-value answers into synthesis pages, and (iii) write-back of external search results into entity pages."
2. `data/raw/arxiv/arxiv-knowledge-compounding/text.txt:37` —— "The engineering contribution is a minimal reproducible implementation in approximately 200 lines of C#, which we believe is the first complete industrial-grade reference implementation of Karpathy's (2026) LLM Wiki paradigm."

## 卡片范围是否成立

- "三机制"是论文明确列出的分类，卡片范围与源完全对齐。
- 卡片中 "(i)+(ii) 等价于 Karpathy 原始 gist 形态" 与 "(iii) 是工程扩展" 这一区分是引申结论，论文没有显式表态；引申基于 Karpathy 原始 gist 只描述 ingest+synthesis、未强调 external-search write-back 这一事实。
- "wiki 可寻址性失效则复利失效" 是基于检索机制的合理边界条件，论文未直接陈述但属合理引申，已标注。

## 发表门控结果

本轮未运行。

## 备注

- 机制 (ii)（高价值答案回灌）与 v2 卡片 `file-outputs-back-as-compounding-loop` 主题强相关，可在 comparison_provenance 阶段联动检查是否需要互相 cite。
