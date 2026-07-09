---
id: llm-wiki-compounding-knowledge
title: 知识复利效应
status: accepted
card_type: design-principle
tags:
- llm-wiki
- compounding
- knowledge-accumulation
- incremental
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- llm-wiki-net
evidence_basis: documentation
justification: ../justification/llm-wiki-compounding-knowledge.md
canonical_concept: compounding-knowledge-effect
aliases:
- knowledge compounding
- every run compounds
- 知识复利
- cumulative research
summary: compounding-knowledge-effect：每次运行都在积累——sources 变为交叉引用文章，文章变为 reports slides study-guides playbooks implementation-plans，研究越多每个输出越强，输出回存 wiki 使下次输出建立在所有先前之上
related:
- llm-wiki-compilation-process
- llm-wiki-output-generation
- context-rot-vs-compounding
- llm-wiki-write-back-compounding
- llm-wiki-lessons-learned
---
llm-wiki 的核心价值主张之一是知识复利效应：每次运行都在积累。Sources 变为交叉引用的文章，文章变为 reports、slide decks、study guides、playbooks 和 implementation plans。[^src-1]

输出被归档回 wiki，使得下一个输出建立在所有先前的输出之上。研究越多，每个输出越强。[^src-2]

这体现了一种增量知识架构——单一命令可以创建 topic wiki、分派 agents、摄取有价值的内容、编译源为文章，并生成建立在此之上的交付物。[^src-3]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Hero" P25 -- "Every run compounds. Sources become cross-referenced articles. Articles become reports, slide decks, study guides, playbooks, and implementation plans."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Output" P39 -- "Reports, slide decks, study guides, playbooks, implementation plans, timelines, glossaries, comparisons. Filed back into the wiki so the next output builds on every previous one."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Hero" P26 -- "One command spins up a topic wiki, dispatches up to ten agents, ingests what's worth keeping..."
