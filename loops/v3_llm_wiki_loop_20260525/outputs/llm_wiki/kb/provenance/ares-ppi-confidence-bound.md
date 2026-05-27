---
schema: accepted_card_provenance.v3
card: ../cards/ares-ppi-confidence-bound.md
material_id: arxiv-ares
digest_id: digest_arxiv-ares
source_paths:
  - data/raw/arxiv/arxiv-ares/agent_source_bundle.txt
draft_card: ../../drafts/cards/ares-ppi-confidence-bound.md
draft_provenance: ../../drafts/provenance/ares-ppi-confidence-bound.md
similarity_result: ../../drafts/similarity/ares-ppi-confidence-bound.json
comparison_provenance: ../../drafts/comparison/ares-ppi-confidence-bound.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:24:00+08:00
  gate_notes: 6/6 通过；PPI 三段折中 + rectifier function + 校准集大小消融 + 真实 RAG 置信宽度全部锁到原文行号；跨域 PPI 失败边界齐全。
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-27T14:24:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:24:00+08:00
- 检查要点：
  - 不是标题复述：PPI 三段折中 + 四条操作含义 + 两条边界。
  - 知识密度足够：机制（rectifier function）+ 数字（25→0.44, 300→0.89; 7.4 / 6.1 pp）+ 反例（跨域 PPI 失效）。
  - 源支撑齐全：每条主张锁到 `agent_source_bundle.txt` 行号。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，mechanism 类型与正文一致。
  - related 已链 ARES 系列、wicer。

## 备注

- PPI 这一概念在 v2 卡片里目前未见专门覆盖。
- comparison 显示 v2 候选无主题重叠，new_card 决策合理。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/ares-ppi-confidence-bound.md`
- draft provenance: `../../drafts/provenance/ares-ppi-confidence-bound.md`
- similarity: `../../drafts/similarity/ares-ppi-confidence-bound.json`
- comparison provenance: `../../drafts/comparison/ares-ppi-confidence-bound.md`
