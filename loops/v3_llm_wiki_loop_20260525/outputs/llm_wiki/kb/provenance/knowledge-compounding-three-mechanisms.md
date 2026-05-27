---
schema: accepted_card_provenance.v3
card: ../cards/knowledge-compounding-three-mechanisms.md
material_id: arxiv-knowledge-compounding
digest_id: digest_arxiv-knowledge-compounding
source_paths:
  - data/raw/arxiv/arxiv-knowledge-compounding/text.txt
draft_card: ../../drafts/cards/knowledge-compounding-three-mechanisms.md
draft_provenance: ../../drafts/provenance/knowledge-compounding-three-mechanisms.md
similarity_result: ../../drafts/similarity/knowledge-compounding-three-mechanisms.json
comparison_provenance: ../../drafts/comparison/knowledge-compounding-three-mechanisms.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:23:00+08:00
  gate_notes: 6/6 项通过：三机制定义与分工 + 操作含义 + 边界，论文原文 text:37 verbatim 引用。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:23:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:23:00+08:00
- 检查要点：
  - 非标题复述：以三机制定义 + 为什么是三个 + 操作含义 + 边界四段实质展开。
  - 知识密度：三机制各自的写入对象、可消融性、与 Karpathy gist 的对应关系。
  - 源支撑：text:37 verbatim + 200 行 C# 参考实现声明。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 6 个 v3 draft id。

## 备注

- 机制 (ii)（高价值答案回灌）与 v2 卡片 `file-outputs-back-as-compounding-loop` 主题强相关，audit 可联动检查。
- Adoption 阶段观察：`ingest` 在 v2 与 draft 中是同名异指（v2 是示例操作 vs draft 是经济学摊销机制），不可 fusion。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/knowledge-compounding-three-mechanisms.md`
- draft provenance: `../../drafts/provenance/knowledge-compounding-three-mechanisms.md`
- similarity: `../../drafts/similarity/knowledge-compounding-three-mechanisms.json`
- comparison provenance: `../../drafts/comparison/knowledge-compounding-three-mechanisms.md`
