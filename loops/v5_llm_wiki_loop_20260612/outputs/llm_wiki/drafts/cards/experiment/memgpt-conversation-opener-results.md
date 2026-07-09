---
id: memgpt-conversation-opener-results
title: MemGPT 对话开场白超越人类基线
status: draft
card_type: empirical-result
tags: [memgpt, conversation-opener, engagement, cosine-similarity, persona]
created_time: 2026-06-12T10:12:00+08:00
edited_time: 2026-06-12T10:12:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-conversation-opener-results.md
canonical_concept: conversation-opener-engagement
aliases: [对话开场白, conversation opener, engagement evaluation, CSIM]
summary: >-
  MemGPT conversation-opener-engagement 在 opener 任务中 MemGPT+GPT-4 的 SIM-1=0.868 超越 Human=0.800，因 MemGPT 生成更冗长且覆盖更多 persona 信息的 openers；working context 存储是关键因素。
related: [memgpt-dmr-task-results, memgpt-working-context-usage]
---

Conversation opener 任务评估 agent 利用长期记忆生成有吸引力开场白的能力：

**评估方法**：使用 CSIM（cosine similarity）度量 agent opener 与 gold persona labels 的相似度——SIM-1（最相似 persona 项）、SIM-3（top-3 平均）、SIM-H（与人类手写 opener 的相似度）。[^src-1]

**核心结果**：
- MemGPT + GPT-4: SIM-1=0.868, SIM-3=0.843, SIM-H=0.773
- MemGPT + GPT-4 Turbo: SIM-1=0.857, SIM-3=0.828, SIM-H=0.767
- Human baseline: SIM-1=0.800, SIM-3=0.800, SIM-H=1.000 [^src-2]

**超越人类的原因**：MemGPT 生成的 openers "更冗长且覆盖更多 persona 信息维度"——人类倾向于简短地引用一两个话题，MemGPT 则倾向全面展示已知信息。[^src-1] 论文观察到 working context 中存储的信息对生成 engaging openers 至关重要。

然而，SIM-H 指标上 MemGPT 低于 Human（0.773 vs 1.000），暗示"更全面"不等于"更自然"——MemGPT 的冗长 openers 与人类的简洁风格有差异。在真实场景中，过度引用用户信息可能显得不自然甚至令人不安。评估仅用 persona 覆盖度衡量 engagement，未考虑自然度或用户实际感受。[^src-1]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Conversation opener task -- "MemGPT tends to craft openers that are both more verbose and cover more aspects of the persona information than the human baseline."
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Table: msc-opener-task -- "GPT-4 SIM-1 0.868 SIM-3 0.843... Human 0.800 0.800 1.000"
[^card-1]: -> memgpt-dmr-task-results -- 本卡评估 MemGPT 的 engagement 能力，该卡评估其一致性（consistency）能力
[^card-2]: -> memgpt-working-context-usage -- 本卡展示 working context 对 opener 质量的重要性，该卡描述 working context 的详细功能
