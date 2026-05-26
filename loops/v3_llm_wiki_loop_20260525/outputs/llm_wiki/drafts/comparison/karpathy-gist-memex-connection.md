---
schema: comparison_provenance.v3
draft_card: ../cards/karpathy-gist-memex-connection.md
draft_provenance: ../provenance/karpathy-gist-memex-connection.md
similarity_result: ../similarity/karpathy-gist-memex-connection.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.2
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1579
  - card_id: llm-wiki-wiki-layer-generated-markdown-directory
    card_path: llm_wiki/kb/cards/llm-wiki-wiki-layer-generated-markdown-directory.md
    score: 0.1429
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选都来自 karpathy gist 的 v2 卡片家族，因此和本 draft 一样共享 `llm`、`wiki`、`的` 这些通用 token。top1 (`schema-configuration-document`) 的 0.2 几乎全部来自这些功能词；top3 (`wiki-layer-generated-markdown-directory`) 还共享了"维护"——因为本 draft 标题里有"谁来维护"，恰好和 v2 卡"由 LLM 生成和维护"的"维护"撞词。表面上有相关性，但都是 token 共享，不是论点共享。

## 2. draft 与候选在哪里不同

- top1 `schema-configuration-document` 讲 schema 在 LLM Wiki 内部充当配置文档、约束 LLM 行为——是**架构内部机制**的卡。本 draft 讲的是 LLM Wiki 与 1945 年 Memex 设想的**历史/概念史关系**，以及"谁来维护"这块 Bush 没解决的拼图。两者论点轴完全不同：机制 vs. 知识管理史定位。
- top2 `three-layer-architecture` 讲 LLM Wiki 的三层（schema / sources / wiki）结构，仍属架构内部分层；不触碰 Memex 的"associative trails""private + curated"概念骨架，也不展开"谁来维护"的历史命题。
- top3 `wiki-layer-generated-markdown-directory` 讲 wiki 层 markdown 由 LLM 生成和维护——只是机制陈述（LLM 接管 wiki 层维护工作），并没有把它放进"Memex 80 年未解决问题"这条长时间线上。本 draft 的"LLM handles that"是把 v2 既有的机制陈述**升维**到知识管理史叙事。

## 3. 下一步的核心依据

(1) 三张候选都是 v2 内部架构卡，没有覆盖 Memex 类比这一概念史维度；(2) 即使最接近的 top3 也只是"LLM 维护 wiki 层"的机制描述，没有引 Bush/1945/associative trails/Memex 设想。本 draft 是一张全新的 source_claim：它把 LLM Wiki 放到知识管理史长时间线上，并给出"任何不解决维护问题的 PKM 都复刻 Memex 失败"这条评估锚点。结论是 `new_card`。

不是 `provenance_delta`：本 draft 内容自成体系，不是给 v2 某卡补一段证据或边界——它是一个**新主题**（Memex 类比），不属于现有任何一张 v2 卡的范围。也不是 `revise_before_gate`：draft 本身证据充分（含原文引文 + 行号 + boundary 声明）、边界明确，可以直接进入 publication_gate。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；建议作为 "Why this matters / 知识管理史" 类的入口卡之一。

## 5. 备注

- 顺带：v2 的 `wiki-layer-generated-markdown-directory` 卡只陈述了 "LLM 接管 wiki 层维护"的事实，未引 Memex；将来如果加 cross-link，可以从该 v2 卡 footnote 反向链接到这张 draft 作"概念史背景"。但这属于 v2 reflection 范畴，不是本卡触发的 provenance_delta。
