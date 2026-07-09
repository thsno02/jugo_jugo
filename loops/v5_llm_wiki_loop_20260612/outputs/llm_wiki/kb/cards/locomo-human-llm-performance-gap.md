---
id: locomo-human-llm-performance-gap
title: LoCoMo 人类与 LLM 的长期记忆性能差距
status: accepted
card_type: finding
tags:
- human-performance
- LLM-limitation
- performance-gap
- long-term-memory
- benchmark-result
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-locomo
evidence_basis: experimental_paper
justification: ../justification/locomo-human-llm-performance-gap.md
canonical_concept: locomo-human-llm-performance-gap
aliases:
- human-LLM performance gap
- 人类与LLM长期记忆差距
- LoCoMo human baseline
summary: locomo-human-llm-performance-gap 人类与 LLM 在超长对话记忆上存在巨大差距。 Human QA overall F1=87.9，最佳模型（GPT-3.5-16K 16K context）仅37.8，差距56%。 人类在所有五类推理中均占优：single-hop 95.1 vs 56.4，temporal 92.6 vs 25.0，adversarial
  89.4 vs 70.2(GPT-4)/2.1(16K)。 即便使用 long-context LLM 或 RAG 策略可带来22-66%改善，模型仍远落后于人类水平。
related:
- locomo-evaluation-framework
- long-context-adversarial-hallucination
- locomo-temporal-reasoning-difficulty
- locomo-dataset
---
LoCoMo 基准揭示了人类与当前最先进 LLM 在长期对话记忆能力上的巨大差距。[^src-1]

Human baseline vs 最佳模型（QA F1）：
- **Overall**: Human 87.9 vs GPT-3.5-16K (16K) 37.8 -- 差距 56%
- **Single-hop**: Human 95.1 vs GPT-3.5-16K (16K) 56.4
- **Multi-hop**: Human 85.8 vs GPT-3.5-16K (16K) 42.0
- **Temporal**: Human 92.6 vs GPT-3.5-16K (12K) 25.0 -- 差距 73%
- **Open-domain**: Human 75.4 vs Observation RAG 41.9
- **Adversarial**: Human 89.4 vs GPT-4-turbo (4K) 70.2 [^src-2]

论文指出：采用 long-context LLM 或 RAG 策略可带来 22-66% 的改善（相对 base model），但模型仍"substantially lag behind human performance"。[^src-3]

时间推理差距最大（73%），表明这是当前 LLM 对话理解的核心瓶颈。[^src-4] [^card-1] [^card-2]

[^src-1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Introduction / Findings" -- "Long-context LLMs and RAG demonstrate effectiveness... but these models still substantially lag behind human performance (by 56%), especially in temporal reasoning (by 73%)"
[^src-2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table qa_results" -- "Human: Single 95.1, Multi 85.8, Temporal 92.6, Open 75.4, Adversarial 89.4, Overall 87.9"
[^src-3]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Introduction" -- "improvements ranging from 22-66%, but still significantly lag behind human levels (by 56%)"
[^src-4]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Introduction" -- "especially in temporal reasoning, (by 73%)"

[^card-1]: 与 [locomo-temporal-reasoning-difficulty] 关联——时间推理差距是性能鸿沟主因
[^card-2]: 与 [long-context-adversarial-hallucination] 关联——adversarial 问题虽 GPT-4 表现尚可但其他模型几乎完全失败
