---
schema: draft_card_provenance.v3
draft_card: ../cards/retrieval-not-enough-for-stale-kb.md
material_id: falconer-enterprise-guide
digest_id: digest_falconer-enterprise-guide
source_paths:
  - data/raw/webpage/falconer-enterprise-guide/text.txt
created_time: 2026-05-26T11:53:00+08:00
edited_time: 2026-05-26T11:53:00+08:00
edited_entity: llm
---

## 源证据

- L124-130："Why retrieval tools don't solve this" 整段。
- L148：FAQ 重申"Without that loop, smarter search over bad context just produces wrong answers faster."
- L74 + L150：Anthropic "context as the scarcest resource for AI agents" 两次引用。

## 卡片范围是否成立

卡片范围是 distinction：把"查询层（retrieval）"与"维护循环（LLM Wiki loop）"切清。核心论断和数据都直接来自源材料：

- "Better retrieval over bad context" 一句是原文逐字引用。
- "PKM 圈子很早就识别了这一点" → 同义改写 L130 "the Obsidian power user who builds a serious vault values the same thing: a system where the notes stay true"。
- 操作含义部分是合理引申：把原文的论断翻译成两个评估问题与一个落地顺序。

边界（"不是说 retrieval 没用" / "retrieval 在没维护时更危险" / "维护成本必然存在，只是换主体"）是源文本的限定性立场，与 stay-current 卡共享语境但聚焦点不同。

## 发表门控结果

本轮未运行。

## 备注

- 与 drift-detection-loop 卡关系：本卡讲"为什么仅靠 retrieval 不够"，drift-detection 卡讲"维护循环具体如何运作"。两者互补、不重复。
- 与 v2 卡片 "auto-index-replaces-rag-at-small-scale" 在主题上有相邻性（都涉及"RAG 不是万能"），但本卡视角是企业规模、底层 freshness，与小规模索引规则角度不同。comparison_provenance 阶段需在内容层区分。
