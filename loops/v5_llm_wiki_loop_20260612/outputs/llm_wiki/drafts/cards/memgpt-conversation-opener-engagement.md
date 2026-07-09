---
id: memgpt-conversation-opener-engagement
title: MemGPT 对话开场白的参与度评估
status: draft
card_type: experimental-result
tags: [conversational-agent, engagement, evaluation, persona-consistency]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: experimental_paper
justification: ../justification/memgpt-conversation-opener-engagement.md
canonical_concept: memgpt-conversation-opener-engagement
aliases: [conversation opener task, 对话开场白任务, opener engagement evaluation]
summary: >-
  MemGPT memgpt-conversation-opener-engagement 对话开场白参与度评估 测试agent利用长期记忆
  生成引人入胜对话开头的能力。使用CSIM(余弦相似度)评分将生成opener与gold persona标签
  及人类基线对比。MemGPT+GPT-4在SIM-1达0.868超过人类基线0.800,
  表明MemGPT能利用working context中的信息生成更具参与度的opener,
  且倾向于更详尽地覆盖persona信息。
related: [memgpt-deep-memory-retrieval, memgpt-main-context-structure]
---

对话开场白任务 (conversation opener task) 评估 agent 利用历史对话积累的知识生成引人入胜消息的能力。[^src-1]

**评估方法**: 使用 CSIM (余弦相似度) 将生成的 opener 与 gold persona 标签进行比较。评测指标包括：
- SIM-1: 与排名第一的 persona 标签的相似度
- SIM-3: 与前三名 persona 标签的平均相似度
- SIM-H: 与人类生成 opener 的相似度 [^src-1]

**实验结果** (Table 2): [^src-2]
| 方法 | SIM-1 | SIM-3 | SIM-H |
|------|-------|-------|-------|
| Human | 0.800 | 0.800 | 1.000 |
| GPT-3.5 Turbo | 0.830 | 0.812 | **0.817** |
| GPT-4 | **0.868** | **0.843** | 0.773 |
| GPT-4 Turbo | 0.857 | 0.828 | 0.767 |

MemGPT 能够生成与人类创建的 opener 表现相当、有时甚至超越的引人入胜开场白。论文观察到 MemGPT 倾向于生成更冗长、覆盖更多 persona 方面的 opener。此外，将信息存储在 working context 中对生成高参与度 opener 至关重要。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/experiments.tex" -- "MemGPT is able to craft engaging openers that perform similarly to and occasionally exceed the hand-written human openers...we can see the storing information in working context is key to generating engaging openers"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "tables/conv_opener_table.tex" -- "GPT-4 & 0.868 & 0.843 & 0.773"
[^card-1]: [memgpt-deep-memory-retrieval] opener 任务测 engagement，DMR 测 consistency，互为补充
[^card-2]: [memgpt-main-context-structure] working context 的信息存储对 opener 质量起关键作用
