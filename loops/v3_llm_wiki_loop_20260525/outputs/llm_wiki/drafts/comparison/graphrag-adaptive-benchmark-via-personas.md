---
schema: comparison_provenance.v3
draft_card: ../cards/graphrag-adaptive-benchmark-via-personas.md
draft_provenance: ../provenance/graphrag-adaptive-benchmark-via-personas.md
similarity_result: ../similarity/graphrag-adaptive-benchmark-via-personas.json
existing_cards:
  - card_id: llm-wiki-wiki-layer-generated-markdown-directory
    card_path: llm_wiki/kb/cards/llm-wiki-wiki-layer-generated-markdown-directory.md
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

similarity 中 top 1 的 0.0556 完全来自共享 token `生成`：draft 标题 "...自适应**生成**全局意义建构基准"，候选 "Wiki 层由 LLM **生成**和维护"。top 2/3 分数 0.0 占位。

## 2. draft 与候选在哪里不同

- draft 描述 GraphRAG 论文为全局意义建构评测设计的协议：`persona × task × question` 自适应出题（K=M=N=5 → 125 题/dataset）、四维 LLM-as-judge 头对头比较（含反向控制 directness）、Claimify 47,075 条 claim 做交叉验证（78% / 69–70% 一致率）。来源 `arxiv-graphrag`。
- top 1 `llm-wiki-wiki-layer-generated-markdown-directory`：Karpathy LLM Wiki 的 wiki 层定义——LLM 生成 markdown 目录、维护交叉引用。
- 两者都谈"生成"，但 draft 的"生成"是 LLM 出评测题，候选的"生成"是 LLM 写 wiki 页面；机制（adaptive benchmarking + LLM-judge vs markdown 维护）、来源完全不同。

## 3. 下一步的核心依据

(1) 与 (2) 表明 jaccard 来自 `生成` 同形，无主题交集。判 `new_card`：直接走 publication_gate。draft 含三块协议（adaptive question gen / LLM-as-judge / claim-based 验证）、四指标定义、反向控制原理与一致率数字，发表条件齐备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

`生成` 是 LLM 文献的高频 token，跨主题误中风险大；这是又一例。
