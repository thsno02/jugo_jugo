---
schema: comparison_provenance.v3
draft_card: ../cards/longmemeval-time-aware-query-expansion.md
draft_provenance: ../provenance/longmemeval-time-aware-query-expansion.md
similarity_result: ../similarity/longmemeval-time-aware-query-expansion.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0526
  - card_id: llm-wiki-query-answer-writeback
    card_path: llm_wiki/kb/cards/llm-wiki-query-answer-writeback.md
    score: 0.05
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.05
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 中 top 1 与 top 3 共享 `的`，top 2 共享 `query`（draft "**query** 扩展" vs 候选 "**Query** 操作回写好答案"）。分数 ≤0.0526，完全来自通用 token 同形。

## 2. draft 与候选在哪里不同

- draft 描述 LongMemEval §5.3 的 **时间感知双侧改造**：indexing 侧让 LLM $\mathcal{M}_T$ 抽 (date, event) 写入平行 index；retrieval 侧让 $\mathcal{M}_T$ 从带时间引用的 query 推断 `{start, end}` 区间做过滤；recall 平均 +11.3% / +6.8%；边界是必须用 GPT-4o 这类强 LLM 才能 N/A 拒答（Llama 3.1 8B 会 false-positive）。来源 `arxiv-longmemeval`。
- top 1 `idea-file-abstract-vague`：Karpathy idea file 抽象性。
- top 2 `llm-wiki-query-answer-writeback`：Karpathy gist 中 query 操作的 known_fact。这里的 query 是 "用户对 wiki 提问" 的概念；draft 中的 query 是 "RAG 评测里的查询" 的具体技术对象。
- top 3 `llm-wiki-three-layer-architecture`：架构定义。
- 论点轴（temporal RAG 召回机制 vs Karpathy 概念定义）、来源（arxiv vs gist）、机制完全不同。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自 `的` / `query` 同形，无主题交集。判 `new_card`：直接走 publication_gate。draft 含完整双侧机制、recall 增益数字、强弱 LLM 对比与"何时不应启用过滤"的边界，发表条件齐备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

`query` 在 RAG 文献与 Karpathy gist 中都是高频词，又是一例同形误中。
