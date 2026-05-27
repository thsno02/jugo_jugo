---
schema: accepted_card_provenance.v3
card: ../cards/llm-wiki-karpathy-runtime-vs-agent-split.md
material_id: clawhub-llm-wiki-karpathy
digest_id: digest_clawhub-llm-wiki-karpathy
source_paths:
  - data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
draft_card: ../../drafts/cards/llm-wiki-karpathy-runtime-vs-agent-split.md
draft_provenance: ../../drafts/provenance/llm-wiki-karpathy-runtime-vs-agent-split.md
similarity_result: ../../drafts/similarity/llm-wiki-karpathy-runtime-vs-agent-split.json
comparison_provenance: ../../drafts/comparison/llm-wiki-karpathy-runtime-vs-agent-split.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:20:00+08:00
  gate_notes: 6/6 项通过；二段责任划分、握手点、out-of-scope 清单一一锚回 README 行号。
created_time: 2026-05-26T11:35:00+08:00
edited_time: 2026-05-27T10:20:00+08:00
edited_entity: llm
---

## 源证据

- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` L146-172："Runtime Philosophy" 一节明确列出 runtime 与 agent 各自拥有的能力。
- L77-95：多模态 ingest 模型解释 `kb_prepare_source_bundle` 的握手作用，"The runtime intentionally does not perform OCR or vision itself."
- L172-175：bridging 段，runtime/agent 在非文本资产上的握手细节。
- L176-189：out-of-scope 清单，确认本卡所写的边界。
- L66-69：`kb_repair_source_ids` 与 stable non-ASCII source ids 的存在确认 runtime 对 ID 的所有权。
- L70: `kb_get_raw_asset` deterministic metadata + safe absolute path —— 确定性 metadata 入口。

## 卡片范围是否成立

卡片范围是"runtime / agent 的责任分割 + 为什么这样切"。所有主张直接来自 README："Runtime Philosophy"、"Multimodal Ingest Model"、"Still Out of Scope"三节。

- 责任清单 → 一一对应原文 bullet。
- "为什么这样切"（可重复性 / 代价对齐 / 可审计）→ 这是合理引申：源文本明确说 runtime 是 deterministic、agent 做合成，所以三条理由都能在 README 文本结构里找到根据。
- 操作含义里 `kb_prepare_source_bundle`、`kb_repair_source_ids`、`kb_map_gaps`/`kb_promote_gap` 都是 README 文本里点名的工具。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:20:00+08:00
- 检查要点：
  - distinction 卡正面列出 runtime / agent 两段责任，非标题复述。
  - 知识密度合格：责任清单 + 设计原因 + 操作含义 + 边界。
  - source_ids 含 `clawhub-llm-wiki-karpathy`，正文锚回 L146-172 / L77-95 等。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 6 张相关卡。

## 备注

- v2 卡片若已有"llm-knowledge-base-five-stage-workflow"或类似总览卡，本卡只补"runtime/agent 责任划分"层，二者属于互补。
- comparison 已确认 v2 高频 token 误中（llm/wiki/的），不存在可合并对象，正确判 new_card。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/llm-wiki-karpathy-runtime-vs-agent-split.md`
- draft provenance: `../../drafts/provenance/llm-wiki-karpathy-runtime-vs-agent-split.md`
- similarity: `../../drafts/similarity/llm-wiki-karpathy-runtime-vs-agent-split.json`
- comparison provenance: `../../drafts/comparison/llm-wiki-karpathy-runtime-vs-agent-split.md`
