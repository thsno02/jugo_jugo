---
schema: comparison_provenance.v3
draft_card: ../cards/alce-three-dimension-citation-metric.md
draft_provenance: ../provenance/alce-three-dimension-citation-metric.md
similarity_result: ../similarity/alce-three-dimension-citation-metric.json
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
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft 之间 **token 共享为零**（`shared_tokens: []`），similarity 分数全部为 0.000。三个候选都是从同一条 Karpathy "llm wiki" launch 推文里抽出的 known_fact 卡：分别讲 `idea file` 的"刻意保持抽象"、`idea file` 是 LLM agents 时代的分享形式、以及 LLM 对 wiki 跑 `health checks`。它们之所以被算进 top 3，仅仅因为 jieba 分词后这是 v2 全 15 张卡里"反正得排前几名"的兜底——它们与 draft 之间没有任何主题邻近。

## 2. draft 与候选在哪里不同

- draft 主题：ALCE benchmark 的三维度评分（fluency / correctness / citation quality）以及"互相牵制堵作弊路径"机制；论据轴是 RAG 自动评测、NLI judge、MAUVE 截断、citation recall/precision 上限。
- 候选 1 (`idea-file-abstract-vague`)：Karpathy 推文对 `idea file` 描述"抽象、可被他人 agent 调整"。论据轴是社交媒体帖文叙述，没有任何评测、citation、benchmark 内容。
- 候选 2 (`idea-file-share-the-idea`)：同一推文对"分享想法 vs 分享代码"的论述，与 RAG 评测无关。
- 候选 3 (`llm-wiki-health-checks`)：LLM 对 wiki 跑健康检查找不一致数据等，是 wiki 维护场景，不是带引用问答的评测。

draft 与三个候选位于完全不重叠的语义域：**RAG 带引用评测 vs Karpathy llm-wiki 概念帖文**。既不是"v2 卡片的扩展"，也不是"同主题不同视角"，更不是同一作者不同时间点。

## 3. 下一步的核心依据

(1) token 完全不共享 + (2) v2 候选体内容确属 Karpathy 推文域，与 ALCE 评测无任何重叠 → 结论是 `new_card`。为什么不是 `revise_before_gate`：draft 本身已经把三维度定义、互锁机制、自动评估准确率、边界都说清并直接对应 `evaluation.tex` 行号 + Footnote 原文 quote；没有缺信息 / 边界 / 证据问题。为什么不是 `provenance_delta`：v2 没有任何邻近卡可"反向链接进 provenance"，没有可加的证据轴。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate，按 ALCE 主题独立 adopt。

## 5. 备注

v2 候选纯属 jieba 兜底排序；不构成实质邻近。v2 KB 目前完全没有 RAG benchmark / 带引用评测主题，本 draft 是首张该域卡。
