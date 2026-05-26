---
schema: comparison_provenance.v3
draft_card: ../cards/aillm-wiki-schema-as-bottleneck.md
draft_provenance: ../provenance/aillm-wiki-schema-as-bottleneck.md
similarity_result: ../similarity/aillm-wiki-schema-as-bottleneck.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.3333
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.125
decision: new_card
audit_required: false
created_time: 2026-05-26T12:08:00+08:00
edited_time: 2026-05-26T12:08:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- **top 1 `llm-wiki-schema-configuration-document` (0.333)**：共享 `llm / schema / wiki / 是 / 的`。两张卡都谈 "schema 在 LLM Wiki 里的角色"——v2 给出 schema 的**静态定义**（"配置文档，规定结构、约定与工作流"），draft 强调"**挑 schema 是真正的工程瓶颈**"。所以是同一概念实体（schema），但论点轴不同。
- **top 2 `llm-wiki-three-layer-architecture` (0.200)**：仅共享 `llm / wiki / 的`，是三层结构中 schema 属于其中一层的关联；论点上不冲突也不重叠。
- **top 3 `llm-wiki-health-checks` (0.125)**：仅共享 `llm / wiki`，token jaccard 误中，主题（health checks vs schema bottleneck）完全无关。

## 2. draft 与候选在哪里不同

- **来源不同且不重叠**：v2 top1 来自 Karpathy gist `raw.txt:33`（schema 定义）；draft 来自 `aillm-wiki-directory`（aillm.wiki 站方的"3-step build"叙述与"hardest part is picking a schema"原句）。两份来源**没有交叉证据**。
- **论点轴不同**：
  - v2 top1 = 定义性事实（"schema 是配置文档，告诉 LLM 如何组织 wiki / 遵循约定 / 执行 ingest-Q&A-maintain 工作流"）。
  - draft = 操作性主张（"五模板 + 三步工作流的真瓶颈在 schema 选择；选错就要回头大改 wiki"）。
- **fact_type 不同**：v2 是 `known_fact`，draft 是 `operational_rule`（站方的工程判断 + 营销话术叠加，draft 自己已标注边界）。
- **范围不同**：v2 只声明 schema 的功能边界（结构/约定/工作流）；draft 谈的是 schema 选择对长期可压缩性 / 可重复性的影响、五模板可选项、以及 "schema 不匹配的信号是手改 frontmatter" 等可操作信号。

## 3. 下一步的核心依据

- (1) 与 (2) 合起来看，draft 与 v2 top1 共享同一个概念实体 schema，但**论点轴完全不同**（定义 vs 操作判断），证据基础也完全不同（Karpathy gist vs aillm.wiki 三步指南）。这是典型的"同主题不同视角"。
- 选 `new_card` 而非 `provenance_delta`，因为 draft 并不为 v2 top1 的 statement（"schema 是配置文档"）提供新证据 / 新边界 / 新数值——它根本是另一类主张（操作瓶颈），不应反向写回 v2 top1 的 provenance。
- 选 `new_card` 而非 `merge_candidate`，因为合并会把"定义事实"与"操作判断"塞进一张卡，失去事实卡的紧致性，也违背 v2 卡 "fact_type: known_fact / scope: 仅限该来源" 的边界约束。
- 选 `new_card` 而非 `revise_before_gate`，因为 draft 边界已显式标注（"站方判断 + 营销话术"、"三步走是简化叙事"），不需要回 revision。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；可在 draft 的 `related` 加上 `llm-wiki-schema-configuration-document`，让"操作瓶颈"卡与"定义"卡互相支撑。

## 5. 备注

- token 共享高（0.333）主要来自 `llm / schema / wiki / 是 / 的` 这种基础 token；jaccard 高分并不暗示 merge。
- 若以后 v2 决定补一张 "schema 在工程实践中的瓶颈位置" 综述，本 draft 可作为重要来源。
