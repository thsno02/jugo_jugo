---
id: review-involvement-spectrum
title: 人类参与程度谱系
status: draft
card_type: distinction
tags: [llm-wiki, human-involvement, review, supervision]
created_time: 2026-06-04T22:45:00+08:00
edited_time: 2026-06-04T22:45:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/review-involvement-spectrum.md
canonical_concept: review-involvement-spectrum
aliases: [参与程度谱系, involvement spectrum, 监督程度, supervision level]
summary: >-
  review-involvement-spectrum 指 LLM Wiki 中人类参与程度是一个可调节的谱系：
  从逐条深度审查到批量低监督处理；作者偏好深度参与但承认批量方式可行，
  材料未讨论审查负担是否随规模增长形成新瓶颈
related: []
---

LLM Wiki 中人类的参与程度不是固定的，而是一个**可调节的谱系**：

**深度参与端**——作者描述了自己的偏好：逐条摄入资料并深度参与——阅读摘要、检查更新、引导 LLM 该强调什么。实践中作者「一侧打开 LLM agent 对话，另一侧打开 Obsidian 实时浏览结果」[^src-1]。

**低监督端**——材料明确指出也可以「在较少监督下批量摄入多份资料」[^src-2]。用户应根据自己的风格选择并记录在 schema 中。

值得注意的是，材料的核心论点（维护成本归零）聚焦在 LLM 消除了维护瓶颈[^src-3]，但未讨论人类审查是否构成新的瓶颈——尤其是在批量摄入模式下如何保证质量。参与程度的选择本质上是**质量保证 vs 吞吐量**的权衡。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" 第4段 -- "I have the LLM agent open on one side and Obsidian open on the other... I browse the results in real time"
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Ingest" -- "you could also batch-ingest many sources at once with less supervision"
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Why this works" 第1段 -- "the cost of maintenance is near zero"
