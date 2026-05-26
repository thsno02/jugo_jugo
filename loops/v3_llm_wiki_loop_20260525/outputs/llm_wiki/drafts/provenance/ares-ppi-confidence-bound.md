---
schema: draft_card_provenance.v3
draft_card: ../cards/ares-ppi-confidence-bound.md
material_id: arxiv-ares
digest_id: digest_arxiv-ares
source_paths:
  - data/raw/arxiv/arxiv-ares/agent_source_bundle.txt
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-26T11:10:00+08:00
edited_entity: llm
---

## 源证据

- `methods.tex` L748-758：纯判官预测 vs 纯人工标注 vs PPI 折中的三段讨论。
- `methods.tex` L753：PPI 的定义引用 Angelopoulos 2023。
- `methods.tex` L756-757：rectifier function 的作用——"learn a rectifier function for constructing a confidence set of the ML model's performance"。
- `methods.tex` L763：排名用置信区间中点。
- `Tables/ppi_comparison_table.tex` L189-197：从 25 到 400 校准集大小的 Kendall's τ 消融。
- `results.tex` L874-876：实测置信区间宽度 7.4 / 6.1，命中率 >95%。
- `results.tex` 跨域段（约 L901-904）：跨语言 / 跨模态 PPI 也救不回来。

## 卡片范围是否成立

卡片把 PPI 单独切出来，强调"它是 ARES 数据效率的核心机制"。范围划分理由：

1. 判官 + 合成数据已经独立成卡（`ares-synthetic-data-pipeline`）；PPI 是评估排序阶段的独立步骤。
2. 卡内的所有数字（150–300、7.4 / 6.1、Kendall's τ 阈值）都来自源材料表与正文，未做外部引申。
3. "PPI 校准失败的边界"使用源材料 `results.tex` 跨域章节的实际数字。

## 发表门控结果

本轮未运行。

## 备注

- PPI 这一概念在 v2 卡片里目前未见专门覆盖。若 v2 有"RAG 评估"通用卡，需要在 comparison_provenance 阶段标明 PPI 是独立、可复用的统计技巧。
