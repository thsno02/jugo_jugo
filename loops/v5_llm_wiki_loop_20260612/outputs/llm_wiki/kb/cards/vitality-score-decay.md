---
id: vitality-score-decay
title: 活力分数与 DECAY 操作
status: accepted
card_type: mechanism-specification
tags:
- vitality
- decay
- retention
- utility-signal
- companion-memory
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-memory-as-metabolism
evidence_basis: theoretical_paper
justification: ../justification/vitality-score-decay.md
canonical_concept: vitality-score-decay
aliases:
- vitality score
- DECAY
- survival-weighted retention
- task_predictive_utility
- 活力分数
- 衰减操作
summary: vitality score 活力分数是 DECAY 操作中每个活跃维基条目的保留信号， 公式为 vitality(entry) = recency_weight*(1/days_since_access) + frequency_weight*access_count + utility_weight*task_predictive_utility(entry) + gravity_weight*memory_gravity(entry)
  - wear_penalty*summarization_distortion(entry)。 DECAY 连续运行于活跃维基，属于 mirror 机制（操作连续性）。 活力低于阈值的条目被压缩为摘要形式而非删除——信息优雅退化。 引力保护底线优先：G_i^base 高于底线的条目即使活力低也免于压缩。 task_predictive_utility 的操作定义是开放问题：延迟噪声用户反馈下的信用分配。
related:
- memory-gravity-mechanism
- mirror-vs-compensate-principle
- pragmatist-truth-via-consequences
---
DECAY 连续运行于活跃维基。每个条目携带活力分数（vitality score），反映其对用户有用结果的贡献加上其在维基自身一致性中的结构角色。[^src-1]

活力公式：
```
vitality(entry) =
    recency_weight   * (1 / days_since_access)
  + frequency_weight * access_count
  + utility_weight   * task_predictive_utility(entry)
  + gravity_weight   * memory_gravity(entry)
  - wear_penalty     * summarization_distortion(entry)
```
[^src-2]

task_predictive_utility 是效用信号：基于此条目行动是否产生了用户判断为有用的结果？在 mirror-vs-compensate 原则下这是 mirror 机制——系统应该保留操作上为用户服务的内容。防止活力函数坍缩为纯满意度追逐的是引力项——对维基自身一致性负载承载的条目即使在直接意义上很少有用也被保护。[^src-3]

活力低于阈值的条目被压缩为摘要形式而非删除。信息优雅退化。活力驱动的压缩不覆盖引力保护底线：G_i^base 高于底线的条目免于压缩——这保留了"安静基础"保证。[^src-4]

一致性不变量：MUST 按规定应用活力公式（允许本地权重调优，不允许项消除）；MUST NOT 衰减 G_i^base 高于引力保护底线的条目；MUST 压缩而非删除衰减资格条目。[^src-5]

task_predictive_utility 的操作定义是论文承认的开放问题：延迟和噪声用户反馈下的信用分配是真实问题，框架未解决。[^src-6]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.3 DECAY" P1 -- "DECAY runs continuously over the active wiki. Every entry carries a vitality score reflecting its contribution to the user's useful outcomes plus its structural role"
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.3" P2 -- "vitality(entry) = recency_weight * (1 / days_since_access) + frequency_weight * access_count..."
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.3" P3 -- "What prevents the vitality function from collapsing into pure satisfaction-chasing is the gravity term"
[^src-4]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.3" P4 -- "Entries below the vitality threshold are compressed into summary form rather than deleted...does not override the gravity-protection floor"
[^src-5]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "7.5 Conformance DECAY" -- "MUST apply the vitality formula as specified...MUST NOT decay entries whose base gravity G_i^base remains above the gravity-protection floor"
[^src-6]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "9. Limitations" P3 -- "Credit assignment under delayed and noisy user feedback is a real problem the framework does not solve."

[^card-1]: memory-gravity-mechanism — 引力项在活力公式中防止纯满意度追逐
