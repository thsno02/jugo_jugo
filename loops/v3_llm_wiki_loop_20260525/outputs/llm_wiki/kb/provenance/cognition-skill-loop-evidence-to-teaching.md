---
schema: accepted_card_provenance.v3
card: ../cards/cognition-skill-loop-evidence-to-teaching.md
material_id: cognitionus-llm-wiki-guide
digest_id: digest_cognitionus-llm-wiki-guide
source_paths:
  - data/raw/webpage/cognitionus-llm-wiki-guide/text.txt
draft_card: ../../drafts/cards/cognition-skill-loop-evidence-to-teaching.md
draft_provenance: ../../drafts/provenance/cognition-skill-loop-evidence-to-teaching.md
similarity_result: ../../drafts/similarity/cognition-skill-loop-evidence-to-teaching.json
comparison_provenance: ../../drafts/comparison/cognition-skill-loop-evidence-to-teaching.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:38:00+08:00
  gate_notes: 6/6 通过；四步闭环 + 四对位机制 + Alice/Bob 场景 + 三承诺全部锁到 cognitionus 行号；边界标注产品宣传材料未公开实现细节。
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-27T14:38:00+08:00
edited_entity: llm
---

## 源证据

- 第 47–48 行："The product is the loop, not the dashboard."
- 第 49–107 行：4 步闭环 verbatim 小标题（SKILL LOOKUP / EVIDENCE LOG / DRAFT SKILL / AGENT CONTEXT）+ 每步描述与场景：
  > "At task start, the agent checks what your team has already figured out."
  > "Commands, file edits, stuck points, and outcomes become evidence for a reusable workflow."
  > "Cognition drafts the SKILL.md and waits for a human yes before sharing it."
  > "Bob hits the same wall later. His agent loads Alice's fix before guessing."
- 第 112–146 行（"Memory that decays, consolidates, and teaches back" + 四对位机制）：Evidence/Consolidation/Decay/Teaching 各一段。
- 第 135–145 行：Confirm-first capture、Person-specific retrieval、Group-code setup 三段安全承诺。

## 卡片范围是否成立

- 卡片以 "4 步闭环 + 与通用大脑的对位 + 三个安全承诺" 为主线，对应页面的核心叙事；范围合理。
- 直接来自源：4 步小标题、Alice/Bob 场景、Evidence/Consolidation/Decay/Teaching 四对位机制、Confirm-first capture / Person-specific retrieval / Group-code setup 三承诺。
- 引申点："适用边界"那一节强调"未公开衰减算法、新鲜度度量与 person-specific 检索实现细节"——这是对页面信息密度的诚实标注，非新增主张。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:38:00+08:00
- 检查要点：
  - 不是标题复述：四步表 + Alice/Bob 场景 + 四对位机制 + 三承诺 + 边界。
  - 知识密度足够：机制 + 类比 + 边界 + 治理承诺。
  - 源支撑齐全：每条主张锁到 cognitionus-llm-wiki-guide 具体行号。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，mechanism 类型与正文一致。
  - related 已链 cognition-human-approved-skill-md、file-outputs-back、idea-file、knowledge-compounding 等。

## 备注

- 这是产品宣传页面，作为 source 时知识密度较低；卡片只取"机制叙事 + 显式安全承诺"，避免重复 marketing。
- 与 v2 卡片中 `idea-file-as-agent-era-artifact` 概念上是同方向，但 Cognition 强调"团队层的人审 skill"，与个人 wiki 立场互补。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/cognition-skill-loop-evidence-to-teaching.md`
- draft provenance: `../../drafts/provenance/cognition-skill-loop-evidence-to-teaching.md`
- similarity: `../../drafts/similarity/cognition-skill-loop-evidence-to-teaching.json`
- comparison provenance: `../../drafts/comparison/cognition-skill-loop-evidence-to-teaching.md`
