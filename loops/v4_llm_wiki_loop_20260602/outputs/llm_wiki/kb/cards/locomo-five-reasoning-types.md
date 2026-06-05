---
id: locomo-five-reasoning-types
title: LoCoMo 对话记忆 QA 的五类推理维度
status: accepted
card_type: distinction
tags: [QA, reasoning-types, evaluation, benchmark, agent-memory]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
justification: ../justification/locomo-five-reasoning-types.md
canonical_concept: locomo-five-reasoning-types
aliases: [LoCoMo QA 五类推理, five reasoning types for conversational memory QA]
summary: >-
  locomo-five-reasoning-types（LoCoMo QA 五类推理, five reasoning types for conversational memory QA）将对话记忆的 QA 评测分为 single-hop（36%）、multi-hop（14.6%）、temporal reasoning（20.6%）、open-domain knowledge（3.9%）、adversarial（24.9%）五类，共 7512 题，揭示了 LLM 在不同记忆维度上的差异化能力缺陷
related: [locomo-benchmark, temporal-reasoning-difficulty, long-context-adversarial-vulnerability, longmemeval-five-memory-abilities]
---

LoCoMo 评测基准将对话记忆的问答任务分为五个互补的推理类别，共 7,512 道题目[^src-1]：

1. **Single-hop**（36%，2,705 题）：答案可从单个会话中获得。人类 F1=95.1，最佳模型（GPT-3.5-turbo-16K 16K）=56.4[^src-2]。

2. **Multi-hop**（14.6%，1,104 题）：需要综合多个不同会话的信息。人类 F1=85.8，最佳模型=42.0[^src-3]。

3. **Temporal reasoning**（20.6%，1,547 题）：需要捕捉对话中的时间线索并进行时序推理。人类 F1=92.6，最佳模型=42.1。差距最大（73%）[^src-4]。

4. **Open-domain knowledge**（3.9%，285 题）：需要将说话者提供的信息与常识或世界知识整合。人类 F1=75.4，在 RAG 设置中反而可能退化（不当检索干扰参数化知识）[^src-5]。

5. **Adversarial**（24.9%，1,871 题）：设计为不可回答的陷阱题，期望模型正确识别并拒绝回答。长上下文模型在此维度最脆弱（2.1%），而 GPT-4-turbo 在 4K 窗口下达到 70.2%[^src-6]。

这种多维度分类比单一准确率指标更能揭示模型记忆能力的真实轮廓。

Mem0 论文在评测中采用了前四类（排除 adversarial），因对抗性问题缺少标准答案，展示了该分类体系在不同评测场景中的裁剪使用 [^card-1]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 4.1" -- "we introduce a question-answering task divided into five distinct reasoning categories"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table dataset_statistics + Table 2" -- "# questions single-hop: 2,705 (36%); Human=95.1; GPT-3.5-turbo-16K 16K=56.4"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table dataset_statistics + Table 2" -- "# questions multi-hop: 1,104 (14.6%); Human=85.8; best=42.0"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 1 + Table 2" -- "temporal reasoning (by 73%); Human=92.6"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 6.1" -- "LLMs struggle with open-domain knowledge and degrade in the RAG setting... introducing improper context from inaccurate retrieval can lead to a decline"
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table 2" -- "Adversarial: GPT-3.5-turbo-16K 16K=2.1; GPT-4-turbo=70.2"
[^card-1]: [LOCOMO 长期对话记忆基准测试设计](locomo-benchmark-design.md) -- Mem0 论文采用 LoCoMo 的四分类（排除 adversarial），因对抗性问题缺少标准答案
