---
schema: comparison_provenance.v3
draft_card: ../cards/wicer-recovery-distribution-exceeds-fc-raw.md
draft_provenance: ../provenance/wicer-recovery-distribution-exceeds-fc-raw.md
similarity_result: ../similarity/wicer-recovery-distribution-exceeds-fc-raw.json
existing_cards:
  - card_id: raw-sources-readonly-source-of-truth
    card_path: llm_wiki/kb/cards/raw-sources-readonly-source-of-truth.md
    score: 0.0588
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

similarity JSON 显示 top 1 的 0.0588 完全来自 `raw` 这一 token 的共享：draft 标题里有 "FC raw"（baseline 名），候选标题 "Raw sources 是只读事实来源" 里也含 `raw`。top 2/3 分数 0.0；它们出现在列表里只是因为 v2 KB 仅 15 张卡，函数仍要补足 top 3。完全是 token 同形误中。

## 2. draft 与候选在哪里不同

- draft 是 WiCER 论文 §6.4 的实证结果卡：在 RepLiQA 17 个主题上，recovery 分布跨度 0–125%，有 3 个主题（news_stories 101% / local_arts_and_culture 116% / small_and_medium_enterprises 125%）在两次迭代后超过 FC raw 基线；并解释为 entity-dense 语料上"压缩 + pinning 抵消 lost-in-the-middle"的机制。
- top 1 `raw-sources-readonly-source-of-truth`：Karpathy LLM Wiki 架构里 "Raw sources" 层是只读、用户策展的事实来源。论 "raw sources" 是层定义；draft 论 "FC raw" 是 RAG 基线方法。同字面 `raw`，完全不同含义。
- top 2/3 是 idea file 主题，与 WiCER 实证结果完全无关。

## 3. 下一步的核心依据

(1) 与 (2) 表明 draft 与所有候选在主题（架构定义 vs 实验数据）、来源（gist vs arxiv-wicer）、论点轴上零交集，分数完全来自同形 token `raw`。判 `new_card`：直接走 publication_gate。draft 已含完整表格、原文引用、机制解释与适用条件，不需 `revise_before_gate`；没有 v2 卡需被反向链接，不需 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

经典 token 同形假阳：`raw` 在两个语境里指代完全不同的概念（Karpathy 架构层名 vs RAG baseline 缩写）。
