---
schema: comparison_provenance.v3
draft_card: ../cards/aillm-wiki-four-defining-properties.md
draft_provenance: ../provenance/aillm-wiki-four-defining-properties.md
similarity_result: ../similarity/aillm-wiki-four-defining-properties.json
existing_cards:
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.2308
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2308
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.2
decision: new_card
audit_required: false
created_time: 2026-05-26T12:36:00+08:00
edited_time: 2026-05-26T12:36:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top 1 `llm-wiki-pattern-file` 与 draft 共享 token `llm / wiki / 模式`，主题邻近但**不是同一事实**：

- v2 卡片描述的是 Karpathy gist 自陈"LLM Wiki 是用 LLM 构建个人知识库的一种模式"——只断言"它是一种模式"这一元事实。
- 本 draft 描述的是 aillm.wiki 这个非官方目录站为该模式总结的四条对外定义性属性（Persistent Knowledge / Markdown-First / LLM-Maintained / Token-Efficient）。

两者讨论的都是"LLM Wiki 是什么"，但层次不同：v2 = 元定义，draft = 四属性话术。

top 2 / top 3 是不同子事实卡（三层架构 / schema 配置）；与 draft 无直接事实重叠，只是同主题板块下 token 误中。

## 2. draft 与候选在哪里不同

- **来源不同**：v2 `llm-wiki-pattern-file` 来源是 Karpathy gist 第 1–5 行；draft 来源是 aillm.wiki 站首页 L25–39（非官方目录站）。
- **覆盖维度不同**：v2 只断言"LLM Wiki 是一种模式 + idea file 可复制给 agent"；draft 给出四条具体属性（含 RAG 对比、400K 词案例、零基础设施声明）+ 三条工程边界（缺哪条不该叫 LLM Wiki / 工具可换 / 平台自陈未经第三方验证）。
- **来源性质不同**：v2 来源是 Karpathy 本人的原始 gist；draft 来源明示"Not affiliated with Anthropic or Andrej Karpathy"——是社区/第三方话术。
- **决策粒度不同**：v2 元定义级；draft "四 lens"框架级，可用作产品评估。
- 不是 v2 卡片的扩展，也不是同视角不同源——是**对同一主题板块的不同社区话术的独立采集**。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 卡片 scope 是 Karpathy gist 一手来源；社区目录站的四属性话术合并进去会破坏 v2 单源边界，也会使"该模式是 Karpathy 提的"与"社区话术"混在一起。
- 不是 `provenance_delta`：v2 卡片只承担"该模式存在 + 是 idea file"这一元事实，draft 的四属性不是对它的新出处证据，而是社区独立解读。
- 不是 `duplicate_skip`：v2 没有"四属性 / 对 RAG 的话术性差异"的任何内容。
- 不是 `revise_before_gate`：draft 证据完整（四属性原文都列了行号）、scope 清晰（distinction 类型卡）、边界（平台自陈未经验证 / "Token-Efficient" 仅 small-to-mid 规模成立）都标注。
- 是 `new_card`：作为社区话术的独立采集，与 v2 元定义卡互补，构成不同 lens。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：走 publication_gate；接受后建议在 audit 阶段把它与 v2 `llm-wiki-pattern-file` 通过 related 链接互相引用（"元定义 vs 社区话术四属性"两个 lens）。

## 5. 备注

- 这张卡是"非官方目录站"作为来源的一个范式案例——边界段已明示"未经第三方验证"，避免读者把社区话术等同于 Karpathy 原意。
- top 1 与 top 2 同分（0.2308）是 jaccard 在小集合上的常见 tie；选 `llm-wiki-pattern-file` 作为对比锚点更贴主题。
