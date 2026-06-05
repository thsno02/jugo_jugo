---
id: temporal-reasoning-difficulty
title: 时序推理是 LLM 对话记忆中最困难的能力维度
status: accepted
card_type: source_claim
tags: [temporal-reasoning, agent-memory, evaluation, benchmark, difficulty]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
justification: ../justification/temporal-reasoning-difficulty.md
canonical_concept: temporal-reasoning-difficulty
aliases: [时序推理困难, temporal reasoning difficulty in dialogue]
summary: >-
  temporal-reasoning-difficulty（时序推理困难, temporal reasoning difficulty in dialogue）LoCoMo QA 中时序推理与人类差距最大（73%），即便最佳 RAG（observation）也仅达 42.1 vs 人类 92.6，LLM 难以理解对话中的时间概念和时序线索，与独立时序推理基准 TRAM 的发现一致
related: [locomo-benchmark, temporal-event-graph-grounding, long-context-comprehension-illusion]
---

LoCoMo 基准测试中，时序推理（temporal reasoning）被确认为 LLM 对话记忆中最困难的能力维度之一[^src-1]。该类问题要求模型捕捉对话中的时间相关数据线索并进行时序推理。

人类在时序推理问题上达到 F1=92.6，而最佳方法（RAG + observation top-10）仅达 42.1，差距达 73%[^src-2]。即便长上下文模型（GPT-3.5-turbo-16K，12K 窗口）也仅达 25.0，基座模型中最好的 GPT-3.5-turbo 也仅 17.5[^src-3]。

值得注意的是，RAG 使用 observation 作为检索单元在时序推理上显著优于使用原始对话（41.9 vs. 21.3，top-5），这可能因为 observation 在提取时已经将时间信息编码为更明确的断言形式[^src-4]。

论文指出，LLM 在理解对话中的时间概念方面面临根本性挑战，这与专门针对 LLM 时序推理能力的 TRAM 基准的发现一致[^src-5]。这意味着对话中的时间推理不仅涉及事实检索，还要求模型理解事件之间的先后顺序、持续时间和时间间隔。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 1" -- "still significantly lag behind human levels (by 56%), especially in temporal reasoning, (by 73%)"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table 2" -- "Human Temporal=92.6; Table 3: Observation top-10 Temporal=42.1"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table 2" -- "GPT-3.5-turbo-16K 12K Temporal=25.0; GPT-3.5-turbo Temporal=17.5"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table 3" -- "Observation top-5 Temporal=41.9 vs Dialog top-5 Temporal=21.3"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 6.1" -- "LLMs face challenges in understanding time concepts within dialogues, which is consistent with findings from other single-turn-based benchmarks focused on temporal reasoning capabilities for LLMs (TRAM)"
