---
schema: comparison_provenance.v3
draft_card: ../cards/lightmem-precompress-and-topic-segmentation.md
draft_provenance: ../provenance/lightmem-precompress-and-topic-segmentation.md
similarity_result: ../similarity/lightmem-precompress-and-topic-segmentation.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0588
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0556
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.05
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选属 v2 高频干扰簇，分数 0.05–0.059。LightMem / LLMLingua-2 / topic segmentation / attention matrix / all-MiniLM-L6-v2 等核心 token 在 v2 不出现。

## 2. draft 与候选在哪里不同

draft 描述 LightMem Light1（感觉记忆层）的两个子模块：(a) pre-compressing 用 LLMLingua-2 给 token 算 retain 概率、动态分位数 τ、空句兜底、超 512 token 递归压缩；(b) topic segmentation 用 LLMLingua-2 高层注意力 ∩ all-MiniLM-L6-v2 相似度交集找切点；ablation 显示去掉 topic seg 后 GPT 掉 6.3% / Qwen 掉 5.4%。

v2 三张候选是 Karpathy LLM Wiki 概念层，无任何 prompt compression、topic segmentation 概念。

## 3. 下一步的核心依据

(1) (2) 共同表明无重叠。draft 完整。结论 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 LightMem 系列其他卡互相 cite。

## 5. 备注

无。
