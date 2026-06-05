---
id: documentation-merge-gate
title: 文档合并门禁机制
status: accepted
card_type: mechanism
tags: [documentation, merge-gate, developer-incentive, workflow]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [writethedocs-docs-as-code]
justification: ../justification/documentation-merge-gate.md
canonical_concept: documentation-merge-gate
aliases: [文档合并门禁, 合并阻断文档要求, docs merge blocking]
summary: >-
  documentation-merge-gate（文档合并门禁 / 合并阻断文档要求 / docs merge blocking）指在 docs-as-code 工作流中，若新功能未附带文档则阻止合并，从而激励开发者在功能记忆犹新时撰写文档
related: [continuous-drift-detection, knowledge-as-work-byproduct]
  - docs-as-code
---

在 Docs as Code 工作流中，一项关键的激励机制是**文档合并门禁**：如果新功能的代码变更未包含相应文档，则阻止该变更被合并[^src-1]。

该机制的核心价值在于**时间激励**——它促使开发者在功能"记忆犹新"（while they are fresh）时就撰写文档，而非事后补写[^src-1]。这一做法也是 Docs as Code 所声称的好处之一：开发者往往会主动写出文档初稿[^src-2]。

Falconer 的企业 LLM Wiki 方案将这一"创建时保障质量"的思路与"创建后持续检测"的思路结合：合并门禁确保文档在变更时产生，而持续偏移检测在后续自动发现文档与代码之间的漂移[^card-1]。Falconer 提出的"知识作为工作副产品"原则更进一步，设想知识图谱从 PR 合并、Slack 讨论等工作流中自动增长，无需显式的文档撰写步骤[^card-2]。

## Footnotes

[^src-1]: `data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "benefits" L30-31 -- "You can block merging of new features if they don't include documentation, which incentivizes developers to write about features while they are fresh"
[^src-2]: `data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "benefits" L29 -- "Developers will often write a first draft of documentation"
[^card-1]: [持续偏移检测](continuous-drift-detection.md) -- 合并门禁在创建时保障文档质量，持续偏移检测在后续自动发现文档与代码的漂移，两者形成文档生命周期的互补覆盖
[^card-2]: [知识作为工作副产品](knowledge-as-work-byproduct.md) -- "知识作为副产品"原则将合并门禁的"写文档才能合并"进一步推向"工作本身就是文档"，设想知识图谱从工作流自动增长
