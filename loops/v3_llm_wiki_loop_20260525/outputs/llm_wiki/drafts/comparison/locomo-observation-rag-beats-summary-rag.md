---
schema: comparison_provenance.v3
draft_card: ../cards/locomo-observation-rag-beats-summary-rag.md
draft_provenance: ../provenance/locomo-observation-rag-beats-summary-rag.md
similarity_result: ../similarity/locomo-observation-rag-beats-summary-rag.json
existing_cards:
  - card_id: rag-document-qa-does-not-accumulate-synthesized-knowledge
    card_path: llm_wiki/kb/cards/rag-document-qa-does-not-accumulate-synthesized-knowledge.md
    score: 0.05
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

similarity 中 top 1 的 0.05 来自共享 token `rag`：draft "**RAG** 检索单元..."，候选 "**RAG** 式文档问答不积累综合知识"。top 2/3 分数 0.0 占位。两者主题家族确实在"RAG"范围内，但论点轴不同。

## 2. draft 与候选在哪里不同

- draft 是 operational_rule 卡：在 LoCoMo 上对比 3 种检索单元（dialog/observation/session summary）在 gpt-3.5-turbo-16k 作 reader 时的 F1 表现；observation top-5 拿 41.4 最高，sumary top-5 只有 32.5；并给出"observation 不是越多越好（5→50 反降）"、"summary 看 recall 高但 QA 差"等 4 条操作含义与 2 条边界。来源 `arxiv-locomo`。
- top 1 `rag-document-qa-does-not-accumulate-synthesized-knowledge`：Karpathy gist 对 RAG 模式"不在 query 之间积累综合知识"的对比性描述，是 known_fact 卡。
- 论点轴完全不同：候选谈"RAG 是什么 / 不积累知识"；draft 谈"RAG 内部的检索单元粒度怎么选"。

## 3. 下一步的核心依据

(1) 与 (2) 表明 jaccard 来自 `rag` 这一通用缩写，主题相邻但 scope 不同。判 `new_card`：直接走 publication_gate。draft 含完整粒度对比表、操作规则与边界，发表条件齐备。不是 `provenance_delta` —— Karpathy 的 RAG 描述卡 scope 限定为该 gist 的对比性描述，不允许吸纳 LoCoMo 的 retrieval ablation 作为证据。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

`rag` 是高频缩写，跨主题 jaccard 命中风险大；本卡是典型例子。
