---
id: thesis-driven-research
title: 论点驱动研究模式
status: accepted
card_type: mechanism
tags: [llm-wiki, research, thesis, confirmation-bias, verdict]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
justification: ../justification/thesis-driven-research.md
canonical_concept: thesis-driven-research
aliases: [论点驱动, thesis mode, 论题研究, thesis-driven]
summary: >-
  thesis-driven-research（论点驱动 / thesis mode / 论题研究 / thesis-driven）是 LLM Wiki
  的特殊研究模式：从一个主张出发，智能体按支持/反对/机制/元分析/相邻五角度分工，
  产出判决而非摘要，第二轮加权反面证据以对抗确认偏误
related: []
---

论点驱动模式（thesis mode）是 LLM Wiki 区别于一般主题研究的特殊模式。启动方式为 `/wiki:research --mode thesis "<claim>"`，以一个具体主张作为过滤器[^src-1]。

**智能体角色分工**按五个角度平衡设计[^src-2]：
- 支持（supporting）
- 反对（opposing）
- 机制解析（mechanistic）
- 元分析/综述（meta/review）
- 相邻领域（adjacent）

与主张变量无关的来源被跳过，保持 wiki 的聚焦度[^src-3]。

**产出是判决（verdict）而非摘要**——结论分为五类：supported、partially supported、contradicted、insufficient evidence、mixed[^src-4]。

**反确认偏误机制**：配合 `--min-time` 进入第二轮时，系统将更多注意力投向证据较弱的一侧，作为对抗确认偏误的平衡权重[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Thesis mode" L24-26 -- "Start from a claim. Agents split across supporting, opposing, mechanistic, meta, and adjacent angles. Output is a verdict — not a summary."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: thesis" L473-474 -- "Agents are split across supporting, opposing, mechanistic, meta/review, and adjacent — balanced by design."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: thesis" L476 -- "Sources that don't relate to the claim's variables are skipped, which keeps the wiki tight."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: thesis" L476 -- "Output is a verdict: supported, partially supported, contradicted, insufficient evidence, or mixed."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: thesis" L478 -- "With --min-time, round two focuses harder on the weaker side of the evidence — counter-weight against confirmation bias."
