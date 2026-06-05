---
id: output-compounding-loop
title: 产出复利循环
status: accepted
card_type: mechanism
tags: [llm-wiki, output, compounding, artifacts]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
justification: ../justification/output-compounding-loop.md
canonical_concept: output-compounding-loop
aliases: [产出复利, output compounding, 产出循环, artifact compounding loop]
summary: >-
  output-compounding-loop（产出复利 / output compounding / 产出循环 / artifact compounding loop）
  是 LLM Wiki 的价值放大机制：产出（报告/幻灯片/计划等）回写进 wiki，
  使每个新产出建立在所有先前研究之上，研究越多产出越强
related: []
---

LLM Wiki 的产出层实现了一个**正反馈的复利循环**[^src-1]：

1. **来源编译为文章**——原始来源经编译通道综合为带交叉引用和置信度评分的 wiki 文章[^src-2]
2. **文章生成产出**——报告、幻灯片大纲、学习指南、行动手册、实施计划、时间线、词汇表、比较分析——七种产出类型[^src-3]
3. **产出回写进 wiki**——生成的制品保存到 `output/` 并自动索引，下一次产出建立在所有先前研究之上[^src-4]

核心论断：**「每一次运行都在积累。研究越多，每个产出越强。」**[^src-5]

跨 wiki 复利也有支持——`--with` 参数可从另一个 wiki 引入知识到当前产出中[^src-6]。项目（project）功能可将相关产出组织到带目标的文件夹中，通过 `WHY.md` 捕获项目目标[^src-7]。

这一机制延伸了已有的 wiki 复利型制品概念——前者描述的是 wiki 层内部的知识积累（交叉引用、矛盾标记、综合叙述），本卡描述的是 wiki 层到产出层再回到 wiki 的闭环。Wen & Ku (2026) 的知识复利理论为这一实践模式提供了形式化经济学框架，将其数学化为知识库覆盖率 H(t) 的凹饱和递推方程[^card-knowledge-compounding]。此外，Qing Claw 实现的搜索回写机制与产出回写形成互补——前者将外部搜索结果写回实体页面，后者将产出制品写回 wiki 索引，共同构成 wiki 的双向呼吸[^card-search-write-back]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- Opening L14 -- "Every run compounds. Sources become cross-referenced articles. Articles become reports, slide decks, study guides, playbooks, and implementation plans. The more you research, the stronger every output gets."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Compile" L44-46 -- "Raw sources become synthesized articles with cross-references and confidence scores."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Using outputs" L372-387 -- "summary, report, study-guide, slides, timeline, glossary, comparison"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Using outputs" L387-388 -- "Outputs are saved to output/ inside the topic wiki and indexed automatically. Every output builds on all compiled articles, so the more you research, the stronger every output gets."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- Opening L14 -- "Every run compounds... The more you research, the stronger every output gets."
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Cross-wiki context" L392-393 -- "Use --with to pull knowledge from another wiki into your output"
[^src-7]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Projects" L394-396 -- "Group related outputs into project folders with goals... WHY.md that captures the goal."
[^card-knowledge-compounding]: [知识复利效应](knowledge-compounding.md) -- Wen & Ku (2026) 将产出复利循环形式化为 H(t) 凹饱和曲线，证明持久化知识层使每任务成本成为时间递减函数，为产出回写的经济合理性提供了理论基础
[^card-search-write-back]: [搜索回写机制](search-write-back.md) -- 搜索回写（外部搜索结果写回实体页面）与产出回写（产出制品写回 wiki 索引）是两种互补的 wiki 双向呼吸机制，共同驱动知识复利
