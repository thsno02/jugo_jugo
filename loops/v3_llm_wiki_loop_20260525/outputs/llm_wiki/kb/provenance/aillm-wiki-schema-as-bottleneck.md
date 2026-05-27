---
schema: accepted_card_provenance.v3
card: ../cards/aillm-wiki-schema-as-bottleneck.md
material_id: aillm-wiki-directory
digest_id: digest_aillm-wiki-directory
source_paths:
  - data/raw/webpage/aillm-wiki-directory/text.txt
draft_card: ../../drafts/cards/aillm-wiki-schema-as-bottleneck.md
draft_provenance: ../../drafts/provenance/aillm-wiki-schema-as-bottleneck.md
similarity_result: ../../drafts/similarity/aillm-wiki-schema-as-bottleneck.json
comparison_provenance: ../../drafts/comparison/aillm-wiki-schema-as-bottleneck.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:02:00+08:00
  gate_notes: 6/6 通过；"hardest part" 原句逐字引用 + L53–73 行号定位，操作含义与边界双段都有。
created_time: 2026-05-26T11:50:00+08:00
edited_time: 2026-05-27T14:02:00+08:00
edited_entity: llm
---

## 源证据

- 三步流程及"hardest part"原句（L53–73）。
- 五模板列表（L59–61, L83–86）。
- "raw → wiki" 词汇与目录结构（L65–67）。

## 卡片范围是否成立

- "挑 schema 才是真瓶颈"是 aillm.wiki 内容里少见的可操作工程判断，单独成卡比放在"四属性"卡里更醒目，对实际工程读者更有指导意义。
- 直接来自源材料：三步流程、"hardest part"原句、五模板列表。
- 引申主张已显式标注：从可压缩性 / 可重复性两个角度解释"为什么是瓶颈"——属于合理的工程外推，非站方原话。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:02:00+08:00
- 检查要点：
  - 不是标题复述：三步骤 + "hardest part" 原文 + 三层解释 + 三条操作含义。
  - 知识密度足够：定义 + 机制（schema 决定形状/可压缩/可重复）+ 操作信号 + 边界。
  - 源支撑齐全：每条主张都有 `aillm-wiki-directory/text.txt` 行号定位。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，operational_rule 类型与正文一致。
  - related 已链 v3 draft 卡（aillm-wiki-four-defining-properties、agents-md-as-schema-layer 等）。

## 备注

- 与 v2 `llm-knowledge-base-five-stage-workflow` 互补：那张谈 Karpathy 自己的五阶段，本卡谈社区站点对落地步骤的简化与瓶颈识别。
- 与 v2 `llm-wiki-schema-configuration-document` 是"同概念实体不同论点轴"——comparison 已论证 new_card 决策合理。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/aillm-wiki-schema-as-bottleneck.md`
- draft provenance: `../../drafts/provenance/aillm-wiki-schema-as-bottleneck.md`
- similarity: `../../drafts/similarity/aillm-wiki-schema-as-bottleneck.json`
- comparison provenance: `../../drafts/comparison/aillm-wiki-schema-as-bottleneck.md`
