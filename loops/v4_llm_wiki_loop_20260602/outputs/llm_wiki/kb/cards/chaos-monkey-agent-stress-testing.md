---
id: chaos-monkey-agent-stress-testing
title: Chaos Monkey 式 Agent 压力测试
status: accepted
card_type: mechanism
tags: [chaos-engineering, agent-robustness, stress-testing, environmental-perturbation, evaluation]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
justification: ../justification/chaos-monkey-agent-stress-testing.md
canonical_concept: chaos-monkey-agent-stress-testing
aliases: [Chaos Monkey for agents, agent压力测试, 混沌猴子agent测试, agent chaos engineering]
summary: >-
  chaos-monkey-agent-stress-testing（Chaos Monkey for agents / agent压力测试）借鉴混沌工程原理，对 web agent 的操作施加概率性扰动（点击丢弃 p=0.4、滚动方向反转 p=1、输入文本 Caesar 密码变换 p=1）来模拟真实部署中的网络延迟、UI 故障等环境噪声，系统性地测试 agent 在压力下的鲁棒性和安全性
related: [audit-stress-test]
  - frustration-exploitation-attack
  - etamp-environment-memory-poisoning
---

eTAMP 论文借鉴 Netflix 混沌工程（Chaos Engineering）原理，提出将 Chaos Monkey 方法应用于 web agent 的鲁棒性测试 [^src-1]。该方法对 agent 在 Task B 执行期间的操作施加三种概率性扰动：**Click Drop**——点击操作以概率 p_click=0.4 被随机转换为空操作，模拟 UI 无响应或网络延迟导致的点击丢失；**Scroll Swap**——滚动方向以概率 p_scroll=1 被反转，模拟意外的页面行为；**Type Transform**——输入文本以概率 p_type=1 通过 Caesar 密码替换进行确定性变换，模拟键盘或输入框故障 [^src-2]。

在这些参数设置下，任务仍然是可完成的，但显著增加了难度。为公平起见，启用 Chaos Monkey 时最大允许步数从 15 步增加到 37 步 [^src-3]。实验数据显示 Chaos Monkey 大约将所需的平均步数翻倍（如 GPT-5-mini 从 7.7 步增至 17.7 步），同时降低大多数模型的任务成功率 [^src-4]。

该方法的价值在于揭示了一个此前被忽视的安全维度：真实世界的 web 环境本质上是有噪声的，而这种噪声不仅影响功能性，还会显著改变 agent 的安全特性。

Chaos Monkey 式压力测试通过外部环境扰动注入来考验 agent 的操作鲁棒性，这与伴侣记忆框架的 AUDIT 压力测试形成对比——AUDIT 通过内省式减法（移除知识条目后观察退化）来考验知识的功能必要性[^dist-1]。两者代表了 agent 压力测试的两种正交范式。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Introduction -- "Inspired by chaos engineering principles that test system resilience through controlled failure injection, we introduce Chaos Monkey to study whether such stress creates a 'frustration window' where agents become more susceptible to manipulation."
[^src-2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Chaos Monkey -- "Click Drop: Click actions are randomly converted to no-ops with probability p_click... Scroll Swap: Scroll directions are inverted... Type Transform: Typed text is deterministically transformed using character substitution (Caesar cipher)"
[^src-3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Chaos Monkey -- "With p_click = 0.4, p_scroll = 1, and p_type = 1, tasks remain completable but significantly harder. The maximum allowed steps was increased from 15 (without chaos) to 37 (chaos)"
[^src-4]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Table 2 caption -- "Chaos Monkey roughly doubles the number of steps required while reducing TSR for most models."
[^dist-1]: [AUDIT 结构性压力测试](audit-stress-test.md) -- 本卡通过外部环境扰动测试 agent 操作鲁棒性（注入噪声后观察存活），该卡通过内部减法测试知识功能必要性（悬挂条目后观察退化）；区分点在于压力方向——外向环境噪声 vs 内向知识审查
