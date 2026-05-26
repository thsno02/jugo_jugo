---
schema: comparison_provenance.v3
draft_card: ../cards/poisonedrag-survives-advanced-rag-and-agents.md
draft_provenance: ../provenance/poisonedrag-survives-advanced-rag-and-agents.md
similarity_result: ../similarity/poisonedrag-survives-advanced-rag-and-agents.json
existing_cards:
  - card_id: llm-wiki-human-llm-role-division
    card_path: llm_wiki/kb/cards/llm-wiki-human-llm-role-division.md
    score: 0.0667
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0625
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.0625
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选都在 0.062–0.067 区间，token 共享应该集中在 `llm` / `agent` 这类泛用词。`llm-wiki-human-llm-role-division` 出现"LLM"和"角色"等通用词，`llm-wiki-health-checks` 也有"LLM"，`llm-wiki-listed-use-cases` 同样是 LLM Wiki 概念语料。没有任何 token 跟 PoisonedRAG / Self-RAG / CRAG / Wikipedia ChatBot / ReAct 等关键概念对应。

## 2. draft 与候选在哪里不同

draft 总结的是 PoisonedRAG 论文在四组"现实化"实验上的鲁棒性证据：Self-RAG 黑盒 ASR 0.73–0.87、CRAG 0.74–0.78、21M Wikipedia 段 5 条恶意文本 ASR 0.94–1.0、ReAct LLM Agent 0.52–0.72、FEVER 事实验证 0.88–0.97。论点轴是"高级 RAG 方案与规模都不能天然防投毒"。

v2 候选完全不同：top 1 是 Karpathy gist 中"人提问 / LLM 维护"的角色分工；top 2 是 LLM 对 wiki 跑 health checks 清理；top 3 是 LLM Wiki 的可能应用场景清单（个人记录、研究、读书等）。这三张卡都不讨论攻击、防御或 RAG 安全。

## 3. 下一步的核心依据

(1) 显示 token 共享仅在泛用词 `LLM`；(2) 显示 v2 候选无任何 RAG 安全相关内容。draft 数字与边界完整，无需 revise。结论 `new_card`。

不选 `provenance_delta`：v2 没有可链回的对应卡。
不选 `merge_candidate`：无重叠论点。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 `poisonedrag-retrieval-generation-two-conditions` 组成 PoisonedRAG 主簇。

## 5. 备注

top 1 / 2 / 3 三张候选全部因为含 `LLM` token 被推到顶端，是 jaccard 在 Karpathy 语料簇内的副产品。
