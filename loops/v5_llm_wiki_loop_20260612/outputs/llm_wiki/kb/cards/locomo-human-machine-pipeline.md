---
id: locomo-human-machine-pipeline
title: LoCoMo Human-Machine 对话生成管线
status: accepted
card_type: method
tags:
- data-generation
- human-machine-pipeline
- LLM-agent
- human-verification
- synthetic-dialogue
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-locomo
evidence_basis: experimental_paper
justification: ../justification/locomo-human-machine-pipeline.md
canonical_concept: locomo-human-machine-pipeline
aliases:
- human-machine pipeline
- LoCoMo generative pipeline
- 人机协作对话生成管线
summary: locomo-human-machine-pipeline LoCoMo 的 human-machine 对话生成管线。四阶段： (1) persona 生成（MSC 4-5句 -> GPT-3.5-turbo 扩展为完整人设含目标/经历/习惯/人际关系）； (2) temporal event graph 构建（text-davinci-003 基于 persona 迭代生成因果链接事件）；
  (3) LLM agent 对话生成（reflect&respond + image sharing/reaction，两 agent 交替）； (4) human verification & editing（编辑15%轮次、替换19%图片、验证事件对齐）。 旨在兼顾规模化与质量，避免纯众包的高成本和纯合成的低一致性。
related:
- locomo-dataset
- reflect-and-respond-agent
- temporal-event-graph-dialogue
---

LoCoMo 的数据生成采用 human-machine pipeline，兼顾规模化产出与长程质量保证。[^src-1]

管线四阶段：

**阶段一：Persona 生成** -- 从 MSC 数据集选取 4-5 句初始属性 p_c，用 GPT-3.5-turbo 扩展为完整 persona p，通常包含目标、过往经历、日常习惯、人际关系以及姓名/年龄/性别。[^src-2]

**阶段二：Temporal Event Graph 构建** -- 用 text-davinci-003 基于 persona 迭代生成事件图 G（最多 25 事件，6-12 个月跨度，含因果连接）。[^src-3]

**阶段三：LLM Agent 对话生成** -- 两个 GPT-3.5-turbo agent 各配备 reflect&respond 机制（短期+长期记忆）和 image sharing/reaction 功能，基于 persona + event graph 交替生成对话。[^src-4]

**阶段四：Human Verification & Editing** -- 人工标注者编辑约 15% 对话轮次（消除长程不一致）、移除/替换约 19% 图片（去除不相关图像）、验证对话与事件图对齐。[^src-5] [^card-1] [^card-2] [^card-3]

[^src-1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Generative Pipeline for LoCoMo" -- "we present the first study of very long-term open-domain multi-modal dialogues... collected via a human-machine pipeline"
[^src-2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Persona" -- "select an initial persona statement p_c from the MSC dataset... employ gpt-3.5-turbo as M to expand these into full persona statement p"
[^src-3]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Temporal Event Graph" -- "we construct a temporal event graph, labeled as G, for each agent... up to 25 events, spread across a time frame of 6 to 12 months"
[^src-4]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Virtual Agent Architecture" -- "We create two virtual agents... each initialized with a LLM M (i.e., gpt-3.5-turbo)"
[^src-5]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Human Verification & Editing" -- "annotators edited nearly 15% of the dialog turns and removed or substituted approx. 19% images"

[^card-1]: 与 [reflect-and-respond-agent] 关联——agent 架构是管线核心组件
[^card-2]: 与 [temporal-event-graph-dialogue] 关联——事件图是管线第二阶段产物
[^card-3]: 与 [locomo-dataset] 关联——管线是数据集的生产方法
