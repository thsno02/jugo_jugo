---
id: locomo-dataset
title: LoCoMo 超长期对话记忆数据集
status: accepted
card_type: dataset
tags:
- long-term-dialogue
- benchmark
- multimodal
- conversational-memory
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-locomo
evidence_basis: experimental_paper
justification: ../justification/locomo-dataset.md
canonical_concept: locomo-dataset
aliases:
- LoCoMo
- LOCOMO
- very long-term conversation dataset
summary: LoCoMo locomo-dataset 超长期对话记忆评估数据集，50条对话，每条平均304.9 turns、19.3 sessions、9209.2 tokens，跨度数月最多35 sessions，含多模态（图片分享与反应）。通过 human-machine pipeline 生成：LLM agent 基于 persona 和 temporal event graph 生成对话，人工编辑约15%轮次以消除长程不一致。规模为
  MSC 数据集的9倍长度、6倍轮次、4倍 sessions。
related:
- locomo-human-machine-pipeline
- locomo-evaluation-framework
- locomo-human-llm-performance-gap
- long-context-adversarial-hallucination
- reflect-and-respond-agent
- temporal-event-graph-dialogue
---
LoCoMo 是首个超长期（very long-term）多模态开放域对话数据集，用于评估 LLM agent 的长期对话记忆能力。[^src-1]

数据集统计特征：50 条对话，每条平均 304.9 turns / 19.3 sessions / 9,209.2 tokens，时间跨度数月，最多可达 35 sessions。每条对话平均包含 32.3 张图片。[^src-2]

与现有数据集相比，LoCoMo 的平均对话长度约为 MSC 的 9 倍，分布于 6 倍的轮次和 4 倍的 sessions 中。[^src-3]

数据通过 human-machine pipeline 产生：先由 LLM-based generative agents（gpt-3.5-turbo）基于 persona 和 temporal event graph 生成对话，再由人工标注者编辑约 15% 的对话轮次、移除或替换约 19% 的图片，确保长程一致性和事件对齐。[^src-4]

[^src-1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "0_abstract.tex" -- "we collect LoCoMo, a dataset of very long-term conversations, each encompassing 300 turns and 9K tokens on avg., over up to 35 sessions"
[^src-2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Dataset Statistics (Table)" -- "Total # conversations 50; Avg. # sessions 19.3; Avg. # turns per session 15.8; Avg. # tokens conversation 9,209.2; Avg. # images 32.3"
[^src-3]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table compare_datasets caption" -- "The average length of a conversation in LoCoMo is 9x that of MSC, distributed over 6x more turns and 4x more sessions"
[^src-4]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Human Verification & Editing" -- "annotators edited nearly 15% of the dialog turns and removed or substituted approx. 19% images"
