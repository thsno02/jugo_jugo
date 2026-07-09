---
id: long-context-adversarial-hallucination
title: 长上下文 LLM 对抗性幻觉加剧
status: accepted
card_type: finding
tags:
- long-context-llm
- adversarial
- hallucination
- context-window
- lost-in-the-middle
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-locomo
evidence_basis: experimental_paper
justification: ../justification/long-context-adversarial-hallucination.md
canonical_concept: long-context-adversarial-hallucination
aliases:
- adversarial hallucination in long context
- 长上下文对抗性幻觉
- long-context LLM hallucination vulnerability
summary: long-context-adversarial-hallucination 长上下文 LLM 对抗性幻觉加剧现象。GPT-3.5-turbo-16K 在16K context 下 adversarial QA F1 仅2.1%，而 GPT-4-turbo 在4K下为70.2%。上下文窗口增大导致模型更易被诱导生成幻觉、错误归因 speaker，尤其在 adversarial questions（设计为不可回答）上几乎完全失败。论文据此推测长上下文模型在
  long contexts 中更易受误导。
related:
- locomo-evaluation-framework
- locomo-dataset
- locomo-event-summarization-degradation
- locomo-human-llm-performance-gap
---

长上下文 LLM 在处理超长对话时表现出严重的对抗性幻觉脆弱性。[^src-1]

实验数据：GPT-3.5-turbo-16K 在 16K context 下，adversarial 问题 F1 score 仅为 2.1%。随上下文窗口从 4K 增加到 16K，adversarial 性能单调下降（13.1% -> 8.4% -> 6.4% -> 2.1%）。作为对比，GPT-4-turbo 在 4K 有限上下文下 adversarial F1 达 70.2%。[^src-2]

论文指出：LLMs 在面对长上下文时更容易被误导生成幻觉（"can be easily misled into generating hallucinations when they are subjected to long contexts"）。模型尤其容易将对话或事件错误归因给错误的 speaker。[^src-3]

这一发现与 "Lost in the Middle"（Liu et al., 2024）中长上下文模型无法稳健利用中部信息的结论一致。[^src-4] [^card-1]

[^src-1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Question Answering Task Results" -- "long-context LLMs can comprehend longer narratives, yet they are prone to generating hallucinations"
[^src-2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table qa_results" -- "GPT-3.5-turbo-16K: 16K context Adversarial 2.1%; GPT-4-turbo 4K context Adversarial 70.2%"
[^src-3]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "QA Results" -- "LLMs can be easily misled into generating hallucinations when they are subjected to long contexts... especially prone to misassigning dialogs or events to the wrong speaker"
[^src-4]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Event Summarization Results" -- "long-context models may not be proficient at utilizing their context appropriately, which also aligns with similar findings in Li et al. (2023)"

[^card-1]: 与 [locomo-evaluation-framework] 关联——此发现来自 QA 任务 adversarial 类型
