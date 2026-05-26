---
schema: comparison_provenance.v3
draft_card: ../cards/retrieval-not-enough-for-stale-kb.md
draft_provenance: ../provenance/retrieval-not-enough-for-stale-kb.md
similarity_result: ../similarity/retrieval-not-enough-for-stale-kb.json
existing_cards:
  - card_id: llm-wiki-query-answer-writeback
    card_path: llm_wiki/kb/cards/llm-wiki-query-answer-writeback.md
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

similarity 中 top 1 的 0.0556 来自共享 token `答案`：draft 标题 "...更快地给出错**答案**"，候选 "Query 操作回写好**答案**"。top 2/3 分数 0.0。**主题层面**两者都触及 Karpathy LLM Wiki 范式：候选讲 Karpathy gist 中的 query 操作流程；draft 引用 Karpathy 作为"维护循环"的范式参考，论 Falconer 的"better retrieval over bad context delivers wrong answers more quickly"。

## 2. draft 与候选在哪里不同

- draft 是 distinction 卡，论 **检索层 vs 维护循环的功能边界**：Glean/Notion AI/Confluence AI search 等检索改进不解决底层 doc 的 freshness 问题；Falconer 把 Karpathy LLM Wiki 列为"维护循环"范式的对照；含 4 条规则、操作含义（评估 KB 产品时分问"如何查 / 如何保证 current"）、3 条边界（不是说 retrieval 没用 / 维护成本必须存在 / agent 消费风险被放大）。来源 `falconer-enterprise-guide`。
- top 1 `llm-wiki-query-answer-writeback` 是 Karpathy gist 中 query 操作的描述：LLM 搜 wiki、读页面、综合带引用答案，并把好答案回写 wiki。来源 `karpathy-gist`，scope 严格限定为该来源对 query 操作的描述。
- 两者论点轴不同：候选是"query 操作怎么工作"的 known_fact；draft 是"为什么 retrieval 不能取代维护循环"的 distinction，并把 Karpathy 模式当成 contrast point 而非主体。

## 3. 下一步的核心依据

(1) 与 (2) 表明 jaccard 仅由 `答案` 触发，主题相邻但 scope 完全错位。判 `new_card`：直接走 publication_gate。不是 `provenance_delta`，因为候选 v2 卡的 scope 限定在 Karpathy gist 对 query 操作的描述，不允许吸纳 Falconer 的 enterprise-level distinction 作为延伸证据；这条 distinction 应作为独立 distinction 卡。不是 `revise_before_gate`，draft 论点轴清晰，含 verbatim 引文、4 条规则、操作含义和边界。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate；在 related 字段链接 v2 `llm-wiki-query-answer-writeback` 与 `llm-wiki-wiki-layer-generated-markdown-directory`（同属"Karpathy 维护循环"主题家族）。

## 5. 备注

主题相邻但 scope 错位的典型案例：draft 用 Karpathy 模式作对照点，v2 候选描述 Karpathy 模式本身。两者互补但不合并。
