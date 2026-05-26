---
schema: comparison_provenance.v3
draft_card: ../cards/lightmem-complexity-formula.md
draft_provenance: ../provenance/lightmem-complexity-formula.md
similarity_result: ../similarity/lightmem-complexity-formula.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0625
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0588
  - card_id: raw-sources-readonly-source-of-truth
    card_path: llm_wiki/kb/cards/raw-sources-readonly-source-of-truth.md
    score: 0.0556
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选都属于 v2 高频干扰簇，分数 0.055–0.062。token 共享在中文虚词上。LightMem / O(N) / r^x / th / STM / LLMLingua 这些核心 token 在 v2 完全不出现。

## 2. draft 与候选在哪里不同

draft 是 LightMem 论文 §Complexity analysis 的成本公式拆解：复杂度表 `O(N) → O(Nr^x T/th)`、降本的三处来源（预压缩 / STM 阈值聚合 / 离线并行更新）、LongMemEval-S 实测对照（57× token 降 / 54× API call 降 / 18× runtime 降）、参数边界（r=0.6 是 ACC 最优、th 越大越省但非单调）。

v2 三张候选是 Karpathy LLM Wiki 概念层卡，无任何 cost model、token economics、memory system complexity 概念。

## 3. 下一步的核心依据

(1) (2) 共同表明无主题重叠。draft 公式、数字、来源、边界完整。结论 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 LightMem 主簇（precompress、sleep-time update）互相 cite。

## 5. 备注

无。
