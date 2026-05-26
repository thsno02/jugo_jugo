---
schema: comparison_provenance.v3
draft_card: ../cards/etamp-direction-asymmetry-and-stealth.md
draft_provenance: ../provenance/etamp-direction-asymmetry-and-stealth.md
similarity_result: ../similarity/etamp-direction-asymmetry-and-stealth.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0625
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0588
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0526
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选都是 v2 高频干扰卡，分数 0.052–0.062，token 共享停留在中文虚词层面。Reddit / Shopping / Classifieds / ASR / Chaos Monkey 等核心 token 在 v2 不出现。

## 2. draft 与候选在哪里不同

draft 报告 eTAMP 论文 Appendix C/D 的两个发现：(a) **cross-site 攻击方向严重非对称**——S→R 对 GPT-5-mini 最易（53.4% ASR_B），R→C 对 GPT-5.2 最易（42.9%）；(b) **ASR_A ≈ 0**，攻击对 Task A 完全隐蔽，11 个组合中 9 个为零，唯二非零各 0.4% / 0.7%。论点轴是"方向画像必须作为模型评测维度 + 基于 Task A 行为的检测不可行"。

v2 候选是 Karpathy LLM Wiki 概念层卡，无任何 agent security、cross-site 攻击、memory poisoning 概念。

## 3. 下一步的核心依据

(1) (2) 共同表明 v2 无相关卡。draft 含表格 + footnote 引用 + 边界说明，完整。结论 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 `etamp-frustration-exploitation` 形成 eTAMP 主簇对照。

## 5. 备注

无。
