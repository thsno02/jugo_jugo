---
id: search-write-back
title: 搜索回写机制
status: accepted
card_type: mechanism
tags: [search-write-back, compounding-mechanism, bidirectional-wiki, qing-claw]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-knowledge-compounding]
justification: ../justification/search-write-back.md
canonical_concept: search-write-back
aliases: [搜索回写, search write-back, 搜索结果回写, auto-write-back of search results]
summary: >-
  search-write-back（搜索回写 / search write-back / 搜索结果回写）是知识复利的第三微观机制：
  当 wiki 不足以回答查询时触发外部搜索，搜索结果不蒸发而是由 wiki 专家合并回写至实体页面，
  使 wiki 从单向（仅接受 INGEST）变为双向呼吸，是 Qing Claw 区别于所有其他 LLM Wiki 实现的关键能力
related: [invest-harvest-cycle, knowledge-compounding, output-compounding-loop, wiki-write-back-mechanism]
  - knowledge-compounding
  - ingest-operation
  - query-and-answer-filing
---

搜索回写（Search Write-Back）是 Wen & Ku (2026) 识别的知识复利第三微观机制，也是**区分 Qing Claw 与所有其他 LLM Wiki 实现的关键能力**[^src-1]。

**机制运作流程**：当 wiki 不足以回答用户问题时，CEO 编排器触发搜索专家从 Web 获取信息——但搜索结果**不蒸发**。CEO 主动将结果传递给 wiki 专家，后者先读取现有实体页面，然后合并新事实并覆盖写入[^src-2]。

**实证案例**：在 Q3 中，搜索专家返回了六条此前不在 wiki 中的新事实（包括"加入 OpenAI"这一关键职业更新）。CEO 主动调用 wiki 专家将这些事实按时间顺序合并到 Peter Steinberger 的实体页面。直接经济后果出现在 Q4：一个全新角度的查询仅用 1 次 fs_read 和 4K token 即完成回答，无需进一步搜索[^src-3]。

**理论意义**：搜索回写使 wiki 从**单向**（仅接受 INGEST 输入、不接受外部信息）变为**双向且呼吸的（bidirectional and respiring）**——同时吸收原始资料、外部搜索结果和问答综合。三种信息流汇入同一个 wiki，使其"温度"（高频访问概率）持续上升[^src-4]。

**实现要求**：搜索回写的 CEO 端通过断路器规则（circuit-breaker rules）实现。先让 wiki 专家检查，只有当 wiki 专家明确报告"不在 wiki 中"时才允许创建搜索专家；搜索补充后，必须调用 wiki 专家将新发现追加到相应页面[^src-5]。

在 GitHub 所有 LLM Wiki 实现的横向比较中，搜索回写能力仅 Qing Claw 支持[^src-6]。llm-wiki.net 的产出复利循环实现了一种互补的回写路径——产出制品（报告/幻灯片）写回 wiki 索引，与搜索回写共同构成 wiki 的多源双向呼吸[^card-output-compounding-loop]。

搜索回写作为知识复利的第三微观机制，在 Wen & Ku 的理论框架中占据核心位置——它是将 wiki 从单向变为双向的关键转折[^card-knowledge-compounding]。四查询实验中 Q3 的 28K token 投资尖峰直接对应搜索回写事件，而 Q4 的 4K token 收获则验证了回写投资的即时回报[^card-invest-harvest-cycle]。my-llm-wiki 的 `llm-wiki note` 命令实现了一种互补形态的回写——以手动 CLI 指令将会话洞察写回知识图谱，与搜索回写的自动编排形成对照[^card-wiki-write-back-mechanism]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 6.3 P25 -- "This is the mechanism that distinguishes Qing Claw from all other LLM Wiki implementations"
[^src-2]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 6.3 P25 -- "the search results do not evaporate. Instead, the CEO actively passes them back to the wiki expert, which first reads the existing entity page, then merges the new facts and overwrites it"
[^src-3]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 6.3 P26 -- "the search expert returned six new facts not previously in the wiki... The CEO actively invoked the wiki expert to merge these facts into Peter Steinberger's entity page in chronological order. The direct economic consequence appeared in Q4: a brand-new query angle was answered with a single fs_read in 4K tokens"
[^src-4]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 6.3 P26 -- "the wiki is bidirectional and respiring: absorbing raw materials, external search results, and Q&A synthesis alike. All three sources of information flow into the same wiki, causing its 'temperature' (probability of high-frequency access) to rise continuously"
[^src-5]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Appendix B P32 -- "Search must be written back to wiki after supplementing it... issue a follow-up call to call_agent_wiki_expert_expert, requesting that the new findings be appended to the corresponding entity/concept page"
[^src-6]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Table 3 P22 -- "Search write-back to wiki... the most critical capability—search write-back to wiki, the soul of the compounding loop—is supported only by Qing Claw"
[^card-output-compounding-loop]: [产出复利循环](output-compounding-loop.md) -- llm-wiki.net 的产出回写（产出制品写回 wiki 索引）与搜索回写（外部搜索结果写回实体页面）是两种互补的 wiki 双向呼吸路径，共同驱动知识复利
[^card-knowledge-compounding]: [知识复利效应](knowledge-compounding.md) -- 本卡详述搜索回写的机制与实证，该卡将搜索回写定位为知识复利三微观机制之一并提供经济学框架
[^card-invest-harvest-cycle]: [投资-收获振荡成本曲线](invest-harvest-cycle.md) -- 本卡阐述搜索回写的机制流程，该卡展示搜索回写事件在成本轨迹中表现为 Q3 投资尖峰（28K）与 Q4 收获波谷（4K）
[^card-wiki-write-back-mechanism]: [Wiki 回写机制](wiki-write-back-mechanism.md) -- 本卡描述 Qing Claw 的自动搜索回写（CEO 编排器触发），该卡描述 my-llm-wiki 的手动回写（`llm-wiki note` CLI 命令），两者是自动 vs. 手动的互补回写路径
