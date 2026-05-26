---
schema: comparison_provenance.v3
draft_card: ../cards/graphrag-pipeline-formalism.md
draft_provenance: ../provenance/graphrag-pipeline-formalism.md
similarity_result: ../similarity/graphrag-pipeline-formalism.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1538
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1333
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0769
decision: new_card
audit_required: false
created_time: 2026-05-26T12:26:00+08:00
edited_time: 2026-05-26T12:26:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top1/top2 共享 `llm`、`的`，top3 只共享 `的`。draft 的核心词 `GraphRAG`、`chunk`、`流水线`、`形式化` 在三张候选中都没出现。所有共享 token 全是高频功能词，jaccard 0.1538 / 0.1333 / 0.0769 都属典型低分批 + 功能词撞分；候选与 draft 主题在领域上无任何交集。

## 2. draft 与候选在哪里不同

- **领域不同**：本 draft 取自 `arxiv-graph-poisoning`（学术论文，关于 GraphRAG 投毒攻击），与 v2 候选（karpathy LLM Wiki / 个人知识库）领域无关。
- **类型不同**：本 draft 是 concept 卡，给出 GraphRAG 流水线的五步形式化（chunks → $f_{\text{extract}}$ → $G_{\text{merged}}$ → $f_{\text{community}}$ + 摘要 → $g_{\text{retrieve}}$ + $\text{LLM}(Q, S_{\text{rel}})$），并据此推出三个 chunk-RAG 没有的结构性质（LLM 视野是摘要不是 chunk、构图阶段是"信任放大器"、图持久化使少量改动撬动全系统）。v2 候选都是 LLM Wiki 相关 known_fact，论点轴完全无交集。
- top1 `three-layer-architecture` 谈 raw/wiki/schema；与 GraphRAG 流水线无关。
- top2 `schema-configuration-document` 谈 karpathy schema 角色；无关。
- top3 `idea-file-abstract-vague` 谈 idea file 抽象性；无关。
- 数学符号（$f_{\text{extract}}$ / $f_{\text{community}}$ / $g_{\text{retrieve}}$ / $\text{Answer}=\text{LLM}(Q, S_{\text{rel}})$）和 "manipulation-only" 攻击面在 v2 KB 完全没有。

## 3. 下一步的核心依据

(1) 三张候选都不覆盖 GraphRAG；(2) draft 来源是 v2 KB 完全未涉的学术论文；(3) concept 卡含完整证据链（论文 L263–275 形式化、L178–185 与传统 RAG 三类攻击对比、L283–287 攻击者能力假设）。结论是 `new_card`。

不是 `provenance_delta`：draft 与 v2 任一卡都无证据补充关系。不是 `merge_candidate`：v2 没有 GraphRAG / 知识图 / pipeline formalism 任何相关卡可合并。不是 `revise_before_gate`：边界明确（实现差异、低层查询会回退、不要外推为通用"图 + 检索"定义），证据全部引到论文行号。不是 `duplicate_skip`：v2 完全无同主题。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；建议在 sources 索引加入 `arxiv-graph-poisoning`；与同源兄弟卡 `graphrag-manipulation-only-attack-surface`（如已存在）做 related 互链作"机制 → 攻击面"链路。

## 5. 备注

- "信任放大器"是本卡对论文论点的提炼措辞，原文未用此词，draft prov 已显式标注；编辑/审稿可视情况保留。
- 本卡为 v3 中第一张 GraphRAG 主题卡，可作为该主题的入口；如未来 v2/v3 引入"图 + 检索"通用范式卡，应对 scope 做明确切分。
