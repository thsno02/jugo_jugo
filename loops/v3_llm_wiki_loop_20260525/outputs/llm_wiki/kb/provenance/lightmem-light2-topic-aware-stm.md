---
schema: accepted_card_provenance.v3
card: ../cards/lightmem-light2-topic-aware-stm.md
material_id: arxiv-lightmem
digest_id: digest_arxiv-lightmem
source_paths:
  - data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt
draft_card: ../../drafts/cards/lightmem-light2-topic-aware-stm.md
draft_provenance: ../../drafts/provenance/lightmem-light2-topic-aware-stm.md
similarity_result: ../../drafts/similarity/lightmem-light2-topic-aware-stm.json
comparison_provenance: ../../drafts/comparison/lightmem-light2-topic-aware-stm.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:30:00+08:00
  gate_notes: 6/6 项通过：Entry schema + topic 粒度对照 + th 非单调 ACC 关系 + 边界。
created_time: 2026-05-26T15:10:00+08:00
edited_time: 2026-05-27T10:30:00+08:00
edited_entity: llm
---

## 源证据

- 行 830–848（§3.2 Light2: Topic-aware short-term memory）：
  - "After obtaining individual topic segments, forming an index structure of \{topic, message turns\}, where message turns = \{$user_i$, $model_i$\}. These are first placed into the STM buffer. When the token count in the buffer reaches a preset threshold, we invoke LLM $f_{\text{sum}}$ to generate concise summaries of every structure. The final index structure stored in LTM is \{topic, \{$sum_i$, $user_i$, $model_i$\}\}."（行 836–838）
  - "Compared with inputting at the granularity of a single turn or session, directly feeding multiple sessions can reduce subsequent API calls but often introduces inaccurate memory entries due to excessive topic mixing, leading to performance degradation. In contrast, topic-constrained input granularity minimizes API calls to the greatest extent while preserving summarization accuracy and maintaining stable system performance."（行 846–848）
  - 公式：`Entry_i = {topic, embedding(sum_i), user_i, model_i}`（行 843–845）。

- 行 643–650（§Analysis of the STM Threshold's Impact）：
  - "A consistent trend is: as $th$ increases, there is a marked improvement in efficiency."（行 646）
  - "In contrast, the effect on QA accuracy is non-monotonic. The optimal threshold for accuracy varies depending on the model and the compression ratio ($r$), indicating that a larger buffer does not always yield better performance."（行 647–648）

- 行 1021（category-wise table caption）："For GPT, LightMem is configured with parameters $r=0.7$ and $\text{th}=512$; for Qwen, LightMem is configured with $r=0.4$ and $\text{th}=768$."

## 卡片范围是否成立

- 卡片核心都在论文 §3.2 直接给出（输入结构、触发条件、Entry schema、topic 粒度论证）；非论文叙述以"实践含义"形式标出。
- "可追溯证据"那一节是合理引申——entry 同时保留 `user_i, model_i` 原文是事实，但论文未明说这是"可追溯"机制；本卡用"双重保险"作描述，没有声称是论文论点。
- ACC 非单调与 `th` 单调 efficiency 是论文显式结论，没有越界。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:30:00+08:00
- 检查要点：
  - 非标题复述：以输入/输出 + 为何 topic 粒度 + th 可调性 + 实践含义 + 边界五段实质展开。
  - 知识密度：Entry schema 公式 + 三粒度对比 + th 单调/ACC 非单调 + GPT 512 / Qwen 768 配置。
  - 源支撑：lightmem 行 830-848 / 643-650 / 1021。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 5 个 v3 draft id。

## 备注

- 与现有 `lightmem-three-stage-atkinson-shiffrin` 卡互补：那张总览三层，本卡专门展开 Light2 的中转逻辑。
- 与 `lightmem-precompress-and-topic-segmentation` 互补：前者是 Light1 把 topic 切出来，本卡是 Light2 怎么消费这些 topic。
- Adoption 阶段观察：v2 候选 shared token 仅「的」，无 fusion 必要。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/lightmem-light2-topic-aware-stm.md`
- draft provenance: `../../drafts/provenance/lightmem-light2-topic-aware-stm.md`
- similarity: `../../drafts/similarity/lightmem-light2-topic-aware-stm.json`
- comparison provenance: `../../drafts/comparison/lightmem-light2-topic-aware-stm.md`
