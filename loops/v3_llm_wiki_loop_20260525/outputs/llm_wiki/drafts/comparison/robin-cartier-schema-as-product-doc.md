---
schema: comparison_provenance.v3
draft_card: ../cards/robin-cartier-schema-as-product-doc.md
draft_provenance: ../provenance/robin-cartier-schema-as-product-doc.md
similarity_result: ../similarity/robin-cartier-schema-as-product-doc.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.2222
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.1111
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1111
decision: provenance_delta
audit_required: true
created_time: 2026-05-26T12:39:00+08:00
edited_time: 2026-05-26T12:39:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top 1 `llm-wiki-schema-configuration-document` 与 draft **真共享主题**——都是关于 schema 文件在 LLM Wiki 中的角色：

- v2 卡片由 Karpathy gist 第 33 行抽取，statement 是"schema 是配置文档，告诉 LLM 如何组织 wiki、遵循约定、执行 ingest/query/maintenance 工作流"。
- 本 draft 由 Robin Cartier 实践者评论文章抽取，核心论断是"真正可推广的创新不是 wiki 而是 schema 文件 + 把 CLAUDE.md 视作 living PRD for an AI colleague"。

共享 token `schema / wiki / 文档 / 的` 反映真实主题对齐。

top 2 / top 3 token overlap 仅 `wiki / 文件` 或 `wiki / 的`，明显是误中。

## 2. draft 与候选在哪里不同

- **来源不同**：v2 来源 Karpathy gist；draft 来源 Robin Cartier 2026-04-08 "A Practitioner's Verdict" 文章。
- **覆盖维度（draft 抬升 + 扩展）**：v2 卡片把 schema 描述为"配置文档"（中性、功能性）；draft 给出 (a) "schema 是真创新而非 wiki" 的价值排序断言、(b) "schema 是 living PRD for AI colleague" 的隐喻升级、(c) "schema 模式可推广到 wiki 以外的任何 agent 自主执行工作流"的扩张论断、(d) "PRD 语义带来产品工程方法论"（清晰度 / 验收准则 / 版本治理 / changelog）。
- **scope 不同**：v2 scope 仅限 Karpathy gist 对 schema 的功能性定义；draft scope 是"Robin Cartier 个人对 schema 角色的价值判断与可推广性主张"——是源主张（`source_claim`）类卡。
- **风险等级不同**：v2 是中性事实；draft 含主观价值排序（"真创新"），draft 自己已标注"是 Robin 的判断，不是 Karpathy 原话"。
- 不是 v2 卡片的扩展，也不是同视角不同源——是**同核心对象（schema 层），但用一个外部主张抬升其重要性 + 扩张其适用范围**。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 卡片是 Karpathy 原始定义事实卡，把 Robin 的价值排序主张合并进去会破坏 v2 的中性事实边界。
- 不是 `new_card`：核心对象（schema 层）已经在 v2 被定义；写一张完全独立的卡会造成"两张 schema 概念卡并列"，读者难以决定先读哪张。但 draft 是 `source_claim` 类型，其独立成卡的价值在于"承载一个具名实践者的可推广性主张"——这一条让我犹豫 `new_card` vs `provenance_delta`。
- 最终选 `provenance_delta`：draft 的核心引文（"The schema file is the real innovation ..."）应该作为 v2 schema 卡 provenance 的外部引用证据（不是事实补充，而是"该 schema 概念被外部实践者评为关键创新"的接收史证据）；audit 阶段决定是否把"living PRD for AI colleague"的隐喻作为 v2 卡的 Note 段或单独 source_claim 卡。
- 不是 `duplicate_skip`：v2 没有 Robin 的判断 / "PRD" 隐喻 / "可推广到 wiki 之外"的扩张主张。
- 不是 `revise_before_gate`：draft 证据完整、边界（Robin 自己判断 / 无监督执行是理想态 / PRD 包装是话术性扩张）都标注。

## 4. 决策

- decision: provenance_delta
- audit_required: true
- 后续动作建议：fusion_audit 把 Robin 的"schema is the real innovation"原句作为 v2 `llm-wiki-schema-configuration-document` 卡 provenance 的外部主张证据补充；audit 判断是否独立保留为 `source_claim` 类型卡（如保留，则与 v2 schema 卡通过 related 双向链接）。

## 5. 备注

- 这是一个 `source_claim` 类卡片与 v2 事实卡的边界情况：如果 v3 决定接受 `source_claim` 作为独立卡类型（schema_type 中已存在），则可改判为 `new_card`；如果只保留事实卡为 first-class，则 `provenance_delta` 是稳健选择。已倾向保守为 `provenance_delta` 留给 audit 决定。
- draft "本仓库 loop capsule 实践"段是把 Robin 主张应用到本项目环境的桥接，明示非源材料事实——audit 时建议保留为读者使用建议而非主张。
