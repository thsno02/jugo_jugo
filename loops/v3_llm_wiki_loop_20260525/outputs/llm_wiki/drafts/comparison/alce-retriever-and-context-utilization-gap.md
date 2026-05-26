---
schema: comparison_provenance.v3
draft_card: ../cards/alce-retriever-and-context-utilization-gap.md
draft_provenance: ../provenance/alce-retriever-and-context-utilization-gap.md
similarity_result: ../similarity/alce-retriever-and-context-utilization-gap.json
existing_cards:
  - card_id: llm-wiki-query-answer-writeback
    card_path: llm_wiki/kb/cards/llm-wiki-query-answer-writeback.md
    score: 0.1111
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1111
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- 候选 #1 `llm-wiki-query-answer-writeback`：共享 `好`、`答案` 两个普通词（draft 标题里"passage 越多不等于答案越好"撞上候选的"回写好答案"）。机械撞分，论点无重叠。
- 候选 #2 `llm-wiki-three-layer-architecture`：共享 `llm`、`的`。无主题重叠。
- 候选 #3 `llm-wiki-schema-configuration-document`：共享 `llm`、`的`。无主题重叠。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-query-answer-writeback`：仅记录 Karpathy gist 第 39–40 行对 Query 操作把好答案回写 wiki 的事实。和 ALCE 的 retrieval recall vs context utilization 实证分析无关。
- 候选 #2、#3：Karpathy gist 的架构与 schema 配置事实卡，无 retrieval/benchmark 维度。
- draft 来源是 `arxiv-alce` 论文，论点轴是"ALCE retrieval 表 + context utilization gap"——含具体 R@k 表（ASQA 上 GTR R@5=56.8、ELI5 BM25 R@100=31.8 等）与 ChatGPT/ChatGPT-16K/GPT-4 不同 passage 数对比表，给出"retrieval 是天花板 / context 限制 / synthesize 能力本身有限"三大挑战。v2 KB 中无 ALCE 卡或 retrieval benchmark 卡。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无 ALCE / retrieval-benchmark 系列卡。
- 不是 `provenance_delta`：候选 #1 是 wiki query 操作事实，与 retrieval recall 论证没有对接面。
- 不是 `duplicate_skip`：无重叠。
- 不是 `revise_before_gate`：draft 已有完整 retrieval recall 表、ChatGPT/16K/GPT-4 对比表、oracle vs vanilla 对比、三条挑战与论文行号锚（results.tex L1428/L1513/L1156 等）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控可核 `tables/asqa_different_llms.tex` 数字与 draft 表是否逐行对齐。

## 5. 备注

- 与 draft 自身 related 列出的 `alce-three-dimension-citation-metric`、`alce-prompting-strategies` 同源系列卡共同覆盖 ALCE 论文不同切面。
- 同批次 `alce-prompting-strategies` 也属同源系列。
