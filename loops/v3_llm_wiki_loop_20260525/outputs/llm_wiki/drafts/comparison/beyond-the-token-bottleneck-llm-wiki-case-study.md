---
schema: comparison_provenance.v3
draft_card: ../cards/beyond-the-token-bottleneck-llm-wiki-case-study.md
draft_provenance: ../provenance/beyond-the-token-bottleneck-llm-wiki-case-study.md
similarity_result: ../similarity/beyond-the-token-bottleneck-llm-wiki-case-study.json
existing_cards:
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.1875
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1875
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1667
decision: new_card
audit_required: false
created_time: 2026-05-26T12:10:00+08:00
edited_time: 2026-05-26T12:10:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选都来自 karpathy gist 卡片家族。top1/top2 jaccard 0.1875 主要来自 `llm`、`wiki`、`模式`（top1 触发"模式"——v2 卡叫"LLM Wiki 作为模式文件"，draft 标题也含"模式"）。top3 0.1667 来自 `llm`/`wiki`/`的`。共享词来自"LLM Wiki 模式"这一标签性概念。

## 2. draft 与候选在哪里不同

- **来源不同**：本 draft 取自 `complete-tech-live-frontier`（CompleteTech LLC 2026-04-06 博客）；v2 三张候选都出自 karpathy `karpathy-gist-llm-wiki`。
- **类型不同**：v2 top1 `llm-wiki-pattern-file` 是 known_fact：声明"LLM Wiki 是一种模式 / 这份 gist 是 idea file"；本 draft 是 `example_pattern`：把这个模式落地到 120+ 页 Obsidian wiki 的真实工程实现（27 源、1400+ 内链、AGENTS.md 作 schema、workflows 目录维护）。前者定义了模式，后者执行了模式。
- top2 `three-layer-architecture` 是抽象三层（raw/wiki/schema）；本 draft 把这三层映射成具体目录（`raw/` 26 篇 PDF、`wiki/` 120+ 页、`AGENTS.md` schema），并加上 `workflows/` 这一**第四个**实操层（create/enrich/audit/query/meta playbooks）——是对三层模型的工程化补充。
- top3 `schema-configuration-document` 谈 schema 概念；本 draft 在 schema 实例化（AGENTS.md 定义 page types / linking conventions / depth standards / "done"标准）层面提供具体数据。
- 关键数字（27 源、120+ 页、1400+ 内链、一篇论文 → 10–15 页 touches）在 v2 都没有；这些是把 karpathy 抽象 "bookkeeping" 概念变成可测量量的关键证据。

## 3. 下一步的核心依据

(1) 三张候选都是 v2 内部的抽象概念卡，没有覆盖案例研究类目；(2) draft 提供 v2 完全没有的规模数字、目录布局、ingest 副作用量化、split license 等 example_pattern 必备信息；(3) 来源是 v2 KB 之外的独立 blog。结论是 `new_card`。

不是 `provenance_delta`：本 draft 不是给 v2 三层架构卡补一条证据——它本身是一份完整的实施案例，含独立的边界声明（单团队、未公开成本、面向研究文献）。不是 `merge_candidate`：v2 没有 example_pattern 类卡可合并。不是 `revise_before_gate`：所有数字都引到行号、边界明确。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；建议在 sources 索引加入 `complete-tech-live-frontier`；与同批 `llm-knowledge-base-five-stage-workflow`（抽象 workflow）建立 related 互链作"模式 → 案例"链路；未来如果 v2/v3 加入"bookkeeping 量化"卡可同向 cross-link。

## 5. 备注

- 案例规模数字（1400+ 内链、一篇论文 10–15 页 touches）特别值得引——这是少见的把 karpathy "bookkeeping" 抽象概念量化的公开数据。
- AGENTS.md 作 schema 的具体写法将来可与 `agents-md-as-schema-layer` 卡（如已存在或将来生成）做对比。
