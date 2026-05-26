---
schema: comparison_provenance.v3
draft_card: ../cards/memory-as-metabolism-architectural-separability.md
draft_provenance: ../provenance/memory-as-metabolism-architectural-separability.md
similarity_result: ../similarity/memory-as-metabolism-architectural-separability.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.125
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1111
  - card_id: llm-wiki-persistent-compounding-artifact
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-compounding-artifact.md
    score: 0.0667
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top 1 共享 token `wiki`、`架构`：draft 标题里"架构可分离性"撞 v2 "三层架构"。top 2 共享 `wiki`、`是`。top 3 仅共享 `wiki`。draft 的核心 token `可分离性`、`权重`、`安全`、`承诺` 等没有任何候选覆盖。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-three-layer-architecture`：仅记录 Karpathy gist 的"raw / wiki / schema"三层静态分层。**不涉及**模型权重 / safety / base-model evolution。
- 候选 #2 `llm-wiki-schema-configuration-document`：仅讲 schema 层的配置文档定义。无关。
- 候选 #3 `llm-wiki-persistent-compounding-artifact`：讲 wiki 是持久复合产物（cross-reference 累积）。与 architectural separability 在论点轴上无交集——后者讨论"wiki 与 base model 权重的关系是 safety commitment"，是企业/科研级 architecture 论证，不是 wiki artifact 性质描述。
- draft 来源是 `arxiv-memory-as-metabolism` §8.3 / §6 / §5.0 row 7 / §9 / §11，论点轴是"separability 作为 base-model evolution 外部纠错通道的安全设计承诺"，明确把"do not fold wiki into weights"作为禁令（含对 ROME/MEMIT 等 model editing 的禁令）。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无任何 architectural separability / safety 维度卡。
- 不是 `provenance_delta`：候选都是 Karpathy 视角的 wiki 性质卡，与 base-model evolution 安全论证不在同一论点轴。
- 不是 `duplicate_skip`：无任何覆盖。
- 不是 `revise_before_gate`：draft 已有 §8.3 完整论证、§6 plain text 存储推荐、§9 limitations 禁令、§5.0 row 7、§11 conclusion 等多锚点引文 + 三条 honest limits 的自我克制；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段可核对 §8.3 Layer 4 的"companion-specific safety rationale"逐字段引文是否对齐。

## 5. 备注

- 同源系列卡（memory-as-metabolism-*）正在并入 v3，本卡是 §8.3 Layer 4 的独立切片，与 five-operations / mirror-vs-compensate 等卡互不重复。
- v2 KB 没有 safety / architecture-as-safety 任何相邻卡，jaccard 撞分纯由"wiki/架构"主题词。
