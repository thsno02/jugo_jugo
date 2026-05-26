---
schema: comparison_provenance.v3
draft_card: ../cards/gragpoison-additive-vs-edit-attack.md
draft_provenance: ../provenance/gragpoison-additive-vs-edit-attack.md
similarity_result: ../similarity/gragpoison-additive-vs-edit-attack.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0714
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0667
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0588
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.08，shared_tokens 仅为「的」。draft 标题主体 token（GraphRAG / 投毒 / additive / edit / in-place / 家族）与 v2 候选（Karpathy LLM-wiki 元描述）无任何术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 distinction 卡，来源 `arxiv-graph-poisoning`，论述 GraphRAG 投毒文献的两条家族划分：additive（GRAGPOISON：注入新 chunk）vs in-place edit（TKPA/UKPA：仅改少量词，0.05-0.06% 即可达 93% ASR），并对比攻击者能力、可观察痕迹、防御切入点、攻击者效用曲线。属于「GraphRAG 安全 / 攻击分类学」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述。论点轴（GraphRAG 攻击 vs 个人 LLM wiki 模式）、来源（学术安全论文 vs Karpathy gist）、读者（安全研究者 vs 个人知识管理者）完全不同。v2 KB 无任何投毒 / 安全相关卡。

## 3. 下一步的核心依据

shared_tokens 全是「的」，无语义关联。draft 引文具体到 L193-205 / L226-230 / L749-757 / L778-789，scope 自洽。无任何 v2 卡可 merge 或 provenance_delta。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `graphrag-manipulation-only-attack-surface` / `tkpa-graph-guided-targeted-poisoning` / `ukpa-coreference-disruption` 同 source 互引。
