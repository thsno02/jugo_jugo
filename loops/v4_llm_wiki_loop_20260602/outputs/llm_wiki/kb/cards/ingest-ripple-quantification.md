---
id: ingest-ripple-quantification
title: 摄入涟漪效应的实证量化
status: accepted
card_type: empirical_finding
tags: [llm-wiki, compounding, empirical, ripple-effect, measurement]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
justification: ../justification/ingest-ripple-quantification.md
canonical_concept: ingest-ripple-quantification
aliases: [涟漪效应量化, ripple effect measurement, 摄入触发编辑数, ingest fan-out]
summary: >-
  ingest-ripple-quantification（涟漪效应量化 / ripple effect measurement / 摄入触发编辑数 /
  ingest fan-out）是六个月实践中对 LLM Wiki 复利行为的实证度量：每次摄入新文章，
  Claude 中位数触及 9 个已有文件（范围 4-23），样本为最近 30 次摄入
related: [knowledge-compounding, wiki-compounding-artifact, lint-operation]
---

在六个月、35 页 wiki + 80 篇原始输入的实践中，作者通过 `log.md`（追加式操作日志）对摄入涟漪效应进行了实证测量[^src-1]：

- **中位数**：每次摄入触及 **9 个已有文件**
- **范围**：4 至 23 个文件
- **样本量**：最近 30 次摄入操作
- **操作类型**：添加反向链接、更新概念索引、标记矛盾、优化 TL;DR

作者的表述是：「当我摄入一篇新文章（如 AI agent memory 主题），Claude 平均触及 8-12 个已有页面」[^src-2]。这一数据来自 `log.md` 的中位数统计[^src-3]。

这是目前已知的对 LLM Wiki「复利效应」最具体的实证数据点。Karpathy 原始 gist 将其称为「ripple effect」但未给出量化；Wen & Ku (2026) 的知识复利理论从经济学角度形式化了这一效应的数学形态（H(t) 凹饱和曲线）[^card-1]，而本卡提供了实践层面的经验验证。wiki-compounding-artifact 枚举了复利积累的五类制品[^card-2]，本卡回答的是「每次操作实际触发多少积累活动」这一操作层面的量化问题。

值得注意的方法论局限：作者明确声明「这不是受控研究——样本量 1，无对照组」，但「方向性正确，且是我自己的数据」[^src-4]。

## Footnotes

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- L63-69 -- "wiki/log.md — append-only operation log, every ingest/lint/edit timestamped... The '8–12 pages touched per ingest' figure is the median over the last 30 ingests; the spread is 4 to 23."
[^src-2]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- L29 -- "When I ingest a new article on, say, AI agent memory, Claude touches an average of 8–12 existing pages: adds backlinks, updates the concepts index, flags one contradiction with a six-month-old note, refines a TL;DR."
[^src-3]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- L29 -- "my log.md says the median ingest touches 9 files"
[^src-4]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- L70 -- "This isn't a controlled study — sample size 1, no comparison group. But it's directional, and it's mine."
[^card-1]: [知识复利效应](knowledge-compounding.md) -- 本卡提供涟漪效应的实证测量（中位 9 文件/次摄入），该卡提供知识复利的经济学理论框架（H(t) 凹饱和曲线），两者从实践与理论两侧验证同一复利现象
[^card-2]: [Wiki 作为复利型知识制品](wiki-compounding-artifact.md) -- 该卡枚举 wiki 中积累的五类制品类型，本卡量化每次摄入实际触发多少积累活动（中位 9 文件），从操作频率维度补充了制品枚举
