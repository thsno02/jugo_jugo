---
schema: comparison_provenance.v3
draft_card: ../cards/ragas-context-relevance-metric.md
draft_provenance: ../provenance/ragas-context-relevance-metric.md
similarity_result: ../similarity/ragas-context-relevance-metric.json
existing_cards:
  - card_id: llm-wiki-human-llm-role-division
    card_path: llm_wiki/kb/cards/llm-wiki-human-llm-role-division.md
    score: 0.0714
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0667
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.0667
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.08，shared_tokens 仅为「llm」一词（任何提到 LLM 的卡都会共享）。draft 标题的实质 token（Ragas / Context Relevance / crucial / 句子 / 占比）与 v2 候选（Karpathy LLM-wiki 元描述）无术语级重合。属于 jaccard 噪声且 LLM 一词在两端语义指向完全不同。

## 2. draft 与候选在哪里不同

draft 是 mechanism 卡，来源 `arxiv-ragas`，论述 Ragas Context Relevance 指标的算法（LLM prompt 抽取 crucial 句子 → 子集大小 / 总句数）、设计要点（不改写抽取、Insufficient Information 出口、方向解读）、与 lost-in-the-middle 的关联、WikiEval 上 0.70 一致率与已知弱点。属于「RAG 评估指标设计」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述（人 LLM 分工、health checks、use case 清单）。论点轴（评估指标算法 vs 个人 LLM wiki 模式）、来源、机制完全不同。

## 3. 下一步的核心依据

shared_tokens 仅是「llm」（语义飘移），无实质关联。v2 候选 scope 限于 Karpathy 来源，无法承载 Ragas 论文的算法定义。draft 引文具体到 L172-182 / L238-244 / L271 / L120，scope 自洽。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `ragas-reference-free-rag-evaluation` / `ragas-faithfulness-metric` / `ragas-answer-relevance-metric` 同 source 互引。
