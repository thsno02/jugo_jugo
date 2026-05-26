---
schema: comparison_provenance.v3
draft_card: ../cards/llm-wiki-contradictions-are-assets.md
draft_provenance: ../provenance/llm-wiki-contradictions-are-assets.md
similarity_result: ../similarity/llm-wiki-contradictions-are-assets.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1875
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1667
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1176
decision: new_card
audit_required: false
created_time: 2026-05-26T12:12:00+08:00
edited_time: 2026-05-26T12:12:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选标题分别含 `llm`/`wiki`/`的`，与本 draft 标题共享这些通用功能词。top1/top2 jaccard 0.1875/0.1667 全部来自通用词；top3 `health-checks` 也只共享 `llm`/`wiki`。draft 关键词 `矛盾`、`资产`、`重写`、`标注`在任何 v2 候选标题中都没出现。属典型的功能词撞分。

## 2. draft 与候选在哪里不同

- **来源不同**：本 draft 取自 `openaitoolshub-six-months`（Rohit v2 + Jim Six-Month 实战 retrospective）；v2 三张候选均出自 karpathy gist / x post 家族。
- **类型不同**：本 draft 是 `distinction` 卡，正面对比"传统 KB 视角（矛盾=bug）"与"LLM Wiki 视角（矛盾=资产）"；v2 三张候选都是 known_fact 类的概念定义/机制。
- top1 `three-layer-architecture` 是 raw/wiki/schema 静态分层；本 draft 是处理冲突的协议（`contradicts:` frontmatter、保留两版、lint 时统一暴露），并显式划出 compliance 场景的不适用边界。两者论点轴完全无交集。
- top2 `schema-configuration-document` 讲 schema 作为配置文档的角色；本 draft 触及"schema 必须把 contradiction protocol 写死"是引申的操作规则，但重点不在 schema 角色本身。
- top3 `health-checks` 讲 LLM 健康检查的抽象事实；本 draft 触及"lint pass 优先列未解决矛盾"是引申，重点是矛盾哲学。
- 关键论点（"重写矛盾会永久丢失旧 reasoning"、"决策演化路径 / 领域结构信号 / 检验后续判断的锚点"三类信息价值、compliance 反例边界）在 v2 完全没有。

## 3. 下一步的核心依据

(1) 三张候选都不覆盖 contradiction 处理协议；(2) draft 是来自全新源（Rohit v2 + Jim retrospective）的 distinction 卡，自身明确写出 compliance 反例边界；(3) v2 没有 distinction 类卡可合并。结论是 `new_card`。

不是 `provenance_delta`：本 draft 不是给 v2 三层架构或 schema 配置文档卡补一段证据——它是另一个论点轴（冲突处理哲学）、另一个源、另一个抽象层。也不是 `revise_before_gate`：draft 有完整证据链（行 96、行 136）、明确边界、可操作规则；可直接进入 publication_gate。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；建议在 sources 索引加入 `openaitoolshub-six-months`；与 `llm-wiki-rohit-v2-improvements` 兄弟卡（如已存在）建立 related 互链作"概览 → 哲学放大"链路。

## 5. 备注

- "frontmatter `do-not-rewrite: true` 锁定关键页"是借自 Pitfall #2 的 schema-level 工程做法，原文未直说；编辑/审稿可视情况裁定。
- compliance 边界声明（regulated 领域不适用）是本卡的硬约束，将来任何引用本卡的下游决策都应保留这条 boundary。
