---
schema: accepted_card_provenance.v3
card: ../cards/llm-wiki-karpathy-multimodal-representation-path.md
material_id: clawhub-llm-wiki-karpathy
digest_id: digest_clawhub-llm-wiki-karpathy
source_paths:
  - data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
draft_card: ../../drafts/cards/llm-wiki-karpathy-multimodal-representation-path.md
draft_provenance: ../../drafts/provenance/llm-wiki-karpathy-multimodal-representation-path.md
similarity_result: ../../drafts/similarity/llm-wiki-karpathy-multimodal-representation-path.json
comparison_provenance: ../../drafts/comparison/llm-wiki-karpathy-multimodal-representation-path.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:18:00+08:00
  gate_notes: 6/6 项通过；两条 ingest 路径、5 步 representation-first 流程、manifest v2 字段与边界齐备。
created_time: 2026-05-26T11:38:00+08:00
edited_time: 2026-05-27T10:18:00+08:00
edited_entity: llm
---

## 源证据

- L77-95 "Multimodal Ingest Model"：两条 ingest 路径的官方描述。
- L46-73 "What 0.4.4 Implements"：manifest v2 字段、compile_readiness 三态、lint 检查项的清单。
- L62：representation 命令在 `.llm-kb/representations/` 下。
- L99-103："CLI Commands"段实际给出了 `kb_get_raw_asset`、`kb_prepare_source_bundle`、`kb_prepare_representation`、`kb_upsert_representation`、`kb_read_representations` 在命令行的使用。
- L181-187 "Still Out of Scope"：再次确认 "built-in OCR, vision, or PDF parsing inside the runtime itself" 不属于本包。

## 卡片范围是否成立

卡片范围是 "non-text 资产的 representation-first 路径机制"，每一步骤都能在 README 的两节里找到对应命令。

- 五步流程 → README 同节按"inspect → bundle → store → ready → upsert"顺序描述。
- compile_readiness 三态 → 直接引用 L67-68。
- 边界（stale / 没有视频音频 / runtime 不重生成）→ 直接来自 lint 警告项与支持 raw kinds 清单。

未做的引申：

- 没有为这条路径具体列出哪些 OCR / vision 工具——README 自己也未列。
- 没有给出 representation 文件的内部 schema 细节，因为 README 未公开。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:18:00+08:00
- 检查要点：
  - 两条路径与 5 步 representation-first 流程清晰展开，非标题复述。
  - 知识密度合格：机制 + 设计意图 + 边界。
  - source_ids 含 `clawhub-llm-wiki-karpathy`，正文锚回 L77-95 / L46-73 等。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 5 张相关卡。

## 备注

- 与 runtime-vs-agent 分割卡有少量交叉（都涉及 `kb_prepare_source_bundle`），但本卡聚焦"非文本资产的具体步骤序"，与 runtime-vs-agent 卡的"职责划分"角度互补。
- adoption 阶段确认与 v2 `llm-wiki-ingest-example-flow` 抽象层级不同，不构成 provenance_delta。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/llm-wiki-karpathy-multimodal-representation-path.md`
- draft provenance: `../../drafts/provenance/llm-wiki-karpathy-multimodal-representation-path.md`
- similarity: `../../drafts/similarity/llm-wiki-karpathy-multimodal-representation-path.json`
- comparison provenance: `../../drafts/comparison/llm-wiki-karpathy-multimodal-representation-path.md`
