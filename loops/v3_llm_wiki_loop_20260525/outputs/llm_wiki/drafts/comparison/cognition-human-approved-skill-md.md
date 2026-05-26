---
schema: comparison_provenance.v3
draft_card: ../cards/cognition-human-approved-skill-md.md
draft_provenance: ../provenance/cognition-human-approved-skill-md.md
similarity_result: ../similarity/cognition-human-approved-skill-md.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0556
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.0526
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0526
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 显示 top 1 与 top 3 共享 `的`，top 2 共享 `作为`（draft 标题 "...**作为**团队级 agent 记忆..."，候选 "LLM Wiki **作为**模式文件"）。0.0556 / 0.0526 的分数完全来自通用助词与介词，主题层无任何共享。

## 2. draft 与候选在哪里不同

- draft 描述 Cognition 产品中 SKILL.md 的**写入闸门规则**：草稿自动 / 保存人审的两阶段不对称、人审动机（私域隔离、错误模式抑制、作者归属）、与 RAG 通用文档库的差别、与"自动 CONSOLIDATE"派的张力，以及 group-code 邀请边界。来源 `cognitionus-llm-wiki-guide`。
- top 1 `idea-file-abstract-vague`：Karpathy idea file 的抽象性设计观察。
- top 2 `llm-wiki-pattern-file`：Karpathy 把 LLM Wiki 当作模式文件——"模式文件" ≠ "SKILL.md 写入规则"，前者是表达层的范式，后者是治理闸门。
- top 3 `llm-wiki-three-layer-architecture`：架构层定义。
- 三者均与"团队级 agent 记忆的人审治理"主题无任何重叠。

## 3. 下一步的核心依据

(1) 与 (2) 共同表明 jaccard 分数来自 `的`/`作为` 通用 token；draft 论点轴（人审 gate + 团队 brain 治理）与候选（架构 / 设计观察 / 表达范式）完全错位。判 `new_card`：直接走 publication_gate。draft 已含规则、动机、实施约束、对比与 verbatim 引文，发表条件齐备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

无；典型低分误中。
