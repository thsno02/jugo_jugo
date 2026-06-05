---
id: literature-velocity-argument
title: 文献速度论点
status: accepted
card_type: source_claim
tags: [llm-wiki, curation, fast-moving-fields, automation-rationale]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [complete-tech-live-frontier]
justification: ../justification/literature-velocity-argument.md
canonical_concept: literature-velocity-argument
aliases: [文献速度论点, literature velocity, 文献增速超过人工策展, curation speed gap]
summary: >-
  literature-velocity-argument（文献速度论点 / literature velocity / 文献增速超过人工策展 / curation speed gap）
  主张在快速演进的研究前沿，手工维护的参考文献在发布前就已过时，而 LLM 维护的交叉引用 wiki 能在不失结构的前提下吸收新工作
related: []
---

在快速演进的研究领域中，文献的增长速度超过了人工策展能力[^src-1]。手工制作的参考文献或综述在完成之前就已经过时——这不是夸张，而是一个结构性问题：当论文之间的**关联**才是真正的信号时，仅靠人力无法在每篇新论文到达时更新所有交叉引用。

LLM 维护的 wiki 解决这一问题的方式是：在不丢失已有结构的前提下吸收新工作[^src-2]。每篇新论文摄入时，LLM 不只是添加一个条目，而是自动更新所有引用该工作的页面、实体档案和主题地图。

这一论点扩展了维护成本归零[^card-1]的经济论证：即使人类有意愿做簿记工作，在文献快速增长的领域中，人类的速度也不足以跟上。不是不愿做，而是**做不完**。

该论点的前提是：研究价值不仅在于单篇论文的内容，更在于**论文之间的连接**[^src-3]——如潜空间推理和潜通信并非两个独立领域，而是一个前沿的两面，真正的信号在跨论文的关联中。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/complete-tech-live-frontier/text.txt` -- "Why we built it" 第一点 -- "The literature is moving faster than human curation can keep up with."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/complete-tech-live-frontier/text.txt` -- "Why we built it" 第一点 -- "A handcrafted bibliography goes stale before it ships. An LLM-maintained, deeply cross-referenced wiki absorbs new work without losing structure."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/complete-tech-live-frontier/text.txt` -- "Why we built it" 第一点 -- "the connections between papers are where the real signal is"
[^card-1]: [维护成本归零论点](maintenance-cost-zero.md) -- 本卡的速度论点是对维护成本论点的场景扩展：不只是成本问题，还是速度问题
