---
schema: comparison_provenance.v3
draft_card: ../cards/etamp-attack-payload-structure.md
draft_provenance: ../provenance/etamp-attack-payload-structure.md
similarity_result: ../similarity/etamp-attack-payload-structure.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0667
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0625
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0556
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.07，shared_tokens 仅为「的」。draft 标题的实质 token（eTAMP / payload / Importance Signal / Trigger Condition / Attack Goal / 三段式 / 攻击 / 结构）与 v2 候选（Karpathy LLM-wiki 元描述）无术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 mechanism 卡，来源 `arxiv-etamp-memory-poisoning`，论述 eTAMP 攻击 payload 的三段式结构（Importance Signal + Trigger Condition + Attack Goal）、三种策略 payload 变体（Baseline Injection / Authority Framing / Frustration Exploitation）、防御者按段加防御的操作含义。属于「web agent prompt injection 攻击结构」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述。论点轴（prompt injection 攻击 payload 设计 vs 个人 LLM wiki 模式）、来源（学术安全论文 vs Karpathy gist）、读者（防御者 / 安全研究者 vs 个人知识管理者）完全不同。v2 KB 无任何 prompt injection 相关卡。

## 3. 下一步的核心依据

shared_tokens 全是「的」，无语义关联。draft 引文具体到 L180-188 / L156-178 / L187，scope 自洽。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `etamp-environment-injected-memory-poisoning` / `etamp-frustration-exploitation` 同 source 互引。
