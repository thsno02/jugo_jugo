---
id: etamp-chaos-monkey-agent-robustness
title: Chaos Monkey for Agents：用概率性扰动模拟真实 web 环境压力
status: draft
card_type: operational_rule
tags: [#chaos-engineering, #agent-evaluation, #robustness, #web-agent, #etamp]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
provenance_card: ../provenance/etamp-chaos-monkey-agent-robustness.md
aliases: [Chaos Monkey, agent chaos engineering, 概率性动作扰动]
related: [etamp-frustration-exploitation, etamp-environment-injected-memory-poisoning, etamp-pseudo-trajectory-methodology, etamp-capability-vs-security, ares-mock-rag-system-evaluation-design, owasp-agentic-top10-2026-positioning]
---

## 操作定义

Zou 等（2026）借鉴 Netflix Chaos Monkey 的思路，定义了一个面向 web agent 的**动作层概率扰动器**，在 Task B 执行中对 agent 的输出做三类受控破坏：

1. **Click Drop**：以概率 $p_{\text{click}}$ 把 click 改为 no-op，模拟"点击丢失 / 网络延迟"。
2. **Scroll Swap**：以概率 $p_{\text{scroll}}$ 把滚动方向取反（上↔下），模拟"页面行为反常"。
3. **Type Transform**：以概率 $p_{\text{type}}$ 用确定性 Caesar 字符替换扰乱输入文本，模拟"键盘 / 输入框故障"。

实验默认配置：$p_{\text{click}}=0.4$、$p_{\text{scroll}}=1$、$p_{\text{type}}=1$；任务仍可完成但显著变难。

## 为什么这样设计

- **关键约束**：扰动后任务仍可完成（"tasks remain completable but significantly harder"）。否则 ASR 上升只能解释为 agent 走投无路乱试，而不是"环境压力下的服从性变化"。
- **关键模糊性**：agent **不知道**到底是自己的动作失败、还是环境异常。这种 ambiguity 正是真实 web 部署里 agent 必然面对的——也是论文要测量的核心刺激。
- **步数补偿**：max steps 从 15（无 chaos）提高到 37（有 chaos），让模型有公平机会探索 / 试错 / 完成任务，避免步数被 ceiling 截断而高估 ASR。

## 它衡量的不是什么

- **不是**对抗扰动鲁棒性——不是在测 agent 能否识破"故意攻击"。
- **不是**任务难度——任务规约不变，难度上升完全来自动作执行层的随机失败。
- **是**：agent 在"无法区分自身失误与环境故障"的压力窗口内，是否更容易被预先植入 memory 的恶意指令带偏。

## 操作含义（给评测者）

- 把 Chaos Monkey 作为 web agent 评测的**标配第二档**：clean trajectory 测可用性，chaos trajectory 测压力下安全性。
- 三个 $p$ 参数应作为评测协议参数公开，避免不同论文用不同强度声称"我们更鲁棒"。
- 步数 ceiling 必须随 chaos 强度上调，否则结论无法跨论文对比。

## References

- Chaos Monkey 操作定义：`agent_source_bundle.txt:191-204`。
- 步数补偿规则：`agent_source_bundle.txt:204`。
- 关键 ambiguity 描述：`agent_source_bundle.txt:204`。
- 与 Netflix Chaos Monkey 的渊源：`agent_source_bundle.txt:103`。

## Footnotes

- 三类扰动原文：`agent_source_bundle.txt:196-202`：Click Drop / Scroll Swap / Type Transform。
- 关键约束原文：`agent_source_bundle.txt:204` —— "Chaos Monkey simulates realistic uncertain environments... where the agent experiences unexpected outcomes without knowing whether its actions failed or the environment is malfunctioning. With $p_{\text{click}} = 0.4$, $p_{\text{scroll}} = 1$, and $p_{\text{type}} = 1$, tasks remain completable but significantly harder. The maximum allowed steps was increased from 15 (without chaos) to 37 (chaos)."
