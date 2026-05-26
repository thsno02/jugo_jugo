---
schema: comparison_provenance.v3
draft_card: ../cards/karpathy-llm-kb-three-layer-arch.md
draft_provenance: ../provenance/karpathy-llm-kb-three-layer-arch.md
similarity_result: ../similarity/karpathy-llm-kb-three-layer-arch.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.5
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.3077
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1538
decision: provenance_delta
audit_required: true
created_time: 2026-05-26T12:05:00+08:00
edited_time: 2026-05-26T12:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- **top 1 `llm-wiki-three-layer-architecture` (0.500)**：共享 token `llm / wiki / 三层 / 架构 / 的`。这是**真共享**：v2 卡的 statement "该来源把 LLM Wiki 架构分成三个层次：原始来源、wiki 和 schema" 与本 draft 的标题"Raw / Schema / Wiki 三层架构"指的是**同一个 Karpathy 概念分层**。v2 的 reference 是 Karpathy gist `raw.txt:25-33`；draft 的 source 是 DevelopersIO/森茂洋的日文文章，但森茂洋整段引用 Karpathy 同一个 `Architecture` 小节，三层名也照搬。
- **top 2 `llm-wiki-schema-configuration-document` (0.308)**：共享 token `llm / schema / wiki / 的`。它是上面三层中 schema 那一层的细化卡，draft 也写到 schema 含义（"分类法、命名规则、互链规则"）。所以也是真主题相邻，但范围窄于本 draft。
- **top 3 `llm-wiki-health-checks` (0.154)**：仅共享 `llm / wiki`，是 Karpathy gist 第四操作（Linting）的事实卡，与本 draft 的"三层结构"层面无关，属低分误中。

## 2. draft 与候选在哪里不同

- **来源不同**：v2 top1 卡直接取自 Karpathy 原 gist；本 draft 来自 DevelopersIO 工程师森茂洋对同一概念的**二次抽象与工程化解读**。这构成"同一事实，新来源的二次证据"。
- **scope 显著更宽**：v2 top1 只是一句 known_fact（"作者把架构分为三层"）；本 draft 是 concept 卡，覆盖：
  - 三层各自定义（与 v2 一致）；
  - **森茂自己的目录映射**（`workspace/knowledge/` → Raw、各 `CLAUDE.md` → Schema、`workspace/wiki/` → Wiki）——v2 完全没有；
  - **工程含义**（人手只能改 raw / schema；wiki 是输出层应可重新编译；schema 是少量高密度、wiki 是大量低密度产物）——v2 完全没有；
  - **边界与误读**（"hacky collection of scripts"、Memory MCP 作为可扩展的第 4 层、"人不直接写 wiki" ≠ "人不可以编辑 wiki"）——v2 没有这些边界讨论。
- 本 draft 不是 v2 top1 的同张卡——它在 v2 top1 的核心事实之上，多带了**二次来源 + 落地映射 + 边界**三类增量信息。

## 3. 下一步的核心依据

- (1) 中确认了 draft 与 v2 top1 谈的是同一个 Karpathy 三层架构，且 draft 援引的是**支撑同一事实的另一份独立来源**（DevelopersIO 森茂洋）。
- (2) 中确认 draft 范围远大于 v2 top1，但其增量内容主要是"对 v2 已有事实的工程化解读 + 一份新来源 + 一组操作边界"，并未推翻 v2 的 statement。
- 这正好命中 `provenance_delta` 的定义："draft 不会改 v2 卡 body 多少，但加了新证据 / 新边界 / 新数值"——这里加的是新证据（DevelopersIO 二次来源）、新落地（森茂的目录映射）、新边界（"hacky collection of scripts"、可扩展第 4 层）。
- 不是 `merge_candidate`，因为本 draft 与 v2 top1 范围与论点轴不同（draft 是 concept 卡，v2 是事实卡，两者并存价值高于合并）。
- 不是 `new_card`，因为核心事实"三层架构"与 v2 top1 完全是同一事实，再创一张 concept 卡会让 v2 top1 的 statement 失去最重要的二次来源链接，破坏后续可追溯性。
- 不是 `duplicate_skip`，因为 draft 携带的增量内容（目录映射、边界、二次来源）值得入库。

## 4. 决策

- decision: provenance_delta
- audit_required: true
- 后续动作建议：把 draft 作为新 card 入库，audit 阶段把 DevelopersIO 来源、森茂目录映射、"hacky collection of scripts" 边界三条反向链接进 v2 `llm-wiki-three-layer-architecture.md` 的 provenance。

## 5. 备注

- draft 的 frontmatter `related` 已经显式提到 `llm-knowledge-base-five-stage-workflow` 与 `aillm-wiki-four-defining-properties`，与 v2 top1 / top2 不冲突；audit 时可再加一条 `related: [llm-wiki-three-layer-architecture]` 指回 v2 top1。
- v2 top2（schema 配置文档卡）可视为 draft 内 `Schema` 段的细化，audit 时如要回链 v2 top2，只需在 v2 top2 的 provenance 里加一条 "DevelopersIO 把 schema 在 Claude Code 实践里映射到分目录的 CLAUDE.md" 的边界注脚即可。
