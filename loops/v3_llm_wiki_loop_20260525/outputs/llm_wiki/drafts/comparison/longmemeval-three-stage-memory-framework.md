---
schema: comparison_provenance.v3
draft_card: ../cards/longmemeval-three-stage-memory-framework.md
draft_provenance: ../provenance/longmemeval-three-stage-memory-framework.md
similarity_result: ../similarity/longmemeval-three-stage-memory-framework.json
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
created_time: 2026-05-26T16:11:00+08:00
edited_time: 2026-05-26T16:11:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "把 long-term memory 系统拆成 indexing / retrieval / reading 三阶段四控制点" **token 共享为空，score 全部 0.000**。三个候选都来自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：LongMemEval 提出的统一框架——把所有 memory-augmented 系统建模为 KV 存储 + 三阶段（Indexing / Retrieval / Reading）+ 四控制点（CP1–CP4），并把 9 个现有系统映射到该框架。论据轴是 memory system framework + plug-and-play 控制点。
- 候选 1 / 2：Karpathy 推文 idea file 抽象性 / 分享逻辑。
- 候选 3：LLM 对 wiki 做 health checks 清理。

draft 与候选无任何论点交叠、无共享 underlying source。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 不含 memory system framework / CP / KV indexing / reading strategy 任何内容 → `new_card`。draft 自带 CP1–CP4 详表、9 系统映射表、原文 quote、framework 边界，证据完整 → 不是 `revise_before_gate`。v2 无 memory framework 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；该卡是 LongMemEval / Mem0 / MemGPT family 在 v3 内 backbone framework 卡，应在 publication 后被这些卡 related 引用。

## 5. 备注

无异常；同 batch 内还有 LongMemEval 其它 draft 与之配合。
