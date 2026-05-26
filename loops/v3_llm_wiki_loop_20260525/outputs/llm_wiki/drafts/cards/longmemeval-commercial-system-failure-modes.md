---
id: longmemeval-commercial-system-failure-modes
title: LongMemEval pilot study——ChatGPT 与 Coze 在长记忆上的两种失败模式
status: draft
card_type: source_claim
tags: [#long-term-memory, #failure-modes, #commercial-systems, #benchmark]
created_time: 2026-05-26T15:21:00+08:00
edited_time: 2026-05-26T15:21:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
provenance_card: ../provenance/longmemeval-commercial-system-failure-modes.md
aliases: ["ChatGPT memory failure", "Coze memory failure", "LongMemEval pilot"]
related: [longmemeval-five-core-memory-abilities, longmemeval-benchmark-construction-pipeline, longmemeval-three-stage-memory-framework, mem0-baseline-failure-modes, locomo-long-context-adversarial-collapse]
---

LongMemEval 论文里最容易被忽视的一节是 §3.4 pilot study——作者拿 97 道题、3–6 个 session 的 *缩水版* 历史（约 LongMemEval-S 的 1/10）去实测 ChatGPT 与 Coze 这两个商业 memory-augmented 助手。结论是：**两个系统都比直接拿全文重读（offline reading）掉 30%–64%**，而且失败模式互不相同——这是 "把 user 事实存起来" 不等于 "拥有长期记忆" 的最直接证据。

**实测数字**：

| 系统 | LLM | Accuracy | vs offline reading 落差 |
|---|---|---|---|
| Offline Reading | GPT-4o | 0.9184 | — |
| ChatGPT | GPT-4o | 0.5773 | **-37%** |
| ChatGPT | GPT-4o-mini | 0.7113 | -22% |
| Coze | GPT-4o | 0.3299 | **-64%** |
| Coze | GPT-3.5-turbo | 0.2474 | -69% |

注意：用更弱的 GPT-4o-mini 反而比 GPT-4o 在 ChatGPT 里跑得高——说明这不是模型能力问题，而是 memory 子系统的失败。

**ChatGPT 的失败模式：覆盖式压缩。**

- 行为：evidence statement 一出现就被立刻 record 下来；
- 失败：随着对话推进，ChatGPT 把历史 "compress" 成更短的 fact 时，会**修改**之前记下的内容（典型如"用户的车型"被覆盖成"用户喜欢电动车"），原始信息丢失。
- 对应 5 类能力里：**KU（Knowledge Update）失败** —— 不是不会更新，而是更新得太激进，把不该改的也改了。

**Coze 的失败模式：拒绝间接表达。**

- 行为：只 record "用户直接陈述" 的事实；
- 失败：当 LongMemEval 的 evidence 通过 *间接* 方式表达（"帮我查车保险" → 隐含 "我有车"）时，Coze 根本没把这件事存进 memory。
- 对应 5 类能力里：**IE（Information Extraction）失败** —— 在事实抽取阶段就漏掉了。

**人工评估细节（appendix）**：

跨四类能力（IE / MR / KU / TR）做的 5 标注员人工评分进一步暴露：

| 系统 | IE | MR | KU | TR |
|---|---|---|---|---|
| ChatGPT (GPT-4o-mini) | 1.000 | 0.647 | 0.667 | 0.652 |
| ChatGPT (GPT-4o) | 0.688 | 0.441 | 0.833 | 0.435 |
| Coze (GPT-3.5) | 0.625 | 0.118 | 0.375 | 0.043 |
| Coze (GPT-4o) | 0.813 | 0.147 | 0.208 | 0.391 |

- ChatGPT IE 高（1.0 / GPT-4o-mini）—— 能记单 session 事实，但 MR / TR 立刻跌；
- Coze 跨 session 推理（MR）和时间推理（TR）都接近 0 —— "用户事实仓库" 模型先天没把跨 session 关联织进结构。

**长上下文 LLM 也不是出路**：

同一节 pilot 还测了 GPT-4o / Llama-3.1-70B / Phi-3 等长上下文 LLM 直读 LongMemEval-S（~115K token）：**30–60% 准确率掉幅**（相对只读 oracle evidence session）。即便加 Chain-of-Note 也救不回。这说明 "把全文塞进 context" 与 "理解全文" 之间存在系统性 gap。

**操作含义 / 设计警示**：

- **不要假设"我存了 user fact = 我有长期记忆"**——存了之后能否原样取出、能否跨 session 关联、能否拒答未发生的事实，都是独立的能力。
- 真实产品里 ChatGPT 类系统的 KU 失败最隐蔽——表面看每次都"记得"，但事实被偷偷篡改。用户察觉时已经迟了。
- Coze 类系统的 IE 失败比 ChatGPT 类更容易调试——只要 evidence 间接表达，failure 就稳定可复现。

## References

- §3.4 LongMemEval represents a significant challenge：`data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` 行 1402–1412。
- 商业系统 pilot 数字表 `fig:proof-of-difficulty-commercial-systems`：行 156–166。
- ChatGPT 失败模式描述："ChatGPT generally records the evidence statements immediately after it has been presented in the evidence session. However, as the interaction proceeds, ChatGPT often modify this information when it compresses the history"——行 1629。
- Coze 失败模式："Coze often failed to record indirectly provided user information."——行 1407。
- 长上下文 LLM 在 LongMemEval-S 掉 30–60%：行 1412 + 表 `fig:proof-of-difficulty-long-context`（行 175–195）。
- 5 标注员人工评分（按能力类）：行 1631–1651（`tab:commercial-system-detailed`）。

## Footnotes

- "Both ChatGPT and Coze exhibited significant performance drops compared to offline reading, underscoring the challenging nature of \BENCHMARK{}."——行 1407。
- "this result highlights the \textbf{gap between building a seemingly personalized chat assistant by recalling isolated facts and demonstrating a genuinely strong memory ability}."——行 1407。
- 评测周期与样本规模："97 questions and created a short chat history of 3-6 sessions (approximately 10x shorter than \BENCHMARK\textsubscript{\textsc{S}})"，"All evaluations were conducted in the first two weeks of August 2024."——行 1407 + 行 1627。
- 长上下文 LLM 30–60% 掉幅："these LLMs showed a 30\% to 60\% performance decline when tasked with reading the entire \BENCHMARK\textsubscript{\textsc{S}} history, regardless of whether the chain-of-note technique was applied"——行 1412。
