---
schema: comparison_provenance.v3
draft_card: ../cards/karpathy-wiki-extraction-granularity.md
draft_provenance: ../provenance/karpathy-wiki-extraction-granularity.md
similarity_result: ../similarity/karpathy-wiki-extraction-granularity.json
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

similarity 中三个 top 候选都只共享 `的`，分数完全是助词同形。主题家族层面 draft 与 v2 候选都关于 Karpathy LLM Wiki 范式：候选描述 gist 的三层定义，draft 描述 Obsidian 社区插件的 ingestion 旋钮设置。

## 2. draft 与候选在哪里不同

- draft 是 operational_rule 卡，描述 **Obsidian Karpathy LLM Wiki 插件**的五档抽取粒度（Minimal/Coarse/Standard/Fine/Custom）、典型条目数、推荐场景、与 Page Generation Concurrency / Batch Delay / Smart Batch Skip 的联动、3 条反对模式。来源 `obsidian-community-plugin` 网页（v1.6.2 / v1.7.7 / v1.10.0 等具体版本）。
- top 1/2/3 是 Karpathy 原始 gist 的架构层定义（idea file 抽象性、三层架构、schema 配置）。
- 论点轴完全不同：v2 候选是"架构定义"的 known_fact；draft 是某个具体 plugin 实现里"成本/深度旋钮怎么调"的 operational_rule。来源类型也不同（gist vs plugin webpage）。

## 3. 下一步的核心依据

(1) 与 (2) 表明 v2 候选 scope 限定为 Karpathy gist 文本，不允许吸纳 plugin 实现细节作为 provenance delta。判 `new_card`：直接走 publication_gate。draft 含五档定义、3 个旋钮联动、反对模式与具体版本号，发表条件齐备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate；在 related 字段链接 v2 三层架构卡，作为"Karpathy LLM Wiki 范式 → 具体 plugin 实现"的演进链路。

## 5. 备注

属于"同范式不同实现层"的相邻关系；scope 错位故不合并。
