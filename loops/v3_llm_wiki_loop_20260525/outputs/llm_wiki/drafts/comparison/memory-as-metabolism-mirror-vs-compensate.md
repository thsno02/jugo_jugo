---
schema: comparison_provenance.v3
draft_card: ../cards/memory-as-metabolism-mirror-vs-compensate.md
draft_provenance: ../provenance/memory-as-metabolism-mirror-vs-compensate.md
similarity_result: ../similarity/memory-as-metabolism-mirror-vs-compensate.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.1
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0909
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0769
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选共享 token 仅为 `的`。draft 的核心 token `伴侣`、`镜像`、`补偿`、`设计原则` 都不出现在任何候选标题。jaccard 0.1 完全由虚词产生。

## 2. draft 与候选在哪里不同

- 候选 #1 `idea-file-abstract-vague`：idea file 抽象性事实。无关。
- 候选 #2 `llm-wiki-three-layer-architecture`：Karpathy gist 三层架构。无关。
- 候选 #3 `llm-wiki-schema-configuration-document`：schema 配置文档定义。无关。
- draft 来源是 `arxiv-memory-as-metabolism` §1.2 + §5.0，论点是 companion memory 的"镜像-补偿"设计原则——operational 维度做 mirror、epistemic failure 维度做 compensate、TRIAGE → CONSOLIDATE → AUDIT 作为时间结构化程序冲突规则。draft 还自我标注论文宣称的核心新贡献"程序冲突规则作为单用户 companion 衬底的绑定"。v2 KB 完全没有 companion memory / governance 卡。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无 companion governance / memory design principle 系列卡。
- 不是 `provenance_delta`：候选都是 Karpathy gist 元事实，无对接面。
- 不是 `duplicate_skip`：无重叠。
- 不是 `revise_before_gate`：draft 已有 §1.2 引文（mirror/compensate 维度定义）、§5.0 操作角色映射表、贡献声明 verbatim、边界（不是真理追踪器 / 安全故事部分性 / AUDIT 灵敏度开放问题）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段建议核 §1.2 mirror/compensate 维度定义与论文行 283–344 是否字面对齐。

## 5. 备注

- 与同源 `memory-as-metabolism-five-operations`、`memory-as-metabolism-architectural-separability` 等卡共同构成 memory-as-metabolism 论文的多切面视图。
- draft 自身 provenance 提到 v2 `idea-file-as-agent-era-artifact`、`llm-knowledge-base-five-stage-workflow` 可建 cross-link，但这两张卡未出现在本批 top 3，属审计阶段动作。
