---
schema: accepted_card_provenance.v3
card: ../cards/cognition-human-approved-skill-md.md
material_id: cognitionus-llm-wiki-guide
digest_id: digest_cognitionus-llm-wiki-guide
source_paths:
  - data/raw/webpage/cognitionus-llm-wiki-guide/text.txt
draft_card: ../../drafts/cards/cognition-human-approved-skill-md.md
draft_provenance: ../../drafts/provenance/cognition-human-approved-skill-md.md
similarity_result: ../../drafts/similarity/cognition-human-approved-skill-md.json
comparison_provenance: ../../drafts/comparison/cognition-human-approved-skill-md.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:36:00+08:00
  gate_notes: 6/6 通过；两阶段闸门 + 人审 verbatim + group-code 邀请边界 + 与自动 CONSOLIDATE 派对照齐全；引申用 hedge 标注。
created_time: 2026-05-26T12:05:00+08:00
edited_time: 2026-05-27T14:36:00+08:00
edited_entity: llm
---

## 源证据

- 第 79–92 行（DRAFT SKILL 步 verbatim 节选）：
  > "Cognition drafts the SKILL.md and waits for a human yes before sharing it."
  > "Vercel env scoping / Status: awaiting approval / Author: Alice / Approve this skill for the team?"
- 第 136 行：
  > "Cognition drafts skills and waits for explicit approval before saving anything to the group."
- 第 140–141 行（Person-specific retrieval）：
  > "Skills keep who taught them and why their judgment worked, so agents can follow the right taste."
- 第 143–144 行（Group-code setup）：
  > "One teammate creates the group. Everyone else joins with the same code and starts sharing memory."

## 卡片范围是否成立

- 卡片以 operational_rule 类型记录"两阶段写入 + 人审闸门"，与页面把"confirm-first capture"作为独立卖点的处理一致。
- 直接来自源：起草 + 等待 yes、作者归属 person-specific retrieval、group-code 邀请边界。
- 引申点：
  - "3 个设计动机"未在页面 verbatim 出现，但用 hedge ("页面虽未展开论证，但...") 表明这是 derived；
  - 与"自动 CONSOLIDATE"的对照是跨材料综合，未对 Cognition 引入新主张。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:36:00+08:00
- 检查要点：
  - 不是标题复述：两阶段规则 + 三条动机 + 与 RAG 对照 + 与 CONSOLIDATE 张力 + 实施约束。
  - 知识密度足够：规则 + 动机（hedged）+ 对照 + 边界。
  - 源支撑齐全：每条主张锁到 cognitionus-llm-wiki-guide 行号 + verbatim。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，operational_rule 类型与正文一致。
  - related 已链 cognition-skill-loop、idea-file-as-agent-era-artifact 等。

## 备注

- 与 `cognition-skill-loop-evidence-to-teaching` 是 zoom-in 关系（闭环卡讲全流程，本卡专攻"写入 gate"）。
- 与 batch `audit-by-suspension-against-entrenchment` 形成 governance 立场对照（人审 vs 反事实 audit）。
- v2 卡片中无对应规则卡，无重叠。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/cognition-human-approved-skill-md.md`
- draft provenance: `../../drafts/provenance/cognition-human-approved-skill-md.md`
- similarity: `../../drafts/similarity/cognition-human-approved-skill-md.json`
- comparison provenance: `../../drafts/comparison/cognition-human-approved-skill-md.md`
