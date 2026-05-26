---
schema: comparison_provenance.v3
draft_card: ../cards/karpathy-llm-wiki-obsidian-plugin-overview.md
draft_provenance: ../provenance/karpathy-llm-wiki-obsidian-plugin-overview.md
similarity_result: ../similarity/karpathy-llm-wiki-obsidian-plugin-overview.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.3333
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1579
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1111
decision: new_card
audit_required: false
created_time: 2026-05-26T12:10:00+08:00
edited_time: 2026-05-26T12:10:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- **top 1 `llm-wiki-three-layer-architecture` (0.333)**：共享 `llm / wiki / 三层 / 架构 / 的`。draft 内确实有一节"Karpathy 三层架构在插件中的实现"（sources/ → wiki/ → schema/），所以与 v2 top1 的"raw / wiki / schema"三层在概念层重合。
- **top 2 `llm-wiki-schema-configuration-document` (0.158)**：仅共享 `llm / wiki / 的`，因 draft 含 `schema/` 目录的描述而被命中，论点上不重叠。
- **top 3 `llm-wiki-health-checks` (0.111)**：仅共享 `llm / wiki`，draft 涉及"Lint wiki"命令，但论点完全不同（v2 是事实卡，draft 是产品功能列表中的一行）。低分误中。

## 2. draft 与候选在哪里不同

- **卡片类型完全不同**：
  - v2 top1 = `known_fact`，仅一句话陈述 Karpathy 把架构分为三层；
  - draft = `example_pattern`，详细描述 Greener-Dalii 在 Obsidian 社区发布的具体插件（v1.10.2、94/100 Obsidian 分数、~781 下载）、命令面、多模型提供商、模型选型档位、矛盾状态机、Smart Fix All 顺序、MIT 许可、4 周 27 个版本等产品级元信息。
- **scope 完全不同**：v2 top1 谈"Karpathy 提出三层结构这件事"；draft 谈"一个具体工程产品如何实现这个三层结构 + 它做了什么额外承诺"（如别名 dedup、矛盾状态机、写保护、本地 + 云的混合模型方案）。
- **来源不同**：v2 top1 来自 Karpathy gist；draft 来自 `obsidian-community-plugin` 的产品页面文本，引用第 80–115、196–212、343–370、256–305、376–390、449 行——与 v2 top1 完全无证据交叉。
- draft 与 v2 top1 不是同张卡的两个版本，是"概念卡 vs 实现卡"的关系。

## 3. 下一步的核心依据

- (1) 共享的 token 高分来自"三层 / 架构"，但 (2) 显示两张卡在卡片类型、scope、来源上都不同——draft 是一个全新的 example_pattern 卡，v2 top1 是一个 known_fact 卡。
- 选 `new_card`：draft 描述的是 Karpathy 三层架构的一个**具体实现实例**，而非对 Karpathy 概念的再陈述或证据补强。v2 top1 的 statement 不需要因 draft 而修改，其 provenance 也不需要回链该插件（v2 top1 的 scope 已声明"仅限该来源提出的架构分层"）。
- 不选 `provenance_delta`：draft 不为"Karpathy 把架构分为三层"这一事实补证据，它讲的是产品功能。
- 不选 `merge_candidate`：把概念卡和插件 overview 合并会破坏 v2 top1 的事实卡紧致性。
- 不选 `revise_before_gate`：draft 自带丰富的引用与边界（依赖 Obsidian、本地 Ollama 上下文受限等），评估细节完备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；建议在 draft `related` 中追加 `llm-wiki-three-layer-architecture`，以方便从 v2 概念卡跳到该实现 overview。

## 5. 备注

- 该 draft 与 batch 中其他 `karpathy-wiki-*` 子主题卡（aliases-and-dedup、full-context-vs-rag、extraction-granularity）共同构成 overview + 子主题集，相互关联通过 draft 内 `related` 已表达。
- 若以后 v2 决定补一张"Karpathy 三层在工具生态中的实现示例索引"，本 draft 是首选条目。
