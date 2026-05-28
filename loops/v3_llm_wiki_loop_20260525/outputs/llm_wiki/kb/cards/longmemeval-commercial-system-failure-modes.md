---
id: longmemeval-commercial-system-failure-modes
title: LongMemEval pilot study——ChatGPT 与 Coze 在长记忆上的两种失败模式
status: accepted
card_type: source_claim
tags: [#long-term-memory, #failure-modes, #commercial-systems, #benchmark]
created_time: 2026-05-26T15:21:00+08:00
edited_time: 2026-05-28T10:34:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
provenance_card: ../provenance/longmemeval-commercial-system-failure-modes.md
aliases: ["ChatGPT memory failure", "Coze memory failure", "LongMemEval pilot"]
related: [longmemeval-five-core-memory-abilities, longmemeval-benchmark-construction-pipeline, longmemeval-three-stage-memory-framework, mem0-baseline-failure-modes, locomo-long-context-adversarial-collapse]
---

LongMemEval 论文里最容易被忽视的一节是 §3.4 pilot study——作者拿 97 道题、3–6 个 session 的 *缩水版* 历史（约 LongMemEval-S 的 1/10）去实测 ChatGPT 与 Coze 这两个商业 memory-augmented 助手[^src1]。结论是：**两个系统都比直接拿全文重读（offline reading）掉 30%–64%**[^src2]，而且失败模式互不相同——这是 "把 user 事实存起来" 不等于 "拥有长期记忆" 的最直接证据。

**实测数字**[^src3]：

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
- 失败：随着对话推进，ChatGPT 把历史 "compress" 成更短的 fact 时，会**修改**之前记下的内容（典型如"用户的车型"被覆盖成"用户喜欢电动车"），原始信息丢失[^src4]。这正是 LightMem case study 用 "Tokyo → Kyoto" 反例论证 hard update 危险的现实证据[^v3-1]。
- 对应 5 类能力里：**KU（Knowledge Update）失败**[^v3-2] —— 不是不会更新，而是更新得太激进，把不该改的也改了。

**Coze 的失败模式：拒绝间接表达。**

- 行为：只 record "用户直接陈述" 的事实；
- 失败：当 LongMemEval 的 evidence 通过 *间接* 方式表达（"帮我查车保险" → 隐含 "我有车"）时[^v3-3]，Coze 根本没把这件事存进 memory[^src5]。
- 对应 5 类能力里：**IE（Information Extraction）失败** —— 在事实抽取阶段就漏掉了。这与 Mem0 自己分析的 baseline 失败模式（full-context / RAG / OpenAI memory 在 LoCoMo 上各类掉分）属于同源问题[^v3-4]。

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

同一节 pilot 还测了 GPT-4o / Llama-3.1-70B / Phi-3 等长上下文 LLM 直读 LongMemEval-S（~115K token）：**30–60% 准确率掉幅**（相对只读 oracle evidence session）[^src6]。即便加 Chain-of-Note 也救不回[^v3-5]。这说明 "把全文塞进 context" 与 "理解全文" 之间存在系统性 gap，与 LoCoMo 长上下文 adversarial 塌陷[^v3-6] 是同一现象的不同切面。

**操作含义 / 设计警示**：

- **不要假设"我存了 user fact = 我有长期记忆"**[^src7]——存了之后能否原样取出、能否跨 session 关联、能否拒答未发生的事实，都是独立的能力。
- 真实产品里 ChatGPT 类系统的 KU 失败最隐蔽——表面看每次都"记得"，但事实被偷偷篡改。用户察觉时已经迟了。
- Coze 类系统的 IE 失败比 ChatGPT 类更容易调试——只要 evidence 间接表达，failure 就稳定可复现。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 行 1402–1412（§3.4 LongMemEval represents a significant challenge）+ 行 1627 — "97 questions and created a short chat history of 3-6 sessions (approximately 10x shorter than \BENCHMARK\textsubscript{\textsc{S}})"。
[^src2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 行 1407 — "Both ChatGPT and Coze exhibited significant performance drops compared to offline reading, underscoring the challenging nature of \BENCHMARK{}."
[^src3]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 行 156–166（`fig:proof-of-difficulty-commercial-systems`）— 商业系统 pilot 数字表。
[^src4]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 行 1629 — "ChatGPT generally records the evidence statements immediately after it has been presented in the evidence session. However, as the interaction proceeds, ChatGPT often modify this information when it compresses the history"。
[^src5]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 行 1407 — "Coze often failed to record indirectly provided user information."
[^src6]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 行 1412 + 行 175–195（`fig:proof-of-difficulty-long-context`）— "these LLMs showed a 30\% to 60\% performance decline when tasked with reading the entire \BENCHMARK\textsubscript{\textsc{S}} history, regardless of whether the chain-of-note technique was applied"。
[^src7]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 行 1407 — "this result highlights the \textbf{gap between building a seemingly personalized chat assistant by recalling isolated facts and demonstrating a genuinely strong memory ability}."
[^v3-1]: [lightmem-sleep-time-offline-parallel-update](lightmem-sleep-time-offline-parallel-update.md) — Tokyo/Kyoto case 是 hard update 危险的另一例证。
[^v3-2]: [longmemeval-five-core-memory-abilities](longmemeval-five-core-memory-abilities.md) — KU/IE/MR/TR/ABS 五能力定义。
[^v3-3]: [longmemeval-benchmark-construction-pipeline](longmemeval-benchmark-construction-pipeline.md) — evidence 间接表达是 pipeline 第 4 步刻意设计的难点。
[^v3-4]: [mem0-baseline-failure-modes](mem0-baseline-failure-modes.md) — Mem0 自己拆解的 baseline 失败模式。
[^v3-5]: [longmemeval-chain-of-note-and-json-reading](longmemeval-chain-of-note-and-json-reading.md) — Chain-of-Note 在 reading 阶段虽有用，对长上下文直读救不回 30–60% 掉幅。
[^v3-6]: [locomo-long-context-adversarial-collapse](locomo-long-context-adversarial-collapse.md) — LoCoMo 上长上下文 adversarial 2.1% 的同源现象。
