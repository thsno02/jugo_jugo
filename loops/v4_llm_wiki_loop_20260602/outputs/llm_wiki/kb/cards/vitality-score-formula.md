---
id: vitality-score-formula
title: 活力评分公式
status: accepted
card_type: mechanism
tags: [companion-memory, vitality, retention, decay, multi-signal, utility]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/vitality-score-formula.md
canonical_concept: vitality-score-formula
aliases: [活力评分, vitality score, 生存加权保留, survival-weighted retention, DECAY 公式]
summary: >-
  vitality-score-formula（活力评分 / vitality score / survival-weighted retention）伴侣记忆框架中 DECAY 操作使用的多信号保留度量：recency + frequency + task_predictive_utility + memory_gravity - summarization_distortion；引力项防止纯满意度追逐、效用项防止纯结构僵化；低于阈值的条目被压缩而非删除
related: [memory-gravity, memory-lifecycle-metadata, companion-knowledge-system]
---

活力评分（vitality score）是伴侣记忆框架中 DECAY 操作持续应用于活跃 wiki 每个条目的多信号保留度量[^src-1]：

```
vitality(entry) =
    recency_weight   * (1 / days_since_access)
  + frequency_weight * access_count
  + utility_weight   * task_predictive_utility(entry)
  + gravity_weight   * memory_gravity(entry)
  - wear_penalty     * summarization_distortion(entry)
```

**各信号的角色**[^src-2]：
- **recency**（近因性）：最近访问的时间距离
- **frequency**（频率）：访问次数
- **task_predictive_utility**（任务预测效用）：基于该条目行动是否产生用户判断为有用的结果
- **memory_gravity**（记忆引力）：条目对 wiki 自身连贯性的结构角色
- **summarization_distortion**（摘要失真）：磨损惩罚，反映压缩累积的信息损失

**防止单信号主导**：纯近因性保留流行噪声；纯访问频率惩罚安静基础；纯效用创造满意度追逐的回音室。引力项保护对 wiki 连贯性具有承重作用但很少直接有用的条目[^src-3]。

**优雅降级**：低于活力阈值的条目被压缩为摘要形式而非删除——信息优雅降级。但活力驱动的压缩不覆盖引力保护下限：基础引力 G_i^base 保持在下限之上的条目即使活力评分降低也受保护[^src-4]。

**三力架构分离**：引力保护结构承重条目，效用通过活力驱动衰减，AUDIT 剥离被证明不再承重的高引力条目的保护。三力保持独立；将效用折叠进引力会坍缩两个不同机制[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.3" -- "DECAY runs continuously over the active wiki. Every entry carries a vitality score"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.3" -- vitality formula
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Abstract" -- "Pure recency retains popular noise; pure access frequency punishes quiet foundations; pure utility creates a satisfaction-chasing echo chamber."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.3" -- "Entries below the vitality threshold are compressed into summary form rather than deleted. Information degrades gracefully."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.6" -- "gravity protects structurally load-bearing entries, utility drives vitality-based decay through §5.3, and AUDIT is the mechanism that strips protection"
