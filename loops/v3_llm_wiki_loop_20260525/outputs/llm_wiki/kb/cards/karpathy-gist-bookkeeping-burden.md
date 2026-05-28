---
id: karpathy-gist-bookkeeping-burden
title: 个人 wiki 真正崩溃的不是读和想，而是"维护成本指数增长"——LLM 把它降到零
status: accepted
card_type: concept
tags: [#llm-wiki, #knowledge-management, #maintenance, #karpathy]
created_time: 2026-05-26T11:50:00+08:00
edited_time: 2026-05-28T11:09:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
provenance_card: ../provenance/karpathy-gist-bookkeeping-burden.md
aliases: [maintenance bottleneck, why LLM wiki works, bookkeeping cost]
related: [karpathy-gist-three-layers, karpathy-gist-memex-connection, robin-cartier-scale-ceiling, enterprise-llm-wiki-drift-detection-loop, retrieval-not-enough-for-stale-kb, kunal-llm-c-rag-misinterpretation]
---

Karpathy 在 gist 的 "Why this works" 段给出 LLM Wiki 模式有效性的核心解释，这一论点本身可独立成立、对评估任何 PKM 设计都有用：

**核心主张**[^src1]：
> "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages."

也就是说，传统人维护 wiki 之所以失败，不是因为**信息处理**太难（人读得动、想得动），而是因为**簿记成本**：
- 每加入一份源材料，可能要触动 10–15 张已有页面[^src3]；
- 交叉引用、概念页摘要、矛盾标注，每条都需要 follow-through；
- 这种维护负担**随页面数超线性增长**——而新内容带来的边际价值是 sub-linear 的；
- 人类对"无聊但必须做的小事"会失去意志，wiki 最终被放弃。

**LLM 改变了什么**：
- LLM 不会无聊、不会忘记一个交叉引用、单次 ingest 可以触 15 个文件；
- "The wiki stays maintained because the cost of maintenance is near zero."
- 人只需要做仍然只有人能做的事：**选源、定向探究、提好问题、思考含义**[^src2]。

**这个论点的可操作含义**：
- 评估一个 PKM 工具，看它是否把"bookkeeping → 零"作为设计目标。如果维护一张交叉引用页仍然要人手动操作，则它注定不可持续；
- 这也解释了为何 wiki 模式的工作流必须**有 ingest/lint 这两个显式入口**[^src4]：ingest 处理"新增带来的全量维护"，lint 处理"漂移带来的累积维护"。两个入口都把维护负担放在 LLM 身上；
- 对人侧的最小操作分工：**人做不可替代的思考层**——curate sources, direct analysis, ask good questions, think about meaning。Karpathy 总结："The LLM's job is everything else."

边界与误用：
- "维护成本接近零"在小规模成立；在数百页以上规模，LLM 也可能漏更新或重复创建近似页面（这是 Robin Cartier 等实践者在大规模下观察到的局限）；
- "人不写 wiki"是默认而非铁律——人有时仍需手写少量页面（例如方法论说明），但写完后须告知 LLM 维护交接；
- LLM 不会"无聊"不代表它不会犯错——错误模式从"忘记更新"变成"幻觉式更新"，问题域转移而非消失。

## References

Karpathy 2026 LLM Wiki gist 的 "Why this works" 段；"Operations" 段说明 ingest/lint 入口对应"新增维护 / 漂移维护"。

- 源路径：`data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`（行 64–70 "Why this works" 完整段；行 37 "A single source might touch 10-15 wiki pages"；行 41 lint 段）。

## Footnotes

- 核心主张原文（行 66）："The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero."
- 人侧分工原文（行 68）："The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."
- 单源触 10–15 页（行 37）："A single source might touch 10-15 wiki pages."
- Lint 处理漂移原文（行 41）："Periodically, ask the LLM to health-check the wiki. Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps that could be filled with a web search."
