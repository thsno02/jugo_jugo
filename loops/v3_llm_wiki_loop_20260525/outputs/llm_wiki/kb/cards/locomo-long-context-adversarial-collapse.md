---
id: locomo-long-context-adversarial-collapse
title: LoCoMo——长上下文 LLM 在 adversarial 问题上崩到 2.1%，是 "能塞 ≠ 能懂" 的清晰证据
status: accepted
card_type: source_claim
tags: [#long-context, #adversarial, #hallucination, #locomo]
created_time: 2026-05-26T15:30:00+08:00
edited_time: 2026-05-28T10:22:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
provenance_card: ../provenance/locomo-long-context-adversarial-collapse.md
aliases: ["GPT-3.5-turbo-16K adversarial 2.1%", "long-context hallucination"]
related: [locomo-three-task-evaluation-framework, locomo-event-summarization-five-error-types, graphrag-context-window-8k-optimal, longmemeval-five-core-memory-abilities, locomo-observation-rag-beats-summary-rag]
---

LoCoMo 用 adversarial 题（不可答、期望模型识别并拒答；adversarial 在 LoCoMo 评测框架中是 5 类 reasoning 之一[^v3-1]）做了一个"控制实验"，把长上下文 LLM 的隐藏缺陷暴露得很清楚：**给同一个 GPT-3.5-turbo-16K，把 context 从 4K 扩到 16K，adversarial F1 从 13.1 暴跌到 2.1**，而总体 F1 反而升到 37.8。换句话说：**喂得越多、越容易瞎编**。

**数据来源（论文 Table `tab:qa_results`）[^src1]**：

| 模型 | Context | Single-Hop | Multi-Hop | Temporal | Open-Dom | **Adversarial** | Overall |
|---|---|---|---|---|---|---|---|
| GPT-3.5-turbo | 4K | 29.9 | 23.3 | 17.5 | 29.5 | 12.8 | 22.4 |
| GPT-4-turbo | 4K | 23.4 | 23.4 | 10.4 | 24.6 | **70.2** | **32.1** |
| Llama-2-Chat-70B | 4K | 19.7 | 14.4 | 13.3 | 15.9 | 22.1 | 17.9 |
| GPT-3.5-turbo-16K | 4K | 31.7 | 25.4 | 16.8 | 27.6 | **13.1** | 24.1 |
| GPT-3.5-turbo-16K | 8K | 38.8 | 31.2 | 21.0 | 35.0 | 8.4 | 25.2 |
| GPT-3.5-turbo-16K | 12K | 51.1 | 40.4 | 25.0 | 36.5 | 6.4 | 33.5 |
| GPT-3.5-turbo-16K | 16K | **56.4** | **42.0** | 20.3 | **37.2** | **2.1** | **37.8** |

注意两组反差：

1. **同一模型、context 从 4K → 16K**：adversarial 13.1 → 8.4 → 6.4 → **2.1**（单调下降，幅度 6 倍）；
2. **同样 4K context、换 GPT-4-turbo**：adversarial **70.2**（是 GPT-3.5 的 5 倍），但 single-hop 反而不如 GPT-3.5。

这两点合在一起给出论文的结论："**LLMs can be easily misled into generating hallucinations when they are subjected to long contexts**"[^src2]。

**为什么 adversarial 会塌**：

- adversarial 题的"正解"是拒答（"对话历史里没提过这件事"）。长上下文里塞了大量无关 distractor session 时，模型的注意力分布被稀释，**更倾向"找出一个看起来沾边的句子并据此作答"**——也就是经典 hallucination 路径。
- GPT-4-turbo 在 4K context 上保持 70% 是因为它的预训练 / 指令调教让它能识别 "context 里没有就别答"；但同一模型若也跑 16K context，论文未给数字，作者推测会同样塌。

**论文挑出来的另一个现象**：长上下文 LLM **misassigns dialogs or events to the wrong speaker**[^src3]——不仅 adversarial 塌，连"谁说了什么"都搞错。这与事件摘要 §6.2 的"speaker attribution 错"是同一根因[^v3-2]（注意力分散导致 "谁" 这个维度先被丢）。GraphRAG 也观察到 8K 是文本生成在 sensemaking 任务上的甜区，超出后性能反而劣化[^v3-3]。

**操作含义**：

- 评一个 long-context LLM 的长记忆能力时，**必须包含 adversarial 控制项**；否则只看 overall F1（37.8 vs 22.4，看起来"长 context 总是更好"）会得到误导结论。
- adversarial 不是 LoCoMo 独创——LongMemEval 的 abstention（ABS）能力是同一思路的精细版本（30 题，false premise）[^v3-4]。
- RAG 视角的解决方案：**控制 retrieved context 数量**（LoCoMo 的 observation RAG 在 top-5 拿到 adversarial 44.7，远好于长上下文 16K 的 2.1）[^v3-5]。

**边界**：

- 这条结论建立在 GPT-3.5-turbo-16K 这一具体模型上；2024 之后的 Claude-3 / GPT-4o / Gemini 1.5 的长上下文 attention 大幅改进，相同实验结果未必复现。
- adversarial 题只占 25% 左右（1,871 / 7,512）[^src4]——大数据集里它不会主导 overall 分；但若只在 adversarial 子集上比，长上下文几乎全输。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` — 行 366–392 — `tab:qa_results` 完整结果。
[^src2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` — 行 444 — "long-context LLMs can comprehend longer narratives, yet they are prone to generating hallucinations. \texttt{gpt-3.5-turbo-16k} outperforms other approaches, but its performance on adversarial questions drops to a mere 2.1\%, as compared to 22.1\% using \texttt{Llama-2-Chat} and 70.2\% using \texttt{GPT-4-turbo} with 4K context windows. This indicates that LLMs can be easily misled into generating hallucinations when they are subjected to long contexts"。
[^src3]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` — 行 193 + 行 444 — "they are especially prone to misassigning dialogs or events to the wrong speaker"。
[^src4]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` — 行 657 — "# questions. adversarial & 1,871 (24.9\%)"。
[^v3-1]: [locomo-three-task-evaluation-framework](locomo-three-task-evaluation-framework.md) — adversarial 在 5 类 reasoning 中的位置。
[^v3-2]: [locomo-event-summarization-five-error-types](locomo-event-summarization-five-error-types.md) — speaker attribution 是事件摘要的第 4 类错误。
[^v3-3]: [graphrag-context-window-8k-optimal](graphrag-context-window-8k-optimal.md) — GraphRAG 也观察到 8K 是上下文窗口的甜区。
[^v3-4]: [longmemeval-five-core-memory-abilities](longmemeval-five-core-memory-abilities.md) — LongMemEval 的 abstention 是 adversarial 思路的精细版本。
[^v3-5]: [locomo-observation-rag-beats-summary-rag](locomo-observation-rag-beats-summary-rag.md) — observation top-5 让 adversarial 回到 44.7。
