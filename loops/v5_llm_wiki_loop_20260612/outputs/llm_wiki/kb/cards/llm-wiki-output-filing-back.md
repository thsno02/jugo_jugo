---
id: llm-wiki-output-filing-back
title: 查询输出归档回 Wiki 的累积效应
status: accepted
card_type: pattern
tags:
- cumulative-knowledge
- output-filing
- wiki-growth
- feedback-loop
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- karpathy-x-launch-post
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-output-filing-back.md
canonical_concept: llm-wiki-output-filing-back
aliases:
- filing outputs back
- output回归wiki
- cumulative exploration
- 输出归档
summary: llm-wiki-output-filing-back 查询输出归档回Wiki的累积效应 Karpathy将LLM查询输出(markdown/slides/images) 归档回wiki以增强后续查询，使个人探索和查询"always add up"形成累积式知识库增长。 这构成正反馈循环：查询→输出→归档→丰富wiki→更好的后续查询。输出格式包括markdown文件、 Marp幻灯片、matplotlib图像。
related:
- llm-knowledge-base-workflow
- obsidian-as-llm-ide
- llm-wiki-linting
---

Karpathy 描述了一种知识正反馈循环模式：将 LLM 查询的输出归档回 wiki，使后续查询可利用先前探索的结果。

**输出格式**：
- Markdown 文件
- 幻灯片（Marp 格式）
- Matplotlib 图像
- 其他依查询而定的可视化格式

**累积机制**："Often, I end up 'filing' the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always 'add up' in the knowledge base."[^src-1]

这构成正反馈循环：
1. 用户对 wiki 发起查询
2. LLM 产出结构化输出
3. 输出归档回 wiki
4. Wiki 内容因此丰富
5. 后续查询可利用先前探索结果

该模式使知识库具备自增长特性——每次使用都增强系统，而非仅消费信息。[^card-1]

[^src-1]: `data/raw/webpage/karpathy-x-launch-post/text.txt` -- "Output" -- "Often, I end up \"filing\" the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always \"add up\" in the knowledge base."
[^card-1]: 参见 [[llm-wiki-linting]] lint 过程同样产出可归档的增强内容
