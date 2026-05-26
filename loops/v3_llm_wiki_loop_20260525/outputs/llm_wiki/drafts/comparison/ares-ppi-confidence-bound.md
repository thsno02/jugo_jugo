---
schema: comparison_provenance.v3
draft_card: ../cards/ares-ppi-confidence-bound.md
draft_provenance: ../provenance/ares-ppi-confidence-bound.md
similarity_result: ../similarity/ares-ppi-confidence-bound.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0625
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0588
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0526
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选 0.052–0.062，全部属于 Karpathy LLM Wiki 概念簇，token 共享在中文虚词或泛用词。和 ARES / PPI / rectifier / Angelopoulos 2023 / Kendall's τ 等关键概念无对应。

## 2. draft 与候选在哪里不同

draft 描述 ARES 用 prediction-powered inference 把 150–300 条 human preference validation set 与 LLM 判官的预测拼起来，输出 RAG 得分的 95% 置信区间；细节包括 rectifier function、midpoint 排名、`ppi_count` 校准集大小下界（25 条时 τ=0.44，300 条时 τ=0.89）、真实 RAG 上区间宽度 7.4 / 6.1pp、跨语言迁移失败模式。

v2 三张候选讨论的是 Karpathy gist 的 idea file 抽象性、三层架构、schema 配置——没有任何统计推断、judge 校准、置信区间相关的论点。

## 3. 下一步的核心依据

(1) (2) 共同表明无主题重叠。draft 完整，可进 gate。结论 `new_card`。

不选 `provenance_delta`：v2 无可链回 ARES PPI 的卡。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 RAG 评估指标簇互相 cite。

## 5. 备注

无。
