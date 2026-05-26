---
schema: comparison_provenance.v3
draft_card: ../cards/ragchecker-claim-entailment-decomposition.md
draft_provenance: ../provenance/ragchecker-claim-entailment-decomposition.md
similarity_result: ../similarity/ragchecker-claim-entailment-decomposition.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0667
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0625
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0556
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选分数 0.055–0.067，都属于 Karpathy LLM Wiki 概念簇。共享 token 大概是中文虚词或泛用名词。没有任何 token 与"claim / entailment / RefChecker / Llama3-70B / RAGChecker"相关。

## 2. draft 与候选在哪里不同

draft 描述的是 Amazon AWS AI 的 RAGChecker 评估框架：核心原语是把回答与 ground-truth 都拆成 claim 集合，再用 RefChecker (Llama3-70B-Instruct) 做 entailment 二元判定，并给出 overall Precision / Recall 公式。论点轴是"事实点对账型评分 vs answer similarity 型评分的根本差异"，以及 meta evaluation 中 RAGChecker 与人类判定相关性领先 RAGAS 等 10 个基线。

v2 候选：idea file 抽象性、三层架构、schema 配置——这三张都属于 LLM Wiki 概念定义层，与 RAG 评估指标毫无重叠。

## 3. 下一步的核心依据

(1) 与 (2) 都指向无任何主题重叠。draft 完整给出公式、实现栈、meta evaluation 数字与边界，结构合规。结论 `new_card`。

不选 `revise_before_gate`：draft 已包含 fact_type 对应的支撑、数字、边界。
不选 `provenance_delta`：v2 无可链回卡。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；可与 `ragas-answer-relevance-metric`、`ares-ppi-confidence-bound`、`alce-citation-recall-precision-nli` 形成 RAG 评估指标簇。

## 5. 备注

无。
