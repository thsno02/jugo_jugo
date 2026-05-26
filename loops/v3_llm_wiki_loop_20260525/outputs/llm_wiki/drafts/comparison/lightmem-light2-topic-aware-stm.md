---
schema: comparison_provenance.v3
draft_card: ../cards/lightmem-light2-topic-aware-stm.md
draft_provenance: ../provenance/lightmem-light2-topic-aware-stm.md
similarity_result: ../similarity/lightmem-light2-topic-aware-stm.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0714
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0667
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0588
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.08，shared_tokens 仅为「的」。draft 标题的实质 token（LightMem / Light2 / STM / topic / summary / 输入粒度）与 v2 候选（Karpathy LLM-wiki 元描述）无术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 mechanism 卡，来源 `arxiv-lightmem`，论述 LightMem Light2 STM 层把 topic-level 切段堆进 buffer，达到 token 阈值 `th` 时触发 `f_sum`，再把 `{topic, embedding(sum_i), user_i, model_i}` 写入 LTM；并量化 `th` 与 API 调用 / runtime 单调下降但与 accuracy 非单调的关系（GPT-4o-mini 选 th=512、Qwen3-30B 选 th=768）。属于「agent 长期记忆架构」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述。论点轴（agent 记忆 architecture vs 个人 LLM wiki 模式）、来源（学术论文 vs Karpathy gist）、机制（topic-aware STM/LTM 三阶段 vs 人 LLM 分工写 markdown）完全不同。

## 3. 下一步的核心依据

shared_tokens 全是「的」，无语义重叠。draft 引文具体到 L830-848 / L643-650 / L1021，scope 自洽。无任何 v2 卡可 merge 或 provenance_delta。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `lightmem-three-stage-atkinson-shiffrin` / `lightmem-precompress-and-topic-segmentation` 同 source 互引。
