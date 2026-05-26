---
schema: comparison_provenance.v3
draft_card: ../cards/llm-wiki-rohit-v2-improvements.md
draft_provenance: ../provenance/llm-wiki-rohit-v2-improvements.md
similarity_result: ../similarity/llm-wiki-rohit-v2-improvements.json
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

similarity 中三个 top 候选都只共享 `的`，分数 0.0556/0.0526/0.0476 完全是助词同形。**主题层面**确实存在一种"相邻关系"：draft 与 v2 候选都关于 Karpathy LLM Wiki 范式——但 v2 卡描述的是 Karpathy 原始 gist 的架构定义，draft 描述的是 Rohit Ghumare v2 在该 gist 之上加的 schema-level 改进。

## 2. draft 与候选在哪里不同

- draft 是 mechanism 卡，描述 **Rohit v2 在 Karpathy v1 上加的三件事**：Memory Lifecycle frontmatter（last_verified / confidence / superseded_by / contradicts）、Typed wikilinks（6 种 relationship type）、Contradiction protocol（"don't overwrite, mark + lint exposure"），并配 Jim Liu 的 35 页验证、Pitfall #3 实证、维护成本对比。来源 `openaitoolshub-six-months`。
- top 1 `idea-file-abstract-vague`：Karpathy 帖文中 idea file 的抽象性。
- top 2 `llm-wiki-three-layer-architecture`：Karpathy gist 的三层架构（raw / wiki / schema）定义。
- top 3 `llm-wiki-schema-configuration-document`：schema 层作为配置文档。
- 三张 v2 卡 scope 严格限定为 `gist_raw/karpathy-gist-llm-wiki` 的层定义；draft 来源是 `openaitoolshub-six-months` 网页对 Rohit v2 / Jim 6-month review 的总结。两者论点轴不同：v2 是"v1 架构是什么"，draft 是"v1 不修就会反复踩的失败模式 + v2 怎么改"。

## 3. 下一步的核心依据

(1) 与 (2) 表明虽属同一主题家族（LLM Wiki 范式），但 v2 候选卡的 scope（Karpathy gist 内部架构）不允许吸纳 Rohit v2 的 schema-level 改进作为 provenance delta——这些改进出自另一来源、另一作者、另一时间点。判 `new_card`：直接走 publication_gate。不是 `provenance_delta`，因为 draft 增加的不是同一条事实的新证据，而是一组新事实（lifecycle / typed link / contradiction protocol）需要独立卡承载。不是 `merge_candidate`，因为内容主体（具体三机制）不与任何 v2 卡 body 重合。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate；在 related 字段链接到 v2 `llm-wiki-three-layer-architecture` 和 `llm-wiki-schema-configuration-document` 作为对比阅读。

## 5. 备注

主题相邻但 scope 不重叠的典型情形：同一范式不同作者 / 不同时间点的改进，应作为独立卡而非 provenance delta。后续 v3 KB 索引可考虑把 Karpathy v1 / Rohit v2 / Jim 6-month review 三组卡组成"Karpathy LLM Wiki 演化"集群。
