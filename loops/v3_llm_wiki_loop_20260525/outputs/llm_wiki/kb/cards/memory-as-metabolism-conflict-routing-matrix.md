---
id: memory-as-metabolism-conflict-routing-matrix
title: §5.0 冲突路由矩阵：把"mirror vs compensate"程序化为 7 类显式路由
status: accepted
card_type: operational_rule
tags: [#memory, #companion-system, #governance, #conflict-routing, #procedural-rule]
created_time: 2026-05-26T15:10:00+08:00
edited_time: 2026-05-28T11:20:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
provenance_card: ../provenance/memory-as-metabolism-conflict-routing-matrix.md
aliases: [conflict routing matrix, mirror-compensate procedural rule, sycophancy override, base-model correction row]
related: [memory-as-metabolism-mirror-vs-compensate, memory-as-metabolism-architectural-separability, audit-by-suspension-against-entrenchment, memory-as-metabolism-five-operations, minority-pressure-promotion, mem0-tool-call-add-update-delete-noop]
---

## 主张

Miteski (2026) §5.0 给出一张 7 行冲突路由矩阵[^src1]，把"mirror vs compensate"[^v3-1]从原则**程序化**为可执行规则——当流式与调度路径同时存在冲突信号时，矩阵指定**谁来处理 / 走哪条 friction / 用什么理由**。论文称之为"the procedural rule that decides how and when each operation applies to the mirror-vs-compensate conflict"——也是 §11 列出的四条 framing contribution 中**第二条**的具体实现[^src2]。

## 路由 legend（必读）

- **Mirror**：在交互 / 工作表示层应用对齐行为，但**不**修改 canonical 条目；
- **Compensate**：以高于默认的 friction 走 CONSOLIDATE；
- **Buffer**：进 minority branch，本周期不整合；
- **AUDIT override**：高优先级进 AUDIT；若失败持续，走 §5.8 gravity-reduction 通路；
- **External correction**：因底模先验变化，标记下一轮 post-update CONSOLIDATE 评审。

## 7 行（按论文表序）

1. **用户词汇与 ontology 偏离 + 无效用退化** → Mirror in interaction，**不**改 canonical wiki；保留 divergence marker 供下次 CONSOLIDATE 审[^v3-2]。
2. **同上但效用在多周期内退化** → Compensate（utility 退化是 operational→epistemic 桥）。
3. **用户反复强化 + 外部安全/认知信号判定有害 + 但用户报满意** → **Compensate regardless of utility**；AUDIT priority queue；最高 friction；强化条目标记 stress-test。**Row 3 是 sycophancy 失败模式的显式拦截**——"some reinforcement patterns must be resisted regardless of user-reported utility"[^src3]。
4. **新证据与高 gravity 条目矛盾、单源单周期** → **默认 Buffer**（进 minority branch）[^v3-3]。**Exception**：实现可定义 high-trust source class 接受 elevated initial weight；框架不锁死 trust model，但**路由规则不可禁掉这个 exception**。
5. **新证据与高 gravity 条目矛盾、多源多周期累积** → Compensate；CONSOLIDATE 评估 promotion；累积 buffer pressure > 现任 effective gravity 时整合（这是 Prediction 4 的 canonical case）[^v3-3]。
6. **高 gravity 条目在多个 AUDIT 周期重复与坏结果相关** → **AUDIT override**；不论 centrality 大小，走 §5.8 gravity-reduction 通路；条目通过 AUDIT 通道而**不是** CONSOLIDATE 通道失去保护[^v3-4]。
7. **底模更新引入与高 gravity 条目矛盾的新先验** → **External correction channel**；下一轮 post-update CONSOLIDATE 评审；**此行结构性依赖 §8.3 separability**[^v3-5]——若 wiki 被折进权重，该行无法实施[^src4]。

## 两条边界（论文显式承认）

- **矩阵不制造信号**：它指定"框架在 conflict 信号存在时怎么行为"，但**不**为外部不提供的信号产生信号——例如 row 3 的"safety/epistemic 外部信号"需要由外部 module 提供；
- **不定校准参数**：cycle counts、source diversity 阈值、friction 系数都是 calibration-dependent，留给实现 + 经验研究；
- **残余失败**：fully novel bad beliefs 不在底模先验中、也不被后续经验 contradict 的 case，矩阵任何一行都覆盖不到——这是 §9 named "residual" 部分。

## 操作含义

- **Row 3 是"伴侣不能只听用户的话"的硬规则**：utility-based routing 在这里**显式被关闭**——这条直接对抗 sycophancy 类失败模式；
- **Row 4 的 exception clause 不是无关条款**：默认"single-source 进 buffer"看似稳健，但 hard veto 会"结构性挡掉"权威单源（如严谨论文）的快速更新；exception 让实现保留 high-trust source 升权而**不**改写默认；
- **Row 7 是 separability 安全承诺的具体落地**：失去 separability，row 7 不可实施，整个矩阵 cross-base-model 一致性塌掉。

## References

- §5.0 矩阵全文：`data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` 第 1072–1129 行（含 legend + 7 行 + Limitation 段）。
- §1.2 程序冲突规则原则化：第 318–328 行。
- §11 conclusion 把"time-structured procedural conflict rule"列为四条 framing contribution 之二：第 2423–2431 行。
- §9 residual failure mode（无信号情况）：第 2226–2230 行。

## Footnotes

[^1]: Row 3 原文（第 1107 行附近）：
    > "User repeatedly reinforces a consistent claim that external safety or epistemic signals (when available) flag as harmful, but user-reported utility remains stable or high — Safety — Compensate regardless of utility signal. Route to AUDIT priority queue; apply the highest available friction in the CONSOLIDATE path to any attempt to integrate reinforcing content; flag high-gravity reinforcing entries for stress test. Do not mirror at the operational layer even if continuity pressure is high. ... Utility-based routing (the standard Operational→Epistemic bridge in row 2) does not trigger. Safety requires an explicit override: some reinforcement patterns must be resisted regardless of user-reported utility."

[^2]: Row 7 与 separability 强依赖原文（第 1115 行附近）：
    > "External correction channel. The wiki entry is flagged for review on the next CONSOLIDATE cycle post-update. This row depends structurally on architectural separability (§8.3): the external correction channel exists only because the wiki is not folded into base model weights. The separability commitment is what keeps this row operational across base model generations."

[^3]: 矩阵 limitation 段原文（第 1120–1129 行）：
    > "Row 7 names the base-model correction channel, but the structural residual—fully novel bad beliefs not represented in the base model and not contradicted by subsequent experience—is not captured by any row in this matrix. This is the limit acknowledged in §9 and not resolved by the routing logic. The matrix specifies how the framework behaves when the relevant conflict signal exists; it does not manufacture signal that external sources do not provide. The matrix does not define calibration parameters (e.g., cycle counts, source diversity thresholds), which are explicitly left to implementation and empirical validation."
