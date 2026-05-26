---
schema: comparison_provenance.v3
draft_card: ../cards/etamp-long-context-recall-diagnostic.md
draft_provenance: ../provenance/etamp-long-context-recall-diagnostic.md
similarity_result: ../similarity/etamp-long-context-recall-diagnostic.json
existing_cards:
  - card_id: rag-document-qa-does-not-accumulate-synthesized-knowledge
    card_path: llm_wiki/kb/cards/rag-document-qa-does-not-accumulate-synthesized-knowledge.md
    score: 0.0556
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0
  - card_id: idea-file-share-the-idea
    card_path: llm_wiki/kb/cards/idea-file-share-the-idea.md
    score: 0.0
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 中 top 1 的 0.0556 完全来自共享 token `不`（draft "召**不**回 / **不**服从"，候选 "**不**积累综合知识"）。top 2/3 分数 0.0 占位。这是中文否定副词同形的低分误中。

## 2. draft 与候选在哪里不同

- draft 描述 eTAMP Appendix F 的 long-context recall 诊断：用 recall rate 区分"low ASR + low recall = incidental defense" vs "low ASR + high recall = intentional resistance"，含 5 个模型在 ~282 条 trajectory 上的数据表（GPT-OSS-120B 6.7% 到 GPT-5.2/Qwen 100%），来源 `arxiv-etamp-memory-poisoning`。
- top 1 `rag-document-qa-does-not-accumulate-synthesized-knowledge` 论 Karpathy gist 中的 RAG 局限：跨 query 不积累综合知识。
- 两者唯一共享是中文否定词 `不`；论点轴（安全评测诊断 vs 知识积累局限）、来源（arxiv vs gist）、机制完全不同。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自 `不` 同形，无实质交集。判 `new_card`：直接走 publication_gate。draft 含诊断方法、数据表、解读规则、边界与操作含义，发表条件齐备。不是 `provenance_delta`——v2 RAG 卡 scope 与 long-context safety 评测无交集。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

无；典型 token 同形误中。
