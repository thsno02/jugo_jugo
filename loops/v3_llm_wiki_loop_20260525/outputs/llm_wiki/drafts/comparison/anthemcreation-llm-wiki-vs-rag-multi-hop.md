---
schema: comparison_provenance.v3
draft_card: ../cards/anthemcreation-llm-wiki-vs-rag-multi-hop.md
draft_provenance: ../provenance/anthemcreation-llm-wiki-vs-rag-multi-hop.md
similarity_result: ../similarity/anthemcreation-llm-wiki-vs-rag-multi-hop.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2143
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1875
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1333
decision: new_card
audit_required: false
created_time: 2026-05-26T12:40:00+08:00
edited_time: 2026-05-26T12:40:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张 v2 候选与 draft token 共享只有 `llm / wiki / 的`，纯属误中：

- v2 三张候选讲 schema 配置文档 / 三层架构 / health checks 清理用途——**没有一张涉及"LLM Wiki vs RAG"的差异分析**。
- 本 draft 由 Anthem Création 法语指南 §"LLM wiki vs. RAG" 抽取，主题是"差异不在速度，在推理深度"+ 五维对比表 + multi-hop 自然性 + 适用规模 10–几百篇 + 混合方向。

主题完全不重叠。

## 2. draft 与候选在哪里不同

- **事实类型不同**：v2 三张是 `known_fact`；draft 是 `distinction`，承担"wiki vs RAG"的对比类知识。
- **来源不同**：v2 来源 Karpathy gist；draft 来源 Anthem Création 法语指南 §"LLM wiki vs. RAG"（独立二手综述）。
- **覆盖维度全新**：五维对比表（时机 / 单位 / 矛盾处理 / 推理深度 / 适用规模）+ "La différence fondamentale n'est pas la vitesse, c'est la profondeur du raisonnement" 关键句 + multi-hop 跨三个概念联接 + 10–几百篇规模区间 + "L'hybridation RAG-vector"演化方向 —— 都不在 v2 任何卡片中。
- **decisional framing 不同**：draft 给出 if-then 选型建议（个人 + 几十-几百篇 + 跨概念推理 → wiki / 千万级文档 + 偶发查询 → RAG / 团队企业级 → 混合）。

不是 v2 卡片的扩展，是**全新的 distinction 类卡**。

## 3. 下一步的核心依据

- 不是 `merge_candidate` / `provenance_delta`：v2 没有 wiki vs RAG 任何内容，找不到合并 / 补强对象。
- 不是 `duplicate_skip`：完全未被 v2 覆盖。
- 不是 `revise_before_gate`：draft 证据扎实（对比表五维都对应原文行号 152–162）、scope 清晰、边界（个人规模 / 弱 LLM 风险 / 无官方实现）都标注。

正确决定是 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：走 publication_gate；audit 阶段建议与同 batch 的 `karpathy-llm-wiki-vs-rag` 与 `hn-llm-wiki-is-just-rag-debate` 形成"wiki vs RAG 三视角"簇；与 v2 `auto-index-replaces-rag-at-small-scale`（若存在）通过 related 互链。

## 5. 备注

- 本 batch 内有三张关于"wiki vs RAG"的 draft（karpathy-llm-wiki-vs-rag 偏 paradigm 区分、本卡偏推理深度/适用区间、hn-llm-wiki-is-just-rag-debate 偏争论综述）——三者视角不同，建议保留三张独立卡而非合并。
- draft 与同源的 `anthemcreation-llm-wiki-three-layer-architecture` / `anthemcreation-llm-wiki-setup-cost-envelope` 形成同源三张卡组合（架构 + setup + vs RAG），audit 可考虑共同挂在"Anthem Création 法语指南"导览卡下。
