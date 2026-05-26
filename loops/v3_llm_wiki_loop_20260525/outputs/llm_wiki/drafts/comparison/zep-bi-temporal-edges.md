---
schema: comparison_provenance.v3
draft_card: ../cards/zep-bi-temporal-edges.md
draft_provenance: ../provenance/zep-bi-temporal-edges.md
similarity_result: ../similarity/zep-bi-temporal-edges.json
existing_cards:
  - card_id: raw-sources-readonly-source-of-truth
    card_path: llm_wiki/kb/cards/raw-sources-readonly-source-of-truth.md
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

similarity 中 top 1 的 0.05 来自共享 token `事实`：draft "...让**事实**'会过期'..."，候选 "Raw sources 是只读**事实**来源"。top 2/3 分数 0.0 占位。

## 2. draft 与候选在哪里不同

- draft 描述 Zep/Graphiti 的 **bi-temporal 边失效机制**：事务时间轴 $T'$ ($t'_\text{created}/t'_\text{expired}$) 与事件时间轴 $T$ ($t_\text{valid}/t_\text{invalid}$) 分离；相对时间统一抽取；新边触发 LLM 比较把旧边的 $t_\text{invalid}$ 设为新边的 $t_\text{valid}$（事实失效而非覆盖）；prompt 模板中的 "Date range: from - to" 槽位；弱模型对时间数据理解局限。来源 `arxiv-zep`。
- top 1 `raw-sources-readonly-source-of-truth`：Karpathy gist 中 Raw sources 层是只读、用户策展的事实来源。这里"事实"指文档级 source of truth；draft 中"事实"指 graph edge 上的 atomic fact 三元组。含义层级完全不同。
- 论点轴（时序知识图 fact invalidation vs 文档层 source of truth）、来源、机制完全不重叠。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自 `事实` 同形，主题层零交集。判 `new_card`：直接走 publication_gate。draft 含双时间线定义、失效机制流程、prompt 模板槽位与弱模型局限，发表条件齐备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

`事实` 在 Karpathy "source of truth" 与 Zep "atomic fact triple" 两个语境里所指对象差异极大，是典型同形误中。
