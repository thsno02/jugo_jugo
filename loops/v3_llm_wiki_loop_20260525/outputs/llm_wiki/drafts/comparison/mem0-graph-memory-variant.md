---
schema: comparison_provenance.v3
draft_card: ../cards/mem0-graph-memory-variant.md
draft_provenance: ../provenance/mem0-graph-memory-variant.md
similarity_result: ../similarity/mem0-graph-memory-variant.json
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
created_time: 2026-05-26T16:11:30+08:00
edited_time: 2026-05-26T16:11:30+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "Mem0g 图记忆变体：实体-关系三元组 + 冲突解决，专攻时序与开放域" **token 共享为空，score 全部 0.000**。三个候选都源自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：Mem0g 图记忆变体——有向带标签图 $G=(V,E,L)$ + 两阶段 LLM 抽取 + 冲突 invalidate + 双路检索 + Neo4j 实现。论据轴是 knowledge graph memory + temporal reasoning + entity-relationship structure。
- 候选 1 / 2：Karpathy 推文 idea file 抽象性 / 分享逻辑。
- 候选 3：LLM 对 wiki 跑 health checks。

draft 与候选完全不在同一域：mem0g 在"图记忆 + 三元组冲突 + Neo4j"，候选在"Karpathy 推文 idea file 概念"——无任何重叠。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 不含 graph memory / triple / Neo4j / LOCOMO eval 任何内容 → `new_card`。draft 自带图定义、抽取/整合/冲突流程、Mem0 vs Mem0g 实测对比、token / 时延数据、原文 quote，证据完整 → 不是 `revise_before_gate`。v2 无 mem0 / graph memory 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 `mem0-extract-update-pipeline`、`mem0-locomo-benchmark-evaluation` 等同 family 卡 related。

## 5. 备注

Mem0 family 在 v2 KB 完全缺席。
