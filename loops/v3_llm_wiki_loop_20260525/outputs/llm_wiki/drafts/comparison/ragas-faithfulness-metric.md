---
schema: comparison_provenance.v3
draft_card: ../cards/ragas-faithfulness-metric.md
draft_provenance: ../provenance/ragas-faithfulness-metric.md
similarity_result: ../similarity/ragas-faithfulness-metric.json
existing_cards:
  - card_id: llm-wiki-human-llm-role-division
    card_path: llm_wiki/kb/cards/llm-wiki-human-llm-role-division.md
    score: 0.0588
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0556
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.0556
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

Similarity JSON 列出 top 1 与 draft 仅共享 `llm` 一个 token，分数 0.0588 完全来自 `llm` 这个高频缩写在两侧标题中同时出现：draft 标题里有 "LLM 验证"，候选标题 "人提问，LLM 维护" 中也有 "LLM"。top 2、top 3 命中同样只靠 `llm`。这是典型的 jaccard 误中——没有任何实质性主题共享。

## 2. draft 与候选在哪里不同

- draft 描述的是 **Ragas Faithfulness 指标的算法**：两步 prompt（statement decomposition + verification）、公式 F = |V|/|S|、WikiEval 上 0.95 一致率、以及"context 本身错则识别失败"等边界。来源是 `arxiv-ragas` 论文。
- top 1 `llm-wiki-human-llm-role-division` 谈的是 Karpathy LLM Wiki 中人与 LLM 的角色分工（人策展来源、LLM 写作维护），来源是 `karpathy-gist`。
- top 2 `llm-wiki-health-checks` 与 top 3 `llm-wiki-listed-use-cases` 同样属于 Karpathy LLM Wiki 架构卡，与 RAG 评估指标算法毫无交叉的论点轴、机制、来源类型。

## 3. 下一步的核心依据

(1) 与 (2) 共同指出，draft 与所有 top 3 候选在主题、来源、机制层面均不相交，分数完全由通用 token `llm` 造成。因此应判 `new_card`：直接走 publication_gate。这不是 `revise_before_gate`，因为 draft 已具备完整公式、prompt 引文、实证数字与边界声明；也不是 `provenance_delta`，因为没有任何 v2 卡片需要从这条 draft 中吸纳新证据。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

无；jaccard 误中纯粹由 `llm` 这一通用 token 引起。
