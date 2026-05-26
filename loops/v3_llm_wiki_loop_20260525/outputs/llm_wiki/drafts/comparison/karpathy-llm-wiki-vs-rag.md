---
schema: comparison_provenance.v3
draft_card: ../cards/karpathy-llm-wiki-vs-rag.md
draft_provenance: ../provenance/karpathy-llm-wiki-vs-rag.md
similarity_result: ../similarity/karpathy-llm-wiki-vs-rag.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.2222
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1765
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1111
decision: new_card
audit_required: false
created_time: 2026-05-26T12:38:00+08:00
edited_time: 2026-05-26T12:38:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张 v2 候选与 draft 是 token 误中，不是事实重叠：

- 共享 token 集 `llm / wiki / 是 / 的` 都是 LLM Wiki 主题板块的高频常见词。
- v2 候选讲 schema 配置文档定义 / 三层架构定义 / health checks 清理用途——**没有一张涉及"LLM Wiki vs RAG"的 paradigm 区分**。

draft 主题是 Marvin Hn 综述 + Karpathy gist 关于"compiled artifact vs transient answer"的范式区分。

## 2. draft 与候选在哪里不同

- **事实类型不同**：v2 三张都是 `known_fact`；draft 是 `distinction`，承担"LLM Wiki 与 RAG 的范式差异"这一比较类知识。
- **来源不同**：v2 来源 Karpathy gist；draft 来源 marvin-hn-persistent-knowledge 综述文章（虽然综述本身指向 Karpathy gist）。
- **覆盖维度全新**：知识形态对比表 / "compiled artifact vs transient answer"关键句 / ingest 时 5 类增量动作清单 / "前 agent 时代 wiki 退化、agent 时代 wiki 复兴"时间线推论 / "在 >10K 文档规模 RAG 仍不可替代"边界 —— 都不在 v2 任何卡片中。
- **决策粒度不同**：v2 是事实定义；draft 是工程选型 lens。

不是 v2 卡片的扩展，是**全新的 distinction 类卡**。

## 3. 下一步的核心依据

- 不是 `merge_candidate` / `provenance_delta`：v2 没有任何 wiki vs RAG 内容，找不到合并 / 补强对象。
- 不是 `duplicate_skip`：v2 未覆盖。
- 不是 `revise_before_gate`：draft 证据扎实（HN 274/89 数字与 compiled artifact 关键句都带行号）、scope 清晰、边界（>10K 规模 RAG 仍优 / 主题极度跳跃时 wiki 复利收益弱）都标注。
- draft 提到的 v2 卡片 `auto-index-replaces-rag-at-small-scale` 不在本 batch top-3，故不在本评估范围内（仅在备注中提示后续 audit 应交叉对齐两者）。

正确决定是 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：走 publication_gate；audit 阶段建议把本卡与 v2 `auto-index-replaces-rag-at-small-scale`（如存在）、本 batch 内的 `anthemcreation-llm-wiki-vs-rag-multi-hop` 与 `hn-llm-wiki-is-just-rag-debate` 三张同主题卡通过 related 形成簇。

## 5. 备注

- 同 batch 内有三张关于"wiki vs RAG"的 draft，它们出自不同来源（Marvin HN 综述 / 法语指南 / HN 原帖辩论），可保留为不同视角的三张独立卡，也可在 audit 阶段决定是否融合一张元卡；本评估只决定 v3 vs v2 是否新建，不评估三张 v3 卡之间关系。
- draft 备注里预测"与 knowledge-compounding-dynamic-roi 互链"——该卡若在 v2 存在但未进本 batch top-3，audit 阶段补建 related。
