---
schema: comparison_provenance.v3
draft_card: ../cards/ragas-answer-relevance-metric.md
draft_provenance: ../provenance/ragas-answer-relevance-metric.md
similarity_result: ../similarity/ragas-answer-relevance-metric.json
existing_cards:
  - card_id: llm-wiki-human-llm-role-division
    card_path: llm_wiki/kb/cards/llm-wiki-human-llm-role-division.md
    score: 0.0625
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0588
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.0588
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选都是 Karpathy LLM Wiki gist 卡，共享 token 应当限于 `llm` / `回答` / `问题` 等通用词。Ragas / Answer Relevance / ada-002 / WikiEval / Faithfulness 等关键概念在 v2 不出现。

## 2. draft 与候选在哪里不同

draft 描述 Ragas 的 Answer Relevance：用 LLM 仅看 answer 反推 n 条 question，用 `text-embedding-ada-002` 计算与原 question 余弦相似度并取均值。给出 WikiEval 一致率 0.78、AR 与 Faithfulness 联用必要性、embedding 选型对绝对分的影响等边界。

v2 候选：top 1 是 Karpathy gist 的人/LLM 分工；top 2 是 LLM 跑 health checks 清理 wiki；top 3 是 LLM Wiki 应用场景清单。三者无任何 RAG 评估指标、embedding 相似度、reverse prompt 概念。

## 3. 下一步的核心依据

(1) (2) 共同表明无重叠。draft 完整。结论 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 RAG 评估指标簇（RAGChecker、ARES、ALCE）互相 cite。

## 5. 备注

无。
