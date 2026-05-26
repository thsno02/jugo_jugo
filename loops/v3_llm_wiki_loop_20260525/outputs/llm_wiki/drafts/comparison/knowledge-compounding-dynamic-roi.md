---
schema: comparison_provenance.v3
draft_card: ../cards/knowledge-compounding-dynamic-roi.md
draft_provenance: ../provenance/knowledge-compounding-dynamic-roi.md
similarity_result: ../similarity/knowledge-compounding-dynamic-roi.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0556
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0526
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0476
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 显示 top 1/2/3 都只共享 `的`。分数完全来自中文助词同形，没有实质性主题共享。

## 2. draft 与候选在哪里不同

- draft 描述 Wen & Ku (2026) 的 **动态 Agentic ROI 模型**：成本不再是常量，而是时间函数 `Cost(t)`，由知识库覆盖率 `H(t)` 控制；实证锚点是 Qing Claw 框架上 4 条 query 实验（47K vs 305K tokens，84.6% 节省）以及 30 天校准的 53.7% / 81.3% 节省。论点是知识复利让 RAG 范式下"任务成本独立"假设失效。来源 `arxiv-knowledge-compounding`。
- top 1/2/3 是 Karpathy LLM Wiki 卡（idea file / 三层架构 / schema 配置文档），关注架构定义与设计取向，不论 ROI 经济学或动态成本模型。
- 即便主题表面接近 "LLM Wiki 经济性"，候选卡 scope 都严格限定在 Karpathy gist 的架构定义，未涉及 ROI 模型或 token 节省实验。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自 `的`，主题层无交集。判 `new_card`：直接走 publication_gate。draft 含模型动机、静态/动态视角对照、实证数字、边界（H(t) 非免费、长尾退化），发表条件齐备。不是 `provenance_delta` —— Karpathy 架构卡 scope 不涵盖动态 ROI。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。本卡与 v2 `llm-wiki-three-layer-architecture` 在主题上相关（同属 wiki 架构议题），可在 v3 publication 后通过 related 字段做跨卡链接，但当下不构成 merge / delta。

## 5. 备注

无；典型 `的` 同形误中。
