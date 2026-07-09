---
id: chaos-monkey-agent-stress-testing
title: Chaos Monkey 式 Agent 环境压力测试
status: draft
card_type: evaluation-method
tags: [chaos-engineering, agent-robustness, stress-testing, web-agent]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
evidence_basis: experimental_paper
justification: ../justification/chaos-monkey-agent-stress-testing.md
canonical_concept: chaos-monkey-agent-stress-testing
aliases: [Chaos Monkey, Agent Chaos Monkey, 混沌猴子, Agent 环境扰动, chaos engineering for agents]
summary: >-
  受 Netflix Chaos Monkey 启发，eTAMP 论文提出针对 Web Agent 的环境压力测试方法。在 Task B 执行期间对 Agent 动作施加概率性变换：Click Drop(p=0.4 点击变空操作)、Scroll Swap(p=1 方向反转)、Type Transform(p=1 Caesar 密码替换文本)。模拟现实网络延迟、UI 不响应、键盘故障等不确定环境。最大步数从 15 增至 37 以保证任务仍可完成但显著困难化。Chaos Monkey 使平均步数翻倍，大部分模型 TSR 下降。
related: []
---

Chaos Monkey 借鉴混沌工程原则（通过受控故障注入测试系统韧性），对 Agent 在 Task B 期间的动作施加概率性变换：[^src-1]

- **Click Drop**: 点击以 p=0.4 概率变为空操作，模拟 UI 不响应/网络延迟丢失点击
- **Scroll Swap**: 滚动方向以 p=1 概率反转，模拟意外页面行为
- **Type Transform**: 输入文本以 p=1 概率经 Caesar 密码确定性变换，模拟键盘/输入字段故障

这些参数设置使任务仍可完成但显著困难化。[^src-2] [^card-1]

实验效果：Chaos Monkey 大致使完成任务所需步数翻倍（如 GPT-5-mini 从 7.7 步增至 17.7 步），多数模型 TSR 下降。GPT-5.2 在 Chaos 下 TSR 略升(13.0%→14.8%)，可能因更高步数上限允许重试。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Chaos Monkey" P1 -- "Inspired by chaos engineering principles that test system resilience through controlled failure injection"
[^src-2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Chaos Monkey" P2 -- "With p_click=0.4, p_scroll=1, and p_type=1, tasks remain completable but significantly harder."
[^src-3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Impact of Chaos Monkey" P2 -- "Chaos Monkey roughly doubles the number of steps required while reducing TSR for most models."

[^card-1]: -> frustration-exploitation-attack
