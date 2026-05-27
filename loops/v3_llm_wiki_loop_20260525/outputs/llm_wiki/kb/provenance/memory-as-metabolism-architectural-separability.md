---
schema: accepted_card_provenance.v3
card: ../cards/memory-as-metabolism-architectural-separability.md
material_id: arxiv-memory-as-metabolism
digest_id: digest_arxiv-memory-as-metabolism
source_paths:
  - data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt
draft_card: ../../drafts/cards/memory-as-metabolism-architectural-separability.md
draft_provenance: ../../drafts/provenance/memory-as-metabolism-architectural-separability.md
similarity_result: ../../drafts/similarity/memory-as-metabolism-architectural-separability.json
comparison_provenance: ../../drafts/comparison/memory-as-metabolism-architectural-separability.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:44:00+08:00
  gate_notes: 6/6 项通过；§8.3 / §6 / §9 / §11 多处 verbatim，定位准确。
created_time: 2026-05-26T15:10:00+08:00
edited_time: 2026-05-27T14:44:00+08:00
edited_entity: llm
---

## 源证据

### §8.3 Layer 4 完整段（第 2117–2141 行）

> "Architectural separability preserves an external correction channel. The separation of external memory from model weights is an established architectural doctrine, not a new claim. Lewis et al. (2020) already justifies it on operational grounds: external knowledge can be 'revised and expanded' without retraining. The Atlas architecture (Izacard et al., arXiv:2208.03299) extends this: knowledge stores can be 'kept up-to-date without retraining, by updating or swapping their index at test time.' The harness engineering review [53] goes further, explicitly recommending cross-model transfer tests as standard practice ... Within this established externalization doctrine, what this paper adds is a companion-specific safety rationale that prior work does not articulate: separability is not merely operationally convenient (updates without retraining, provenance auditing) but structurally necessary for base-model evolution to function as an external correction channel specifically against user-coupled epistemic entrenchment. That rationale is narrower than 'keep knowledge external.' It is a safety commitment with a named mechanism: a user running a companion system for five years benefits from the model's improved factual priors and alignment training precisely because swapping the base model is a configuration change, not a wiki operation. Fold the wiki into weights and this channel closes permanently."

### §8.3 三条 honest limits（第 2143–2152 行）

> "This is a real correction channel but an incomplete one. Three honest limits: the wiki still anchors interpretation, so high-gravity false entries still bias outputs; base model updates are not always corrections, since labs update for many reasons including some that may make the system worse for a specific user; and the user does not control when updates happen. The framework benefits from this channel without being able to rely on it."

### §6 plain text 存储设计承诺（第 1643–1665 行）

> "Plain text as primary representation makes that survival auditable in a way embeddings-only storage does not, because a model swap forces re-embedding during which meaning can shift in ways the user cannot inspect after the fact. Because model swaps also invalidate existing embedding indices—different base models have different embedding spaces and semantic geometries—the framework assumes a re-indexing pass over the plain-text wiki content is a required step of any base-model generation update; the embedding layer is a derived artifact, while the plain-text layer is the preserved one."

### §5.0 冲突路由矩阵 row 7（第 1115 行附近）

> "Base model update introduces a factual prior contradicting a high-gravity wiki entry ... External correction channel. The wiki entry is flagged for review on the next CONSOLIDATE cycle post-update. This row depends structurally on architectural separability (§8.3): the external correction channel exists only because the wiki is not folded into base model weights. The separability commitment is what keeps this row operational across base model generations."

### §9 limitations（第 2175–2182 行）

> "Architectural commitment: do not fold the wiki into weights. The external correction channel in Section 8.3 depends on the companion layer remaining separable from the base model weights. Model editing research may eventually make weight-level integration technically possible; the framework's safety story specifically rules this out as a design move. This is a principled constraint, not a current limitation to overcome."

### §11 conclusion 把 separability 列为四条 framing contribution 之一（第 2446–2456 行）

> "Architectural separability from base-model weights as a safety design commitment whose specific rationale has not been articulated in prior work: within the externalization doctrine established by Lewis et al. (2020) and Atlas (Izacard et al., arXiv:2208.03299), separability is not just operationally convenient but structurally necessary for base-model evolution to function as an external correction channel against user-coupled epistemic entrenchment."

## 卡片范围是否成立

本卡聚焦 separability 作为安全承诺。现有五张 memory-as-metabolism 卡片都未覆盖：
- mirror-vs-compensate 卡里只在边界一段提及 §8.3 三时间尺度通道；
- five-operations、memory-gravity、minority-pressure、audit-by-suspension 都不在 §8.3 layer 4 的论证范围内。

本卡所有主张直接来自 §8.3 Layer 4、§6 存储推荐、§9 limitations 第二条、§5.0 row 7、§11 conclusion。"对 model editing 的禁令"是本卡综合 §9 限制 + §8.3 论证得到的操作含义，但论文 §9 已显式 rule out。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:44:00+08:00
- 检查要点：
  - 主张-论证-边界结构清晰；非标题复述。
  - 知识密度高：主张、三件被守住的事、三条诚实、操作含义、边界 5 节。
  - 源支撑：5 段 verbatim 引用 + 章节行号。
  - References + Footnotes 双在。
  - frontmatter 完整；related 含 5 张相关卡。

## 备注

- 与 ETAMP 卡片有"记忆与 base model 关系"的潜在跨论文张力：ETAMP 把 memory 当攻击面（即"persistent across base-model-equivalent reruns"是坏属性）；本卡把 separability 当安全资产（即"persistent across model swaps"是好属性）。两条不矛盾，但 wiki 内做 cross-reference 时应说明。
- 与 wicer-hardware-architecture-deployment 卡片无直接交集，但都属于"长期部署友好性"主题。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/memory-as-metabolism-architectural-separability.md`
- draft provenance: `../../drafts/provenance/memory-as-metabolism-architectural-separability.md`
- similarity: `../../drafts/similarity/memory-as-metabolism-architectural-separability.json`
- comparison provenance: `../../drafts/comparison/memory-as-metabolism-architectural-separability.md`
