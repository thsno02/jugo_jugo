---
schema: comparison_provenance.v3
draft_card: ../cards/ukpa-edit-distance-stealth-tradeoff.md
draft_provenance: ../provenance/ukpa-edit-distance-stealth-tradeoff.md
similarity_result: ../similarity/ukpa-edit-distance-stealth-tradeoff.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0526
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.05
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0455
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 中三个 top 候选都只共享 `的`。分数完全是助词同形误中。

## 2. draft 与候选在哪里不同

- draft 描述 UKPA（图毒化攻击）的编辑距离 ablation：$d_{\text{edit}} \leq 3$ 时 QA 从 0.95 降到 0.50/0.45，$\leq 5$ 时攻击力饱和但 perplexity 显著上升；机制是共指破坏对 1–3 个 token 改动最敏感；含默认权重 $(\alpha,\beta,\gamma)=(0.25,0.25,0.5)$、防御侧检测线索与边界（度量定义不严格、只在 RUW + MS GraphRAG / LightRAG 验证）。来源 `arxiv-graph-poisoning`。
- top 1/2/3 是 Karpathy LLM Wiki 架构卡，与 GraphRAG 毒化攻击的 ablation 主题完全不同。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自 `的`，主题无交集。判 `new_card`：直接走 publication_gate。draft 含 ablation 三档数字、机制解释、防御启示与边界，发表条件齐备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

无；典型 `的` 同形误中。
