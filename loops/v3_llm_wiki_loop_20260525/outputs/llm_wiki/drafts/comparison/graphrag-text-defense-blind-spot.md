---
schema: comparison_provenance.v3
draft_card: ../cards/graphrag-text-defense-blind-spot.md
draft_provenance: ../provenance/graphrag-text-defense-blind-spot.md
similarity_result: ../similarity/graphrag-text-defense-blind-spot.json
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
created_time: 2026-05-26T16:08:00+08:00
edited_time: 2026-05-26T16:08:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "现有文本侧防御为何对 GraphRAG 投毒近乎失明" **无 token 共享，score 全部 0.000**。三个候选均源自同一条 Karpathy "llm wiki" launch 推文，本质是 v2 候选池仅 15 张卡的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：Wen 等人测试 PF / LLMDet / SCC 三类 RAG 投毒防御对 TKPA / UKPA 全部失效，原因是它们结构性看不到"chunk 之间的 graph 拓扑差"。论据轴是 graph poisoning attack defense + PPL / NLI judge 失效。
- 候选 1：Karpathy 推文里 idea file 抽象性的事实卡。
- 候选 2：同推文 idea file 分享逻辑的事实卡。
- 候选 3：LLM 对 wiki 跑 health checks。

draft 与候选既没有共享 underlying source（draft 来自 `arxiv-graph-poisoning`，候选来自 `karpathy-x-launch-post`），也没有共享论点（draft 谈攻击防御失效；候选谈 wiki 概念叙述）。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 与 RAG 投毒防御毫不相关 → `new_card`。draft 自带 PPL Ratio 数字、F1 数字、按攻击类型的失效解释、操作含义、边界，证据完整 → 不是 `revise_before_gate`。v2 无 RAG 安全 / graph poisoning 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 `tkpa-graph-guided-targeted-poisoning`、`ukpa-coreference-disruption` 在 v3 内 related 互联。

## 5. 备注

RAG / GraphRAG 安全在 v2 KB 完全缺席；本卡所属系列将首次填补该域。
