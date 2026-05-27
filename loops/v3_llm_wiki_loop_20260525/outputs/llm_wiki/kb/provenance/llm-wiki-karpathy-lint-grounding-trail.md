---
schema: accepted_card_provenance.v3
card: ../cards/llm-wiki-karpathy-lint-grounding-trail.md
material_id: clawhub-llm-wiki-karpathy
digest_id: digest_clawhub-llm-wiki-karpathy
source_paths:
  - data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
draft_card: ../../drafts/cards/llm-wiki-karpathy-lint-grounding-trail.md
draft_provenance: ../../drafts/provenance/llm-wiki-karpathy-lint-grounding-trail.md
similarity_result: ../../drafts/similarity/llm-wiki-karpathy-lint-grounding-trail.json
comparison_provenance: ../../drafts/comparison/llm-wiki-karpathy-lint-grounding-trail.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:14:00+08:00
  gate_notes: 6/6 项通过；8 个 lint 检查项均锚到 README 行号，边界与 lint/agent 责任分工显式标注。
created_time: 2026-05-26T11:40:00+08:00
edited_time: 2026-05-27T10:14:00+08:00
edited_entity: llm
---

## 源证据

- L73：lint 检查项官方完整清单。
- L172-175：lint 对 multimodal "review trail" 的强制要求。
- L67-68：`kb_map_gaps` / `kb_promote_gap` 是 lint 与 agent 之间的接口。
- L66-67：`kb_repair_source_ids` 对旧 vault 升级的修复角色。

## 卡片范围是否成立

卡片范围是 "kb_lint 都查哪些项 + 这些项意味着什么"。每个 lint 项直接来自 README L73 的一行。

- 把"unsupported claims"对应到 Karpathy 个人 vault 健康检查的引申，是基于源材料 L172-175 "before the wiki starts depending on them" 的同义解读。
- "lint 不修复、agent 修复" 是合理引申：lint 在 README 中只描述检测能力，没有写自动修复，且 README 在多处强调 agent 拥有合成 / 决策。
- 边界（lint 不做语义判断、依赖 manifest v2、contradiction 不消解）→ 直接来自 README 文本的限定。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:14:00+08:00
- 检查要点：
  - 8 个 lint 项一一列出且各有解读，非标题复述。
  - 知识密度合格：lint 项 + 操作含义 + 边界三层结构。
  - source_ids 含 `clawhub-llm-wiki-karpathy`，正文锚到 L73 / L172-175 / L67-68。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 6 张相关卡。

## 备注

- 与 runtime-vs-agent 卡有轻度重叠（都涉及 lint 与责任划分）。本卡聚焦"lint 项列表 + 操作约束"，划分清晰。
- 与 v2 `llm-wiki-health-checks` 存在"想法 → 实现"血缘，但 v2 scope 明确禁止外推到具体产品，所以本卡走 new_card 而非 provenance_delta。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/llm-wiki-karpathy-lint-grounding-trail.md`
- draft provenance: `../../drafts/provenance/llm-wiki-karpathy-lint-grounding-trail.md`
- similarity: `../../drafts/similarity/llm-wiki-karpathy-lint-grounding-trail.json`
- comparison provenance: `../../drafts/comparison/llm-wiki-karpathy-lint-grounding-trail.md`
