---
schema: comparison_provenance.v3
draft_card: ../cards/etamp-environment-injected-memory-poisoning.md
draft_provenance: ../provenance/etamp-environment-injected-memory-poisoning.md
similarity_result: ../similarity/etamp-environment-injected-memory-poisoning.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0556
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0526
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0476
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 显示 top 1/2/3 都只共享 `的`。0.0556/0.0526/0.0476 的分数完全是中文助词同形。

## 2. draft 与候选在哪里不同

- draft 描述 eTAMP 攻击：仅靠环境观测（user-generated content）就能完成跨 session、跨 site 的 agent 记忆投毒；含威胁模型对比、三条独有特性、(Visual)WebArena 上 19.5%-22.3% 攻击成功率与 raw-vs-consolidated memory 的范围边界。来源 `arxiv-etamp-memory-poisoning`。
- top 1/2/3 全部为 Karpathy LLM Wiki 架构卡（idea file 抽象性、三层架构、schema 配置文档），与"agent memory 安全/投毒攻击"主题没有任何机制、来源、论点轴交集。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自助词同形，主题层零交集。判 `new_card`：直接走 publication_gate。draft 含攻击定义、威胁模型对比、实证数字与范围边界，发表条件已具备。不是 `provenance_delta`——v2 Karpathy 架构卡的 scope 不涉及 agent memory 安全。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

无；典型 `的` 同形误中。
