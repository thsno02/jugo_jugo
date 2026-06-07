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
related: [parallel-multi-agent-research, contradiction-as-asset, gap-mapping-promotion]
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

论点驱动模式复用了并行多智能体研究的基础设施——同样启动多智能体并行搜索，但将角度从通用的学术/技术/新闻替换为围绕主张的支持/反对/机制分工[^card-1]。判决输出中「contradicted」类别与 wiki 层面的矛盾保留原则形成呼应——thesis mode 产出的矛盾证据不应被丢弃，而应作为知识资产被标记保留[^card-2]。每轮结束后的缺口报告可通过缺口映射与晋升机制持久化为 wiki 中的正式页面，驱动后续迭代[^card-3]。

## Footnotes

[^card-1]: [并行多智能体研究机制](parallel-multi-agent-research.md) -- 论点驱动模式复用并行研究基础设施，将通用角度替换为围绕主张的支持/反对/机制分工
[^card-2]: [矛盾作为知识资产](contradiction-as-asset.md) -- thesis mode 的 contradicted 判决与矛盾保留原则呼应：冲突证据应标记保留而非丢弃
[^card-3]: [缺口映射与晋升机制](gap-mapping-promotion.md) -- thesis mode 每轮缺口报告可通过 gap mapping 持久化为 wiki 正式页面

[^src-1]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Thesis mode" L24-26 -- "Start from a claim. Agents split across supporting, opposing, mechanistic, meta, and adjacent angles. Output is a verdict — not a summary."
[^src-2]: `data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: thesis" L473-474 -- "Agents are split across supporting, opposing, mechanistic, meta/review, and adjacent — balanced by design."
[^src-3]: `data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: thesis" L476 -- "Sources that don't relate to the claim's variables are skipped, which keeps the wiki tight."
[^src-4]: `data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: thesis" L476 -- "Output is a verdict: supported, partially supported, contradicted, insufficient evidence, or mixed."
[^src-5]: `data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: thesis" L478 -- "With --min-time, round two focuses harder on the weaker side of the evidence — counter-weight against confirmation bias."
