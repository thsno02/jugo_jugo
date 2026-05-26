---
schema: comparison_provenance.v3
draft_card: ../cards/karpathy-wiki-aliases-and-dedup.md
draft_provenance: ../provenance/karpathy-wiki-aliases-and-dedup.md
similarity_result: ../similarity/karpathy-wiki-aliases-and-dedup.json
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

三张候选都属于 Karpathy LLM Wiki 概念簇。token 共享集中在 `wiki` / `LLM` / `的`。理论上 draft 与 v2 候选**同属 Karpathy 概念家族**（两者都和 Karpathy LLM Wiki 有关），所以共享词应当比纯外部论文卡稍多一些。但仅看 jaccard，仍然只到 0.062，意味着关键概念词（aliases / dedup / Tier 1/2 / Lint / Merge Duplicates）在 v2 都不出现。

## 2. draft 与候选在哪里不同

draft 描述的是 **Karpathy LLM Wiki 的 Obsidian 社区插件**（v1.7.10+）的两个机制：(a) 强制别名（每页 ≥ 1 alias，frontmatter `aliases: []`）；(b) 两层语义重复检测（Tier 1 = 跨语言/缩写直接匹配，全部 LLM 验证；Tier 2 = 共享链接/中等相似度，仅在 token 预算允许时纳入）。同时给出 `Complete Aliases` / `Merge Duplicates` 命令与 < v1.7.11 升级路径，来源是 `data/raw/webpage/obsidian-community-plugin`。

v2 候选完全是 Karpathy gist 概念层卡，描述 idea file 的抽象性、wiki 三层架构、schema 配置——不涉及任何插件实现细节、aliases、dedup、Lint 工作流。draft 来源是社区插件页面，v2 候选来源是 Karpathy gist 原文，两者是**同一概念家族下不同抽象层**：gist 描述"模式"，插件描述"实现"。但具体论点轴（aliases / dedup）在 v2 中无对应。

## 3. 下一步的核心依据

虽然 draft 与 v2 同家族（都和 Karpathy LLM Wiki 有关），但论点轴并不重叠：v2 没有任何关于别名机制或语义重复检测的卡。draft 是该插件的具体功能记录，应作为新的实现层卡进入。结论 `new_card`。

不选 `provenance_delta`：v2 候选讨论的是 gist 概念层，无 body 可被 dedup 机制证据补充。
不选 `merge_candidate`：没有任何 v2 卡讨论 aliases / dedup。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；本卡可作为 Karpathy LLM Wiki 实现层（Obsidian 插件）系列的入口卡。

## 5. 备注

虽然 draft 与 v2 同源 Karpathy 主题，但 v2 当前覆盖的是 gist 概念层；插件实现层在 v2 完全空缺，本 draft 与其他插件衍生 draft 应在 publication 后形成独立 cluster。
