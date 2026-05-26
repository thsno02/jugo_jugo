---
schema: draft_card_provenance.v3
draft_card: ../cards/llm-wiki-karpathy-lint-grounding-trail.md
material_id: clawhub-llm-wiki-karpathy
digest_id: digest_clawhub-llm-wiki-karpathy
source_paths:
  - data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
created_time: 2026-05-26T11:40:00+08:00
edited_time: 2026-05-26T11:40:00+08:00
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

本轮未运行。

## 备注

- 与 runtime-vs-agent 卡有轻度重叠（都涉及 lint 与责任划分）。本卡聚焦"lint 项列表 + 操作约束"，划分清晰。
