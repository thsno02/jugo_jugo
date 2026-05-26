---
schema: comparison_provenance.v3
draft_card: ../cards/graphrag-context-window-8k-optimal.md
draft_provenance: ../provenance/graphrag-context-window-8k-optimal.md
similarity_result: ../similarity/graphrag-context-window-8k-optimal.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0
  - card_id: idea-file-share-the-idea
    card_path: llm_wiki/kb/cards/idea-file-share-the-idea.md
    score: 0.0
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0
decision: new_card
audit_required: false
created_time: 2026-05-26T16:07:00+08:00
edited_time: 2026-05-26T16:07:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft 标题"GraphRAG 用 8K 上下文窗口反而压过 16K/32K/64K——"小窗口"更全" **无 token 共享，score 全部 0.000**。它们出现在 top 3 是因为 v2 KB 仅有 15 张卡，算法必须返回 3 个候选。三个候选均来自同一条 Karpathy "llm wiki" launch 推文。

## 2. draft 与候选在哪里不同

- draft 主题：GraphRAG 论文 Appendix C 的 context window ablation——8K 在 comprehensiveness / diversity / empowerment 上都最优，论据轴是 map-reduce sensemaking pipeline + lost-in-the-middle 现象。
- 候选 1：Karpathy 推文对 idea file "抽象性"的描述。
- 候选 2：同推文对 idea file 分享逻辑的描述。
- 候选 3：LLM 对 wiki 跑 health checks 清理数据。

draft 完全在 RAG 评测 / 长上下文注意力领域；三个候选完全在 Karpathy llm-wiki 概念帖文领域。没有共享主张、没有共享术语、没有共享底层 source。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 完全无 GraphRAG / context window / sensemaking 相关内容 → `new_card`。draft 自带胜率表、行号引用、Lost-in-the-middle 引用、边界说明（gpt-4-turbo 特定 + 不覆盖长引用任务），证据完整 → 不是 `revise_before_gate`。v2 无任何 RAG / GraphRAG 邻近卡可反向链接 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；同 GraphRAG 系列其它 draft（`graphrag-root-community-token-efficiency`、`graphrag-global-sensemaking-pipeline` 等）在 v3 related 字段挂连。

## 5. 备注

v2 KB 尚无任何 GraphRAG / 全局 sensemaking RAG 主题，本 draft 系该域首批。
