---
id: etamp-pseudo-trajectory-methodology
title: Pseudo vs non-pseudo trajectory：用 PR=100% 控制变量隔离攻击效力
status: accepted
card_type: operational_rule
tags: [#agent-security, #methodology, #experimental-design, #pseudo-trajectory, #etamp]
created_time: 2026-05-26T15:20:00+08:00
edited_time: 2026-05-28T15:14:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
provenance_card: ../provenance/etamp-pseudo-trajectory-methodology.md
aliases: [pseudo trajectory ETAMP, poison rate methodology, ASR conditional on PR]
related: [etamp-environment-injected-memory-poisoning, etamp-attack-payload-structure, etamp-chaos-monkey-agent-robustness, etamp-direction-asymmetry-and-stealth, ares-mock-rag-system-evaluation-design, poisonedrag-baselines-isolate-two-conditions]
---

## 主张

Zou 等（2026）主表的所有 ASR$_B$ 数字（GPT-5-mini 32.5%、GPT-5.2 23.4% 等）用的是 **pseudo trajectory**：直接把恶意 payload 嵌进 paired 目标产品页面，**保证 Poison Rate (PR) = 100%**——即 agent 在 Task A 一定会看到污染[^src1]。论文这么做不是 cheating，是**变量隔离**——把"攻击有效性"与"infrastructure noise (页面没加载 / agent 没访问到污染页)"拆开[^src3]。这一"按条件拆分基线"的方法学，与 PoisonedRAG 把 retrieval condition 与 generation condition 通过五个基线分别消融[^v3-2]、以及 ARES 用 mock RAG 系统作为已知 ranking 锚[^v3-1] 同源。

## 两种实验配置

| 维度 | Pseudo | Non-pseudo |
| --- | --- | --- |
| 目标产品选择 | 任务配对时已知 | 运行时由 agent 自由导航 |
| 污染注入位置 | 直接嵌进目标产品页 | 嵌进 Task A 起始环境 |
| Poison Rate (PR) | 100%（构造保证） | < 100%（取决于 agent 行为） |
| 测量目标 | 纯攻击有效性 | 端到端攻击有效性（含 agent 导航 noise） |

## 关键验证：ASR$_B$ | PR ≈ Pseudo ASR$_B$

论文用 Table tab:pseudo_comparison 直接证明两种实验等价（条件化在 PR）：

| 模型 / 攻击 | Non-Pseudo PR | Non-Pseudo ASR | **Non-Pseudo ASR\|PR** | Pseudo ASR |
| --- | --- | --- | --- | --- |
| Qwen3.5-122B / Frustration | 67.1% | 2.8% | **4.2%** | 2.1% |
| GPT-OSS-120B / Baseline | 75.2% | 13.5% | **17.9%** | 19.5% |
| GPT-OSS-120B / Authority | 70.9% | 7.4% | **10.5%** | 14.5% |
| GPT-5-mini / Baseline | 75.7% | 4.6% | **6.1%** | 4.6% |
| Qwen3-32B / Baseline | 76.6% | 4.6% | **6.0%** | 4.3% |

**条件化 ASR | PR 与 pseudo ASR 平均误差 ~2 个百分点**——证明 pseudo 模式作为主表数据**是合理近似**，同时大幅降低大模型 (GPT-5.2) 跑 full pipeline 的成本[^src2]。

## 为什么这条 methodology 重要

- **PR 把两类失败拆开**：(a) 攻击文本到了 agent context 但 agent 没服从（这是攻击有效性问题）；(b) 攻击文本根本没进 agent context（这是 retrieval / navigation 问题）[^src3]。如果只报 raw ASR，两类失败混在一起，无法对比模型。
- **降低成本**：pseudo 模式可以用 clean trajectories 近似 Task A，不必为每个评测重跑大模型的 Task A——论文称之为"approximate Task A trajectories with malicious content using clean trajectories without actually running them"[^src2]。
- **方法学复用**：任何"环境注入"类研究都应区分"infrastructure success rate (PR)"和"attack-once-injected success rate (ASR | PR)"，否则跨论文 ASR 数字无法比较。

## 边界

- pseudo 模式假设"已知 paired target product"——对于实际部署时**攻击者不知道用户具体行为**的现实，仍需 non-pseudo 验证（论文也做了）；
- 论文未对 GPT-5.2 和 Qwen2.5-VL-72B 做 non-pseudo 全 pipeline（"due to cost constraints"）——所以这两个模型的 ASR 数字理论上只在 PR=100% 边界下有保证；
- "ASR | PR ≈ pseudo ASR"是经验观察，不是定理——某些攻击策略下 PR 与 ASR 可能不独立（例如 frustration 触发依赖 agent 真实失败信号，pseudo 化可能影响这些信号的真实性）。

## 操作含义

- **新评测协议**应同时报告 **PR、ASR、ASR | PR、Pseudo ASR** 四个数字；
- **比较模型时**用 ASR | PR 或 Pseudo ASR 而非 raw ASR；
- **报告攻击效力**时区分"infrastructure 可靠性"与"对齐 / 鲁棒性"两个独立轴。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` — 行 793-796 — "Our main results use pseudo trajectories where PR = 100% by construction... we directly embed the malicious instructions into the relevant page (product description or Reddit post)... non-pseudo experiments run the full pipeline where the agent navigates freely... resulting in PR < 100%."
[^src2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` — 行 794 — "Using pseudo mode also reduces cost for large models like GPT-5.2, as we can approximate Task A trajectories with malicious content using clean trajectories without actually running them; this does not affect our conclusions."
[^src3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` — 行 786-790 — "Poison Rate (PR): The fraction of Task A executions where the resulting trajectory contains the injected environment observations... Conditional ASR_B (ASR_B | PR): Attack success rate computed only over successfully poisoned task pairs, providing a cleaner measure of attack effectiveness independent of infrastructure issues."
[^v3-1]: [ares-mock-rag-system-evaluation-design](ares-mock-rag-system-evaluation-design.md) — 用已知准确率梯度的 mock 系统隔离评测变量，与 PR=100% 隔离攻击效力同构
[^v3-2]: [poisonedrag-baselines-isolate-two-conditions](poisonedrag-baselines-isolate-two-conditions.md) — 通过基线分别"丢"一个条件来消融，与 pseudo / non-pseudo 拆分同源
