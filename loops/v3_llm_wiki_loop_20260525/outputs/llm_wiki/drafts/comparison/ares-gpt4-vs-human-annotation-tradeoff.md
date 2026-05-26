---
schema: comparison_provenance.v3
draft_card: ../cards/ares-gpt4-vs-human-annotation-tradeoff.md
draft_provenance: ../provenance/ares-gpt4-vs-human-annotation-tradeoff.md
similarity_result: ../similarity/ares-gpt4-vs-human-annotation-tradeoff.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0556
  - card_id: llm-wiki-persistent-wiki-alternative-mode
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md
    score: 0.0556
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0526
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 显示 top 1 与 top 3 共享 `的`，top 2 共享 `替代`（draft 标题 "GPT-4 标注**替代** human preference set"，候选 "持久 wiki **替代**模式"）。分数 0.0556 完全来自这种通用 token 同形，没有任何主题层共享。

## 2. draft 与候选在哪里不同

- draft 是 ARES 论文的**消融实验**：用 500 条 GPT-4 标注代替 human preference validation set，导致 Kendall's τ 下降 0.05–0.30 的成本/精度权衡，含 NQ/ReCoRD/MultiRC 三数据集的具体数字与 PPI 行为。来源 `arxiv-ares`。
- top 1 `idea-file-abstract-vague`：Karpathy idea file 的抽象性设计取向。
- top 2 `llm-wiki-persistent-wiki-alternative-mode`：Karpathy wiki 中"持久 wiki 替代模式"——这里的 "替代" 是 wiki vs RAG 模式的替代，与 draft 的 "GPT-4 替代人工标注" 完全不同语义。
- top 3 `llm-wiki-three-layer-architecture`：架构层定义。
- 三者均与 RAG 评估指标判官的标注成本权衡无任何论点轴、机制、来源类型重叠。

## 3. 下一步的核心依据

(1) 与 (2) 表明这是 `的` / `替代` 等高频 token 触发的低分误中。判 `new_card`。draft 含完整数字表、机制解释、操作建议与诚实边界，已具发表条件。不是 `provenance_delta`——三张 v2 卡的 scope 与本卡完全互斥。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

`替代` 是中文动词常用词，在不同语境下指代完全不同的替换关系，是 jaccard 的弱区分性导致的同形误中。
