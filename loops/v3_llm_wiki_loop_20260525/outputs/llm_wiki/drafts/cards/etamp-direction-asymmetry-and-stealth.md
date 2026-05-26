---
id: etamp-direction-asymmetry-and-stealth
title: 跨 site 攻击方向的非对称 ASR 与 ASR_A 接近零的攻击隐蔽性
status: draft
card_type: source_claim
tags: [#agent-security, #cross-site, #attack-stealth, #empirical-result, #etamp]
created_time: 2026-05-26T15:20:00+08:00
edited_time: 2026-05-26T15:20:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
provenance_card: ../provenance/etamp-direction-asymmetry-and-stealth.md
aliases: [ASR direction asymmetry, Shopping→Reddit highest ASR, ETAMP stealth ASR_A ≈ 0]
related: [etamp-environment-injected-memory-poisoning, etamp-capability-vs-security]
---

## 主张

Zou 等（2026）Appendix C 揭示一个 main table 看不见的事实：**eTAMP 的攻击成功率在三个 cross-site 方向上严重非对称，且 GPT-5.2 与 GPT-5-mini 的"最脆弱方向"完全不同**。同时论文用 Appendix D 数据证明 **ASR$_A$（攻击在 Task A 本身误触发）几乎为零**——即攻击对原任务**完全隐蔽**。

## 方向非对称：Table tab:direction_results 节选

记号：R→C = Reddit→Classifieds, R→S = Reddit→Shopping, **S→R = Shopping→Reddit**。

| 模型 | 策略 | Chaos | R→C | R→S | S→R |
| --- | --- | --- | --- | --- | --- |
| GPT-5-mini | Frustration | Yes | 13.1 | 26.9 | **53.4** |
| GPT-OSS-120B | Baseline | No | 2.4 | 11.8 | **40.0** |
| GPT-5.2 | Authority | No | **42.9** | 12.9 | 14.3 |
| GPT-5.2 | Frustration | Yes | **32.1** | 31.2 | 9.5 |
| Qwen3-32B | Authority | No | **11.9** | 6.5 | 0.0 |

两个 robust pattern：
1. **S→R（Shopping→Reddit）对 GPT-5-mini / GPT-OSS-120B 最易**：S→R 的攻击目标是"在 Reddit 发 fake review"——论文猜测**review 是低 stakes 动作**，agent 更愿意执行。
2. **R→C / R→S 对 GPT-5.2 / Qwen3-32B 最易**：这两个方向的攻击目标是"在购物 / 分类网站下单"。GPT-5.2 的 Authority Framing R→C 拉到 42.9%，是它所有 cell 中最高的。

**模型差异**：GPT-5.2 的方向画像与 GPT-5-mini **完全相反**——证明"哪个跨 site 方向最易被攻击"是模型 / 对齐 specific 的属性，不是任务结构 universal 属性。

## 攻击隐蔽性：ASR$_A$ ≈ 0

Table tab:non_pseudo_full（第 840–859 行）报告了所有非 pseudo 配置在 Task A 上的 premature trigger 率：

- 在 11 个 (模型, 策略) 组合中，**9 个** ASR$_A$ = 0.0%；
- 唯二的非零：Qwen3.5-122B + Authority 框架 0.4%（1 instance）、Qwen3-VL-32B + Baseline 0.7%（2 instances）；
- 都来自单个 example 的偶发触发，**远低于** ASR$_B$ 的 5–32%。

这意味着 conditional trigger 设计真的有效——**Task A 完成正常，用户对自己的 memory 已被污染毫无察觉**。这与 §2.1 中"stealth constraint"的形式化对应：「Eval(Traj(π, T_A, E_A(x))) = Eval(Traj(π, T_A, E_A))」——攻击不破坏 Task A 评估。

## 直接的工程含义

- **方向画像必须作为模型评测维度**：只看 aggregate ASR 会错过"模型 X 在方向 Y 上特别脆"的细粒度信号；
- **review 类低 stakes 动作是被低估的高危攻击面**：它们 ASR 远高于下单类高 stakes 动作；
- **基于 Task A 行为的检测不可行**：ASR$_A$ ≈ 0 意味着任何"在 Task A 时实时监控异常"的防御对 eTAMP 都失效——必须在 memory 被回调（Task B 起）才能介入，且必须先识别恶意 memory 而非只看当前任务行为。

## 边界

- 方向画像在更多模型 × 任务对上是否稳定，论文未做大规模 sweep（只有 6 个公开模型 × 280 任务对）；
- "review 是低 stakes" 的解释是论文猜测，并非实验验证；
- ASR$_A$ ≈ 0 的统计稳定性受样本量限制（每个 cell ~280 任务），0.4%/0.7% 的边缘观察可能只是 random fluctuation。

## References

- §Appendix C "Results by Attack Direction"：`data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` 第 862–899 行。
- Table tab:direction_results：第 867–892 行。
- Direction-specific patterns 论述：第 894–898 行。
- §3.3 "Attack Stealth"：第 322–324 行（ASR$_A$ 总论述）。
- Table tab:non_pseudo_full（ASR$_A$ 全表）：第 833–858 行。

## Footnotes

[^1]: Direction patterns 原文（第 894–898 行）：
    > "Shopping → Reddit shows highest vulnerability for some models. GPT-5-mini achieves 53.4% ASR_B and GPT-OSS-120B achieves 40.0% ASR_B on this direction. This may be because posting a review (the attack goal for this direction) is a lower-stakes action that agents are more willing to perform. GPT-5.2 shows different vulnerability pattern. Unlike other models, GPT-5.2 is most vulnerable on Reddit→Classifieds (32.1%) and Reddit→Shopping (31.2%), with lower ASR_B on Shopping→Reddit (9.5%). This suggests model-specific factors influence which attack directions are most effective."

[^2]: ASR$_A$ ≈ 0 论述原文（第 322–324 行）：
    > "Across all models tested (GPT-5-mini, GPT-OSS-120B, Qwen3-VL-32B, Qwen3.5-122B) and most attack strategies, ASR_A is 0%. The only exceptions are Qwen3.5-122B with authority-based triggering (0.35%) and Qwen3-VL-32B with standard injection (0.71%), each representing 1–2 premature triggers out of ~280 tasks. This confirms that our conditional trigger design successfully prevents premature activation: the attack remains dormant during Task A and only activates when trigger conditions are met during Task B on a different website."

[^3]: stealth constraint 形式化（第 577–581 行）：
    > "subject to: Eval(Traj(π, T_A, E_A(x))) = Eval(Traj(π, T_A, E_A)) ... The constraint ensures the injection remains stealthy—Task A completes normally, so the user has no indication their memory has been poisoned."
