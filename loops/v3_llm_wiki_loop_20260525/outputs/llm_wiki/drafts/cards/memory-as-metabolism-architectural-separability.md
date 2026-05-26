---
id: memory-as-metabolism-architectural-separability
title: 架构可分离性：把 wiki 留在权重之外是安全承诺，不是工程便利
status: draft
card_type: operational_rule
tags: [#memory, #companion-system, #safety, #architectural-separability, #base-model-evolution]
created_time: 2026-05-26T15:10:00+08:00
edited_time: 2026-05-26T15:10:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
provenance_card: ../provenance/memory-as-metabolism-architectural-separability.md
aliases: [architectural separability, separability as safety commitment, base-model correction channel, do not fold wiki into weights]
related: [memory-as-metabolism-mirror-vs-compensate, audit-by-suspension-against-entrenchment, memory-as-metabolism-conflict-routing-matrix, memory-as-metabolism-five-operations, karpathy-llm-wiki-vs-rag]
---

## 主张

Miteski (2026) 把"companion wiki 必须保持与 base model 权重分离"作为四条"framing contributions"之一。这条主张的关键不是新——Lewis et al. (2020) 与 Atlas (Izacard 等, arXiv:2208.03299) 已在 operational 层面建立"externalization doctrine"——而是**给出 companion-specific 的安全理由**：

> 分离不仅是"更新无需重训"等运营便利，而是**结构必要条件**——让 base model evolution 作为对抗用户耦合认知固化（user-coupled epistemic entrenchment）的**外部纠错通道**。「Fold the wiki into weights and this channel closes permanently.」[^1]

## 三件被分离守住的事

1. **底模更新 = 配置变更，不是 wiki 操作**：用户跑 5 年 companion，底模换两轮（新事实先验、新对齐训练、新能力），companion 系统**自动**继承这些更新。
2. **纠错通道结构性存在**：§5.0 冲突路由矩阵第 7 行（base model 更新引入与高 gravity wiki 条目冲突的事实先验）的**所有处理**都依赖"wiki 是独立 artifact"——若 wiki 被折进权重，该行无法实施。
3. **存储表示也跟着锁死**：§6 推荐 plain text + embeddings hybrid（不是仅 embeddings），理由是底模换代会**重新 embed**——纯 embedding 存储下底模换代会导致 wiki 内容被 silently rewritten。论文称之为"plain text 让 cross-generation 可审计性可能"，并把"换底模必然需要 re-indexing pass on plain-text wiki content"作为设计假设。

## 三条对自身的诚实

1. **wiki 仍 anchor interpretation**：高 gravity 错条目仍偏置输出；
2. **底模更新不总是改进**：labs 出于多种理由更新，某些更新可能让特定用户的体验**更差**；
3. **用户控不了更新时点**：companion 框架受益于此通道但不能依赖它。

## 操作含义

- **设计层**：禁止把 companion layer 折进 fine-tune（DPO/SFT in user-specific weights）；禁止用 model editing（如 ROME、MEMIT）把 wiki 内容直接写入权重。这是论文 §9 limitation 中点名的"principled constraint, not a current limitation to overcome"。
- **存储层**：plain text 是 primary representation，embeddings 是 derived artifact；底模换代后 wiki 内容**保留**、embedding **重建**——这条假设让模型生成的"reinterpretation"可被审计。
- **评测层**：与 harness engineering review (Zhou 等 arXiv:2604.08224) 推荐的 cross-model transfer tests 同方向——separability 让 cross-model swap 可测。

## 边界

- 这是"why never fold wiki into weights"的**论证**，不是"separability 自动解决一切"的承诺。论文反复强调安全故事是 partial：四层（honest naming / compensate mechanisms / batched consolidation / separability）合起来对"reinforcement of bad beliefs"也是不完整防御，对"fully novel bad beliefs not represented in the base model"无机制覆盖（§9 residual）。
- 与 MemOS / Context Cartography 的 governance 框架不同：那两个框架在 governance 层级讨论 separability，但**没有把"base-model evolution 作为外部纠错通道"作为单独的安全机制理由化**。这是论文声称的 companion-specific contribution。

## References

- §8.3 Layer 4 完整论证：`data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` 第 2117–2152 行。
- §6 存储表示推荐：第 1643–1665 行。
- §9 limitations 第二条："Architectural commitment: do not fold the wiki into weights"：第 2175–2182 行。
- §11 conclusion 把 separability 作为四条 framing contribution 之一：第 2446–2456 行。
- §1 abstract 关于三时间尺度纠错通道：第 219–222 行。

## Footnotes

[^1]: 第 2129–2141 行（§8.3 Layer 4）：
    > "Within this established externalization doctrine, what this paper adds is a companion-specific safety rationale that prior work does not articulate: separability is not merely operationally convenient (updates without retraining, provenance auditing) but structurally necessary for base-model evolution to function as an external correction channel specifically against user-coupled epistemic entrenchment ... a user running a companion system for five years benefits from the model's improved factual priors and alignment training precisely because swapping the base model is a configuration change, not a wiki operation. Fold the wiki into weights and this channel closes permanently."

[^2]: §6 plain text 推荐原文（第 1647–1665 行）：
    > "Plain text as primary representation makes that survival auditable in a way embeddings-only storage does not, because a model swap forces re-embedding during which meaning can shift in ways the user cannot inspect after the fact. Because model swaps also invalidate existing embedding indices ... the framework assumes a re-indexing pass over the plain-text wiki content is a required step of any base-model generation update; the embedding layer is a derived artifact, while the plain-text layer is the preserved one."

[^3]: §9 limitations 原文（第 2175–2182 行）：
    > "Architectural commitment: do not fold the wiki into weights. The external correction channel in Section 8.3 depends on the companion layer remaining separable from the base model weights. Model editing research may eventually make weight-level integration technically possible; the framework's safety story specifically rules this out as a design move. This is a principled constraint, not a current limitation to overcome."
