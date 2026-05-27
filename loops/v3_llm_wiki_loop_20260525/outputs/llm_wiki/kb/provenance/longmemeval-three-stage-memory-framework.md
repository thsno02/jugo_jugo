---
schema: accepted_card_provenance.v3
card: ../cards/longmemeval-three-stage-memory-framework.md
material_id: arxiv-longmemeval
digest_id: digest_arxiv-longmemeval
source_paths:
  - data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt
draft_card: ../../drafts/cards/longmemeval-three-stage-memory-framework.md
draft_provenance: ../../drafts/provenance/longmemeval-three-stage-memory-framework.md
similarity_result: ../../drafts/similarity/longmemeval-three-stage-memory-framework.json
comparison_provenance: ../../drafts/comparison/longmemeval-three-stage-memory-framework.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T11:32:00+08:00
  gate_notes: 6/6 项通过；三阶段四 CP 定义 + 九系统映射表 + reading 的 10 分增益 + 边界齐备。
created_time: 2026-05-26T14:25:00+08:00
edited_time: 2026-05-27T11:32:00+08:00
edited_entity: llm
---

## 源证据

- 第 1418-1456 行（§4 unified view + §4.2 CP1-CP4 完整定义）。
- 第 1428 行："we formulate three stages for a memory-augmented assistant: (1) \textit{indexing}, converting each history session $(t_i, S_i)$ into one or more key-value items, (2) \textit{retrieval}, formulating a retrieval query and collecting $k$ most relevant items, and (3) \textit{reading} ..."
- 第 1141-1153 行：表 `tab:memory-system-dimensions-comp`，九系统与"Our Design"对四个 CP 的填法。
- 第 1521 行："even with perfect retrieval, a suboptimal reading strategy results in up to a 10-point absolute performance drop compared to the best approach for GPT-4o."
- 第 1345 行（related work）：明确把"long-context 直读"与"context compression with online indexing"区分开。

## 卡片范围是否成立

- 三阶段四 CP、九系统映射、"reading 也很关键"都直接来自原文，无引申。
- "online context compression vs 其他路线"边界说明对应原文 §2 末尾的明确表态。
- "Value/Key/Query/Reading 是离散选项"是对实验设计的归纳，未跨论文综合。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T11:32:00+08:00
- 检查要点：
  - concept 卡给出三阶段四 CP 完整表 + 九系统映射 + 设计动机 + 边界，非标题复述。
  - 知识密度合格。
  - source_ids 含 `arxiv-longmemeval`，正文锚到第 1418-1456 / 1141-1153 / 1521 行。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 6 张相关卡。

## 备注

- 与 v2 卡片 `auto-index-replaces-rag-at-small-scale` 概念域不同：v2 关注"小规模时索引能替代 RAG"，本卡关注"任何规模 RAG 系统的三阶段抽象"——可作互补。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/longmemeval-three-stage-memory-framework.md`
- draft provenance: `../../drafts/provenance/longmemeval-three-stage-memory-framework.md`
- similarity: `../../drafts/similarity/longmemeval-three-stage-memory-framework.json`
- comparison provenance: `../../drafts/comparison/longmemeval-three-stage-memory-framework.md`
