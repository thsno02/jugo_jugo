---
id: llm-wiki-compilation-process
title: Wiki 编译与文章合成
status: accepted
card_type: mechanism
tags:
- llm-wiki
- compilation
- synthesis
- confidence-scores
- cross-references
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- llm-wiki-net
evidence_basis: documentation
justification: ../justification/llm-wiki-compilation-process.md
canonical_concept: wiki-compilation-process
aliases:
- compile
- wiki compilation
- article synthesis
- LLM 编译
- 文章合成
summary: wiki-compilation-process：raw sources 编译为 wiki/concepts/ topics/ references/
  三类合成文章，带交叉引用双向链接和置信度评分（high/medium/low），使用双链格式 [[wikilink]] + markdown link，每个输出基于所有已编译文章递增强化
related:
- llm-wiki-immutable-raw-sources
- wiki-compilation-by-llm
- originals-folder-verbatim
- llm-wiki-audit-trust-verification
- llm-wiki-compounding-knowledge
- llm-wiki-librarian-quality-scoring
- llm-wiki-output-generation
- dual-link-obsidian-agent-compatibility
---
llm-wiki 的编译过程将 raw sources 合成为结构化 wiki 文章，组织在三个类别下：
- concepts/：基础概念、机制、理论
- topics/：具体主题、比较、领域现状
- references/：工具、框架、数据表、查阅资源[^src-1]

文章带有交叉引用和双向链接，以及置信度评分（high/medium/low）反映源质量和佐证情况。[^src-2]

关键设计：每个输出都建立在所有已编译文章之上，因此研究越多，每个输出越强（"Every run compounds"）。[^src-3]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Architecture" P198-201 -- "Wiki articles (wiki/) are LLM-compiled syntheses organized into three categories: Concepts, Topics, References"
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Architecture" P205 -- "Confidence scores (high/medium/low) reflect source quality and corroboration."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Hero" P25 -- "Every run compounds. Sources become cross-referenced articles. Articles become reports, slide decks, study guides, playbooks, and implementation plans."
