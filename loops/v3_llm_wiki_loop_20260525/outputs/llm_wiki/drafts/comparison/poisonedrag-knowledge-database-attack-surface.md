---
schema: comparison_provenance.v3
draft_card: ../cards/poisonedrag-knowledge-database-attack-surface.md
draft_provenance: ../provenance/poisonedrag-knowledge-database-attack-surface.md
similarity_result: ../similarity/poisonedrag-knowledge-database-attack-surface.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1333
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0769
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0714
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

shared token 只有 `的`、`是`：典型 jaccard 在中文小池子里的高频虚词撞分。draft 的核心 token `RAG`、`攻击面`、`知识库`、`投毒` 等没有任何候选覆盖。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-schema-configuration-document`：仅记录 Karpathy gist 中 schema 是配置文档这一事实。和 RAG 安全/投毒攻击面无任何关系。
- 候选 #2 `idea-file-abstract-vague`：idea file 抽象性事实。无关。
- 候选 #3 `llm-wiki-three-layer-architecture`：Karpathy gist 三层架构。无关。
- draft 来源是 `arxiv-poisonedrag` 论文，论点轴是"RAG 知识库本身构成一个新的攻击面"，含具体数字（5/2,681,468 → 97% ASR）、跨 LLM 与跨 retriever 的稳定性、附带影响极低。这属于 RAG 安全研究维度，v2 KB（Karpathy gist 个人 wiki 视角）完全没有此类卡。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无 RAG 安全/投毒系列。
- 不是 `provenance_delta`：候选都是 Karpathy gist 元事实，与 PoisonedRAG 论点轴无对接面。
- 不是 `duplicate_skip`：无重叠。
- 不是 `revise_before_gate`：draft 已有威胁模型描述、四组数字、跨模型/跨 retriever 稳定性、操作启示与论文锚句；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；建议门控阶段核对 ASR 数字与论文 Table 是否逐字对齐（尤其 Table `tab:ablation-llm-tmp-results` 的多模型行）。

## 5. 备注

- 与 draft 自身 related 列出的 `poisonedrag-retrieval-generation-two-conditions` 构成"攻击面 + 攻击条件"双卡。
- jaccard 0.1333 由 `是 / 的` 两个虚词产生，本质是中文 jieba 分词下不可避免的低分误中。
