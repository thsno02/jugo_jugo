---
id: llm-wiki-output-generation
title: 输出制品生成系统
status: draft
card_type: mechanism
tags: [llm-wiki, output, artifacts, report, slides, study-guide]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-output-generation.md
canonical_concept: output-artifact-generation
aliases: [output generation, wiki output, artifact generation, 输出生成, deliverables]
summary: >-
  output-artifact-generation 系统：支持 summary report study-guide slides timeline glossary comparison 七种类型，存入 output/ 并自动索引，每个输出基于所有编译文章递增强化，支持 --with 跨 wiki 上下文和 --project 分组，可回溯至 wiki 和 raw sources
related: [llm-wiki-compilation-process, llm-wiki-audit-trust-verification]
---

llm-wiki 的输出系统从编译的 wiki 文章生成多种制品类型：
- summary：简洁概览
- report：详细分析，含引用和证据
- study-guide：结构化学习材料，含关键概念和复习问题
- slides：幻灯片大纲含讲者笔记
- timeline：时间线视图
- glossary：从文章提取的术语定义
- comparison：两个或多个主题的并排分析[^src-1]

输出保存到 topic wiki 的 output/ 目录并自动索引。每个输出建立在所有编译文章之上，研究越多输出越强。[^src-2]

支持 --with <wiki> 引入跨 wiki 知识，以及 --project 将相关输出分组到带 WHY.md 的项目文件夹。[^src-3]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Output" P259-267 -- "summary, report, study-guide, slides, timeline, glossary, comparison"
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Output" P267 -- "Outputs are saved to output/ inside the topic wiki and indexed automatically. Every output builds on all compiled articles, so the more you research, the stronger every output gets."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Output" P269-273 -- "Cross-wiki context: Use --with to pull knowledge from another wiki... Projects: Group related outputs into project folders with goals"
