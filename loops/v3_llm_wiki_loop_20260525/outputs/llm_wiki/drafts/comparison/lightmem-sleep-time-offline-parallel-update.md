---
schema: comparison_provenance.v3
draft_card: ../cards/lightmem-sleep-time-offline-parallel-update.md
draft_provenance: ../provenance/lightmem-sleep-time-offline-parallel-update.md
similarity_result: ../similarity/lightmem-sleep-time-offline-parallel-update.json
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

三张候选属于 v2 高频干扰簇，分数 0.052–0.062。token 共享停留在虚词层。LightMem / sleep-time / soft update / LTM / Tokyo trip case study 等核心概念在 v2 不出现。

## 2. draft 与候选在哪里不同

draft 描述 LightMem 把 LTM 维护拆成 online soft update（只 timestamped 插入，推迟 add/delete/merge/update）+ offline parallel update（每条 entry 独立的 top-k 候选队列 Q(e_i)，时间戳约束 t_j ≥ t_i，可并行）。给出 hard vs soft update 的 Tokyo/Kyoto case study，以及 sleep-time 工程边界。

v2 三张候选是 Karpathy LLM Wiki 概念层，与 memory system 设计无关。

## 3. 下一步的核心依据

(1) (2) 共同表明无主题重叠。draft 完整。结论 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 LightMem 系列其他卡互相 cite。

## 5. 备注

无。
