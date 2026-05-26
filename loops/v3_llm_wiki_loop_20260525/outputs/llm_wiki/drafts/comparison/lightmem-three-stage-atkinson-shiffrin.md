---
schema: comparison_provenance.v3
draft_card: ../cards/lightmem-three-stage-atkinson-shiffrin.md
draft_provenance: ../provenance/lightmem-three-stage-atkinson-shiffrin.md
similarity_result: ../similarity/lightmem-three-stage-atkinson-shiffrin.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2667
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1053
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0588
---

## 1. draft 与候选为什么看起来相关

top 1 `llm-wiki-three-layer-architecture` 与 draft 共享 `llm / 三层 / 架构 / 的` 这些 token，看起来主题相关但**完全是 jieba 切词的 surface 重合**：

- v2 卡片讲的是 Karpathy LLM Wiki gist 的 "raw / wiki / schema" 三层；
- 本 draft 讲的是 LightMem 论文中 Atkinson–Shiffrin 人类记忆模型的"感觉记忆 / 短期记忆 / 长期记忆"三模块，对应到 LLM agent 的三层记忆架构。

两者唯一的形式共性是"都是三层"。所属研究领域、所属系统对象、所引文献、所讨论的 trade-off 完全不同——一个是知识库设计模式，一个是 agent memory system 的论文方案。

top 2 / top 3 token overlap 极低（`llm / 的`、`的`），明显也是 token 误中。

## 2. draft 与候选在哪里不同

- **研究领域不同**：LLM Wiki 是文档与知识库工程；LightMem 是 LLM agent memory system 论文（ICLR 2026 投稿）。
- **所谓"层"含义不同**：v2 三层 = 数据 / 派生工件 / 配置；draft 三层 = 感觉记忆 / 短期记忆 / 长期记忆（人脑模型映射）。
- **机制完全不同**：v2 卡片只断言一个划分事实；draft 给出 token-level 预压缩 + topic 分段 + STM 阈值触发 summary + LTM offline parallel update 等具体机制 + 帕累托 trade-off + 数值评测（LongMemEval、LoCoMo）。
- **来源不同**：v2 来源 Karpathy gist；draft 来源 arxiv-lightmem 论文。

本 draft 与 v2 三张候选**没有任何事实重叠**，是一张纯新主题卡。

## 3. 下一步的核心依据

- 不是 `merge_candidate` / `provenance_delta` / `duplicate_skip`：v2 没有任何关于 agent memory system 的卡片，找不到合并 / 补强 / 重复对象。
- 不是 `revise_before_gate`：draft 证据完整（abstract、§3、Figure caption、experiments 数字、超参表都点到了原文行号），边界（Single-Assistant 反例、超参依赖 backbone）也标注。

正确决定是 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接走 publication_gate；本卡是一个独立主题板块（agent memory architecture）的根节点，未来其 3 个子卡（pre-compress / topic-aware STM / sleep-time update）将挂在它下面。

## 5. 备注

- 这是"低 IDF 中文 token 把不同领域的卡片拉到 top 1"的标准案例。下次设计相似度 metric 时建议把 `的 / 是 / llm / wiki` 列为停用词，或加 TF-IDF 权重以避免这种 surface-level 误中。
- draft 自己预测的 `merge_candidate`（与 Mem0 / A-MEM 卡）在 v2 不存在，故不适用。
